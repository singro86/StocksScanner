#!/usr/bin/env python3
"""Weekday scanner for penny-stock universes.

Fetches Yahoo daily bars (not Equibles — reserve that quota), appends
research/timeseries/<slug>.csv, writes markdown briefs, and emails one
ranked HTML digest covering both lists. Never places trades.

Defaults to a combined digest of the 9-name primary list and the 20-name
secondary watchlist. Pass --universe to scan a single list.
"""

from __future__ import annotations

import argparse
import csv
import html
import json
import os
import ssl
import sys
import urllib.error
import urllib.request
from datetime import datetime, timedelta, timezone
from pathlib import Path
from statistics import mean
from zoneinfo import ZoneInfo

ROOT = Path(__file__).resolve().parents[2]
PRIMARY_UNIVERSE = ROOT / "portfolio" / "penny9-universe.yaml"
SECONDARY_UNIVERSE = ROOT / "portfolio" / "penny-secondary-watchlist.yaml"
PROFILE = ROOT / "portfolio" / "profile.yaml"
PEAK = ROOT / "portfolio" / "peak-value.yaml"
HOLDINGS = ROOT / "portfolio" / "holdings.yaml"
TIMESERIES = ROOT / "research" / "timeseries"
REPORTS = ROOT / "research" / "reports"
LOCAL_ENV_FILES = (ROOT / "config" / "wsli.env", ROOT / ".env")

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


def load_local_env() -> None:
    """Load gitignored notify secrets without overriding a real environment."""
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
YAHOO = "https://query1.finance.yahoo.com/v8/finance/chart/{ticker}?range=3mo&interval=1d"
UA = "Mozilla/5.0 (compatible; 1MillionPortfolio/1.0; daily-penny9-scan)"

CSV_FIELDS = [
    "date",
    "ticker",
    "close",
    "volume",
    "pct_1d",
    "pct_5d",
    "sma20",
    "rsi14",
    "quality",
    "action",
    "recommendation",
]


def _read_simple_yaml_map(path: Path) -> dict:
    data: dict = {}
    for raw in path.read_text(encoding="utf-8").splitlines():
        line = raw.split("#", 1)[0].rstrip()
        if not line or line.startswith(" ") or line.startswith("-"):
            continue
        if ":" not in line:
            continue
        key, val = line.split(":", 1)
        data[key.strip()] = val.strip().strip('"').strip("'")
    return data


def load_universe(path: Path) -> list[dict]:
    tickers: list[dict] = []
    current: dict | None = None
    for raw in path.read_text(encoding="utf-8").splitlines():
        line = raw.split("#", 1)[0].rstrip()
        if not line.strip():
            continue
        stripped = line.strip()
        if stripped.startswith("- ticker:"):
            if current:
                tickers.append(current)
            current = {"ticker": stripped.split(":", 1)[1].strip()}
            continue
        if current is not None and ":" in stripped and not stripped.startswith("-"):
            key, val = stripped.split(":", 1)
            current[key.strip()] = val.strip().strip('"').strip("'")
    if current:
        tickers.append(current)
    if not tickers:
        raise SystemExit(f"No tickers in {path}")
    return tickers


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
            held.add(raw.split(":", 1)[1].strip().strip('"').strip("'"))
    return held


def paper_trading_complete() -> bool:
    for raw in PROFILE.read_text(encoding="utf-8").splitlines():
        if "paper_trading_complete:" in raw:
            return raw.split(":", 1)[1].strip().lower() == "true"
    return False


def fetch_chart(ticker: str) -> dict:
    req = urllib.request.Request(YAHOO.format(ticker=ticker), headers={"User-Agent": UA})
    ctx = ssl.create_default_context()
    with urllib.request.urlopen(req, timeout=30, context=ctx) as resp:
        payload = json.loads(resp.read().decode("utf-8"))
    result = payload["chart"]["result"][0]
    quotes = result["indicators"]["quote"][0]
    ts = result["timestamp"]
    closes, volumes = [], []
    for t, c, v in zip(ts, quotes["close"], quotes["volume"]):
        if c is None:
            continue
        closes.append((t, float(c), int(v or 0)))
    if len(closes) < 21:
        raise RuntimeError(f"{ticker}: need 21 daily closes, got {len(closes)}")
    return {"rows": closes, "currency": result["meta"].get("currency", "USD")}


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


