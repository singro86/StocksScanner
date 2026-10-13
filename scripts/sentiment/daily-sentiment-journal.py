#!/usr/bin/env python3
"""RAVEN Morning Journal — AI-Powered Market Intelligence by Rohit.

Two editions (GitHub Actions cron):
  --edition morning    Overnight headlines + macro dashboard + risk-on/off
  --edition premarket  Analyst / options / retail + sentiment+price agreement list

Reuses Yahoo Finance HTTP patterns and Resend email from daily-penny9-scan.py.
Sentiment journal only — never places trades or proposes buy/sell tickets.
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
import xml.etree.ElementTree as ET
from datetime import datetime, timedelta, timezone
from email.utils import parsedate_to_datetime
from pathlib import Path
from statistics import mean
from zoneinfo import ZoneInfo

ROOT = Path(__file__).resolve().parents[2]
CONFIG = ROOT / "config" / "sentiment-sources.yaml"
PRIMARY_UNIVERSE = ROOT / "portfolio" / "penny9-universe.yaml"
SECONDARY_UNIVERSE = ROOT / "portfolio" / "penny-secondary-watchlist.yaml"
WATCHLIST = ROOT / "portfolio" / "watchlist.yaml"
PROFILE = ROOT / "portfolio" / "profile.yaml"
PEAK = ROOT / "portfolio" / "peak-value.yaml"
HOLDINGS = ROOT / "portfolio" / "holdings.yaml"
TIMESERIES = ROOT / "research" / "timeseries"
REPORTS = ROOT / "research" / "reports"
LOCAL_ENV_FILES = (ROOT / "config" / "wsli.env", ROOT / ".env")

UA = "Mozilla/5.0 (compatible; 1MillionPortfolio/1.0; raven-morning-journal)"
YAHOO_CHART = "https://query1.finance.yahoo.com/v8/finance/chart/{ticker}?range=3mo&interval=1d"
YAHOO_QUOTE = "https://query1.finance.yahoo.com/v7/finance/quote?symbols={symbols}"
YAHOO_SUMMARY = (
    "https://query2.finance.yahoo.com/v10/finance/quoteSummary/{ticker}"
    "?modules=upgradeDowngradeHistory&crumb={crumb}"
)
YAHOO_OPTIONS = "https://query2.finance.yahoo.com/v7/finance/options/{ticker}?crumb={crumb}"
YAHOO_CRUMB = "https://query2.finance.yahoo.com/v1/test/getcrumb"
YAHOO_COOKIE = "https://fc.yahoo.com"

CSV_FIELDS = [
    "date",
    "edition",
    "risk_verdict",
    "risk_score",
    "vix",
    "vix3m",
    "fear_greed",
    "es_pct",
    "nq_pct",
    "breadth_pct",
    "top_tickers",
    "top_scores",
    "headline_count",
    "notes",
]

TICKER_RE = re.compile(r"\b([A-Z]{1,5})\b")
COMMON_WORDS = {
    "A", "I", "US", "CEO", "CFO", "IPO", "ETF", "GDP", "CPI", "FED", "SEC", "AI",
    "DD", "YOLO", "IMO", "ATM", "OTM", "ITM", "EPS", "PE", "ATH", "ALL", "THE",
    "AND", "FOR", "ARE", "BUT", "NOT", "YOU", "CAN", "HAS", "WAS", "NEW", "NOW",
    "OUT", "TOP", "BIG", "LOW", "HIGH", "BUY", "SELL", "HOLD", "CALL", "PUT",
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
    for key in ("America/Toronto", "America/New_York", "America/Edmonton", "EST5EDT"):
        try:
            return ZoneInfo(key)
        except Exception:
            continue
    return timezone(timedelta(hours=-4))


TZ = _tz()


# --- minimal YAML helpers (stdlib only; config is intentionally simple) ---


def _parse_scalar(val: str):
    v = val.strip().strip('"').strip("'")
    if v.lower() in {"true", "false"}:
        return v.lower() == "true"
    if v.startswith("[") and v.endswith("]"):
        inner = v[1:-1].strip()
        if not inner:
            return []
        parts = [p.strip() for p in inner.split(",")]
        out = []
        for p in parts:
            try:
                out.append(int(p) if "." not in p else float(p))
            except ValueError:
                out.append(p.strip('"').strip("'"))
        return out
    try:
        if "." in v:
            return float(v)
        return int(v)
    except ValueError:
        return v


def load_sources_config(path: Path = CONFIG) -> dict:
    """Parse the flat-ish sentiment-sources.yaml without PyYAML."""
    cfg: dict = {
        "brand": "RAVEN Morning Journal",
        "brand_full": "RAVEN — AI-Powered Market Intelligence by Rohit",
        "brand_tag": "RAVEN",
        "macro_tickers": [],
        "rss_feeds": [],
        "retail_rss": [],
        "headline_limit": 8,
        "stocktwits": {},
        "yahoo_trending_url": "https://query1.finance.yahoo.com/v1/finance/trending/US?count=20",
        "fear_greed_url": "https://production.dataviz.cnn.io/index/fearandgreed/graphdata",
        "market_option_gauges": ["SPY", "QQQ"],
        "score_weights": {
            "news_catalyst": 2,
            "analyst_revisions": 2,
            "options_flow": 1,
            "social_sentiment": 1,
            "price_volume": 2,
        },
        "score_bands": {"strong": [8, 11], "watch": [5, 7], "weak": [3, 4], "avoid": [0, 2]},
        "agreement_top_n": 10,
        "agreement_min_score": 5,
        "risk_verdict": {"vix_elevated": 20, "vix_calm": 15},
        "editions": {},
    }
    if not path.exists():
        return cfg

    current_list: str | None = None
    current_item: dict | None = None
    current_map: str | None = None
    current_nested: str | None = None

    def flush_item():
        nonlocal current_item
        if current_list and current_item:
            cfg.setdefault(current_list, []).append(current_item)
        current_item = None

    for raw in path.read_text(encoding="utf-8").splitlines():
        if not raw.strip() or raw.lstrip().startswith("#"):
            continue
        indent = len(raw) - len(raw.lstrip(" "))
        line = raw.split("#", 1)[0].rstrip()
        stripped = line.strip()

        if indent == 0 and stripped.endswith(":") and ":" == stripped[-1]:
            flush_item()
            key = stripped[:-1]
            current_list = None
            current_map = None
            current_nested = None
            if key in {
                "macro_tickers",
                "rss_feeds",
                "retail_rss",
                "market_option_gauges",
            }:
                current_list = key
                cfg[key] = []
            elif key in {"stocktwits", "score_weights", "score_bands", "risk_verdict", "editions"}:
                current_map = key
                cfg[key] = {}
            else:
                current_map = None
            continue

        if indent == 0 and ":" in stripped:
            flush_item()
            current_list = current_map = current_nested = None
            key, val = stripped.split(":", 1)
            if val.strip():
                cfg[key.strip()] = _parse_scalar(val)
            continue

        if current_list == "market_option_gauges" and stripped.startswith("- "):
            cfg["market_option_gauges"].append(stripped[2:].strip().strip('"').strip("'"))
            continue

        if current_list in {"macro_tickers", "rss_feeds", "retail_rss"}:
            if stripped.startswith("- "):
                flush_item()
                rest = stripped[2:]
                current_item = {}
                if ":" in rest:
                    k, v = rest.split(":", 1)
                    current_item[k.strip()] = _parse_scalar(v)
                continue
            if current_item is not None and ":" in stripped:
                k, v = stripped.split(":", 1)
                current_item[k.strip()] = _parse_scalar(v)
            continue

        if current_map and indent == 2:
            flush_item()
            if stripped.endswith(":") and not stripped.startswith("-"):
                current_nested = stripped[:-1]
                cfg[current_map][current_nested] = {}
                continue
            if ":" in stripped:
                k, v = stripped.split(":", 1)
                if v.strip():
                    cfg[current_map][k.strip()] = _parse_scalar(v)
                else:
                    current_nested = k.strip()
                    cfg[current_map][current_nested] = {}
            continue

        if current_map and current_nested and indent >= 4 and ":" in stripped:
            k, v = stripped.split(":", 1)
            cfg[current_map][current_nested][k.strip()] = _parse_scalar(v)

    flush_item()
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


def load_universe_tickers(path: Path) -> list[str]:
    tickers: list[str] = []
    if not path.exists():
        return tickers
    for raw in path.read_text(encoding="utf-8").splitlines():
        line = raw.split("#", 1)[0].rstrip()
        stripped = line.strip()
        if stripped.startswith("- ticker:"):
            t = stripped.split(":", 1)[1].strip().strip('"').strip("'")
            if t and t.lower() != "null":
                tickers.append(t.upper())
    return tickers


def load_watchlist_tickers() -> list[str]:
    tickers: list[str] = []
    if not WATCHLIST.exists():
        return tickers
    for raw in WATCHLIST.read_text(encoding="utf-8").splitlines():
        line = raw.split("#", 1)[0].rstrip()
        stripped = line.strip()
        if stripped.startswith("- ticker:"):
            t = stripped.split(":", 1)[1].strip().strip('"').strip("'")
            if t and t.lower() != "null":
                tickers.append(t.upper())
    return tickers


def load_held_tickers() -> list[str]:
    held: list[str] = []
    if not HOLDINGS.exists():
        return held
    in_positions = False
    for raw in HOLDINGS.read_text(encoding="utf-8").splitlines():
        if raw.startswith("positions:"):
            in_positions = True
            continue
        if in_positions and raw.strip().startswith("- ticker:"):
            held.append(raw.split(":", 1)[1].strip().strip('"').strip("'").upper())
    return held


def paper_trading_complete() -> bool:
    if not PROFILE.exists():
        return False
    for raw in PROFILE.read_text(encoding="utf-8").splitlines():
        if "paper_trading_complete:" in raw:
            return raw.split(":", 1)[1].strip().lower() == "true"
    return False


def console_status(peak: dict, paper_done: bool) -> str:
    """Operator-only status for stdout — never shown in the email body."""
    parts = []
    if not paper_done:
        parts.append("paper trading active")
    mode = peak.get("mode", "normal")
    if mode == "review_only":
        parts.append("drawdown review-only")
    if os.environ.get("PAUSE_ALL_TRADING", "").lower() == "true":
        parts.append("PAUSE_ALL_TRADING")
    return ", ".join(parts) if parts else "ok"


def public_errors(errors: list[str]) -> list[str]:
    """Drop blocked/auth noise from reader-facing notes (403/401/Forbidden)."""
    skip = ("403", "401", "blocked", "forbidden", "unauthorized")
    kept = []
    for e in errors:
        low = e.lower()
        if any(s in low for s in skip):
            continue
        kept.append(e)
    return collapse_errors(kept)


# --- HTTP ---


class YahooSession:
    """Cookie + crumb for Yahoo quoteSummary / options (chart often works without)."""

    def __init__(self) -> None:
        self._opener: urllib.request.OpenerDirector | None = None
        self.crumb: str | None = None
        self._ok = False

    def ensure(self, errors: list[str]) -> bool:
        if self._ok and self.crumb:
            return True
        try:
            import http.cookiejar

            jar = http.cookiejar.CookieJar()
            ctx = ssl.create_default_context()
            https = urllib.request.HTTPSHandler(context=ctx)
            self._opener = urllib.request.build_opener(https, urllib.request.HTTPCookieProcessor(jar))
            # Seed cookies (404 is normal on fc.yahoo.com)
            try:
                req = urllib.request.Request(YAHOO_COOKIE, headers={"User-Agent": UA})
                self._opener.open(req, timeout=20).read()
            except urllib.error.HTTPError:
                pass
            req = urllib.request.Request(YAHOO_CRUMB, headers={"User-Agent": UA})
            crumb = self._opener.open(req, timeout=20).read().decode("utf-8").strip()
            if not crumb or "<" in crumb:
                errors.append("yahoo crumb: empty or HTML response")
                return False
            self.crumb = crumb
            self._ok = True
            return True
        except Exception as exc:
            errors.append(f"yahoo crumb session: {exc}")
            return False

    def get_json(self, url: str, timeout: int = 25) -> dict | list:
        if not self._opener:
            raise RuntimeError("Yahoo session not initialized")
        req = urllib.request.Request(url, headers={"User-Agent": UA, "Accept": "application/json"})
        with self._opener.open(req, timeout=timeout) as resp:
            return json.loads(resp.read().decode("utf-8"))


_YAHOO = YahooSession()


def http_get(url: str, timeout: int = 25) -> bytes:
    req = urllib.request.Request(url, headers={"User-Agent": UA, "Accept": "*/*"})
    ctx = ssl.create_default_context()
    with urllib.request.urlopen(req, timeout=timeout, context=ctx) as resp:
        return resp.read()


def http_get_json(url: str, timeout: int = 25) -> dict | list:
    return json.loads(http_get(url, timeout=timeout).decode("utf-8"))


def safe_get_json(url: str, errors: list[str], label: str) -> dict | list | None:
    try:
        return http_get_json(url)
    except (urllib.error.URLError, TimeoutError, json.JSONDecodeError, OSError) as exc:
        errors.append(f"{label}: {exc}")
        return None


def safe_yahoo_json(url: str, errors: list[str], label: str) -> dict | list | None:
    if not _YAHOO.ensure(errors):
        return safe_get_json(url.split("?crumb=")[0] if "crumb=" in url else url, errors, label)
    try:
        return _YAHOO.get_json(url)
    except Exception as exc:
        errors.append(f"{label}: {exc}")
        return None


def collapse_errors(errors: list[str], limit: int = 20) -> list[str]:
    """Group repeated 'prefix TICKER: same error' into one line."""
    buckets: dict[str, list[str]] = {}
    plain: list[str] = []
    for e in errors:
        # e.g. "analyst IRWD: HTTP Error 401: Unauthorized"
        if ": " in e:
            left, right = e.split(": ", 1)
            parts = left.split(" ", 1)
            if len(parts) == 2 and parts[1].isupper() and len(parts[1]) <= 8:
                key = f"{parts[0]}: {right}"
                buckets.setdefault(key, []).append(parts[1])
                continue
        plain.append(e)
    out = list(plain)
    for key, tickers in buckets.items():
        if len(tickers) == 1:
            prefix = key.split(":", 1)[0]
            out.append(f"{prefix} {tickers[0]}: {key.split(': ', 1)[1]}")
        else:
            out.append(f"{key} ({len(tickers)} tickers: {', '.join(tickers[:8])}{'…' if len(tickers) > 8 else ''})")
    return out[:limit]


# --- indicators (from penny scan) ---


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


def fetch_chart(ticker: str) -> dict:
    payload = http_get_json(YAHOO_CHART.format(ticker=urllib.parse.quote(ticker, safe="^=.-")))
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
    return {"rows": closes, "meta": result.get("meta", {})}


def fetch_quotes_batch(symbols: list[str], errors: list[str]) -> dict[str, dict]:
    out: dict[str, dict] = {}
    if not symbols:
        return out
    _YAHOO.ensure(errors)
    for i in range(0, len(symbols), 40):
        chunk = symbols[i : i + 40]
        enc = urllib.parse.quote(",".join(chunk), safe=",^=.-")
        url = YAHOO_QUOTE.format(symbols=enc)
        if _YAHOO.crumb:
            url += f"&crumb={urllib.parse.quote(_YAHOO.crumb)}"
        data = (
            safe_yahoo_json(url, errors, "yahoo_quote")
            if _YAHOO.crumb
            else safe_get_json(url, errors, "yahoo_quote")
        )
        if not data:
            for sym in chunk:
                try:
                    chart = fetch_chart(sym)
                    rows = chart["rows"]
                    closes = [c for _, c, _ in rows]
                    last = closes[-1]
                    prev = closes[-2] if len(closes) >= 2 else None
                    five = closes[-6] if len(closes) >= 6 else None
                    out[sym] = {
                        "symbol": sym,
                        "regularMarketPrice": last,
                        "regularMarketChangePercent": pct(last, prev),
                        "fiftyDayAverage": None,
                        "pct_5d": pct(last, five),
                    }
                except Exception as exc:
                    errors.append(f"{sym} chart fallback: {exc}")
            continue
        for q in data.get("quoteResponse", {}).get("result", []) or []:
            sym = q.get("symbol")
            if not sym:
                continue
            out[sym] = q
    return out


# --- Edition 1: headlines + macro + risk ---


def fetch_headlines(cfg: dict, errors: list[str]) -> list[dict]:
    limit = int(cfg.get("headline_limit") or 8)
    items: list[dict] = []
    seen: set[str] = set()
    for feed in cfg.get("rss_feeds") or []:
        name = feed.get("name", "RSS")
        url = feed.get("url")
        if not url:
            continue
        try:
            raw = http_get(url)
            root = ET.fromstring(raw)
        except Exception as exc:
            errors.append(f"RSS {name}: {exc}")
            continue
        for item in root.findall(".//item"):
            title = (item.findtext("title") or "").strip()
            link = (item.findtext("link") or "").strip()
            pub = (item.findtext("pubDate") or "").strip()
            if not title:
                continue
            key = title.lower()
            if key in seen:
                continue
            seen.add(key)
            pub_iso = ""
            if pub:
                try:
                    pub_iso = parsedate_to_datetime(pub).astimezone(TZ).strftime("%H:%M %Z")
                except Exception:
                    pub_iso = pub[:22]
            items.append({"source": name, "title": title, "link": link, "when": pub_iso})
    return items[:limit]


def enrich_macro(cfg: dict, quotes: dict[str, dict], errors: list[str]) -> list[dict]:
    rows = []
    for m in cfg.get("macro_tickers") or []:
        sym = m["symbol"]
        q = quotes.get(sym)
        if not q:
            # try chart
            try:
                chart = fetch_chart(sym)
                closes = [c for _, c, _ in chart["rows"]]
                last = closes[-1]
                p1 = pct(last, closes[-2] if len(closes) >= 2 else None)
                p5 = pct(last, closes[-6] if len(closes) >= 6 else None)
                rows.append(
                    {
                        "symbol": sym,
                        "label": m.get("label", sym),
                        "role": m.get("role", ""),
                        "last": last,
                        "pct_1d": p1,
                        "pct_5d": p5,
                    }
                )
            except Exception as exc:
                errors.append(f"macro {sym}: {exc}")
                rows.append(
                    {
                        "symbol": sym,
                        "label": m.get("label", sym),
                        "role": m.get("role", ""),
                        "last": None,
                        "pct_1d": None,
                        "pct_5d": None,
                    }
                )
            continue
        last = q.get("regularMarketPrice")
        p1 = q.get("regularMarketChangePercent")
        # 5d from chart when available
        p5 = q.get("pct_5d")
        if p5 is None:
            try:
                chart = fetch_chart(sym)
                closes = [c for _, c, _ in chart["rows"]]
                p5 = pct(closes[-1], closes[-6] if len(closes) >= 6 else None)
            except Exception:
                p5 = None
        rows.append(
            {
                "symbol": sym,
                "label": m.get("label", sym),
                "role": m.get("role", ""),
                "last": float(last) if last is not None else None,
                "pct_1d": float(p1) if p1 is not None else None,
                "pct_5d": float(p5) if p5 is not None else None,
            }
        )
    return rows


def fetch_fear_greed(cfg: dict, errors: list[str]) -> dict | None:
    """CNN Fear & Greed index (0-100). Soft-fails when blocked."""
    url = cfg.get("fear_greed_url")
    if not url:
        return None
    try:
        req = urllib.request.Request(
            url,
            headers={
                "User-Agent": (
                    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 "
                    "(KHTML, like Gecko) Chrome/122.0.0.0 Safari/537.36"
                ),
                "Accept": "application/json",
            },
        )
        ctx = ssl.create_default_context()
        with urllib.request.urlopen(req, timeout=20, context=ctx) as resp:
            data = json.loads(resp.read().decode("utf-8"))
        fg = data.get("fear_and_greed") or {}
        score = fg.get("score")
        rating = fg.get("rating")
        if score is None:
            return None
        return {"score": round(float(score), 1), "rating": str(rating or "").lower()}
    except Exception as exc:
        low = str(exc).lower()
        if "403" not in low and "401" not in low and "418" not in low:
            errors.append(f"fear&greed: {exc}")
        return None


def risk_verdict(
    macro: list[dict], cfg: dict, fear_greed: dict | None = None
) -> tuple[str, int, str]:
    """Score risk-on (+)/risk-off (−). Returns verdict, score, rationale."""
    score = 0
    notes: list[str] = []
    thr = cfg.get("risk_verdict") or {}
    vix_elev = float(thr.get("vix_elevated", 20))
    vix_calm = float(thr.get("vix_calm", 15))

    vix_last = next((r.get("last") for r in macro if r.get("role") == "fear"), None)
    vix3m_last = next((r.get("last") for r in macro if r.get("role") == "vix_term"), None)
    global_up = global_down = 0

    for r in macro:
        role = r.get("role")
        chg = r.get("pct_1d")
        last = r.get("last")
        if role == "equity" and chg is not None:
            if chg > 0.15:
                score += 1
                notes.append(f"{r['label']} +")
            elif chg < -0.15:
                score -= 1
                notes.append(f"{r['label']} −")
        if role == "fear" and last is not None:
            if last >= vix_elev:
                score -= 2
                notes.append(f"VIX elevated ({fmt(last, 1)})")
            elif last <= vix_calm:
                score += 1
                notes.append(f"VIX calm ({fmt(last, 1)})")
            if chg is not None:
                if chg > 5:
                    score -= 1
                    notes.append("VIX rising")
                elif chg < -5:
                    score += 1
                    notes.append("VIX falling")
        if role == "rates" and chg is not None:
            if chg > 1.5:
                score -= 1
                notes.append("yields up")
            elif chg < -1.5:
                score += 1
                notes.append("yields down")
        if role == "usd" and chg is not None:
            if chg > 0.3:
                score -= 1
                notes.append("USD firm")
            elif chg < -0.3:
                score += 1
                notes.append("USD soft")
        if role == "credit" and chg is not None:
            if chg > 0.25:
                score += 1
                notes.append("HY credit bid")
            elif chg < -0.35:
                score -= 1
                notes.append("HY credit soft")
        if role == "crypto" and chg is not None:
            if chg > 2:
                score += 1
                notes.append("crypto risk appetite")
            elif chg < -3:
                score -= 1
                notes.append("crypto risk-off")
        if role == "safe_haven" and chg is not None:
            if chg > 0.5:
                score -= 1
                notes.append("gold bid")
            elif chg < -0.5:
                score += 1
                notes.append("gold soft")
        if role == "oil" and chg is not None:
            if chg > 1.5:
                notes.append("oil firm (mixed)")
            elif chg < -1.5:
                notes.append("oil soft (mixed)")
        if role == "global" and chg is not None:
            if chg > 0.3:
                global_up += 1
            elif chg < -0.3:
                global_down += 1

    # VIX term structure: spot above 3-month = backwardation = stress
    if vix_last and vix3m_last:
        ratio = vix_last / vix3m_last
        if ratio >= 1.0:
            score -= 2
            notes.append(f"VIX backwardation ({ratio:.2f})")
        elif ratio <= 0.9:
            score += 1
            notes.append("VIX curve in contango (calm)")

    if global_up - global_down >= 2:
        score += 1
        notes.append(f"global tape green ({global_up} up)")
    elif global_down - global_up >= 2:
        score -= 1
        notes.append(f"global tape red ({global_down} down)")

    if fear_greed:
        fg_score = fear_greed["score"]
        if fg_score <= 25:
            score -= 1
            notes.append(f"Fear&Greed extreme fear ({fg_score:.0f})")
        elif fg_score >= 75:
            score += 1
            notes.append(f"Fear&Greed greed ({fg_score:.0f}) — contrarian caution")

    if score >= 2:
        verdict = "RISK-ON"
    elif score <= -2:
        verdict = "RISK-OFF"
    else:
        verdict = "NEUTRAL"
    rationale = "; ".join(notes[:8]) if notes else "insufficient macro moves"
    return verdict, score, rationale


# --- Edition 2: analyst / options / social / scoring ---


def build_universe(extra: list[str] | None = None) -> list[str]:
    tickers: list[str] = []
    for path in (PRIMARY_UNIVERSE, SECONDARY_UNIVERSE):
        tickers.extend(load_universe_tickers(path))
    tickers.extend(load_watchlist_tickers())
    tickers.extend(load_held_tickers())
    if extra:
        tickers.extend(extra)
    # stable unique; skip QQQ (benchmark only) from agreement scoring noise
    seen: set[str] = set()
    out: list[str] = []
    for t in tickers:
        t = t.upper().strip()
        if not t or t == "QQQ" or t in seen:
            continue
        seen.add(t)
        out.append(t)
    return out


def fetch_analyst_actions(tickers: list[str], errors: list[str], hours: int = 36) -> list[dict]:
    cutoff = datetime.now(timezone.utc) - timedelta(hours=hours)
    actions: list[dict] = []
    if not _YAHOO.ensure(errors):
        errors.append("analyst: Yahoo crumb unavailable — skipping upgrade/downgrade history")
        return actions
    crumb = urllib.parse.quote(_YAHOO.crumb or "")
    for ticker in tickers[:40]:
        data = safe_yahoo_json(
            YAHOO_SUMMARY.format(ticker=urllib.parse.quote(ticker), crumb=crumb),
            errors,
            f"analyst {ticker}",
        )
        if not data:
            continue
        hist = (
            data.get("quoteSummary", {})
            .get("result", [{}])[0]
            .get("upgradeDowngradeHistory", {})
            .get("history", [])
            or []
        )
        for h in hist[:8]:
            epoch = h.get("epochGradeDate")
            if not epoch:
                continue
            when = datetime.fromtimestamp(int(epoch), tz=timezone.utc)
            if when < cutoff:
                continue
            actions.append(
                {
                    "ticker": ticker,
                    "firm": h.get("firm") or "",
                    "to": h.get("toGrade") or "",
                    "from": h.get("fromGrade") or "",
                    "action": h.get("action") or "",
                    "when": when.astimezone(TZ).strftime("%Y-%m-%d %H:%M"),
                }
            )
    actions.sort(key=lambda a: a["when"], reverse=True)
    return actions[:25]


def fetch_options_positioning(tickers: list[str], errors: list[str]) -> list[dict]:
    rows: list[dict] = []
    if not _YAHOO.ensure(errors):
        errors.append("options: Yahoo crumb unavailable — skipping options chains")
        return rows
    crumb = urllib.parse.quote(_YAHOO.crumb or "")
    for ticker in tickers[:30]:
        data = safe_yahoo_json(
            YAHOO_OPTIONS.format(ticker=urllib.parse.quote(ticker), crumb=crumb),
            errors,
            f"options {ticker}",
        )
        if not data:
            continue
        try:
            result = data["optionChain"]["result"][0]
            opt = (result.get("options") or [None])[0]
            if not opt:
                continue
            calls = opt.get("calls") or []
            puts = opt.get("puts") or []
            call_vol = sum(int(c.get("volume") or 0) for c in calls)
            put_vol = sum(int(p.get("volume") or 0) for p in puts)
            call_oi = sum(int(c.get("openInterest") or 0) for c in calls)
            put_oi = sum(int(p.get("openInterest") or 0) for p in puts)
            cp = (call_vol / put_vol) if put_vol else (float("inf") if call_vol else None)
            unusual = []
            for side, contracts in (("call", calls), ("put", puts)):
                for c in contracts:
                    vol = int(c.get("volume") or 0)
                    oi = int(c.get("openInterest") or 0)
                    if vol >= 200 and oi > 0 and vol >= oi * 2:
                        unusual.append(f"{side} {c.get('strike')} vol={vol} oi={oi}")
            rows.append(
                {
                    "ticker": ticker,
                    "call_vol": call_vol,
                    "put_vol": put_vol,
                    "call_oi": call_oi,
                    "put_oi": put_oi,
                    "cp_ratio": None if cp is None or cp == float("inf") else round(cp, 2),
                    "cp_label": (
                        "call-heavy"
                        if (cp or 0) >= 1.5
                        else ("put-heavy" if cp is not None and cp <= 0.67 else "balanced")
                    ),
                    "unusual": "; ".join(unusual[:3]),
                }
            )
        except (KeyError, IndexError, TypeError, ValueError) as exc:
            errors.append(f"options parse {ticker}: {exc}")
    return rows


def fetch_stocktwits(cfg: dict, errors: list[str]) -> tuple[list[str], dict[str, dict]]:
    st = cfg.get("stocktwits") or {}
    trending_url = st.get("trending_url") or "https://api.stocktwits.com/api/2/trending/symbols.json"
    stream_tpl = st.get("stream_url") or "https://api.stocktwits.com/api/2/streams/symbol/{symbol}.json"
    trending: list[str] = []
    data = safe_get_json(trending_url, errors, "stocktwits trending")
    if data:
        for s in (data.get("symbols") or [])[:25]:
            sym = (s.get("symbol") or "").upper()
            if sym:
                trending.append(sym)

    sentiment: dict[str, dict] = {}
    for sym in trending[:15]:
        stream = safe_get_json(stream_tpl.format(symbol=urllib.parse.quote(sym)), errors, f"st {sym}")
        if not stream:
            continue
        bull = bear = 0
        for msg in (stream.get("messages") or [])[:40]:
            sent = (msg.get("entities") or {}).get("sentiment") or {}
            basic = (sent.get("basic") or "").lower()
            if basic == "bullish":
                bull += 1
            elif basic == "bearish":
                bear += 1
        total = bull + bear
        sentiment[sym] = {
            "bullish": bull,
            "bearish": bear,
            "bias": "bullish" if bull > bear else ("bearish" if bear > bull else "mixed"),
            "ratio": (bull / total) if total else None,
        }
    return trending, sentiment


def fetch_yahoo_trending(cfg: dict, errors: list[str]) -> list[str]:
    url = cfg.get("yahoo_trending_url") or "https://query1.finance.yahoo.com/v1/finance/trending/US?count=20"
    data = None
    if _YAHOO.ensure(errors):
        crumb = urllib.parse.quote(_YAHOO.crumb or "")
        joined = "&" if "?" in url else "?"
        data = safe_yahoo_json(f"{url}{joined}crumb={crumb}", errors, "yahoo trending")
    if not data:
        data = safe_get_json(url, errors, "yahoo trending")
    out: list[str] = []
    if not data:
        return out
    try:
        for block in data.get("finance", {}).get("result", []) or []:
            for quote in block.get("quotes") or []:
                sym = (quote.get("symbol") or "").upper()
                if sym and "." not in sym and sym not in {"SQQQ", "TQQQ"}:
                    out.append(sym)
    except (AttributeError, TypeError, KeyError) as exc:
        errors.append(f"yahoo trending parse: {exc}")
    return out[:20]


def fetch_retail_mentions(cfg: dict, universe: set[str], errors: list[str]) -> tuple[dict[str, int], list[str]]:
    """Retail attention without direct Reddit API (often 403).

    Sources:
      1. Google News RSS scoped to reddit.com/r/wallstreetbets and r/stocks
      2. Yahoo Finance US trending tickers
    Returns (mention_counts_in_universe, narrative_headlines).
    """
    counts: dict[str, int] = {}
    narratives: list[str] = []
    for feed in cfg.get("retail_rss") or []:
        name = feed.get("name", "retail RSS")
        url = feed.get("url")
        if not url:
            continue
        try:
            raw = http_get(url)
            root = ET.fromstring(raw)
        except Exception as exc:
            # Soft-fail: do not surface transient RSS issues as red source notes unless unexpected
            if "403" not in str(exc) and "401" not in str(exc):
                errors.append(f"{name}: {exc}")
            continue
        for item in root.findall(".//item")[:12]:
            title = (item.findtext("title") or "").strip()
            if not title:
                continue
            narratives.append(f"{name}: {title}")
            text = title.upper()
            found = set(TICKER_RE.findall(text))
            found |= set(re.findall(r"\$([A-Z]{1,5})\b", text))
            for t in found:
                if t in COMMON_WORDS:
                    continue
                if t in universe:
                    counts[t] = counts.get(t, 0) + 1

    for sym in fetch_yahoo_trending(cfg, errors):
        if sym in universe:
            counts[sym] = counts.get(sym, 0) + 1
        # also keep trending symbols for narrative even if outside universe
        narratives.append(f"Yahoo trending: {sym}")

    # Dedupe narratives, keep first ~12
    seen_n: set[str] = set()
    uniq: list[str] = []
    for n in narratives:
        key = n.lower()
        if key in seen_n:
            continue
        seen_n.add(key)
        uniq.append(n)
    return counts, uniq[:12]


def fetch_price_rows(tickers: list[str], errors: list[str]) -> dict[str, dict]:
    out: dict[str, dict] = {}
    for ticker in tickers:
        try:
            chart = fetch_chart(ticker)
        except Exception as exc:
            errors.append(f"price {ticker}: {exc}")
            continue
        series = chart["rows"]
        closes = [c for _, c, _ in series]
        vols = [v for _, _, v in series]
        last_close = closes[-1]
        last_vol = vols[-1]
        avg_vol = mean(vols[-20:]) if len(vols) >= 20 else mean(vols)
        rvol = (last_vol / avg_vol) if avg_vol else None
        out[ticker] = {
            "ticker": ticker,
            "close": round(last_close, 4),
            "volume": last_vol,
            "pct_1d": None if pct(last_close, closes[-2] if len(closes) >= 2 else None) is None else round(pct(last_close, closes[-2]), 3),
            "pct_5d": None if pct(last_close, closes[-6] if len(closes) >= 6 else None) is None else round(pct(last_close, closes[-6]), 3),
            "sma20": round(mean(closes[-20:]), 4),
            "rsi14": None if rsi(closes, 14) is None else round(rsi(closes, 14), 2),
            "rvol": None if rvol is None else round(rvol, 2),
        }
    return out


def score_ticker(
    ticker: str,
    cfg: dict,
    price: dict | None,
    analyst: list[dict],
    options: dict | None,
    social_st: dict | None,
    retail_n: int,
    headline_hits: int,
) -> dict:
    w = cfg.get("score_weights") or {}
    news_w = int(w.get("news_catalyst", 2))
    anal_w = int(w.get("analyst_revisions", 2))
    opt_w = int(w.get("options_flow", 1))
    soc_w = int(w.get("social_sentiment", 1))
    px_w = int(w.get("price_volume", 2))

    parts = {
        "news": 0,
        "analyst": 0,
        "options": 0,
        "social": 0,
        "price": 0,
    }
    why: list[str] = []

    if headline_hits > 0:
        parts["news"] = news_w
        why.append(f"news mentions ({headline_hits})")

    upgrades = [a for a in analyst if a["ticker"] == ticker]
    if upgrades:
        bullish_acts = {"up", "upgrade", "raise", "initiates", "reiterates"}
        bearish_acts = {"down", "downgrade", "lower", "drop"}
        act = " ".join((a.get("action") or "").lower() for a in upgrades)
        if any(b in act for b in bearish_acts):
            parts["analyst"] = 0
            why.append("analyst downgrade/target cut")
        elif any(b in act for b in bullish_acts) or upgrades:
            parts["analyst"] = anal_w
            why.append("analyst action")

    if options:
        cp = options.get("cp_ratio")
        unusual = options.get("unusual") or ""
        if unusual or (cp is not None and (cp >= 1.5 or cp <= 0.67)):
            parts["options"] = opt_w
            why.append(options.get("cp_label") or "options activity")

    social_pts = 0
    if social_st:
        if social_st.get("bias") == "bullish" and (social_st.get("bullish") or 0) >= 2:
            social_pts = soc_w
            why.append("Stocktwits bullish")
        elif social_st.get("bias") == "bearish" and (social_st.get("bearish") or 0) >= 2:
            social_pts = 0
            why.append("Stocktwits bearish")
    if retail_n >= 1:
        social_pts = max(social_pts, soc_w)
        why.append(f"retail attention ({retail_n})")
    parts["social"] = social_pts

    if price:
        p1 = price.get("pct_1d") or 0
        p5 = price.get("pct_5d") or 0
        rvol = price.get("rvol") or 0
        rsi14 = price.get("rsi14")
        above_sma = price.get("close") and price.get("sma20") and price["close"] >= price["sma20"]
        bullish_px = (p1 > 0 and p5 > 0) or (above_sma and p1 > 0)
        vol_ok = rvol >= 1.2
        if bullish_px and vol_ok:
            parts["price"] = px_w
            why.append(f"price+vol confirm (RVOL {fmt(rvol)})")
        elif bullish_px:
            parts["price"] = max(1, px_w // 2) if px_w >= 2 else 1
            why.append("price constructive, muted volume")
        elif p1 < -2 or (rsi14 is not None and rsi14 < 35 and p5 < 0):
            parts["price"] = 0
            why.append("price weak / no confirm")

    total = sum(parts.values())
    # Agreement: sentiment lean and price lean same direction
    sent_lean = parts["news"] + parts["analyst"] + parts["options"] + parts["social"]
    px_lean = parts["price"]
    agree = sent_lean >= 2 and px_lean >= 1

    band = "avoid"
    bands = cfg.get("score_bands") or {}
    for name, rng in (("strong", bands.get("strong", [8, 11])), ("watch", bands.get("watch", [5, 7])), ("weak", bands.get("weak", [3, 4])), ("avoid", bands.get("avoid", [0, 2]))):
        lo, hi = int(rng[0]), int(rng[1])
        if lo <= total <= hi:
            band = name
            break
    if total > 11:
        band = "strong"

    return {
        "ticker": ticker,
        "score": total,
        "band": band,
        "agree": agree,
        "parts": parts,
        "why": "; ".join(why) if why else "no clear signals",
        "close": None if not price else price.get("close"),
        "pct_1d": None if not price else price.get("pct_1d"),
        "pct_5d": None if not price else price.get("pct_5d"),
        "rsi14": None if not price else price.get("rsi14"),
        "rvol": None if not price else price.get("rvol"),
    }


def headline_ticker_hits(headlines: list[dict], universe: set[str]) -> dict[str, int]:
    hits: dict[str, int] = {}
    for h in headlines:
        text = h.get("title") or ""
        for m in TICKER_RE.findall(text.upper()):
            if m in universe:
                hits[m] = hits.get(m, 0) + 1
        # also match $TICKER
        for m in re.findall(r"\$([A-Z]{1,5})\b", text.upper()):
            if m in universe:
                hits[m] = hits.get(m, 0) + 1
    return hits


# --- outputs ---


def send_email(subject: str, text: str, html_body: str | None = None, tag: str = "sentiment_journal") -> None:
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


def append_csv_row(day: str, edition: str, row: dict) -> None:
    path = TIMESERIES / "sentiment-daily.csv"
    path.parent.mkdir(parents=True, exist_ok=True)
    existing: list[dict] = []
    if path.exists():
        with path.open(newline="", encoding="utf-8") as f:
            existing = [
                r
                for r in csv.DictReader(f)
                if not (r.get("date") == day and r.get("edition") == edition)
            ]
    with path.open("w", newline="", encoding="utf-8") as f:
        w = csv.DictWriter(f, fieldnames=CSV_FIELDS)
        w.writeheader()
        for r in existing:
            w.writerow({k: r.get(k, "") for k in CSV_FIELDS})
        w.writerow({k: "" if row.get(k) is None else row[k] for k in CSV_FIELDS})


def _chg_html(n: float | None) -> str:
    if n is None:
        return "—"
    color = "#05603a" if n >= 0 else "#b42318"
    return f'<span style="color:{color};font-variant-numeric:tabular-nums;">{n:+.2f}%</span>'


def _verdict_banner(verdict: str) -> tuple[str, str, str]:
    if verdict == "RISK-ON":
        return "#05603a", "#ecfdf3", verdict
    if verdict == "RISK-OFF":
        return "#b42318", "#fef3f2", verdict
    return "#175cd3", "#eff8ff", verdict


def build_morning_md(
    day: str,
    brand: str,
    brand_full: str,
    headlines: list[dict],
    macro: list[dict],
    verdict: str,
    score: int,
    rationale: str,
    fear_greed: dict | None,
    errors: list[str],
    as_of: str,
) -> str:
    hl = ["| When | Source | Headline |", "|------|--------|----------|"]
    for h in headlines:
        title = h["title"].replace("|", "/")
        hl.append(f"| {h.get('when', '')} | {h['source']} | [{title}]({h.get('link', '')}) |")
    if len(hl) == 2:
        hl.append("| — | — | No headlines fetched |")

    mac = ["| Instrument | Last | 1d % | 5d % |", "|------------|-----:|-----:|-----:|"]
    for r in macro:
        mac.append(
            f"| {r['label']} (`{r['symbol']}`) | {fmt(r['last'])} | {signed(r['pct_1d'])} | {signed(r['pct_5d'])} |"
        )

    notes = public_errors(errors)
    err = ""
    if notes:
        err = "\n## Source notes\n\n" + "\n".join(f"- {e}" for e in notes) + "\n"

    return f"""# {brand} — Overnight & Macro — {day}

