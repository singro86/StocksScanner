#!/usr/bin/env python3
"""Weekday market-movers scanner.

Pulls Yahoo predefined screeners (day_gainers, day_losers, most_actives),
filters to liquid Wealthsimple-friendly names, overlays holdings + GARP
watchlist, ranks top movers, and emails a Buy / Hold / Sell digest.

Never places trades. Never uses Equibles or Rebalance-MCP (CI-safe).
Config: config/market-movers.yaml
"""

from __future__ import annotations

import argparse
import csv
import html
import json
import os
import re
import ssl
import sys
import urllib.error
import urllib.parse
import urllib.request
from datetime import datetime, timedelta, timezone
from pathlib import Path
from statistics import mean
from zoneinfo import ZoneInfo

ROOT = Path(__file__).resolve().parents[2]
CONFIG_PATH = ROOT / "config" / "market-movers.yaml"
PROFILE = ROOT / "portfolio" / "profile.yaml"
PEAK = ROOT / "portfolio" / "peak-value.yaml"
HOLDINGS = ROOT / "portfolio" / "holdings.yaml"
WATCHLIST = ROOT / "portfolio" / "watchlist.yaml"
TIMESERIES = ROOT / "research" / "timeseries"
REPORTS = ROOT / "research" / "reports"
LOCAL_ENV_FILES = (ROOT / "config" / "wsli.env", ROOT / ".env")

YAHOO_CHART = "https://query1.finance.yahoo.com/v8/finance/chart/{ticker}?range=3mo&interval=1d"
YAHOO_SCREENER = (
    "https://query1.finance.yahoo.com/v1/finance/screener/predefined/saved"
    "?formatted=false&lang=en-US&region=US&scrIds={scr_id}&count={count}"
)
UA = "Mozilla/5.0 (compatible; 1MillionPortfolio/1.0; daily-market-movers-scan)"

REC_RANK = {"Buy (paper)": 0, "Buy": 0, "Sell": 1, "Hold": 2, "Watch": 3, "Avoid": 4}
REC_TO_ACTION = {
    "Buy (paper)": "PAPER_CANDIDATE",
    "Buy": "CANDIDATE",
    "Sell": "SELL",
    "Hold": "HOLD",
    "Watch": "WATCH",
    "Avoid": "AVOID",
}
BADGE = {
    "Buy (paper)": ("#05603a", "#ecfdf3"),
    "Buy": ("#05603a", "#ecfdf3"),
    "Sell": ("#b42318", "#fef3f2"),
    "Hold": ("#175cd3", "#eff8ff"),
    "Watch": ("#b54708", "#fffaeb"),
    "Avoid": ("#475467", "#f2f4f7"),
}

CSV_FIELDS = [
    "date",
    "ticker",
    "close",
    "volume",
    "pct_1d",
    "pct_5d",
    "sma20",
    "rsi14",
    "rel_volume",
    "source",
    "action",
    "recommendation",
]

DEFAULT_CONFIG: dict = {
    "slug": "market-movers",
    "report_title": "Market movers scan",
    "screeners": ["day_gainers", "day_losers", "most_actives"],
    "screener_count": 25,
    "max_candidates": 50,
    "top_n": 10,
    "filters": {
        "min_price": 5.0,
        "min_avg_volume": 1_000_000,
        "min_rel_volume": 1.5,
        "exclude_exchange_substrings": ["OTC", "PINK", "GREY", "PNKS"],
        "exclude_ticker_suffixes": [".W", ".WS", "-WT", "-W"],
    },
    "classify": {
        "max_buys": 2,
        "min_pct_1d_buy": 3.0,
        "max_rsi_buy": 75,
        "min_rel_volume_buy": 1.5,
        "min_pct_1d_sell": -3.0,
        "min_rel_volume_sell": 1.5,
        "stretched_above_sma20_pct": 25,
    },
    "overlay": {
        "include_holdings": True,
        "include_watchlist": True,
        "skip_sleeves": ["benchmark"],
    },
}


def load_local_env() -> None:
    for path in LOCAL_ENV_FILES:
        if not path.exists():
            continue
        for raw in path.read_text(encoding="utf-8").splitlines():
            line = raw.strip()
            if not line or line.startswith("#") or "=" not in line:
                continue
            key, val = line.split("=", 1)
            key = key.strip()
            val = val.strip().strip('"').strip("'")
            if key and key not in os.environ:
                os.environ[key] = val


def _tz():
    for key in ("America/Toronto", "America/New_York", "EST5EDT"):
        try:
            return ZoneInfo(key)
        except Exception:
            continue
    return timezone(timedelta(hours=-4))


TZ = _tz()


