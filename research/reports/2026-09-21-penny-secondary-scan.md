# Secondary penny watchlist scan — 2026-09-21

> I am an AI research assistant, not a licensed financial advisor. This is educational information, not personalized financial advice. Consider a qualified advisor for your situation.

**Paper trading active — dry-run only. Buy lines are paper recommendations, never live Wealthsimple orders.**

## What to buy today (from 20 names)

NONE — no buy today.

Official Rebalance-MCP GARP scores are not computed in this job. Quality flags come from `portfolio/penny-secondary-watchlist.yaml`. A live ticket still needs GARP ≥ 60.

| Rank | Ticker | List | Rec | Close | 1d % | 5d % | SMA20 | RSI14 | Why |
|-----:|--------|------|-----|------:|-----:|-----:|------:|------:|-----|
| 1 | SABR | Secondary 20 | Watch | 2.31 | +1.99 | +5.98 | 2.18 | 56.3 | No official GARP ≥ 60 yet. Not auto-promoted after a crash. |
| 2 | SITC | Secondary 20 | Watch | 3.04 | +3.05 | +4.83 | 2.92 | 58.2 | No official GARP ≥ 60 yet. Not auto-promoted after a crash. |
| 3 | MDXG | Secondary 20 | Watch | 4.75 | -0.31 | +2.48 | 4.57 | 63.0 | No official GARP ≥ 60 yet. Not auto-promoted after a crash. |
| 4 | AISP | Secondary 20 | Watch | 1.97 | +2.34 | +2.34 | 2.04 | 36.8 | No official GARP ≥ 60 yet. Not auto-promoted after a crash. |
| 5 | VFF | Secondary 20 | Watch | 2.90 | +2.04 | +2.04 | 2.87 | 51.7 | No official GARP ≥ 60 yet. Not auto-promoted after a crash. |
| 6 | ALTO | Secondary 20 | Watch | 3.95 | -1.25 | -0.25 | 4.03 | 49.4 | No official GARP ≥ 60 yet. Not auto-promoted after a crash. |
| 7 | SPRO | Secondary 20 | Watch | 1.14 | +0.44 | -0.44 | 1.18 | 30.2 | No official GARP ≥ 60 yet. Not auto-promoted after a crash. |
| 8 | NAGE | Secondary 20 | Watch | 3.00 | +0.17 | -1.48 | 3.11 | 30.4 | No official GARP ≥ 60 yet. Not auto-promoted after a crash. |
| 9 | CYH | Secondary 20 | Watch | 2.90 | +0.87 | -1.86 | 2.92 | 47.6 | No official GARP ≥ 60 yet. Not auto-promoted after a crash. |
| 10 | TYGO | Secondary 20 | Watch | 1.01 | +3.55 | -1.98 | 1.04 | 34.1 | No official GARP ≥ 60 yet. Not auto-promoted after a crash. |
| 11 | ABUS | Secondary 20 | Watch | 5.03 | +0.30 | -2.05 | 5.12 | 42.0 | No official GARP ≥ 60 yet. Not auto-promoted after a crash. |
| 12 | VRRM | Secondary 20 | Watch | 3.56 | +2.15 | -2.07 | 3.96 | 18.4 | No official GARP ≥ 60 yet. Not auto-promoted after a crash. |
| 13 | AREC | Secondary 20 | Watch | 2.00 | +0.76 | -2.21 | 2.30 | 28.1 | No official GARP ≥ 60 yet. Not auto-promoted after a crash. |
| 14 | GORO | Secondary 20 | Watch | 3.49 | -2.78 | -2.24 | 3.68 | 43.8 | No official GARP ≥ 60 yet. Not auto-promoted after a crash. |
| 15 | GDRX | Secondary 20 | Watch | 3.39 | +0.30 | -4.78 | 3.46 | 43.9 | No official GARP ≥ 60 yet. Not auto-promoted after a crash. |
| 16 | UWMC | Secondary 20 | Watch | 1.25 | +0.40 | -5.64 | 1.38 | 29.9 | No official GARP ≥ 60 yet. Not auto-promoted after a crash. |
| 17 | ARKO | Secondary 20 | Watch | 4.25 | +0.59 | -7.11 | 4.53 | 38.8 | No official GARP ≥ 60 yet. Not auto-promoted after a crash. |
| 18 | HLLY | Secondary 20 | Watch | 2.51 | -1.18 | -7.72 | 2.82 | 33.6 | No official GARP ≥ 60 yet. Not auto-promoted after a crash. |
| 19 | TBLA | Secondary 20 | Watch | 3.60 | -0.14 | -8.06 | 3.76 | 41.7 | No official GARP ≥ 60 yet. Not auto-promoted after a crash. |
| 20 | AMPY | Secondary 20 | Watch | 4.34 | -3.44 | -9.67 | 4.78 | 24.7 | No official GARP ≥ 60 yet. Not auto-promoted after a crash. |

Prices: Yahoo Finance daily bars, 2026-09-21 America/Toronto. SMA20 and RSI14 from the last 3 months of daily closes. Do not use Equibles for this routine price check.


## Rules

- Ranked Buy → Sell → Hold → Watch → Avoid. Max one Buy (paper) per morning.
- `Avoid` never becomes a buy because it bounced. `Sell` only if you already hold that avoid-quality name.
- `Watch` is not auto-promoted after a crash.
- This job never calls wsli and never sets TRADE_APPROVED.
