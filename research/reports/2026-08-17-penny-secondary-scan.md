# Secondary penny watchlist scan — 2026-08-17

> I am an AI research assistant, not a licensed financial advisor. This is educational information, not personalized financial advice. Consider a qualified advisor for your situation.

**Paper trading active — dry-run only. Buy lines are paper recommendations, never live Wealthsimple orders.**

## What to buy today (from 20 names)

NONE — no buy today.

Official Rebalance-MCP GARP scores are not computed in this job. Quality flags come from `portfolio/penny-secondary-watchlist.yaml`. A live ticket still needs GARP ≥ 60.

| Rank | Ticker | List | Rec | Close | 1d % | 5d % | SMA20 | RSI14 | Why |
|-----:|--------|------|-----|------:|-----:|-----:|------:|------:|-----|
| 1 | AMPY | Secondary 20 | Watch | 4.86 | +1.57 | +16.71 | 4.13 | 79.3 | No official GARP ≥ 60 yet. Not auto-promoted after a crash. |
| 2 | GORO | Secondary 20 | Watch | 2.87 | +4.36 | +16.19 | 2.36 | 77.2 | No official GARP ≥ 60 yet. Not auto-promoted after a crash. |
| 3 | VFF | Secondary 20 | Watch | 2.62 | +3.75 | +10.76 | 2.14 | 77.5 | No official GARP ≥ 60 yet. Not auto-promoted after a crash. |
| 4 | UWMC | Secondary 20 | Watch | 1.52 | -4.40 | +7.80 | 1.70 | 40.2 | No official GARP ≥ 60 yet. Not auto-promoted after a crash. |
| 5 | SABR | Secondary 20 | Watch | 2.22 | -0.45 | +7.25 | 1.96 | 66.3 | No official GARP ≥ 60 yet. Not auto-promoted after a crash. |
| 6 | ABUS | Secondary 20 | Watch | 4.79 | +2.46 | +4.25 | 4.50 | 66.0 | No official GARP ≥ 60 yet. Not auto-promoted after a crash. |
| 7 | AREC | Secondary 20 | Watch | 2.90 | +0.52 | +1.58 | 2.21 | 89.8 | No official GARP ≥ 60 yet. Not auto-promoted after a crash. |
| 8 | ARKO | Secondary 20 | Watch | 4.76 | -1.75 | +1.38 | 6.75 | 15.7 | No official GARP ≥ 60 yet. Not auto-promoted after a crash. |
| 9 | GDRX | Secondary 20 | Watch | 3.71 | -0.67 | +1.23 | 3.34 | 68.1 | No official GARP ≥ 60 yet. Not auto-promoted after a crash. |
| 10 | CYH | Secondary 20 | Watch | 2.94 | -2.17 | -0.17 | 2.90 | 59.4 | No official GARP ≥ 60 yet. Not auto-promoted after a crash. |
| 11 | AISP | Secondary 20 | Watch | 2.02 | +3.32 | -0.25 | 1.95 | 54.6 | No official GARP ≥ 60 yet. Not auto-promoted after a crash. |
| 12 | ALTO | Secondary 20 | Watch | 4.20 | +0.48 | -0.71 | 4.58 | 44.9 | No official GARP ≥ 60 yet. Not auto-promoted after a crash. |
| 13 | MDXG | Secondary 20 | Watch | 4.21 | -1.29 | -1.29 | 4.24 | 43.4 | No official GARP ≥ 60 yet. Not auto-promoted after a crash. |
| 14 | NAGE | Secondary 20 | Watch | 2.99 | -0.99 | -1.97 | 3.21 | 38.5 | No official GARP ≥ 60 yet. Not auto-promoted after a crash. |
| 15 | SPRO | Secondary 20 | Watch | 1.22 | -0.81 | -3.17 | 1.23 | 55.7 | No official GARP ≥ 60 yet. Not auto-promoted after a crash. |
| 16 | TYGO | Secondary 20 | Watch | 1.18 | -3.28 | -3.28 | 1.55 | 34.9 | No official GARP ≥ 60 yet. Not auto-promoted after a crash. |
| 17 | SITC | Secondary 20 | Watch | 2.92 | -1.35 | -3.31 | 3.66 | 10.7 | No official GARP ≥ 60 yet. Not auto-promoted after a crash. |
| 18 | HLLY | Secondary 20 | Watch | 3.06 | -1.77 | -3.63 | 2.84 | 66.7 | No official GARP ≥ 60 yet. Not auto-promoted after a crash. |
| 19 | VRRM | Secondary 20 | Watch | 4.66 | -1.27 | -4.90 | 4.72 | 58.8 | No official GARP ≥ 60 yet. Not auto-promoted after a crash. |
| 20 | TBLA | Secondary 20 | Watch | 3.87 | -4.44 | -5.61 | 4.63 | 32.1 | No official GARP ≥ 60 yet. Not auto-promoted after a crash. |

Prices: Yahoo Finance daily bars, 2026-08-17 America/Toronto. SMA20 and RSI14 from the last 3 months of daily closes. Do not use Equibles for this routine price check.


## Rules

- Ranked Buy → Sell → Hold → Watch → Avoid. Max one Buy (paper) per morning.
- `Avoid` never becomes a buy because it bounced. `Sell` only if you already hold that avoid-quality name.
- `Watch` is not auto-promoted after a crash.
- This job never calls wsli and never sets TRADE_APPROVED.