def _parse_scalar(val: str):
    v = val.strip().strip('"').strip("'")
    if v.lower() in {"true", "yes"}:
        return True
    if v.lower() in {"false", "no"}:
        return False
    try:
        if "." in v:
            return float(v)
        return int(v)
    except ValueError:
        return v


def load_config(path: Path = CONFIG_PATH) -> dict:
    """Load market-movers.yaml with a tiny schema-aware parser (no PyYAML dependency)."""
    cfg = json.loads(json.dumps(DEFAULT_CONFIG))
    if not path.exists():
        return cfg

    section: str | None = None
    list_key: str | None = None

    for raw in path.read_text(encoding="utf-8").splitlines():
        if not raw.strip() or raw.lstrip().startswith("#"):
            continue
        indent = len(raw) - len(raw.lstrip(" "))
        line = raw.strip()

        # Top-level scalar: key: value
        if indent == 0 and ":" in line:
            key, rest = line.split(":", 1)
            key, rest = key.strip(), rest.strip()
            if rest == "":
                section = key
                list_key = None
                if section == "screeners":
                    cfg["screeners"] = []
                elif section in {"filters", "classify", "overlay"}:
                    if not isinstance(cfg.get(section), dict):
                        cfg[section] = {}
                continue
            cfg[key] = _parse_scalar(rest)
            section = None
            list_key = None
            continue

        if section == "screeners" and line.startswith("- "):
            cfg["screeners"].append(str(_parse_scalar(line[2:].strip())))
            continue

        if section in {"filters", "classify", "overlay"} and indent == 2:
            if line.startswith("- "):
                continue
            if ":" not in line:
                continue
            key, rest = line.split(":", 1)
            key, rest = key.strip(), rest.strip()
            if rest == "":
                cfg[section][key] = []
                list_key = key
            else:
                cfg[section][key] = _parse_scalar(rest)
                list_key = None
            continue

        if (
            section in {"filters", "classify", "overlay"}
            and list_key
            and indent >= 4
            and line.startswith("- ")
        ):
            cfg[section][list_key].append(_parse_scalar(line[2:].strip()))
            continue

    return cfg


def _read_simple_yaml_map(path: Path) -> dict:
    data: dict = {}
    if not path.exists():
        return data
    for raw in path.read_text(encoding="utf-8").splitlines():
        line = raw.split("#", 1)[0].rstrip()
        if not line or line.startswith(" ") or line.startswith("-"):
            continue
        if ":" not in line:
            continue
        key, val = line.split(":", 1)
        data[key.strip()] = val.strip().strip('"').strip("'")
    return data


def load_held_tickers() -> set[str]:
    if not HOLDINGS.exists():
        return set()
    held: set[str] = set()
    in_positions = False
    for raw in HOLDINGS.read_text(encoding="utf-8").splitlines():
        if raw.startswith("positions:"):
            in_positions = True
            continue
        if in_positions and raw.strip().startswith("- ticker:"):
            t = raw.split(":", 1)[1].strip().strip('"').strip("'")
            if t and t.lower() != "null":
                held.add(t.upper())
    return held


def load_watchlist_tickers(skip_sleeves: list[str]) -> set[str]:
    if not WATCHLIST.exists():
        return set()
    tickers: set[str] = set()
    current_sleeve: str | None = None
    skip = {s.lower() for s in skip_sleeves}
    for raw in WATCHLIST.read_text(encoding="utf-8").splitlines():
        line = raw.split("#", 1)[0].rstrip()
        if not line.strip():
            continue
        # sleeve headers under core: are indented 2 spaces and end with :
        m = re.match(r"^  ([a-z0-9_]+):\s*$", line)
        if m:
            current_sleeve = m.group(1)
            continue
        if line.strip().startswith("- ticker:"):
            t = line.split(":", 1)[1].strip().strip('"').strip("'")
            if not t or t.lower() == "null":
                continue
            if current_sleeve and current_sleeve.lower() in skip:
                continue
            # screener_slots sit outside core sleeves — current_sleeve may be stale
            if "screener_slots" in line:
                continue
            tickers.add(t.upper())
    # Also pick screener_slots explicitly
    in_slots = False
    for raw in WATCHLIST.read_text(encoding="utf-8").splitlines():
        if raw.startswith("screener_slots:"):
            in_slots = True
            continue
        if in_slots and raw.startswith("screener_criteria:"):
            break
        if in_slots and raw.strip().startswith("- ticker:"):
            t = raw.split(":", 1)[1].strip().strip('"').strip("'")
            if t and t.lower() != "null":
                tickers.add(t.upper())
    return tickers


def paper_trading_complete() -> bool:
    if not PROFILE.exists():
        return False
    for raw in PROFILE.read_text(encoding="utf-8").splitlines():
        if "paper_trading_complete:" in raw:
            return raw.split(":", 1)[1].strip().lower() == "true"
    return False