*{brand_full}*

> I am an AI research assistant, not a licensed financial advisor. This is educational information, not personalized financial advice. Consider a qualified advisor for your situation.

## Risk verdict

**{verdict}** (score {score:+d}) — {rationale}

{f"**CNN Fear & Greed:** {fear_greed['score']:.0f}/100 ({fear_greed['rating']})" if fear_greed else "_CNN Fear & Greed unavailable this run._"}

As of {as_of}.

## Market & macro summary

**Watch only — no trades.** This table classifies overnight *risk appetite* (risk-on vs risk-off) from index futures, the VIX curve, yields, the US dollar, high-yield credit, Bitcoin, oil, gold, and the global overnight tape. It frames your pre-market routine — it is not a recommendation to buy or sell any security.

**Why:** Equity futures and VIX show how overnight risk is priced; the VIX term structure (spot vs 3-month) flags stress regimes; yields, USD, and high-yield credit show rates/FX/credit pressure; Bitcoin adds a 24/7 risk-appetite read; oil and gold add inflation / safe-haven context; Nikkei, Hang Seng, and DAX show the overnight global tape. Together they answer “risk-on or risk-off?” before you look at single names.

**Data sources:** Yahoo Finance quotes/charts (ES=F, NQ=F, ^VIX, ^VIX3M, ^TNX, DX-Y.NYB, HYG, BTC-USD, CL=F, GC=F, USDCAD=X, ^N225, ^HSI, ^GDAXI) and CNN Fear & Greed — as of {as_of}.

