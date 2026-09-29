# Secondary penny watchlist scan — 2026-09-29

> I am an AI research assistant, not a licensed financial advisor. This is educational information, not personalized financial advice. Consider a qualified advisor for your situation.

**Paper trading active — dry-run only. Buy lines are paper recommendations, never live Wealthsimple orders.**

## What to buy today (from 20 names)

NONE — no buy today.

Official Rebalance-MCP GARP scores are not computed in this job. Quality flags come from `portfolio/penny-secondary-watchlist.yaml`. A live ticket still needs GARP ≥ 60.

| Rank | Ticker | List | Rec | Close | 1d % | 5d % | SMA20 | RSI14 | Why |
|-----:|--------|------|-----|------:|-----:|-----:|------:|------:|-----|
| 1 | VFF | Secondary 20 | Watch | 3.08 | -1.75 | +3.52 | 2.94 | 59.5 | No official GARP ≥ 60 yet. Not auto-promoted after a crash. |
| 2 | SITC | Secondary 20 | Watch | 3.11 | +1.97 | +1.63 | 2.94 | 75.0 | No official GARP ≥ 60 yet. Not auto-promoted after a crash. |
| 3 | AMPY | Secondary 20 | Watch | 4.20 | +0.12 | -0.83 | 4.63 | 21.6 | No official GARP ≥ 60 yet. Not auto-promoted after a crash. |
| 4 | UWMC | Secondary 20 | Watch | 1.23 | -1.60 | -2.38 | 1.31 | 26.7 | No official GARP ≥ 60 yet. Not auto-promoted after a crash. |
| 5 | ABUS | Secondary 20 | Watch | 4.83 | -0.51 | -3.49 | 5.03 | 16.2 | No official GARP ≥ 60 yet. Not auto-promoted after a crash. |
| 6 | CYH | Secondary 20 | Watch | 2.91 | +0.69 | -3.64 | 2.92 | 47.1 | No official GARP ≥ 60 yet. Not auto-promoted after a crash. |
| 7 | NAGE | Secondary 20 | Watch | 2.97 | -0.34 | -3.88 | 3.05 | 39.5 | No official GARP ≥ 60 yet. Not auto-promoted after a crash. |
| 8 | ARKO | Secondary 20 | Watch | 4.17 | -2.11 | -4.14 | 4.44 | 34.8 | No official GARP ≥ 60 yet. Not auto-promoted after a crash. |
| 9 | TBLA | Secondary 20 | Watch | 3.41 | +0.34 | -4.71 | 3.68 | 33.8 | No official GARP ≥ 60 yet. Not auto-promoted after a crash. |
| 10 | ALTO | Secondary 20 | Watch | 3.62 | -1.50 | -5.37 | 3.92 | 24.8 | No official GARP ≥ 60 yet. Not auto-promoted after a crash. |
| 11 | GDRX | Secondary 20 | Watch | 3.25 | -1.66 | -5.38 | 3.41 | 44.3 | No official GARP ≥ 60 yet. Not auto-promoted after a crash. |
| 12 | SABR | Secondary 20 | Watch | 2.12 | +1.19 | -6.39 | 2.18 | 49.1 | No official GARP ≥ 60 yet. Not auto-promoted after a crash. |
| 13 | AISP | Secondary 20 | Watch | 1.84 | +2.23 | -6.83 | 1.96 | 32.1 | No official GARP ≥ 60 yet. Not auto-promoted after a crash. |
| 14 | MDXG | Secondary 20 | Watch | 4.58 | -2.03 | -7.00 | 4.66 | 44.8 | No official GARP ≥ 60 yet. Not auto-promoted after a crash. |
| 15 | HLLY | Secondary 20 | Watch | 2.47 | +2.07 | -7.49 | 2.69 | 31.7 | No official GARP ≥ 60 yet. Not auto-promoted after a crash. |
| 16 | GORO | Secondary 20 | Watch | 3.20 | -4.76 | -9.86 | 3.61 | 27.7 | No official GARP ≥ 60 yet. Not auto-promoted after a crash. |
| 17 | AREC | Secondary 20 | Watch | 1.81 | -0.82 | -10.59 | 2.10 | 18.5 | No official GARP ≥ 60 yet. Not auto-promoted after a crash. |
| 18 | VRRM | Secondary 20 | Watch | 3.04 | +1.84 | -11.48 | 3.60 | 20.9 | No official GARP ≥ 60 yet. Not auto-promoted after a crash. |
| 19 | SPRO | Secondary 20 | Watch | 1.19 | +0.00 | -12.50 | 1.19 | 51.9 | No official GARP ≥ 60 yet. Not auto-promoted after a crash. |
| 20 | TYGO | Secondary 20 | Watch | 0.82 | -0.44 | -16.27 | 0.99 | 14.3 | No official GARP ≥ 60 yet. Not auto-promoted after a crash. |

Prices: Yahoo Finance daily bars, 2026-09-29 America/Toronto. SMA20 and RSI14 from the last 3 months of daily closes. Do not use Equibles for this routine price check.


## Rules

- Ranked Buy → Sell → Hold → Watch → Avoid. Max one Buy (paper) per morning.
- `Avoid` never becomes a buy because it bounced. `Sell` only if you already hold that avoid-quality name.
- `Watch` is not auto-promoted after a crash.
- This job never calls wsli and never sets TRADE_APPROVED.