def gates(profile_complete: bool, peak: dict) -> tuple[bool, str]:
    if os.environ.get("PAUSE_ALL_TRADING", "").lower() == "true":
        return False, "PAUSE_ALL_TRADING is set — no buy proposals."
    if peak.get("mode") == "review_only":
        return False, "Drawdown review-only mode — no new buy proposals."
    if not profile_complete:
        return (
            True,
            "Paper trading active — dry-run only. Buy lines are paper recommendations, never live Wealthsimple orders.",
        )
    return True, "Paper trading complete in profile — this job still never places a live order."


def http_get_json(url: str, timeout: int = 30) -> dict:
    req = urllib.request.Request(url, headers={"User-Agent": UA})
    ctx = ssl.create_default_context()
    with urllib.request.urlopen(req, timeout=timeout, context=ctx) as resp:
        return json.loads(resp.read().decode("utf-8"))


def fetch_screener(scr_id: str, count: int) -> list[dict]:
    url = YAHOO_SCREENER.format(scr_id=urllib.parse.quote(scr_id), count=count)
    payload = http_get_json(url)
    finance = payload.get("finance") or {}
    results = finance.get("result") or []
    if not results:
        raise RuntimeError(f"{scr_id}: empty screener result")
    quotes = results[0].get("quotes") or []
    out: list[dict] = []
    for q in quotes:
        sym = (q.get("symbol") or "").upper().strip()
        if not sym:
            continue
        out.append(
            {
                "ticker": sym,
                "name": q.get("shortName") or q.get("longName") or "",
                "price": q.get("regularMarketPrice"),
                "pct_1d_screener": q.get("regularMarketChangePercent"),
                "volume_screener": q.get("regularMarketVolume"),
                "exchange": str(q.get("fullExchangeName") or q.get("exchange") or ""),
                "source": scr_id,
            }
        )
    return out


def fetch_chart(ticker: str) -> dict:
    req = urllib.request.Request(YAHOO_CHART.format(ticker=ticker), headers={"User-Agent": UA})
    ctx = ssl.create_default_context()
    with urllib.request.urlopen(req, timeout=30, context=ctx) as resp:
        payload = json.loads(resp.read().decode("utf-8"))
    result = payload["chart"]["result"][0]
    quotes = result["indicators"]["quote"][0]
    ts = result["timestamp"]
    closes = []
    for t, c, v in zip(ts, quotes["close"], quotes["volume"]):
        if c is None:
            continue
        closes.append((t, float(c), int(v or 0)))
    if len(closes) < 21:
        raise RuntimeError(f"{ticker}: need 21 daily closes, got {len(closes)}")
    meta = result.get("meta") or {}
    return {
        "rows": closes,
        "currency": meta.get("currency", "USD"),
        "exchange": str(meta.get("exchangeName") or meta.get("fullExchangeName") or ""),
    }


def rsi(values: list[float], period: int = 14) -> float | None:
    if len(values) <= period:
        return None
    window = values[-(period + 1) :]
    gains, losses = [], []
    for i in range(1, len(window)):
        d = window[i] - window[i - 1]
        gains.append(max(d, 0.0))
        losses.append(max(-d, 0.0))
    avg_gain = mean(gains)
    avg_loss = mean(losses)
    if avg_loss == 0:
        return 100.0
    rs = avg_gain / avg_loss
    return 100.0 - (100.0 / (1.0 + rs))


def pct(new: float, old: float | None) -> float | None:
    if old is None or old == 0:
        return None
    return (new / old - 1.0) * 100.0


def fmt(n: float | None, digits: int = 2) -> str:
    if n is None:
        return "—"
    return f"{n:.{digits}f}"


def signed(n: float | None, digits: int = 2) -> str:
    if n is None:
        return "—"
    return f"{n:+.{digits}f}"


def passes_ticker_filters(ticker: str, exchange: str, filters: dict) -> bool:
    for suf in filters.get("exclude_ticker_suffixes") or []:
        if ticker.upper().endswith(str(suf).upper()):
            return False
    ex = (exchange or "").upper()
    for sub in filters.get("exclude_exchange_substrings") or []:
        if str(sub).upper() in ex:
            return False
    # Common OTC-looking symbols
    if ticker.endswith("F") and len(ticker) >= 5:
        # many OTC end in F; still allow if exchange is NYSE/Nasdaq — only drop when exchange says OTC
        pass
    return True


