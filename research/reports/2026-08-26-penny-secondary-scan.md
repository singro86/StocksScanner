# Secondary penny watchlist scan — 2026-08-26

> I am an AI research assistant, not a licensed financial advisor. This is educational information, not personalized financial advice. Consider a qualified advisor for your situation.

**Paper trading active — dry-run only. Buy lines are paper recommendations, never live Wealthsimple orders.**

## What to buy today (from 20 names)

NONE — no buy today.

Official Rebalance-MCP GARP scores are not computed in this job. Quality flags come from `portfolio/penny-secondary-watchlist.yaml`. A live ticket still needs GARP ≥ 60.

| Rank | Ticker | List | Rec | Close | 1d % | 5d % | SMA20 | RSI14 | Why |
|-----:|--------|------|-----|------:|-----:|-----:|------:|------:|-----|
| 1 | GORO | Secondary 20 | Watch | 3.64 | -5.94 | +28.62 | 2.71 | 81.7 | No official GARP ≥ 60 yet. Not auto-promoted after a crash. |
| 2 | VFF | Secondary 20 | Watch | 2.83 | -1.56 | +8.62 | 2.38 | 84.7 | No official GARP ≥ 60 yet. Not auto-promoted after a crash. |
| 3 | AISP | Secondary 20 | Watch | 2.22 | -1.33 | +7.77 | 2.01 | 69.2 | No official GARP ≥ 60 yet. Not auto-promoted after a crash. |
| 4 | SABR | Secondary 20 | Watch | 2.24 | -0.89 | +6.16 | 2.11 | 50.0 | No official GARP ≥ 60 yet. Not auto-promoted after a crash. |
| 5 | ABUS | Secondary 20 | Watch | 5.21 | +0.19 | +4.62 | 4.73 | 74.5 | No official GARP ≥ 60 yet. Not auto-promoted after a crash. |
| 6 | NAGE | Secondary 20 | Watch | 3.25 | -0.61 | +2.52 | 3.17 | 69.1 | No official GARP ≥ 60 yet. Not auto-promoted after a crash. |
| 7 | AREC | Secondary 20 | Watch | 2.69 | -0.92 | +2.08 | 2.53 | 62.0 | No official GARP ≥ 60 yet. Not auto-promoted after a crash. |
| 8 | CYH | Secondary 20 | Watch | 2.98 | +0.34 | +2.06 | 2.94 | 52.3 | No official GARP ≥ 60 yet. Not auto-promoted after a crash. |
| 9 | ARKO | Secondary 20 | Watch | 4.67 | +0.00 | -0.64 | 5.60 | 15.9 | No official GARP ≥ 60 yet. Not auto-promoted after a crash. |
| 10 | UWMC | Secondary 20 | Watch | 1.48 | -1.99 | -0.67 | 1.56 | 64.9 | No official GARP ≥ 60 yet. Not auto-promoted after a crash. |
| 11 | SPRO | Secondary 20 | Watch | 1.22 | -0.81 | -0.81 | 1.22 | 41.1 | No official GARP ≥ 60 yet. Not auto-promoted after a crash. |
| 12 | SITC | Secondary 20 | Watch | 2.97 | -0.34 | -1.98 | 3.19 | 35.7 | No official GARP ≥ 60 yet. Not auto-promoted after a crash. |
| 13 | GDRX | Secondary 20 | Watch | 3.46 | -0.43 | -2.26 | 3.51 | 36.0 | No official GARP ≥ 60 yet. Not auto-promoted after a crash. |
| 14 | MDXG | Secondary 20 | Watch | 4.29 | -1.06 | -3.51 | 4.27 | 54.9 | No official GARP ≥ 60 yet. Not auto-promoted after a crash. |
| 15 | VRRM | Secondary 20 | Watch | 4.48 | +1.13 | -3.66 | 4.87 | 28.1 | No official GARP ≥ 60 yet. Not auto-promoted after a crash. |
| 16 | AMPY | Secondary 20 | Watch | 4.59 | -1.62 | -4.08 | 4.43 | 65.6 | No official GARP ≥ 60 yet. Not auto-promoted after a crash. |
| 17 | TBLA | Secondary 20 | Watch | 3.68 | -0.54 | -4.66 | 4.14 | 34.2 | No official GARP ≥ 60 yet. Not auto-promoted after a crash. |
| 18 | ALTO | Secondary 20 | Watch | 3.96 | -0.73 | -5.46 | 4.38 | 29.4 | No official GARP ≥ 60 yet. Not auto-promoted after a crash. |
| 19 | TYGO | Secondary 20 | Watch | 1.07 | +1.91 | -6.14 | 1.32 | 27.7 | No official GARP ≥ 60 yet. Not auto-promoted after a crash. |
| 20 | HLLY | Secondary 20 | Watch | 2.88 | -0.52 | -8.44 | 3.00 | 43.7 | No official GARP ≥ 60 yet. Not auto-promoted after a crash. |

Prices: Yahoo Finance daily bars, 2026-08-26 America/Toronto. SMA20 and RSI14 from the last 3 months of daily closes. Do not use Equibles for this routine price check.


## Rules

- Ranked Buy → Sell → Hold → Watch → Avoid. Max one Buy (paper) per morning.
- `Avoid` never becomes a buy because it bounced. `Sell` only if you already hold that avoid-quality name.
- `Watch` is not auto-promoted after a crash.
- This job never calls wsli and never sets TRADE_APPROVED.
