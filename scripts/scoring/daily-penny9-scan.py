#!/usr/bin/env python3
"""Weekday scanner for mega-cap core + penny-stock universes.

Fetches Yahoo daily bars (not Equibles — reserve that quota), appends
research/timeseries/<slug>.csv, writes markdown briefs, and emails one
ranked HTML digest. Never places trades.

Defaults to a combined digest: mega-cap core (NVDA/MSFT/GOOGL/AAPL) pinned
at the top, primary 9 + secondary 20 penny picks, plus a Markets & macro
brief (gold, Fed, US–Iran). Pass --universe to scan a single list.
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
import urllib.parse
import urllib.request
import xml.etree.ElementTree as ET
from datetime import datetime, timedelta, timezone
from pathlib import Path
from statistics import mean
from zoneinfo import ZoneInfo

ROOT = Path(__file__).resolve().parents[2]
PRIMARY_UNIVERSE = ROOT / "portfolio" / "penny9-universe.yaml"
SECONDARY_UNIVERSE = ROOT / "portfolio" / "penny-secondary-watchlist.yaml"
MEGA_UNIVERSE = ROOT / "portfolio" / "mega-cap-scan-universe.yaml"
PROFILE = ROOT / "portfolio" / "profile.yaml"
PEAK = ROOT / "portfolio" / "peak-value.yaml"
HOLDINGS = ROOT / "portfolio" / "holdings.yaml"
TIMESERIES = ROOT / "research" / "timeseries"
REPORTS = ROOT / "research" / "reports"
LOCAL_ENV_FILES = (ROOT / "config" / "wsli.env", ROOT / ".env")
TZ_NAME = "America/Denver"
GOLD_TICKER = "GC=F"
NEWS_TOPICS = (
    ("US–Iran", "US Iran"),
    ("Federal Reserve", "Federal Reserve"),
    ("Gold", "gold price"),
)

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
    for key in (TZ_NAME, "America/Denver", "MST7MDT", "America/Phoenix"):
        try:
            return ZoneInfo(key)
        except Exception:
            continue
    return timezone(timedelta(hours=-7))


TZ = _tz()
YAHOO = "https://query1.finance.yahoo.com/v8/finance/chart/{ticker}?range=3mo&interval=1d"
GOOGLE_NEWS_RSS = "https://news.google.com/rss/search?q={query}&hl=en-US&gl=US&ceid=US:en"
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
    encoded = urllib.parse.quote(ticker, safe="")
    req = urllib.request.Request(YAHOO.format(ticker=encoded), headers={"User-Agent": UA})
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


def fetch_gold_quote() -> dict:
    """Yahoo front-month gold futures (GC=F). Soft structure for digest macro block."""
    chart = fetch_chart(GOLD_TICKER)
    series = chart["rows"]
    closes = [c for _, c, _ in series]
    last_ts, last_close, _ = series[-1]
    day = datetime.fromtimestamp(last_ts, tz=timezone.utc).date().isoformat()
    pct_1d = pct(last_close, closes[-2] if len(closes) >= 2 else None)
    return {
        "ticker": GOLD_TICKER,
        "close": round(last_close, 2),
        "pct_1d": None if pct_1d is None else round(pct_1d, 3),
        "day": day,
        "source": "Yahoo Finance",
        "error": None,
    }


def fetch_news_bullets(query: str, limit: int = 2) -> list[dict]:
    """Google News RSS headlines. Returns [{title, link}] up to limit."""
    url = GOOGLE_NEWS_RSS.format(query=urllib.parse.quote_plus(query))
    req = urllib.request.Request(url, headers={"User-Agent": UA})
    ctx = ssl.create_default_context()
    with urllib.request.urlopen(req, timeout=20, context=ctx) as resp:
        raw = resp.read()
    root = ET.fromstring(raw)
    items: list[dict] = []
    for item in root.findall(".//item"):
        title = (item.findtext("title") or "").strip()
        link = (item.findtext("link") or "").strip()
        if not title:
            continue
        items.append({"title": title, "link": link})
        if len(items) >= limit:
            break
    return items


def build_macro_brief(day: str) -> dict:
    """Gold spot + Fed / US–Iran / gold headlines. Soft-fail per feed."""
    gold: dict = {
        "ticker": GOLD_TICKER,
        "close": None,
        "pct_1d": None,
        "day": day,
        "source": "Yahoo Finance",
        "error": None,
    }
    try:
        gold = fetch_gold_quote()
    except Exception as exc:  # noqa: BLE001 — digest must still send
        gold["error"] = str(exc)

    topics: list[dict] = []
    for label, query in NEWS_TOPICS:
        entry: dict = {"label": label, "query": query, "bullets": [], "error": None}
        try:
            entry["bullets"] = fetch_news_bullets(query, limit=2)
            if not entry["bullets"]:
                entry["error"] = "No headlines returned"
        except Exception as exc:  # noqa: BLE001
            entry["error"] = str(exc)
        topics.append(entry)

    return {"day": day, "gold": gold, "topics": topics, "source": "Google News RSS + Yahoo Finance"}


def format_macro_markdown(macro: dict) -> str:
    gold = macro.get("gold") or {}
    lines = ["## Markets & macro", ""]
    if gold.get("error"):
        lines.append(f"**Gold ({GOLD_TICKER}):** unavailable — {gold['error']}")
    else:
        lines.append(
            f"**Gold ({GOLD_TICKER}):** ${fmt(gold.get('close'))} "
            f"({signed(gold.get('pct_1d'))}% 1d) — {gold.get('source', 'Yahoo Finance')}, "
            f"{gold.get('day', macro.get('day', ''))}."
        )
    lines.append("")
    for topic in macro.get("topics") or []:
        lines.append(f"### {topic['label']}")
        if topic.get("error"):
            lines.append(f"- Unavailable: {topic['error']}")
        else:
            for b in topic.get("bullets") or []:
                title = b.get("title") or ""
                link = b.get("link") or ""
                if link:
                    lines.append(f"- [{title}]({link})")
                else:
                    lines.append(f"- {title}")
        lines.append("")
    lines.append(
        f"_Headlines: Google News RSS · Gold: Yahoo Finance · as of {macro.get('day', '')} {TZ_NAME}. "
        "Educational summary only — not investment advice._"
    )
    lines.append("")
    return "\n".join(lines)


def format_macro_html(macro: dict) -> str:
    gold = macro.get("gold") or {}
    if gold.get("error"):
        gold_line = (
            f'<p style="margin:0 0 12px 0;font-size:14px;">'
            f'<strong>Gold ({html.escape(GOLD_TICKER)}):</strong> unavailable — '
            f'{html.escape(str(gold["error"]))}</p>'
        )
    else:
        gold_line = (
            f'<p style="margin:0 0 12px 0;font-size:14px;">'
            f'<strong>Gold ({html.escape(GOLD_TICKER)}):</strong> '
            f'${fmt(gold.get("close"))} ({_chg_html(gold.get("pct_1d"))} 1d) · '
            f'{html.escape(str(gold.get("source") or "Yahoo Finance"))}, '
            f'{html.escape(str(gold.get("day") or ""))}</p>'
        )

    topic_blocks: list[str] = []
    for topic in macro.get("topics") or []:
        label = html.escape(topic.get("label") or "")
        if topic.get("error"):
            body = f'<li style="margin:0 0 4px 0;color:#667085;">Unavailable: {html.escape(str(topic["error"]))}</li>'
        else:
            items = []
            for b in topic.get("bullets") or []:
                title = html.escape(b.get("title") or "")
                link = html.escape(b.get("link") or "", quote=True)
                if link:
                    items.append(
                        f'<li style="margin:0 0 6px 0;line-height:1.45;">'
                        f'<a href="{link}" style="color:#175cd3;text-decoration:none;">{title}</a></li>'
                    )
                else:
                    items.append(f'<li style="margin:0 0 6px 0;line-height:1.45;">{title}</li>')
            body = "".join(items) or '<li style="color:#667085;">No headlines</li>'
        topic_blocks.append(
            f'<div style="margin:0 0 14px 0;">'
            f'<div style="font-size:12px;font-weight:700;letter-spacing:0.04em;text-transform:uppercase;'
            f'color:#475467;margin-bottom:6px;">{label}</div>'
            f'<ul style="margin:0;padding-left:18px;font-size:13px;color:#344054;">{body}</ul></div>'
        )

    return f"""
        <tr><td style="padding:8px 28px 24px 28px;">
          <div style="border:1px solid #eaecf0;border-radius:12px;padding:16px 18px;background:#f9fafb;">
            <div style="font-size:12px;letter-spacing:0.08em;text-transform:uppercase;color:#667085;font-weight:700;">Markets &amp; macro</div>
            <div style="font-size:18px;font-weight:800;margin:4px 0 12px 0;color:#101828;">US–Iran · Fed · Gold</div>
            {gold_line}
            {''.join(topic_blocks)}
            <p style="margin:8px 0 0 0;font-size:11px;color:#98a2b3;line-height:1.45;">
              Headlines: Google News RSS · Gold: Yahoo Finance · {html.escape(str(macro.get('day') or ''))} {TZ_NAME}.
              Educational summary only — not investment advice.
            </p>
          </div>
        </td></tr>"""


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


EMAIL_TOP_N = 10
ACTION_RECS = {"Buy (paper)", "Buy", "Sell"}


def top_email_rows(rows: list[dict], n: int = EMAIL_TOP_N) -> list[dict]:
    """Buy and Sell first, then Hold/Watch/Avoid, capped at n."""
    ranked = sorted(rows, key=rank_key)
    action = [r for r in ranked if r["recommendation"] in ACTION_RECS]
    rest = [r for r in ranked if r["recommendation"] not in ACTION_RECS]
    return (action + rest)[:n]


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


def _mega_markdown(mega_rows: list[dict]) -> str:
    if not mega_rows:
        return ""
    lines = [
        "## Mega-cap core",
        "",
        "| Ticker | Name | Close | 1d % | 5d % | SMA20 | RSI14 | Note |",
        "|--------|------|------:|-----:|-----:|------:|------:|------|",
    ]
    for r in mega_rows:
        lines.append(
            f"| {r['ticker']} | {r.get('name', '')} | {fmt(r['close'])} | "
            f"{signed(r['pct_1d'])} | {signed(r['pct_5d'])} | {fmt(r['sma20'])} | "
            f"{fmt(r['rsi14'], 1)} | Display-only (watch) — not a paper Buy from this job. |"
        )
    lines.append("")
    return "\n".join(lines)


def build_report(
    day: str,
    gate_note: str,
    rows: list[dict],
    errors: list[str],
    meta: dict,
    mega_rows: list[dict] | None = None,
    macro: dict | None = None,
) -> str:
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

    mega_block = _mega_markdown(mega_rows or [])
    if mega_block and not mega_block.endswith("\n\n"):
        mega_block = mega_block.rstrip("\n") + "\n\n"
    macro_block = format_macro_markdown(macro) if macro else ""

    return f"""# {meta['title']} — {day}