def classify(
    row: dict,
    allow_buys: bool,
    paper: bool,
    held: set[str],
    rules: dict,
) -> tuple[str, str]:
    ticker = row["ticker"]
    close = row["close"]
    sma20 = row["sma20"]
    rsi14 = row["rsi14"]
    pct_1d = row.get("pct_1d")
    rel_vol = row.get("rel_volume") or 0.0
    above_sma = sma20 and close >= sma20
    below_sma = sma20 and close < sma20
    stretch_pct = rules.get("stretched_above_sma20_pct", 25)
    stretched = sma20 and close > sma20 * (1.0 + stretch_pct / 100.0)
    overbought = rsi14 is not None and rsi14 >= rules.get("max_rsi_buy", 75)

    # Held breakdown → Sell
    if ticker in held and below_sma and pct_1d is not None:
        if pct_1d <= rules.get("min_pct_1d_sell", -3.0) and rel_vol >= rules.get(
            "min_rel_volume_sell", 1.5
        ):
            return "Sell", "Held name breaking down below SMA20 on elevated volume. Paper sell only."

    # Strong upside → Buy (paper)
    buy_ok = (
        allow_buys
        and pct_1d is not None
        and pct_1d >= rules.get("min_pct_1d_buy", 3.0)
        and above_sma
        and not overbought
        and not stretched
        and rel_vol >= rules.get("min_rel_volume_buy", 1.5)
    )
    if buy_ok:
        if ticker in held:
            return "Hold", "Already held; momentum ok but do not chase size from this scan."
        if not paper:
            return (
                "Buy (paper)",
                "Liquid mover above SMA20 with volume confirmation. Paper ticket only — GARP ≥ 60 still required before any live buy.",
            )
        return "Buy", "Liquid mover above SMA20 with volume confirmation. This job still does not place the order."

    if ticker in held:
        return "Hold", "On holdings overlay — monitor; no breakdown sell signal."

    if overbought or stretched:
        return "Watch", "Extended or overbought — wait for a cleaner entry."

    if pct_1d is not None and pct_1d <= -3.0 and below_sma:
        return "Avoid", "Sharp drop below SMA20 and not held — do not catch the knife from this scan."

    if row.get("source", "").startswith("overlay"):
        return "Hold", "Watchlist/holdings overlay — not a top mover today."

    return "Watch", "On the move but signals mixed — research only until GARP ≥ 60."


def trim_buys(rows: list[dict], max_buys: int) -> None:
    buys = [r for r in rows if r["recommendation"] in {"Buy (paper)", "Buy"}]
    if len(buys) <= max_buys:
        return
    buys_sorted = sorted(
        buys,
        key=lambda r: (
            -(r.get("move_score") or 0),
            -(r.get("pct_1d") or -999),
        ),
    )
    keep = set(id(r) for r in buys_sorted[:max_buys])
    for r in buys:
        if id(r) in keep:
            continue
        r["recommendation"] = "Watch"
        r["reason"] = f"Buy trimmed — max {max_buys} paper candidates per morning."
        r["action"] = "WATCH"


def move_score(row: dict) -> float:
    """Rank by absolute 1d move scaled by relative volume."""
    p = abs(row.get("pct_1d") or 0.0)
    rv = row.get("rel_volume") or 1.0
    return p * min(rv, 5.0)


def rank_key(row: dict) -> tuple:
    rec = row.get("recommendation", "Avoid")
    rec_rank = REC_RANK.get(rec, 9)
    score = -(row.get("move_score") or 0)
    return (rec_rank, score, row["ticker"])


def top_rows(rows: list[dict], n: int) -> list[dict]:
    ranked = sorted(rows, key=rank_key)
    action = [r for r in ranked if r["recommendation"] in {"Buy (paper)", "Buy", "Sell"}]
    rest = [r for r in ranked if r["recommendation"] not in {"Buy (paper)", "Buy", "Sell"}]
    # Prefer highest move_score within rest
    rest = sorted(rest, key=lambda r: -(r.get("move_score") or 0))
    return (action + rest)[:n]


def append_csv(path: Path, rows: list[dict], day: str) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    existing_days: set[str] = set()
    if path.exists():
        with path.open(encoding="utf-8", newline="") as f:
            for row in csv.DictReader(f):
                existing_days.add(row.get("date", ""))
    write_header = not path.exists()
    # Replace same-day rows
    if day in existing_days:
        kept = []
        with path.open(encoding="utf-8", newline="") as f:
            for row in csv.DictReader(f):
                if row.get("date") != day:
                    kept.append(row)
        with path.open("w", encoding="utf-8", newline="") as f:
            w = csv.DictWriter(f, fieldnames=CSV_FIELDS)
            w.writeheader()
            for row in kept:
                w.writerow({k: row.get(k, "") for k in CSV_FIELDS})
        write_header = False
    with path.open("a", encoding="utf-8", newline="") as f:
        w = csv.DictWriter(f, fieldnames=CSV_FIELDS)
        if write_header:
            w.writeheader()
        for r in rows:
            w.writerow({k: r.get(k, "") for k in CSV_FIELDS})