{chr(10).join(mac)}

Ask: Risk-on or risk-off? → **{verdict}**

## What changed overnight?

{chr(10).join(hl)}

**Headline sources:** Google News RSS filtered to Reuters, CNBC, and MarketWatch (Reuters has no public RSS feed).

{err}
## Next

Edition 2 (Sentiment & Watchlist) follows ~7:00 AM MT. Open TradingView after that digest for the 5–10 agreement names.
"""


def build_premarket_md(
    day: str,
    brand: str,
    brand_full: str,
    analyst: list[dict],
    options: list[dict],
    market_gauges: list[dict],
    breadth_pct: float | None,
    trending: list[str],
    st_sent: dict[str, dict],
    retail: dict[str, int],
    retail_notes: list[str],
    agreement: list[dict],
    errors: list[str],
    as_of: str,
) -> str:
    a_rows = ["| When | Ticker | Firm | Action | From → To |", "|------|--------|------|--------|-----------|"]
    for a in analyst[:15]:
        a_rows.append(
            f"| {a['when']} | {a['ticker']} | {a['firm']} | {a['action']} | {a['from']} → {a['to']} |"
        )
    if len(a_rows) == 2:
        a_rows.append("| — | — | — | No recent Yahoo upgrade/downgrade history | — |")

    g_rows = ["| Gauge | Call vol | Put vol | Put/Call | Read |", "|-------|--------:|--------:|--------:|------|"]
    for g in market_gauges:
        pcr = (g["put_vol"] / g["call_vol"]) if g.get("call_vol") else None
        read = "—"
        if pcr is not None:
            read = "defensive/hedged" if pcr >= 1.2 else ("complacent/bullish" if pcr <= 0.8 else "balanced")
        g_rows.append(
            f"| {g['ticker']} | {g['call_vol']} | {g['put_vol']} | {fmt(pcr)} | {read} |"
        )
    if len(g_rows) == 2:
        g_rows.append("| — | — | — | — | Market gauge unavailable |")

    o_rows = ["| Ticker | Call vol | Put vol | C/P | Unusual |", "|--------|--------:|--------:|-----|---------|"]
    notable = [
        o
        for o in options
        if o.get("unusual")
        or (o.get("cp_ratio") is not None and (o["cp_ratio"] >= 1.5 or o["cp_ratio"] <= 0.67))
    ]
    for o in (notable or options)[:12]:
        o_rows.append(
            f"| {o['ticker']} | {o['call_vol']} | {o['put_vol']} | {o.get('cp_label', '—')} | {o.get('unusual') or '—'} |"
        )
    if len(o_rows) == 2:
        o_rows.append("| — | — | — | — | No options data |")

    retail_lines = []
    if trending:
        retail_lines.append("**Stocktwits trending:** " + ", ".join(trending[:15]))
    for sym, s in list(st_sent.items())[:10]:
        retail_lines.append(
            f"- {sym}: {s['bias']} (bull {s['bullish']} / bear {s['bearish']})"
        )
    if retail:
        top_r = sorted(retail.items(), key=lambda x: -x[1])[:10]
        retail_lines.append(
            "**Retail / trending overlap (universe):** " + ", ".join(f"{t}×{n}" for t, n in top_r)
        )
    if retail_notes:
        retail_lines.append("**Retail narratives (Google News · Reddit threads + Yahoo trending):**")
        for n in retail_notes[:8]:
            retail_lines.append(f"- {n}")
    if not retail_lines:
        retail_lines.append("_Retail feeds quiet today._")

    agr = [
        "| Rank | Ticker | Score | Band | Agree | Close | 1d % | 5d % | Why |",
        "|-----:|--------|------:|------|-------|------:|-----:|-----:|-----|",
    ]
    for i, r in enumerate(agreement, 1):
        agr.append(
            f"| {i} | {r['ticker']} | {r['score']} | {r['band']} | {'yes' if r['agree'] else 'no'} | "
            f"{fmt(r['close'])} | {signed(r['pct_1d'])} | {signed(r['pct_5d'])} | {r['why']} |"
        )
    if len(agr) == 2:
        agr.append("| — | — | — | — | — | — | — | — | No agreement names today |")

    notes = public_errors(errors)
    err = ""
    if notes:
        err = "\n## Source notes\n\n" + "\n".join(f"- {e}" for e in notes) + "\n"

    return f"""# {brand} — Sentiment & Watchlist — {day}