> I am an AI research assistant, not a licensed financial advisor. This is educational information, not personalized financial advice. Consider a qualified advisor for your situation.

**{gate_note}**

{mega_block}## What to buy today (from {len(rows)} names)

{today_line}

Official Rebalance-MCP GARP scores are not computed in this job. Quality flags come from `{meta.get('universe_rel', 'universe YAML')}`. A live ticket still needs GARP ≥ 60.

{chr(10).join(table)}

Prices: Yahoo Finance daily bars, {day} {TZ_NAME}. SMA20 and RSI14 from the last 3 months of daily closes. Do not use Equibles for this routine price check.

{macro_block}{err_block}
## Rules

- Ranked Buy → Sell → Hold → Watch → Avoid. Max one Buy (paper) per morning.
- Mega-cap core (NVDA / MSFT / GOOGL / AAPL) is display-only in the digest top section — never the morning paper Buy.
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


def _mega_table_html(mega_rows: list[dict]) -> str:
    if not mega_rows:
        return ""
    body_rows = []
    for i, r in enumerate(mega_rows, 1):
        bg = "#f9fafb" if i % 2 == 0 else "#ffffff"
        name = html.escape(r.get("name") or "")
        ticker = html.escape(r["ticker"])
        body_rows.append(
            f'<tr style="background:{bg};">'
            f'<td style="padding:12px 8px;width:90px;"><strong style="font-size:15px;">{ticker}</strong>'
            f'<div style="font-size:11px;color:#667085;">{name}</div></td>'
            f'<td style="padding:12px 8px;text-align:right;font-variant-numeric:tabular-nums;width:70px;">${fmt(r["close"])}</td>'
            f'<td style="padding:12px 8px;text-align:right;width:62px;">{_chg_html(r["pct_1d"])}</td>'
            f'<td style="padding:12px 8px;text-align:right;width:62px;">{_chg_html(r["pct_5d"])}</td>'
            f'<td style="padding:12px 10px 12px 12px;font-size:13px;line-height:1.45;color:#344054;">'
            f'Display-only · RSI {fmt(r.get("rsi14"), 1)} · SMA20 ${fmt(r.get("sma20"))}</td>'
            f"</tr>"
        )
    return f"""
        <tr><td style="padding:20px 16px 8px 16px;">
          <div style="padding:0 12px 10px 12px;">
            <div style="font-size:12px;letter-spacing:0.08em;text-transform:uppercase;color:#667085;font-weight:700;">Scanner · top section</div>
            <div style="font-size:18px;font-weight:800;margin-top:2px;color:#101828;">Mega-cap core</div>
            <div style="font-size:12px;color:#667085;margin-top:2px;">NVDA · MSFT · GOOGL · AAPL — watch only, not the morning paper Buy</div>
          </div>
          <table role="presentation" width="100%" cellspacing="0" cellpadding="0" style="border:1px solid #eaecf0;border-radius:12px;overflow:hidden;font-size:13px;">
            <tr style="background:#1d2939;color:#ffffff;">
              <th style="padding:10px 8px;text-align:left;width:90px;">Ticker</th>
              <th style="padding:10px 8px;text-align:right;width:70px;">Price</th>
              <th style="padding:10px 8px;text-align:right;width:62px;">1d</th>
              <th style="padding:10px 8px;text-align:right;width:62px;">5d</th>
              <th style="padding:10px 12px;text-align:left;">Note</th>
            </tr>
            {''.join(body_rows)}
          </table>
        </td></tr>"""


