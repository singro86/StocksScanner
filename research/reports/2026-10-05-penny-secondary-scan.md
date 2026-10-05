# Secondary penny watchlist scan — 2026-10-05

> I am an AI research assistant, not a licensed financial advisor. This is educational information, not personalized financial advice. Consider a qualified advisor for your situation.

**Paper trading active — dry-run only. Buy lines are paper recommendations, never live Wealthsimple orders.**

## What to buy today (from 20 names)

NONE — no buy today.

Official Rebalance-MCP GARP scores are not computed in this job. Quality flags come from `portfolio/penny-secondary-watchlist.yaml`. A live ticket still needs GARP ≥ 60.

| Rank | Ticker | List | Rec | Close | 1d % | 5d % | SMA20 | RSI14 | Why |
|-----:|--------|------|-----|------:|-----:|-----:|------:|------:|-----|
| 1 | AISP | Secondary 20 | Watch | 2.02 | -4.72 | +12.22 | 1.95 | 57.3 | No official GARP ≥ 60 yet. Not auto-promoted after a crash. |
| 2 | SITC | Secondary 20 | Watch | 3.24 | -5.26 | +6.23 | 3.04 | 67.3 | No official GARP ≥ 60 yet. Not auto-promoted after a crash. |
| 3 | AMPY | Secondary 20 | Watch | 4.43 | +1.60 | +5.73 | 4.51 | 31.1 | No official GARP ≥ 60 yet. Not auto-promoted after a crash. |
| 4 | TYGO | Secondary 20 | Watch | 0.86 | -0.50 | +5.21 | 0.95 | 29.9 | No official GARP ≥ 60 yet. Not auto-promoted after a crash. |
| 5 | ALTO | Secondary 20 | Watch | 3.79 | +0.53 | +3.27 | 3.86 | 27.3 | No official GARP ≥ 60 yet. Not auto-promoted after a crash. |
| 6 | UWMC | Secondary 20 | Watch | 1.29 | +2.38 | +3.20 | 1.27 | 51.4 | No official GARP ≥ 60 yet. Not auto-promoted after a crash. |
| 7 | GDRX | Secondary 20 | Watch | 3.36 | +2.44 | +1.51 | 3.37 | 40.0 | No official GARP ≥ 60 yet. Not auto-promoted after a crash. |
| 8 | ARKO | Secondary 20 | Watch | 4.21 | +0.96 | -1.17 | 4.32 | 36.7 | No official GARP ≥ 60 yet. Not auto-promoted after a crash. |
| 9 | SPRO | Secondary 20 | Watch | 1.16 | -2.52 | -2.52 | 1.18 | 52.5 | No official GARP ≥ 60 yet. Not auto-promoted after a crash. |
| 10 | MDXG | Secondary 20 | Watch | 4.55 | -0.87 | -2.78 | 4.69 | 37.7 | No official GARP ≥ 60 yet. Not auto-promoted after a crash. |
| 11 | GORO | Secondary 20 | Watch | 3.25 | -0.31 | -3.27 | 3.48 | 34.5 | No official GARP ≥ 60 yet. Not auto-promoted after a crash. |
| 12 | TBLA | Secondary 20 | Watch | 3.27 | +1.24 | -3.82 | 3.57 | 17.1 | No official GARP ≥ 60 yet. Not auto-promoted after a crash. |
| 13 | ABUS | Secondary 20 | Watch | 4.67 | +4.94 | -3.91 | 4.93 | 33.0 | No official GARP ≥ 60 yet. Not auto-promoted after a crash. |
| 14 | VRRM | Secondary 20 | Watch | 2.87 | +2.13 | -4.01 | 3.35 | 22.8 | No official GARP ≥ 60 yet. Not auto-promoted after a crash. |
| 15 | CYH | Secondary 20 | Watch | 2.76 | +1.47 | -4.50 | 2.90 | 36.4 | No official GARP ≥ 60 yet. Not auto-promoted after a crash. |
| 16 | AREC | Secondary 20 | Watch | 1.74 | -2.79 | -4.92 | 1.98 | 22.9 | No official GARP ≥ 60 yet. Not auto-promoted after a crash. |
| 17 | HLLY | Secondary 20 | Watch | 2.29 | -2.14 | -5.37 | 2.56 | 31.1 | No official GARP ≥ 60 yet. Not auto-promoted after a crash. |
| 18 | SABR | Secondary 20 | Watch | 1.93 | -2.03 | -8.10 | 2.17 | 41.5 | No official GARP ≥ 60 yet. Not auto-promoted after a crash. |
| 19 | NAGE | Secondary 20 | Watch | 2.68 | -3.94 | -10.07 | 2.97 | 30.9 | No official GARP ≥ 60 yet. Not auto-promoted after a crash. |
| 20 | VFF | Secondary 20 | Watch | 2.72 | -4.22 | -13.38 | 2.93 | 42.5 | No official GARP ≥ 60 yet. Not auto-promoted after a crash. |

Prices: Yahoo Finance daily bars, 2026-10-05 America/Toronto. SMA20 and RSI14 from the last 3 months of daily closes. Do not use Equibles for this routine price check.


## Rules

- Ranked Buy → Sell → Hold → Watch → Avoid. Max one Buy (paper) per morning.
- `Avoid` never becomes a buy because it bounced. `Sell` only if you already hold that avoid-quality name.
- `Watch` is not auto-promoted after a crash.
- This job never calls wsli and never sets TRADE_APPROVED.