def counts(rows: list[dict]) -> dict[str, int]:
    out = {"Buy (paper)": 0, "Buy": 0, "Sell": 0, "Hold": 0, "Watch": 0, "Avoid": 0}
    for r in rows:
        rec = r.get("recommendation", "Avoid")
        out[rec] = out.get(rec, 0) + 1
    return out


def build_report(day: str, gate_note: str, rows: list[dict], errors: list[str], top_n: int) -> str:
    picks = top_rows(rows, top_n)
    n = counts(rows)
    lines = [
        f"# Market movers scan — {day}",
        "",
        f"**Gate:** {gate_note}",
        "",
        "Official Rebalance-MCP GARP scores are not computed in this job. "
        "A live ticket still needs GARP ≥ 60.",
        "",
        f"Universe: Yahoo `day_gainers` / `day_losers` / `most_actives` + holdings/watchlist overlay. "
        f"Showing top {len(picks)} of {len(rows)} candidates.",
        "",
        f"| Rec | Count |",
        f"|-----|------:|",
        f"| Buy (paper) | {n.get('Buy (paper)', 0)} |",
        f"| Buy | {n.get('Buy', 0)} |",
        f"| Sell | {n.get('Sell', 0)} |",
        f"| Hold | {n.get('Hold', 0)} |",
        f"| Watch | {n.get('Watch', 0)} |",
        f"| Avoid | {n.get('Avoid', 0)} |",
        "",
        "| # | Ticker | Rec | Price | 1d | 5d | RelVol | RSI | Source | Why |",
        "|--:|--------|-----|------:|---:|---:|-------:|----:|--------|-----|",
    ]
    for i, r in enumerate(picks, 1):
        lines.append(
            f"| {i} | {r['ticker']} | {r['recommendation']} | ${fmt(r['close'])} | "
            f"{signed(r.get('pct_1d'))}% | {signed(r.get('pct_5d'))}% | "
            f"{fmt(r.get('rel_volume'), 2)} | {fmt(r.get('rsi14'), 1)} | "
            f"{r.get('source', '')} | {r.get('reason', '')} |"
        )
    if errors:
        lines.extend(["", "## Fetch errors", ""])
        for e in errors:
            lines.append(f"- {e}")
    lines.extend(
        [
            "",
            "## Disclaimer",
            "",
            "I am an AI research assistant, not a licensed financial advisor. "
            "This is educational information, not personalized financial advice. "
            "This job never calls wsli and never sets TRADE_APPROVED.",
            "",
        ]
    )
    return "\n".join(lines)


def _badge(rec: str) -> str:
    fg, bg = BADGE.get(rec, ("#475467", "#f2f4f7"))
    return (
        f'<span style="display:inline-block;padding:2px 8px;border-radius:999px;'
        f'font-size:12px;font-weight:700;color:{fg};background:{bg};">{html.escape(rec)}</span>'
    )


def _chg_html(n: float | None) -> str:
    if n is None:
        return "—"
    color = "#05603a" if n >= 0 else "#b42318"
    return f'<span style="color:{color};font-variant-numeric:tabular-nums;">{n:+.2f}%</span>'