*{brand_full}*

> I am an AI research assistant, not a licensed financial advisor. This is educational information, not personalized financial advice. Consider a qualified advisor for your situation.

**Watch only — no trades.** The shortlist below is a TradingView research list where sentiment and price action roughly agree. Scores follow an educational framework (Sentiment_Based_Trading_Guide §11) — not a buy signal and not a live order.

As of {as_of}.

## Analyst revisions

**Source:** Yahoo Finance `upgradeDowngradeHistory` (MarketBeat substitute) — last ~36 hours.

{chr(10).join(a_rows)}

## Market positioning gauge

**Source:** Yahoo Finance options chains on SPY/QQQ (nearest expiry, put/call volume) + universe breadth.

{chr(10).join(g_rows)}

**Breadth (universe above 20-day average):** {f"{breadth_pct:.0f}%" if breadth_pct is not None else "—"} — above 60% is broadly constructive, below 40% is defensive.

## Unusual options / positioning

**Source:** Yahoo Finance options chains. Confirmation only — large call buying can be hedges or spreads.

{chr(10).join(o_rows)}

## Retail buzz

**Sources:** Stocktwits public API (trending + bull/bear); Google News RSS scoped to reddit.com/r/wallstreetbets and r/stocks; Yahoo Finance US trending. (Direct Reddit JSON is not used.)

