# Mega-cap core scan — 2026-11-19

> I am an AI research assistant, not a licensed financial advisor. This is educational information, not personalized financial advice. Consider a qualified advisor for your situation.

**Paper trading active — dry-run only. Buy lines are paper recommendations, never live Wealthsimple orders.**

## What to buy today (from 4 names)

NONE — no buy today.

Official Rebalance-MCP GARP scores are not computed in this job. Quality flags come from `portfolio/mega-cap-scan-universe.yaml`. A live ticket still needs GARP ≥ 60.

| Rank | Ticker | List | Rec | Close | 1d % | 5d % | SMA20 | RSI14 | Why |
|-----:|--------|------|-----|------:|-----:|-----:|------:|------:|-----|
| 1 | AAPL | Mega-cap | Watch | 349.21 | -0.92 | -1.60 | 347.74 | 53.5 | No official GARP ≥ 60 yet. Not auto-promoted after a crash. |
| 2 | MSFT | Mega-cap | Watch | 498.30 | -1.97 | -4.72 | 524.96 | 42.6 | No official GARP ≥ 60 yet. Not auto-promoted after a crash. |
| 3 | GOOGL | Mega-cap | Watch | 272.66 | -3.46 | -8.72 | 292.20 | 44.5 | No official GARP ≥ 60 yet. Not auto-promoted after a crash. |
| 4 | NVDA | Mega-cap | Watch | 145.98 | -3.30 | -12.16 | 185.73 | 16.6 | No official GARP ≥ 60 yet. Not auto-promoted after a crash. |

Prices: Yahoo Finance daily bars, 2026-11-19 America/Phoenix. SMA20 and RSI14 from the last 3 months of daily closes. Do not use Equibles for this routine price check.


## Rules

- Ranked Buy → Sell → Hold → Watch → Avoid. Max one Buy (paper) per morning.
- Mega-cap core (NVDA / MSFT / GOOGL / AAPL) is display-only in the digest top section — never the morning paper Buy.
- `Avoid` never becomes a buy because it bounced. `Sell` only if you already hold that avoid-quality name.
- `Watch` is not auto-promoted after a crash.
- This job never calls wsli and never sets TRADE_APPROVED.
