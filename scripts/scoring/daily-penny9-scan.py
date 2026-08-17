#!/usr/bin/env python3
"""Weekday scanner for a penny-stock universe.

Fetches Yahoo daily bars (not Equibles — reserve that quota), appends
research/timeseries/<slug>.csv, writes a markdown brief, and optionally emails
via Resend. Never places trades.

Defaults to portfolio/penny9-universe.yaml. Pass --universe to scan another
list, e.g. portfolio/penny-secondary-watchlist.yaml.
"""

from __future__ import annotations

import argparse
import csv
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
UNIVERSE = ROOT / "portfolio" / "penny9-universe.yaml"
PROFILE = ROOT / "portfolio" / "profile.yaml"
PEAK = ROOT / "portfolio" / "peak-value.yaml"
TIMESERIES = ROOT / "research" / "timeseries"
REPORTS = ROOT / "research" / "reports"
LOCAL_ENV_FILES = (ROOT / "config" / "wsli.env", ROOT / ".env")


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


def gates(profile: dict, peak: dict) -> tuple[bool, str]:
    if os.environ.get("PAUSE_ALL_TRADING", "").lower() == "true":
        return False, "PAUSE_ALL_TRADING is set — no buy proposals."
    if peak.get("mode") == "review_only":
        return False, "Drawdown review-only mode — no new buy proposals."
    paper = profile.get("paper_trading_complete", "false").lower() == "true"
    if not paper:
        return True, "Paper trading active — dry-run only. Recommendations are PAPER_CANDIDATE at most, never LIVE_BUY."
    return True, "Paper trading complete in profile — still no live execution from this job."


def decide(row: dict, allow_buys: bool, paper: bool) -> str:
    if not allow_buys:
        return "NONE"
    quality = row.get("quality", "avoid")
    if quality == "avoid":
        return "AVOID"
    if quality == "watch":
        return "WATCH"
    if quality == "pass":
        close = row["close"]
        sma20 = row["sma20"]
        rsi14 = row["rsi14"]
        target = float(row.get("three_x_usd") or 0)
        stretched = sma20 and close > sma20 * 1.25
        overbought = rsi14 is not None and rsi14 >= 75
        already_there = target and close >= target * 0.85
        if stretched or overbought or already_there:
            return "WATCH"
        return "PAPER_CANDIDATE" if not paper else "CANDIDATE"
    return "WATCH"


def send_email(subject: str, body: str, tag: str = "daily_scan") -> None:
    api_key = os.environ.get("RESEND_API_KEY")
    to = os.environ.get("NOTIFY_EMAIL_TO")
    from_addr = os.environ.get("NOTIFY_EMAIL_FROM", "portfolio@yourdomain.com")
    outbox = ROOT / "portfolio" / "cache" / "email-outbox"
    if not api_key or not to:
        outbox.mkdir(parents=True, exist_ok=True)
        stamp = datetime.now(TZ).strftime("%Y%m%d-%H%M%S")
        dest = outbox / f"{stamp}-{tag}.md"
        dest.write_text(f"# {subject}\n\n{body}\n", encoding="utf-8")
        print(f"Email skipped (missing secrets). Saved {dest}")
        return
    payload = json.dumps({"from": from_addr, "to": [to], "subject": subject, "text": body}).encode()
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
        dest.write_text(f"# {subject}\n\n{body}\n", encoding="utf-8")
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
            w.writerow({k: r[k] for k in CSV_FIELDS})