def gates(profile: dict, peak: dict) -> tuple[bool, str]:
    if os.environ.get("PAUSE_ALL_TRADING", "").lower() == "true":
        return False, "PAUSE_ALL_TRADING is set — no buy proposals."
    if peak.get("mode") == "review_only":
        return False, "Drawdown review-only mode — no new buy proposals."
    paper = profile.get("paper_trading_complete", "false").lower() == "true"
    if not paper:
        return True, "Paper trading active — dry-run only. Buy lines are paper recommendations, never live Wealthsimple orders."
    return True, "Paper trading complete in profile — this job still never places a live order."


def classify(row: dict, allow_buys: bool, paper: bool, held: set[str]) -> tuple[str, str]:
    quality = row.get("quality", "avoid")
    ticker = row["ticker"]
    if quality == "avoid":
        if ticker in held:
            return "Sell", "Avoid-quality name. Paper sell if you hold it — not a live order."
        return "Avoid", "Earnings-quality fail or not GARP. Do not buy the bounce."
    if quality == "watch":
        return "Watch", "No official GARP ≥ 60 yet. Not auto-promoted after a crash."
    if not allow_buys:
        return "Hold", "Gates blocked new buys (pause or drawdown review-only)."
    close = row["close"]
    sma20 = row["sma20"]
    rsi14 = row["rsi14"]
    target = float(row.get("three_x_usd") or 0)
    stretched = sma20 and close > sma20 * 1.25
    overbought = rsi14 is not None and rsi14 >= 75
    already_there = target and close >= target * 0.85
    if stretched:
        return "Hold", "Pass name, but stretched more than 25% above the 20-day average."
    if overbought:
        return "Hold", "Pass name, but RSI is 75 or higher (overbought)."
    if already_there:
        return "Hold", "Already near the documented 3x marker."
    if not paper:
        return "Buy (paper)", "Pass quality, not stretched. Paper ticket only — GARP ≥ 60 still required before any live buy."
    return "Buy", "Pass quality, not stretched. This job still does not place the order."


def trim_to_one_buy(rows: list[dict], primary: str | None) -> None:
    buys = [r for r in rows if r["recommendation"] in {"Buy (paper)", "Buy"}]
    if len(buys) <= 1:
        return
    keep = next((r for r in buys if r["ticker"] == primary), buys[0])
    for r in buys:
        if r is keep:
            continue
        r["recommendation"] = "Hold"
        r["reason"] = "Second buy trimmed — max one paper candidate per morning."
        r["action"] = "HOLD"


def rank_key(row: dict) -> tuple:
    rec = row.get("recommendation", "Avoid")
    rec_rank = REC_RANK.get(rec, 9)
    buy_primary = 0 if rec_rank == 0 and row.get("role") == "primary_3x_rerate" else 1
    five = row.get("pct_5d")
    five_sort = -(five if five is not None else -999)
    return (rec_rank, buy_primary, five_sort, row["ticker"])


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
    payload = json.dumps(payload_obj).encode()
    req = urllib.request.Request(
        "https://api.resend.com/emails",
        data=payload,
        headers={
            "Authorization": f"Bearer {api_key}",
            "Content-Type": "application/json",
            "Accept": "application/json",
            "User-Agent": UA,
        },
        method="POST",
    )
    try:
        with urllib.request.urlopen(req, timeout=30) as resp:
            resp.read()
    except urllib.error.HTTPError as exc:
        detail = exc.read().decode("utf-8", "replace")[:500]
        outbox.mkdir(parents=True, exist_ok=True)
        stamp = datetime.now(TZ).strftime("%Y%m%d-%H%M%S")
        dest = outbox / f"{stamp}-{tag}.md"
        dest.write_text(f"# {subject}\n\n{text}\n", encoding="utf-8")
        print(f"Resend rejected the email ({exc.code}): {detail}", file=sys.stderr)
        print(f"Saved to outbox instead: {dest}", file=sys.stderr)
        return
    print(f"Email sent: {subject}")