def build_digest_html(day: str, gate_note: str, rows: list[dict], errors: list[str], top_n: int) -> str:
    picks = top_rows(rows, top_n)
    n = counts(rows)
    buy_n = n.get("Buy (paper)", 0) + n.get("Buy", 0)
    buys = [r for r in sorted(rows, key=rank_key) if r["recommendation"] in {"Buy (paper)", "Buy"}]
    if buys:
        b = buys[0]
        headline = (
            f"{html.escape(b['ticker'])} leads today’s paper buy at ${fmt(b['close'])} "
            f"({signed(b['pct_1d'])}% today). Not a live Wealthsimple order."
        )
    else:
        headline = "No buy today. Top 10 below are ranked Sell first, then Hold/Watch/Avoid."

    cards = [
        ("Buy", buy_n, "#05603a", "#ecfdf3"),
        ("Sell", n["Sell"], "#b42318", "#fef3f2"),
        ("Hold", n["Hold"], "#175cd3", "#eff8ff"),
        ("Watch", n["Watch"], "#b54708", "#fffaeb"),
        ("Avoid", n["Avoid"], "#475467", "#f2f4f7"),
    ]
    card_html = "".join(
        f'<td style="padding:8px;text-align:center;">'
        f'<div style="background:{bg};border-radius:10px;padding:12px 8px;">'
        f'<div style="font-size:22px;font-weight:800;color:{fg};">{val}</div>'
        f'<div style="font-size:11px;font-weight:700;letter-spacing:0.04em;text-transform:uppercase;color:{fg};">{label}</div>'
        f"</div></td>"
        for label, val, fg, bg in cards
    )

    body_rows = []
    for i, r in enumerate(picks, 1):
        bg = "#f9fafb" if i % 2 == 0 else "#ffffff"
        name = html.escape(r.get("name") or "")
        ticker = html.escape(r["ticker"])
        why = html.escape(r.get("reason") or "")
        body_rows.append(
            f'<tr style="background:{bg};">'
            f'<td style="padding:12px 8px;text-align:center;color:#667085;width:36px;">{i}</td>'
            f'<td style="padding:12px 8px;width:90px;"><strong style="font-size:15px;">{ticker}</strong>'
            f'<div style="font-size:11px;color:#667085;">{name}</div></td>'
            f'<td style="padding:12px 8px;white-space:nowrap;width:110px;">{_badge(r["recommendation"])}</td>'
            f'<td style="padding:12px 8px;text-align:right;font-variant-numeric:tabular-nums;width:70px;">${fmt(r["close"])}</td>'
            f'<td style="padding:12px 8px;text-align:right;width:62px;">{_chg_html(r["pct_1d"])}</td>'
            f'<td style="padding:12px 8px;text-align:right;width:62px;">{_chg_html(r["pct_5d"])}</td>'
            f'<td style="padding:12px 10px 12px 12px;font-size:13px;line-height:1.45;color:#344054;">{why}</td>'
            f"</tr>"
        )

    err_html = ""
    if errors:
        items = "".join(f"<li>{html.escape(e)}</li>" for e in errors)
        err_html = f'<p style="color:#b42318;font-size:13px;"><strong>Fetch errors</strong></p><ul>{items}</ul>'

    return f"""<!DOCTYPE html>
<html><body style="margin:0;padding:0;background:#eef2f6;font-family:-apple-system,BlinkMacSystemFont,'Segoe UI',Helvetica,Arial,sans-serif;color:#101828;">
  <table role="presentation" width="100%" cellspacing="0" cellpadding="0" style="background:#eef2f6;padding:24px 12px;">
    <tr><td align="center">
      <table role="presentation" width="760" cellspacing="0" cellpadding="0" style="max-width:760px;background:#ffffff;border-radius:16px;overflow:hidden;">
        <tr><td style="background:#0b1220;color:#ffffff;padding:24px 28px;">
          <div style="font-size:12px;letter-spacing:0.12em;text-transform:uppercase;color:#98a2b3;">1MillionPortfolio · TFSA paper scan</div>
          <div style="font-size:24px;font-weight:800;margin-top:6px;">Top 10 market movers</div>
          <div style="font-size:14px;color:#d0d5dd;margin-top:4px;">{html.escape(day)} · America/Toronto · Yahoo screeners</div>
        </td></tr>
        <tr><td style="padding:20px 28px 8px 28px;">
          <p style="margin:0 0 12px 0;font-size:15px;line-height:1.5;">{html.escape(headline)}</p>
          <p style="margin:0 0 16px 0;font-size:13px;color:#667085;">{html.escape(gate_note)}</p>
          <table role="presentation" width="100%" cellspacing="0" cellpadding="0"><tr>{card_html}</tr></table>
        </td></tr>
        <tr><td style="padding:8px 16px 20px 16px;">
          <table role="presentation" width="100%" cellspacing="0" cellpadding="0" style="border:1px solid #eaecf0;border-radius:12px;overflow:hidden;font-size:13px;">
            <tr style="background:#0b1220;color:#ffffff;">
              <th style="padding:10px 8px;text-align:center;width:36px;">#</th>
              <th style="padding:10px 8px;text-align:left;width:90px;">Ticker</th>
              <th style="padding:10px 8px;text-align:left;width:110px;">Rec</th>
              <th style="padding:10px 8px;text-align:right;width:70px;">Price</th>
              <th style="padding:10px 8px;text-align:right;width:62px;">1d</th>
              <th style="padding:10px 8px;text-align:right;width:62px;">5d</th>
              <th style="padding:10px 12px;text-align:left;">Why</th>
            </tr>
            {''.join(body_rows)}
          </table>
        </td></tr>
        <tr><td style="padding:0 28px 24px 28px;font-size:12px;color:#667085;line-height:1.55;">
          {err_html}
          <p style="margin:0 0 8px 0;">Table shows the top {len(picks)} liquid movers (price ≥ $5), ranked Buy → Sell → Hold → Watch → Avoid. Official GARP scores are not computed here — live tickets still need GARP ≥ 60.</p>
          <p style="margin:0;">I am an AI research assistant, not a licensed financial advisor. This is educational information, not personalized financial advice. This job never calls wsli and never sets TRADE_APPROVED.</p>
        </td></tr>
      </table>
    </td></tr>
  </table>
</body></html>"""