{chr(10).join(retail_lines)}

## Sentiment + price agreement (TradingView shortlist)

Bands: 8–11 strong investigate · 5–7 watch · 3–4 weak · 0–2 avoid.

{chr(10).join(agr)}

Open TradingView on these names. Confirm VWAP / opening range before any paper ticket elsewhere.

{err}
## Rules

- This journal never places trades and never sets TRADE_APPROVED.
- Social sentiment is secondary (guide §12 hierarchy).
- Official GARP ≥ 60 still required before any live buy in this portfolio system.
"""


def build_morning_html(
    day: str,
    brand: str,
    brand_full: str,
    headlines: list[dict],
    macro: list[dict],
    verdict: str,
    score: int,
    rationale: str,
    fear_greed: dict | None,
    errors: list[str],
    as_of: str,
) -> str:
    fg, bg, label = _verdict_banner(verdict)
    hl_rows = []
    for i, h in enumerate(headlines[:8], 1):
        row_bg = "#f9fafb" if i % 2 == 0 else "#ffffff"
        hl_rows.append(
            f'<tr style="background:{row_bg};">'
            f'<td style="padding:10px 8px;font-size:12px;color:#667085;white-space:nowrap;">{html.escape(h.get("when") or "")}</td>'
            f'<td style="padding:10px 8px;font-size:12px;color:#667085;">{html.escape(h["source"])}</td>'
            f'<td style="padding:10px 12px;font-size:13px;"><a href="{html.escape(h.get("link") or "#")}" style="color:#101828;text-decoration:none;">{html.escape(h["title"])}</a></td>'
            f"</tr>"
        )
    if not hl_rows:
        hl_rows.append('<tr><td colspan="3" style="padding:12px;">No headlines fetched.</td></tr>')

    mac_rows = []
    for i, r in enumerate(macro, 1):
        row_bg = "#f9fafb" if i % 2 == 0 else "#ffffff"
        mac_rows.append(
            f'<tr style="background:{row_bg};">'
            f'<td style="padding:10px 12px;"><strong>{html.escape(r["label"])}</strong>'
            f'<div style="font-size:11px;color:#667085;">{html.escape(r["symbol"])}</div></td>'
            f'<td style="padding:10px 8px;text-align:right;font-variant-numeric:tabular-nums;">{fmt(r["last"])}</td>'
            f'<td style="padding:10px 8px;text-align:right;">{_chg_html(r["pct_1d"])}</td>'
            f'<td style="padding:10px 8px;text-align:right;">{_chg_html(r["pct_5d"])}</td>'
            f"</tr>"
        )

    notes = public_errors(errors)
    err_html = ""
    if notes:
        items = "".join(f"<li>{html.escape(e)}</li>" for e in notes[:12])
        err_html = f'<p style="color:#b42318;font-size:13px;"><strong>Source notes</strong></p><ul style="font-size:12px;color:#667085;">{items}</ul>'

    watch_box = (
        '<div style="background:#fffaeb;border-radius:12px;padding:12px 16px;margin:0 0 14px 0;font-size:13px;color:#344054;line-height:1.5;">'
        '<strong style="color:#b54708;">Watch only — no trades.</strong> '
        "This table classifies overnight <em>risk appetite</em> (risk-on vs risk-off) from futures, the VIX curve, yields, USD, high-yield credit, Bitcoin, oil, gold, and the global overnight tape. "
        "It frames your pre-market routine — not a recommendation to buy or sell any security.<br/>"
        f'<span style="font-size:12px;color:#667085;">Sources: Yahoo Finance (ES=F, NQ=F, ^VIX, ^VIX3M, ^TNX, DX-Y.NYB, HYG, BTC-USD, CL=F, GC=F, USDCAD=X, ^N225, ^HSI, ^GDAXI) + CNN Fear &amp; Greed as of {html.escape(as_of)}. '
        "Headlines: Google News RSS · Reuters / CNBC / MarketWatch.</span>"
        "</div>"
    )

    return f"""<!DOCTYPE html>