def append_csv(csv_path: Path, rows: list[dict], day: str) -> None:
    csv_path.parent.mkdir(parents=True, exist_ok=True)
    existing: list[dict] = []
    if csv_path.exists():
        with csv_path.open(newline="", encoding="utf-8") as f:
            existing = [r for r in csv.DictReader(f) if r.get("date") != day]
    with csv_path.open("w", newline="", encoding="utf-8") as f:
        w = csv.DictWriter(f, fieldnames=CSV_FIELDS)
        w.writeheader()
        for r in existing:
            w.writerow({k: r.get(k, "") for k in CSV_FIELDS})
        for r in rows:
            w.writerow({k: "" if r.get(k) is None else r[k] for k in CSV_FIELDS})


def counts(rows: list[dict]) -> dict[str, int]:
    out = {k: 0 for k in ("Buy (paper)", "Buy", "Sell", "Hold", "Watch", "Avoid")}
    for r in rows:
        rec = r.get("recommendation", "Avoid")
        out[rec] = out.get(rec, 0) + 1
    return out


def build_report(day: str, gate_note: str, rows: list[dict], errors: list[str], meta: dict) -> str:
    ranked = sorted(rows, key=rank_key)
    buys = [r for r in ranked if r["recommendation"] in {"Buy (paper)", "Buy"}]
    today_line = "NONE — no buy today."
    if buys:
        b = buys[0]
        today_line = (
            f"**{b['recommendation']}: {b['ticker']}** at ${fmt(b['close'])} "
            f"(1d {signed(b['pct_1d'])}%, vs SMA20 {fmt(b['sma20'])}). "
            "Not a live Wealthsimple order."
        )

    table = [
        "| Rank | Ticker | List | Rec | Close | 1d % | 5d % | SMA20 | RSI14 | Why |",
        "|-----:|--------|------|-----|------:|-----:|-----:|------:|------:|-----|",
    ]
    for i, r in enumerate(ranked, 1):
        table.append(
            f"| {i} | {r['ticker']} | {r.get('list', '')} | {r['recommendation']} | "
            f"{fmt(r['close'])} | {signed(r['pct_1d'])} | {signed(r['pct_5d'])} | "
            f"{fmt(r['sma20'])} | {fmt(r['rsi14'], 1)} | {r.get('reason', '')} |"
        )

    err_block = ""
    if errors:
        err_block = "\n## Fetch errors\n\n" + "\n".join(f"- {e}" for e in errors) + "\n"

    return f"""# {meta['title']} — {day}

> I am an AI research assistant, not a licensed financial advisor. This is educational information, not personalized financial advice. Consider a qualified advisor for your situation.

**{gate_note}**

## What to buy today (from {len(rows)} names)

{today_line}

Official Rebalance-MCP GARP scores are not computed in this job. Quality flags come from `{meta.get('universe_rel', 'universe YAML')}`. A live ticket still needs GARP ≥ 60.

{chr(10).join(table)}

Prices: Yahoo Finance daily bars, {day} America/Toronto. SMA20 and RSI14 from the last 3 months of daily closes. Do not use Equibles for this routine price check.

{err_block}
## Rules

- Ranked Buy → Sell → Hold → Watch → Avoid. Max one Buy (paper) per morning.
- `Avoid` never becomes a buy because it bounced. `Sell` only if you already hold that avoid-quality name.
- `Watch` is not auto-promoted after a crash.
- This job never calls wsli and never sets TRADE_APPROVED.
"""


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