def build_digest_html(
    day: str,
    gate_note: str,
    rows: list[dict],
    errors: list[str],
    mega_rows: list[dict] | None = None,
    macro: dict | None = None,
) -> str:
    ranked = sorted(rows, key=rank_key)
    picks = top_email_rows(rows)
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
        headline = "No buy today. Top 10 below are ranked Sell first, then Hold/Watch. Watch stays research-only until GARP ≥ 60."

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

    mega_html = _mega_table_html(mega_rows or [])
    macro_html = format_macro_html(macro) if macro else ""

    return f"""<!DOCTYPE html>
<html><body style="margin:0;padding:0;background:#eef2f6;font-family:-apple-system,BlinkMacSystemFont,'Segoe UI',Helvetica,Arial,sans-serif;color:#101828;">
  <table role="presentation" width="100%" cellspacing="0" cellpadding="0" style="background:#eef2f6;padding:24px 12px;">
    <tr><td align="center">
      <table role="presentation" width="760" cellspacing="0" cellpadding="0" style="max-width:760px;background:#ffffff;border-radius:16px;overflow:hidden;">
        <tr><td style="background:#0b1220;color:#ffffff;padding:24px 28px;">
          <div style="font-size:12px;letter-spacing:0.12em;text-transform:uppercase;color:#98a2b3;">1MillionPortfolio · TFSA paper scan</div>
          <div style="font-size:24px;font-weight:800;margin-top:6px;">Morning digest</div>
          <div style="font-size:14px;color:#d0d5dd;margin-top:4px;">{html.escape(day)} · {TZ_NAME} · Yahoo daily bars</div>
        </td></tr>
        {mega_html}
        <tr><td style="padding:20px 28px 8px 28px;">
          <div style="font-size:12px;letter-spacing:0.08em;text-transform:uppercase;color:#667085;font-weight:700;margin-bottom:4px;">Penny sleeve</div>
          <div style="font-size:18px;font-weight:800;margin:0 0 10px 0;color:#101828;">Top 10 penny picks</div>
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
        {macro_html}
        <tr><td style="padding:0 28px 24px 28px;font-size:12px;color:#667085;line-height:1.55;">
          {err_html}
          <p style="margin:0 0 8px 0;">Penny table shows the top {len(picks)} of {len(rows)} names, ranked Buy → Sell → Hold → Watch → Avoid so Buy/Sell sit first. Mega-caps stay pinned above and never take the paper Buy slot. SMA20 and RSI stay in the saved markdown report. Official GARP scores are not computed here — live tickets still need GARP ≥ 60.</p>
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
        help="Scan mega-cap core + primary 9 + secondary 20, add macro brief, send one ranked email.",
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

    mega_rows, mega_err, mega_meta = scan_universe(
        MEGA_UNIVERSE, allow, paper, held, "Mega-cap"
    )
    # Mega-caps are digest display-only — never the morning paper Buy.
    for r in mega_rows:
        if r["recommendation"] in {"Buy (paper)", "Buy", "Sell"}:
            r["recommendation"] = "Watch"
            r["reason"] = "Mega-cap core is display-only in the digest — not a paper Buy from this job."
            r["action"] = "WATCH"

    primary_rows, primary_err, primary_meta = scan_universe(
        PRIMARY_UNIVERSE, allow, paper, held, "Primary 9"
    )
    secondary_rows, secondary_err, secondary_meta = scan_universe(
        SECONDARY_UNIVERSE, allow, paper, held, "Secondary 20"
    )
    if not primary_rows and not secondary_rows and not mega_rows:
        print("No quotes fetched.", file=sys.stderr)
        return 1

    trim_to_one_buy(primary_rows, primary_meta.get("primary"))
    # Secondary names are watch-only; never promote them even if a flag drifts.
    for r in secondary_rows:
        if r["recommendation"] in {"Buy (paper)", "Buy"}:
            r["recommendation"] = "Watch"
            r["reason"] = "Secondary list is watch-only until GARP ≥ 60 and an earnings-quality review."
            r["action"] = "WATCH"

    if mega_rows:
        write_universe_outputs(day, gate_note, mega_rows, mega_err, mega_meta)
    if primary_rows:
        write_universe_outputs(day, gate_note, primary_rows, primary_err, primary_meta)
    if secondary_rows:
        write_universe_outputs(day, gate_note, secondary_rows, secondary_err, secondary_meta)

    all_rows = primary_rows + secondary_rows
    all_err = mega_err + primary_err + secondary_err
    macro = build_macro_brief(day)
    digest_meta = {
        "title": "Morning digest (mega-cap + primary 9 + secondary 20)",
        "universe_rel": (
            "portfolio/mega-cap-scan-universe.yaml + portfolio/penny9-universe.yaml "
            "+ portfolio/penny-secondary-watchlist.yaml"
        ),
        "primary": primary_meta.get("primary"),
    }
    digest = build_report(
        day, gate_note, all_rows, all_err, digest_meta, mega_rows=mega_rows, macro=macro
    )
    digest_path = REPORTS / f"{day}-penny-digest-scan.md"
    digest_path.write_text(digest, encoding="utf-8")
    print(digest_path)

    if not args.no_email:
        html_body = build_digest_html(
            day, gate_note, all_rows, all_err, mega_rows=mega_rows, macro=macro
        )
        send_email(
            f"1M Portfolio — Morning digest {day}",
            digest,
            html_body=html_body,
            tag="penny-digest",
        )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