<html><body style="margin:0;padding:0;background:#eef2f6;font-family:-apple-system,BlinkMacSystemFont,'Segoe UI',Helvetica,Arial,sans-serif;color:#101828;">
  <table role="presentation" width="100%" cellspacing="0" cellpadding="0" style="background:#eef2f6;padding:24px 12px;">
    <tr><td align="center">
      <table role="presentation" width="760" cellspacing="0" cellpadding="0" style="max-width:760px;background:#ffffff;border-radius:16px;overflow:hidden;">
        <tr><td style="background:#0b1220;color:#ffffff;padding:24px 28px;">
          <div style="font-size:12px;letter-spacing:0.12em;text-transform:uppercase;color:#98a2b3;">{html.escape(brand_full)}</div>
          <div style="font-size:24px;font-weight:800;margin-top:6px;">{html.escape(brand)} — Overnight &amp; Macro</div>
          <div style="font-size:14px;color:#d0d5dd;margin-top:4px;">{html.escape(day)} · {html.escape(as_of)}</div>
        </td></tr>
        <tr><td style="padding:20px 28px;">
          <div style="background:{bg};border-radius:12px;padding:16px 18px;margin-bottom:16px;">
            <div style="font-size:11px;font-weight:700;letter-spacing:0.08em;text-transform:uppercase;color:{fg};">Risk verdict</div>
            <div style="font-size:28px;font-weight:800;color:{fg};margin-top:4px;">{html.escape(label)} <span style="font-size:16px;">({score:+d})</span></div>
            <div style="font-size:13px;color:#344054;margin-top:6px;">{html.escape(rationale)}</div>
            <div style="font-size:12px;color:#667085;margin-top:6px;">{html.escape(f"CNN Fear & Greed: {fear_greed['score']:.0f}/100 ({fear_greed['rating']})" if fear_greed else "CNN Fear & Greed unavailable this run")}</div>
          </div>
          <p style="margin:0 0 8px 0;font-size:14px;font-weight:700;">Market &amp; macro summary</p>
          {watch_box}
          <table role="presentation" width="100%" cellspacing="0" cellpadding="0" style="border:1px solid #eaecf0;border-radius:12px;overflow:hidden;font-size:13px;margin-bottom:18px;">
            <tr style="background:#0b1220;color:#ffffff;">
              <th style="padding:10px 12px;text-align:left;">Instrument</th>
              <th style="padding:10px 8px;text-align:right;">Last</th>
              <th style="padding:10px 8px;text-align:right;">1d</th>
              <th style="padding:10px 8px;text-align:right;">5d</th>
            </tr>
            {''.join(mac_rows)}
          </table>
          <p style="margin:0 0 8px 0;font-size:14px;font-weight:700;">What changed overnight?</p>
          <p style="margin:0 0 8px 0;font-size:12px;color:#667085;">Google News RSS filtered to Reuters, CNBC, and MarketWatch.</p>
          <table role="presentation" width="100%" cellspacing="0" cellpadding="0" style="border:1px solid #eaecf0;border-radius:12px;overflow:hidden;font-size:13px;">
            <tr style="background:#0b1220;color:#ffffff;">
              <th style="padding:10px 8px;text-align:left;">When</th>
              <th style="padding:10px 8px;text-align:left;">Source</th>
              <th style="padding:10px 12px;text-align:left;">Headline</th>
            </tr>
            {''.join(hl_rows)}
          </table>
        </td></tr>
        <tr><td style="padding:0 28px 24px 28px;font-size:12px;color:#667085;line-height:1.55;">
          {err_html}
          <p style="margin:0 0 8px 0;">Edition 2 (Sentiment &amp; Watchlist) arrives ~7:00 AM MT.</p>
          <p style="margin:0;">I am an AI research assistant, not a licensed financial advisor. Educational information only.</p>
        </td></tr>
      </table>
    </td></tr>
  </table>