def build_digest_html(day: str, gate_note: str, rows: list[dict], errors: list[str]) -> str:
    ranked = sorted(rows, key=rank_key)
    n = counts(rows)
    buy_n = n.get("Buy (paper)", 0) + n.get("Buy", 0)
    buys = [r for r in ranked if r["recommendation"] in {"Buy (paper)", "Buy"}]
    if buys:
        b = buys[0]
        headline = (
            f"{html.escape(b['ticker'])} is today’s paper buy at ${fmt(b['close'])} "
            f"({signed(b['pct_1d'])}% today). Not a live Wealthsimple order."
        )
    else:
        headline = "No buy today. Scan both lists below — Watch names stay research-only until GARP ≥ 60."

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
    for i, r in enumerate(ranked, 1):
        bg = "#f9fafb" if i % 2 == 0 else "#ffffff"
        name = html.escape(r.get("name") or "")
        ticker = html.escape(r["ticker"])
        why = html.escape(r.get("reason") or "")
        lst = html.escape(r.get("list") or "")
        body_rows.append(
            f'<tr style="background:{bg};">'
            f'<td style="padding:10px 8px;text-align:center;color:#667085;">{i}</td>'
            f'<td style="padding:10px 8px;"><strong>{ticker}</strong>'
            f'<div style="font-size:11px;color:#667085;">{name}</div></td>'
            f'<td style="padding:10px 8px;font-size:12px;color:#667085;">{lst}</td>'
            f'<td style="padding:10px 8px;white-space:nowrap;">{_badge(r["recommendation"])}</td>'
            f'<td style="padding:10px 8px;text-align:right;font-variant-numeric:tabular-nums;">${fmt(r["close"])}</td>'
            f'<td style="padding:10px 8px;text-align:right;">{_chg_html(r["pct_1d"])}</td>'
            f'<td style="padding:10px 8px;text-align:right;">{_chg_html(r["pct_5d"])}</td>'
            f'<td style="padding:10px 8px;text-align:right;font-variant-numeric:tabular-nums;">{fmt(r["sma20"])}</td>'
            f'<td style="padding:10px 8px;text-align:right;font-variant-numeric:tabular-nums;">{fmt(r["rsi14"], 1)}</td>'
            f'<td style="padding:10px 8px;font-size:12px;color:#475467;">{why}</td>'
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
      <table role="presentation" width="720" cellspacing="0" cellpadding="0" style="max-width:720px;background:#ffffff;border-radius:16px;overflow:hidden;">
        <tr><td style="background:#0b1220;color:#ffffff;padding:24px 28px;">
          <div style="font-size:12px;letter-spacing:0.12em;text-transform:uppercase;color:#98a2b3;">1MillionPortfolio · TFSA paper scan</div>
          <div style="font-size:24px;font-weight:800;margin-top:6px;">Daily penny digest</div>
          <div style="font-size:14px;color:#d0d5dd;margin-top:4px;">{html.escape(day)} · America/Toronto · Yahoo daily bars</div>
        </td></tr>
        <tr><td style="padding:20px 28px 8px 28px;">
          <p style="margin:0 0 12px 0;font-size:15px;line-height:1.5;">{html.escape(headline)}</p>
          <p style="margin:0 0 16px 0;font-size:13px;color:#667085;">{html.escape(gate_note)}</p>
          <table role="presentation" width="100%" cellspacing="0" cellpadding="0"><tr>{card_html}</tr></table>
        </td></tr>
        <tr><td style="padding:8px 16px 20px 16px;">
          <table role="presentation" width="100%" cellspacing="0" cellpadding="0" style="border:1px solid #eaecf0;border-radius:12px;overflow:hidden;font-size:13px;">
            <tr style="background:#0b1220;color:#ffffff;">
              <th style="padding:10px 8px;text-align:center;">#</th>
              <th style="padding:10px 8px;text-align:left;">Ticker</th>
              <th style="padding:10px 8px;text-align:left;">List</th>
              <th style="padding:10px 8px;text-align:left;">Rec</th>
              <th style="padding:10px 8px;text-align:right;">Price</th>
              <th style="padding:10px 8px;text-align:right;">1d</th>
              <th style="padding:10px 8px;text-align:right;">5d</th>
              <th style="padding:10px 8px;text-align:right;">SMA20</th>
              <th style="padding:10px 8px;text-align:right;">RSI</th>
              <th style="padding:10px 8px;text-align:left;">Why</th>
            </tr>
            {''.join(body_rows)}
          </table>
        </td></tr>
        <tr><td style="padding:0 28px 24px 28px;font-size:12px;color:#667085;line-height:1.55;">
          {err_html}
          <p style="margin:0 0 8px 0;">Sorted Buy → Sell → Hold → Watch → Avoid. Primary 9 outranks the secondary watchlist when the recommendation is the same. SMA20 and RSI14 use 3 months of Yahoo daily closes. Official GARP scores are not computed here — live tickets still need GARP ≥ 60.</p>
          <p style="margin:0;">I am an AI research assistant, not a licensed financial advisor. This is educational information, not personalized financial advice. This job never calls wsli and never sets TRADE_APPROVED.</p>
        </td></tr>
      </table>
    </td></tr>
  </table>
</body></html>"""


def scan_universe(
    universe_path: Path,
    allow: bool,
    paper: bool,
    held: set[str],
    list_label: str,
) -> tuple[list[dict], list[str], dict]:
    universe = load_universe(universe_path)
    header = _read_simple_yaml_map(universe_path)
    slug = header.get("slug") or universe_path.stem
    meta = {
        "slug": slug,
        "title": header.get("report_title") or f"{slug} daily scan",
        "universe_rel": (
            universe_path.relative_to(ROOT).as_posix()
            if universe_path.is_relative_to(ROOT)
            else universe_path.as_posix()
        ),
        "primary": next((t["ticker"] for t in universe if t.get("role") == "primary_3x_rerate"), None),
        "list": list_label,
    }
    rows: list[dict] = []
    errors: list[str] = []
    for item in universe:
        ticker = item["ticker"]
        try:
            chart = fetch_chart(ticker)
        except (urllib.error.URLError, TimeoutError, RuntimeError, KeyError, IndexError, json.JSONDecodeError) as exc:
            errors.append(f"{ticker}: {exc}")
            continue
        series = chart["rows"]
        closes = [c for _, c, _ in series]
        last_ts, last_close, last_vol = series[-1]
        last_day = datetime.fromtimestamp(last_ts, tz=timezone.utc).date().isoformat()
        pct_1d = pct(last_close, closes[-2] if len(closes) >= 2 else None)
        pct_5d = pct(last_close, closes[-6] if len(closes) >= 6 else None)
        sma20 = mean(closes[-20:])
        rsi14 = rsi(closes, 14)
        rec = {
            "date": last_day,
            "ticker": ticker,
            "name": item.get("name", ""),
            "list": list_label,
            "role": item.get("role", ""),
            "close": round(last_close, 4),
            "volume": last_vol,
            "pct_1d": None if pct_1d is None else round(pct_1d, 3),
            "pct_5d": None if pct_5d is None else round(pct_5d, 3),
            "sma20": round(sma20, 4),
            "rsi14": None if rsi14 is None else round(rsi14, 2),
            "quality": item.get("quality", "avoid"),
            "three_x_usd": item.get("three_x_usd", ""),
            "action": "",
            "recommendation": "",
            "reason": "",
        }
        recommendation, reason = classify(rec, allow, paper, held)
        rec["recommendation"] = recommendation
        rec["reason"] = reason
        rec["action"] = REC_TO_ACTION.get(recommendation, "WATCH")
        rows.append(rec)
    return rows, errors, meta


def write_universe_outputs(day: str, gate_note: str, rows: list[dict], errors: list[str], meta: dict) -> Path:
    if not rows:
        raise RuntimeError(f"No quotes fetched for {meta['slug']}")
    csv_path = TIMESERIES / f"{meta['slug']}.csv"
    append_csv(csv_path, rows, rows[0]["date"])
    REPORTS.mkdir(parents=True, exist_ok=True)
    report = build_report(day, gate_note, rows, errors, meta)
    report_path = REPORTS / f"{day}-{meta['slug']}-scan.md"
    report_path.write_text(report, encoding="utf-8")
    print(report_path)
    return report_path


def parse_args(argv: list[str] | None = None) -> argparse.Namespace:
    p = argparse.ArgumentParser(description=__doc__)
    p.add_argument(
        "--universe",
        help="Scan a single universe YAML (no combined email). Default is the combined digest.",
    )
    p.add_argument(
        "--digest",
        action="store_true",
        help="Scan primary 9 + secondary 20 and send one ranked email.",
    )
    p.add_argument("--no-email", action="store_true", help="Write reports only; skip Resend.")
    return p.parse_args(argv)


def main(argv: list[str] | None = None) -> int:
    load_local_env()
    args = parse_args(argv)
    paper = paper_trading_complete()
    peak = _read_simple_yaml_map(PEAK)
    allow, gate_note = gates({"paper_trading_complete": "true" if paper else "false"}, peak)
    held = load_held_tickers()
    day = datetime.now(TZ).date().isoformat()
    run_digest = args.digest or args.universe is None

    if args.universe and not run_digest:
        universe_path = Path(args.universe)
        if not universe_path.is_absolute():
            universe_path = (ROOT / universe_path).resolve()
        if not universe_path.exists():
            print(f"Universe not found: {universe_path}", file=sys.stderr)
            return 1
        label = "Primary 9" if "penny9" in universe_path.name else "Secondary 20"
        rows, errors, meta = scan_universe(universe_path, allow, paper, held, label)
        if not rows:
            print("No quotes fetched.", file=sys.stderr)
            for e in errors:
                print(e, file=sys.stderr)
            return 1
        trim_to_one_buy(rows, meta.get("primary"))
        write_universe_outputs(day, gate_note, rows, errors, meta)
        if not args.no_email:
            send_email(
                f"1M Portfolio — {meta['title']} {day}",
                build_report(day, gate_note, rows, errors, meta),
                tag=meta["slug"],
            )
        return 0

    primary_rows, primary_err, primary_meta = scan_universe(
        PRIMARY_UNIVERSE, allow, paper, held, "Primary 9"
    )
    secondary_rows, secondary_err, secondary_meta = scan_universe(
        SECONDARY_UNIVERSE, allow, paper, held, "Secondary 20"
    )
    if not primary_rows and not secondary_rows:
        print("No quotes fetched.", file=sys.stderr)
        return 1

    trim_to_one_buy(primary_rows, primary_meta.get("primary"))
    # Secondary names are watch-only; never promote them even if a flag drifts.
    for r in secondary_rows:
        if r["recommendation"] in {"Buy (paper)", "Buy"}:
            r["recommendation"] = "Watch"
            r["reason"] = "Secondary list is watch-only until GARP ≥ 60 and an earnings-quality review."
            r["action"] = "WATCH"

    if primary_rows:
        write_universe_outputs(day, gate_note, primary_rows, primary_err, primary_meta)
    if secondary_rows:
        write_universe_outputs(day, gate_note, secondary_rows, secondary_err, secondary_meta)

    all_rows = primary_rows + secondary_rows
    all_err = primary_err + secondary_err
    digest_meta = {
        "title": "Penny digest (primary 9 + secondary 20)",
        "universe_rel": "portfolio/penny9-universe.yaml + portfolio/penny-secondary-watchlist.yaml",
        "primary": primary_meta.get("primary"),
    }
    digest = build_report(day, gate_note, all_rows, all_err, digest_meta)
    digest_path = REPORTS / f"{day}-penny-digest-scan.md"
    digest_path.write_text(digest, encoding="utf-8")
    print(digest_path)

    if not args.no_email:
        html_body = build_digest_html(day, gate_note, all_rows, all_err)
        send_email(
            f"1M Portfolio — Penny digest {day}",
            digest,
            html_body=html_body,
            tag="penny-digest",
        )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