def send_email(subject: str, text: str, html_body: str | None = None, tag: str = "daily_scan") -> None:
    api_key = os.environ.get("RESEND_API_KEY")
    to = os.environ.get("NOTIFY_EMAIL_TO")
    from_addr = os.environ.get("NOTIFY_EMAIL_FROM", "portfolio@yourdomain.com")
    outbox = ROOT / "portfolio" / "cache" / "email-outbox"
    if not api_key or not to:
        outbox.mkdir(parents=True, exist_ok=True)
        stamp = datetime.now(TZ).strftime("%Y%m%d-%H%M%S")
        dest = outbox / f"{stamp}-{tag}.md"
        dest.write_text(f"# {subject}\n\n{text}\n", encoding="utf-8")
        print(f"Email skipped (missing secrets). Saved {dest}")
        return
    payload_obj: dict = {"from": from_addr, "to": [to], "subject": subject, "text": text}
    if html_body:
        payload_obj["html"] = html_body
    data = json.dumps(payload_obj).encode("utf-8")
    req = urllib.request.Request(
        "https://api.resend.com/emails",
        data=data,
        headers={
            "Authorization": f"Bearer {api_key}",
            "Content-Type": "application/json",
            "User-Agent": UA,
        },
        method="POST",
    )
    try:
        with urllib.request.urlopen(req, timeout=30) as resp:
            print(f"Email sent ({resp.status})")
    except Exception as exc:
        outbox.mkdir(parents=True, exist_ok=True)
        stamp = datetime.now(TZ).strftime("%Y%m%d-%H%M%S")
        dest = outbox / f"{stamp}-{tag}-failed.md"
        dest.write_text(f"# {subject}\n\nSend failed: {exc}\n\n{text}\n", encoding="utf-8")
        print(f"Email failed; saved {dest}", file=sys.stderr)


def collect_candidates(cfg: dict) -> tuple[dict[str, dict], list[str]]:
    """Return ticker -> seed meta, and errors."""
    errors: list[str] = []
    by_ticker: dict[str, dict] = {}
    count = int(cfg.get("screener_count") or 25)
    for scr in cfg.get("screeners") or []:
        try:
            quotes = fetch_screener(str(scr), count)
        except (urllib.error.URLError, TimeoutError, RuntimeError, KeyError, json.JSONDecodeError) as exc:
            errors.append(f"screener {scr}: {exc}")
            continue
        for q in quotes:
            t = q["ticker"]
            if t not in by_ticker:
                by_ticker[t] = q
            else:
                # Prefer gainers/losers label; append source
                prev = by_ticker[t]
                if q["source"] not in str(prev.get("source", "")):
                    prev["source"] = f"{prev['source']}+{q['source']}"
    return by_ticker, errors