</body></html>"""


def build_premarket_html(
    day: str,
    brand: str,
    brand_full: str,
    analyst: list[dict],
    options: list[dict],
    market_gauges: list[dict],
    breadth_pct: float | None,
    trending: list[str],
    retail_notes: list[str],
    agreement: list[dict],
    errors: list[str],
    as_of: str,
) -> str:
    agr_rows = []
    for i, r in enumerate(agreement, 1):
        row_bg = "#f9fafb" if i % 2 == 0 else "#ffffff"
        band_fg, band_bg = {
            "strong": ("#05603a", "#ecfdf3"),
            "watch": ("#b54708", "#fffaeb"),
            "weak": ("#175cd3", "#eff8ff"),
            "avoid": ("#475467", "#f2f4f7"),
        }.get(r["band"], ("#475467", "#f2f4f7"))
        badge = (
            f'<span style="display:inline-block;padding:2px 8px;border-radius:999px;'
            f'font-size:11px;font-weight:700;color:{band_fg};background:{band_bg};">{html.escape(r["band"])}</span>'
        )
        agr_rows.append(
            f'<tr style="background:{row_bg};">'
            f'<td style="padding:10px 8px;text-align:center;color:#667085;">{i}</td>'
            f'<td style="padding:10px 8px;"><strong>{html.escape(r["ticker"])}</strong></td>'
            f'<td style="padding:10px 8px;text-align:center;font-weight:700;">{r["score"]}</td>'
            f'<td style="padding:10px 8px;">{badge}</td>'
            f'<td style="padding:10px 8px;text-align:right;">{fmt(r["close"])}</td>'
            f'<td style="padding:10px 8px;text-align:right;">{_chg_html(r["pct_1d"])}</td>'
            f'<td style="padding:10px 12px;font-size:12px;color:#344054;">{html.escape(r["why"])}</td>'
            f"</tr>"
        )
    if not agr_rows:
        agr_rows.append('<tr><td colspan="7" style="padding:12px;">No agreement names today.</td></tr>')

    a_preview = ""
    if analyst:
        items = "".join(
            f"<li><strong>{html.escape(a['ticker'])}</strong> — {html.escape(a['action'])} "
            f"({html.escape(a['from'])} → {html.escape(a['to'])}) · {html.escape(a['firm'])}</li>"
            for a in analyst[:8]
        )
        a_preview = f'<ul style="margin:0;padding-left:18px;font-size:13px;line-height:1.5;">{items}</ul>'
    else:
        a_preview = '<p style="margin:0;font-size:13px;color:#667085;">No recent Yahoo upgrade/downgrade history in window.</p>'

    opt_note = f"{len([o for o in options if o.get('unusual')])} unusual volume-vs-OI outliers among {len(options)} chains checked."
    gauge_bits = []
    for g in market_gauges:
        pcr = (g["put_vol"] / g["call_vol"]) if g.get("call_vol") else None
        if pcr is not None:
            read = "defensive" if pcr >= 1.2 else ("complacent/bullish" if pcr <= 0.8 else "balanced")
            gauge_bits.append(f"{g['ticker']} put/call {pcr:.2f} ({read})")
    breadth_bit = f"breadth {breadth_pct:.0f}% above SMA20" if breadth_pct is not None else "breadth —"
    market_line = "; ".join(gauge_bits + [breadth_bit]) if (gauge_bits or breadth_pct is not None) else "unavailable"
    trend_line = ", ".join(trending[:12]) if trending else "quiet"
    narrative_html = ""
    if retail_notes:
        items = "".join(f"<li>{html.escape(n)}</li>" for n in retail_notes[:6])
        narrative_html = f'<ul style="margin:8px 0 0 0;padding-left:18px;font-size:12px;color:#344054;">{items}</ul>'

    notes = public_errors(errors)
    err_html = ""
    if notes:
        items = "".join(f"<li>{html.escape(e)}</li>" for e in notes[:12])
        err_html = f'<p style="color:#b42318;font-size:13px;"><strong>Source notes</strong></p><ul style="font-size:12px;color:#667085;">{items}</ul>'

    return f"""<!DOCTYPE html>
<html><body style="margin:0;padding:0;background:#eef2f6;font-family:-apple-system,BlinkMacSystemFont,'Segoe UI',Helvetica,Arial,sans-serif;color:#101828;">
  <table role="presentation" width="100%" cellspacing="0" cellpadding="0" style="background:#eef2f6;padding:24px 12px;">
    <tr><td align="center">
      <table role="presentation" width="760" cellspacing="0" cellpadding="0" style="max-width:760px;background:#ffffff;border-radius:16px;overflow:hidden;">
        <tr><td style="background:#0b1220;color:#ffffff;padding:24px 28px;">
          <div style="font-size:12px;letter-spacing:0.12em;text-transform:uppercase;color:#98a2b3;">{html.escape(brand_full)}</div>
          <div style="font-size:24px;font-weight:800;margin-top:6px;">{html.escape(brand)} — Sentiment &amp; Watchlist</div>
          <div style="font-size:14px;color:#d0d5dd;margin-top:4px;">{html.escape(day)} · {html.escape(as_of)}</div>
        </td></tr>
        <tr><td style="padding:20px 28px;">
          <div style="background:#fffaeb;border-radius:12px;padding:12px 16px;margin-bottom:16px;font-size:13px;color:#344054;line-height:1.5;">
            <strong style="color:#b54708;">Watch only — no trades.</strong>
            TradingView research shortlist where sentiment and price roughly agree. Educational score (guide §11) — not a buy signal.
          </div>
          <p style="margin:0 0 8px 0;font-size:14px;font-weight:700;">Analyst revisions</p>
          <p style="margin:0 0 8px 0;font-size:12px;color:#667085;">Yahoo Finance upgradeDowngradeHistory (~36h).</p>
          {a_preview}
          <p style="margin:16px 0 8px 0;font-size:14px;font-weight:700;">Market positioning gauge</p>
          <p style="margin:0 0 8px 0;font-size:13px;color:#344054;">{html.escape(market_line)}</p>
          <p style="margin:16px 0 8px 0;font-size:14px;font-weight:700;">Options positioning</p>
          <p style="margin:0 0 8px 0;font-size:13px;color:#344054;">{html.escape(opt_note)} Source: Yahoo options chains (confirmation only).</p>
          <p style="margin:16px 0 8px 0;font-size:14px;font-weight:700;">Retail buzz</p>
          <p style="margin:0;font-size:13px;">Stocktwits trending: {html.escape(trend_line)}</p>
          <p style="margin:6px 0 0 0;font-size:12px;color:#667085;">Also: Google News RSS (reddit.com/r/wallstreetbets, r/stocks) + Yahoo US trending.</p>
          {narrative_html}
          <p style="margin:16px 0 8px 0;font-size:14px;font-weight:700;">Sentiment + price agreement</p>
          <table role="presentation" width="100%" cellspacing="0" cellpadding="0" style="border:1px solid #eaecf0;border-radius:12px;overflow:hidden;font-size:13px;">
            <tr style="background:#0b1220;color:#ffffff;">
              <th style="padding:10px 8px;text-align:center;">#</th>
              <th style="padding:10px 8px;text-align:left;">Ticker</th>
              <th style="padding:10px 8px;text-align:center;">Score</th>
              <th style="padding:10px 8px;text-align:left;">Band</th>
              <th style="padding:10px 8px;text-align:right;">Price</th>
              <th style="padding:10px 8px;text-align:right;">1d</th>
              <th style="padding:10px 12px;text-align:left;">Why</th>
            </tr>
            {''.join(agr_rows)}
          </table>
        </td></tr>
        <tr><td style="padding:0 28px 24px 28px;font-size:12px;color:#667085;line-height:1.55;">
          {err_html}
          <p style="margin:0 0 8px 0;">Score weights from research/Sentiment_Based_Trading_Guide.md §11. Not a proven predictive model.</p>
          <p style="margin:0;">I am an AI research assistant, not a licensed financial advisor. Educational information only.</p>
        </td></tr>
      </table>
    </td></tr>
  </table>