def build_report(day: str, gate_note: str, rows: list[dict], errors: list[str], meta: dict) -> str:
    ranked = sorted(rows, key=lambda r: (0 if r["action"] == "PAPER_CANDIDATE" or r["action"] == "CANDIDATE" else 1, r["ticker"]))
    buys = [r for r in rows if r["action"] in {"PAPER_CANDIDATE", "CANDIDATE"}]
    if len(buys) > 1:
        primary = meta.get("primary")
        keep = next((r for r in buys if r["ticker"] == primary), buys[0])
        for r in buys:
            if r is not keep:
                r["action"] = "WATCH"
        buys = [keep]

    today_line = "NONE — no buy today."
    if buys:
        b = buys[0]
        today_line = (
            f"**{b['action']}: {b['ticker']}** at ${fmt(b['close'])} "
            f"(1d {fmt(b['pct_1d'])}%, vs SMA20 {fmt(b['sma20'])}). "
            "Not a live Wealthsimple order."
        )

    table = [
        "| Ticker | Close | 1d % | 5d % | SMA20 | RSI14 | Quality | Action |",
        "|--------|------:|-----:|-----:|------:|------:|---------|--------|",
    ]
    for r in ranked:
        table.append(
            f"| {r['ticker']} | {fmt(r['close'])} | {fmt(r['pct_1d'])} | {fmt(r['pct_5d'])} | "
            f"{fmt(r['sma20'])} | {fmt(r['rsi14'], 1)} | {r['quality']} | {r['action']} |"
        )

    err_block = ""
    if errors:
        err_block = "\n## Fetch errors\n\n" + "\n".join(f"- {e}" for e in errors) + "\n"

    watch_only = all(r["quality"] != "pass" for r in rows)
    tier_note = (
        "Every name on this list is flagged `watch`, so the scanner cannot promote any of them. "
        "Getting to a candidate requires a Rebalance-MCP GARP score of 60 or better plus an earnings-quality review."
        if watch_only
        else "A `pass` name still needs GARP >= 60 before any live ticket."
    )

    return f"""# {meta['title']} — {day}

> I am an AI research assistant, not a licensed financial advisor. This is educational information, not personalized financial advice. Consider a qualified advisor for your situation.

**{gate_note}**

## What to buy today (from {len(rows)} names)

{today_line}

Official Rebalance-MCP GARP scores are not computed in this job. Quality flags come from `{meta['universe_rel']}`. {tier_note}

{chr(10).join(table)}

Prices: Yahoo Finance daily bars, {day} America/Toronto. SMA20 and RSI14 from the last 3 months of daily closes. Do not use Equibles for this routine price check.

{err_block}
## Rules

- Max one candidate per morning.
- `avoid` never becomes a buy because it bounced.
- `watch` is not auto-promoted after a crash.
- This job never calls wsli and never sets TRADE_APPROVED.
"""


def parse_args(argv: list[str] | None = None) -> argparse.Namespace:
    p = argparse.ArgumentParser(description=__doc__)
    p.add_argument(
        "--universe",
        default=str(UNIVERSE),
        help="Universe YAML to scan (default: portfolio/penny9-universe.yaml)",
    )
    return p.parse_args(argv)


def main(argv: list[str] | None = None) -> int:
    load_local_env()
    args = parse_args(argv)
    universe_path = Path(args.universe)
    if not universe_path.is_absolute():
        universe_path = (ROOT / universe_path).resolve()
    if not universe_path.exists():
        print(f"Universe not found: {universe_path}", file=sys.stderr)
        return 1

    now = datetime.now(TZ)
    day = now.date().isoformat()
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
        "primary": next(
            (t["ticker"] for t in universe if t.get("role") == "primary_3x_rerate"),
            None,
        ),
    }
    csv_path = TIMESERIES / f"{slug}.csv"

    profile = _read_simple_yaml_map(PROFILE)
    # Nested keys: paper_trading_complete lives under execution
    paper_complete = False
    for raw in PROFILE.read_text(encoding="utf-8").splitlines():
        if "paper_trading_complete:" in raw:
            paper_complete = raw.split(":", 1)[1].strip().lower() == "true"
    peak = _read_simple_yaml_map(PEAK)
    allow, gate_note = gates(
        {"paper_trading_complete": "true" if paper_complete else "false"},
        peak,
    )

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
            "close": round(last_close, 4),
            "volume": last_vol,
            "pct_1d": None if pct_1d is None else round(pct_1d, 3),
            "pct_5d": None if pct_5d is None else round(pct_5d, 3),
            "sma20": round(sma20, 4),
            "rsi14": None if rsi14 is None else round(rsi14, 2),
            "quality": item.get("quality", "avoid"),
            "three_x_usd": item.get("three_x_usd", ""),
            "action": "",
        }
        rec["action"] = decide(rec, allow, paper_complete)
        rows.append(rec)

    if not rows:
        print("No quotes fetched.", file=sys.stderr)
        for e in errors:
            print(e, file=sys.stderr)
        return 1

    # CSV keyed by Yahoo last bar date (usually last US session).
    csv_day = rows[0]["date"]
    csv_rows = []
    for r in rows:
        csv_rows.append({k: "" if r.get(k) is None else r[k] for k in CSV_FIELDS})
    append_csv(csv_path, csv_rows, csv_day)

    REPORTS.mkdir(parents=True, exist_ok=True)
    report = build_report(day, gate_note, rows, errors, meta)
    report_path = REPORTS / f"{day}-{slug}-scan.md"
    report_path.write_text(report, encoding="utf-8")
    print(report_path)

    send_email(f"1M Portfolio — {meta['title']} {day}", report, tag=slug)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