def enrich_and_filter(
    seeds: dict[str, dict],
    overlay: set[str],
    overlay_held: set[str],
    cfg: dict,
) -> tuple[list[dict], list[str]]:
    filters = cfg.get("filters") or {}
    max_cand = int(cfg.get("max_candidates") or 50)
    min_price = float(filters.get("min_price") or 5.0)
    min_avg_vol = float(filters.get("min_avg_volume") or 1_000_000)
    min_rel = float(filters.get("min_rel_volume") or 1.5)

    # Merge overlay tickers
    for t in overlay:
        if t not in seeds:
            src = "overlay_held" if t in overlay_held else "overlay_watch"
            seeds[t] = {"ticker": t, "name": "", "exchange": "", "source": src}

    rows: list[dict] = []
    errors: list[str] = []
    # Process screener names first (higher priority), then overlay
    ordered = sorted(
        seeds.values(),
        key=lambda q: (0 if str(q.get("source", "")).startswith("overlay") else 1, q["ticker"]),
        reverse=True,
    )

    for q in ordered:
        if len(rows) >= max_cand and not str(q.get("source", "")).startswith("overlay"):
            continue
        ticker = q["ticker"]
        try:
            chart = fetch_chart(ticker)
        except (urllib.error.URLError, TimeoutError, RuntimeError, KeyError, IndexError, json.JSONDecodeError) as exc:
            errors.append(f"{ticker}: {exc}")
            continue
        series = chart["rows"]
        closes = [c for _, c, _ in series]
        vols = [v for _, _, v in series]
        last_ts, last_close, last_vol = series[-1]
        last_day = datetime.fromtimestamp(last_ts, tz=timezone.utc).date().isoformat()
        avg_vol20 = mean(vols[-20:]) if len(vols) >= 20 else mean(vols)
        rel_volume = (last_vol / avg_vol20) if avg_vol20 else 0.0
        exchange = q.get("exchange") or chart.get("exchange") or ""

        is_overlay = str(q.get("source", "")).startswith("overlay")
        if not passes_ticker_filters(ticker, exchange, filters):
            if not is_overlay:
                continue
        if last_close < min_price and not is_overlay:
            continue
        # Liquidity: avg volume OR relative volume (overlays always kept)
        if not is_overlay:
            if avg_vol20 < min_avg_vol and rel_volume < min_rel:
                continue

        pct_1d = pct(last_close, closes[-2] if len(closes) >= 2 else None)
        pct_5d = pct(last_close, closes[-6] if len(closes) >= 6 else None)
        sma20 = mean(closes[-20:])
        rsi14 = rsi(closes, 14)
        row = {
            "date": last_day,
            "ticker": ticker,
            "name": q.get("name") or "",
            "close": round(last_close, 4),
            "volume": last_vol,
            "pct_1d": None if pct_1d is None else round(pct_1d, 3),
            "pct_5d": None if pct_5d is None else round(pct_5d, 3),
            "sma20": round(sma20, 4),
            "rsi14": None if rsi14 is None else round(rsi14, 2),
            "rel_volume": round(rel_volume, 3),
            "source": q.get("source", ""),
            "action": "",
            "recommendation": "",
            "reason": "",
            "move_score": 0.0,
        }
        row["move_score"] = round(move_score(row), 3)
        rows.append(row)

        # Cap non-overlay after fill
        non_overlay = [r for r in rows if not str(r.get("source", "")).startswith("overlay")]
        if len(non_overlay) >= max_cand:
            # keep collecting overlays only
            pass

    return rows, errors


def parse_args(argv: list[str] | None = None) -> argparse.Namespace:
    p = argparse.ArgumentParser(description=__doc__)
    p.add_argument("--config", default=str(CONFIG_PATH), help="Path to market-movers.yaml")
    p.add_argument("--no-email", action="store_true", help="Write reports only; skip Resend.")
    p.add_argument("--top", type=int, default=None, help="Override top_n from config.")
    return p.parse_args(argv)


def main(argv: list[str] | None = None) -> int:
    load_local_env()
    args = parse_args(argv)
    cfg = load_config(Path(args.config) if args.config else CONFIG_PATH)
    paper_done = paper_trading_complete()
    peak = _read_simple_yaml_map(PEAK)
    allow, gate_note = gates(paper_done, peak)
    held = load_held_tickers()
    overlay_cfg = cfg.get("overlay") or {}
    overlay: set[str] = set()
    if overlay_cfg.get("include_holdings", True):
        overlay |= held
    if overlay_cfg.get("include_watchlist", True):
        overlay |= load_watchlist_tickers(list(overlay_cfg.get("skip_sleeves") or []))
    day = datetime.now(TZ).date().isoformat()
    top_n = int(args.top or cfg.get("top_n") or 10)

    seeds, scr_errors = collect_candidates(cfg)
    rows, enrich_errors = enrich_and_filter(seeds, overlay, held, cfg)
    errors = scr_errors + enrich_errors
    if not rows:
        print("No quotes fetched.", file=sys.stderr)
        for e in errors:
            print(e, file=sys.stderr)
        return 1

    rules = cfg.get("classify") or {}
    for r in rows:
        rec, reason = classify(r, allow, paper_done, held, rules)
        r["recommendation"] = rec
        r["reason"] = reason
        r["action"] = REC_TO_ACTION.get(rec, "WATCH")

    trim_buys(rows, int(rules.get("max_buys") or 2))

    # Persist top_n + any held overlay rows for history
    picks = top_rows(rows, top_n)
    held_extra = [r for r in rows if r["ticker"] in held and r not in picks]
    persist = picks + held_extra

    slug = cfg.get("slug") or "market-movers"
    csv_path = TIMESERIES / f"{slug}.csv"
    append_csv(csv_path, persist, persist[0]["date"] if persist else day)

    REPORTS.mkdir(parents=True, exist_ok=True)
    report = build_report(day, gate_note, rows, errors, top_n)
    report_path = REPORTS / f"{day}-{slug}-scan.md"
    report_path.write_text(report, encoding="utf-8")
    print(report_path)
    print(csv_path)

    if not args.no_email:
        html_body = build_digest_html(day, gate_note, rows, errors, top_n)
        send_email(
            f"1M Portfolio — Market movers {day}",
            report,
            html_body=html_body,
            tag="market-movers",
        )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