</body></html>"""


def write_or_append_journal(day: str, section_md: str, edition: str) -> Path:
    REPORTS.mkdir(parents=True, exist_ok=True)
    path = REPORTS / f"{day}-sentiment-journal.md"
    if edition == "morning" or not path.exists():
        path.write_text(section_md, encoding="utf-8")
    else:
        existing = path.read_text(encoding="utf-8")
        path.write_text(existing.rstrip() + "\n\n---\n\n" + section_md, encoding="utf-8")
    return path


def run_morning(cfg: dict, day: str, no_email: bool) -> int:
    errors: list[str] = []
    as_of = datetime.now(TZ).strftime("%Y-%m-%d %H:%M %Z")
    brand = cfg.get("brand") or "RAVEN Morning Journal"
    brand_full = cfg.get("brand_full") or "RAVEN — AI-Powered Market Intelligence by Rohit"

    headlines = fetch_headlines(cfg, errors)
    symbols = [m["symbol"] for m in (cfg.get("macro_tickers") or [])]
    quotes = fetch_quotes_batch(symbols, errors)
    macro = enrich_macro(cfg, quotes, errors)
    fear_greed = fetch_fear_greed(cfg, errors)
    verdict, score, rationale = risk_verdict(macro, cfg, fear_greed)

    md = build_morning_md(
        day, brand, brand_full, headlines, macro, verdict, score, rationale, fear_greed, errors, as_of
    )
    path = write_or_append_journal(day, md, "morning")
    print(path)

    vix = next((r["last"] for r in macro if r["symbol"] == "^VIX"), None)
    vix3m = next((r["last"] for r in macro if r["symbol"] == "^VIX3M"), None)
    es = next((r["pct_1d"] for r in macro if r["symbol"] == "ES=F"), None)
    nq = next((r["pct_1d"] for r in macro if r["symbol"] == "NQ=F"), None)
    append_csv_row(
        day,
        "morning",
        {
            "date": day,
            "edition": "morning",
            "risk_verdict": verdict,
            "risk_score": score,
            "vix": "" if vix is None else round(vix, 2),
            "vix3m": "" if vix3m is None else round(vix3m, 2),
            "fear_greed": "" if not fear_greed else fear_greed["score"],
            "es_pct": "" if es is None else round(es, 3),
            "nq_pct": "" if nq is None else round(nq, 3),
            "breadth_pct": "",
            "top_tickers": "",
            "top_scores": "",
            "headline_count": len(headlines),
            "notes": rationale[:200],
        },
    )

    if not no_email:
        html_body = build_morning_html(
            day, brand, brand_full, headlines, macro, verdict, score, rationale, fear_greed, errors, as_of
        )
        send_email(
            f"RAVEN Morning Journal — Overnight & Macro — {day}",
            md,
            html_body=html_body,
            tag="sentiment-morning",
        )
    return 0


def run_premarket(cfg: dict, day: str, no_email: bool) -> int:
    errors: list[str] = []
    as_of = datetime.now(TZ).strftime("%Y-%m-%d %H:%M %Z")
    brand = cfg.get("brand") or "RAVEN Morning Journal"
    brand_full = cfg.get("brand_full") or "RAVEN — AI-Powered Market Intelligence by Rohit"

    trending, st_sent = fetch_stocktwits(cfg, errors)
    trending = [t for t in trending if "." not in t]
    yahoo_trend = fetch_yahoo_trending(cfg, errors)
    universe = build_universe(extra=trending + yahoo_trend)
    uni_set = set(universe)

    headlines = fetch_headlines(cfg, errors)
    news_hits = headline_ticker_hits(headlines, uni_set)

    analyst = fetch_analyst_actions(universe, errors)
    options = fetch_options_positioning(universe, errors)
    options_by = {o["ticker"]: o for o in options}
    retail, retail_notes = fetch_retail_mentions(cfg, uni_set, errors)

    # Market-wide options gauge (SPY/QQQ put/call volume)
    market_gauges = fetch_options_positioning(
        [g for g in (cfg.get("market_option_gauges") or [])], errors
    )

    price_universe = universe[:45]
    prices = fetch_price_rows(price_universe, errors)

    # Breadth proxy: % of scanned universe above its 20-day average
    above = [p for p in prices.values() if p.get("close") and p.get("sma20") and p["close"] >= p["sma20"]]
    breadth_pct = round(100.0 * len(above) / len(prices), 1) if prices else None

    scored: list[dict] = []
    for t in price_universe:
        scored.append(
            score_ticker(
                t,
                cfg,
                prices.get(t),
                analyst,
                options_by.get(t),
                st_sent.get(t),
                retail.get(t, 0),
                news_hits.get(t, 0),
            )
        )

    min_score = int(cfg.get("agreement_min_score") or 5)
    top_n = int(cfg.get("agreement_top_n") or 10)
    agreement = sorted(
        [s for s in scored if s["agree"] and s["score"] >= min_score],
        key=lambda s: (-s["score"], -(s.get("pct_1d") or -999), s["ticker"]),
    )[:top_n]
    if len(agreement) < 5:
        fillers = sorted(scored, key=lambda s: (-s["score"], -(s.get("pct_1d") or -999)))
        seen = {a["ticker"] for a in agreement}
        for s in fillers:
            if s["ticker"] in seen:
                continue
            agreement.append(s)
            seen.add(s["ticker"])
            if len(agreement) >= min(5, top_n):
                break

    md = build_premarket_md(
        day,
        brand,
        brand_full,
        analyst,
        options,
        market_gauges,
        breadth_pct,
        trending,
        st_sent,
        retail,
        retail_notes,
        agreement,
        errors,
        as_of,
    )
    path = write_or_append_journal(day, md, "premarket")
    print(path)

    append_csv_row(
        day,
        "premarket",
        {
            "date": day,
            "edition": "premarket",
            "risk_verdict": "",
            "risk_score": "",
            "vix": "",
            "vix3m": "",
            "fear_greed": "",
            "es_pct": "",
            "nq_pct": "",
            "breadth_pct": "" if breadth_pct is None else breadth_pct,
            "top_tickers": "|".join(a["ticker"] for a in agreement),
            "top_scores": "|".join(str(a["score"]) for a in agreement),
            "headline_count": len(headlines),
            "notes": f"agreement={len(agreement)}; universe={len(universe)}",
        },
    )

    if not no_email:
        html_body = build_premarket_html(
            day,
            brand,
            brand_full,
            analyst,
            options,
            market_gauges,
            breadth_pct,
            trending,
            retail_notes,
            agreement,
            errors,
            as_of,
        )
        send_email(
            f"RAVEN Morning Journal — Sentiment & Watchlist — {day}",
            md,
            html_body=html_body,
            tag="sentiment-premarket",
        )
    return 0


def parse_args(argv: list[str] | None = None) -> argparse.Namespace:
    p = argparse.ArgumentParser(description=__doc__)
    p.add_argument(
        "--edition",
        choices=("morning", "premarket"),
        required=True,
        help="morning = Overnight & Macro; premarket = Sentiment & Watchlist",
    )
    p.add_argument("--no-email", action="store_true", help="Write journal/CSV only; skip Resend.")
    return p.parse_args(argv)


def main(argv: list[str] | None = None) -> int:
    load_local_env()
    args = parse_args(argv)
    cfg = load_sources_config()
    peak = _read_simple_yaml_map(PEAK)
    paper = paper_trading_complete()
    day = datetime.now(TZ).date().isoformat()

    print(f"RAVEN Morning Journal · {args.edition} · {day}")
    status = console_status(peak, paper)
    if status != "ok":
        print(f"status: {status}")

    if args.edition == "morning":
        return run_morning(cfg, day, args.no_email)
    return run_premarket(cfg, day, args.no_email)


if __name__ == "__main__":
    raise SystemExit(main())
