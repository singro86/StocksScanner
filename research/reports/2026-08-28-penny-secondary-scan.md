# Secondary penny watchlist scan — 2026-08-28

> I am an AI research assistant, not a licensed financial advisor. This is educational information, not personalized financial advice. Consider a qualified advisor for your situation.

**Paper trading active — dry-run only. Buy lines are paper recommendations, never live Wealthsimple orders.**

## What to buy today (from 20 names)

NONE — no buy today.

Official Rebalance-MCP GARP scores are not computed in this job. Quality flags come from `portfolio/penny-secondary-watchlist.yaml`. A live ticket still needs GARP ≥ 60.

| Rank | Ticker | List | Rec | Close | 1d % | 5d % | SMA20 | RSI14 | Why |
|-----:|--------|------|-----|------:|-----:|-----:|------:|------:|-----|
| 1 | GORO | Secondary 20 | Watch | 3.65 | -3.69 | +14.42 | 2.87 | 74.8 | No official GARP ≥ 60 yet. Not auto-promoted after a crash. |
| 2 | VFF | Secondary 20 | Watch | 2.91 | +1.75 | +6.99 | 2.48 | 82.1 | No official GARP ≥ 60 yet. Not auto-promoted after a crash. |
| 3 | UWMC | Secondary 20 | Watch | 1.49 | +0.68 | +6.43 | 1.52 | 55.1 | No official GARP ≥ 60 yet. Not auto-promoted after a crash. |
| 4 | SABR | Secondary 20 | Watch | 2.20 | +2.80 | +4.76 | 2.13 | 57.8 | No official GARP ≥ 60 yet. Not auto-promoted after a crash. |
| 5 | MDXG | Secondary 20 | Watch | 4.50 | -0.22 | +3.93 | 4.31 | 60.8 | No official GARP ≥ 60 yet. Not auto-promoted after a crash. |
| 6 | NAGE | Secondary 20 | Watch | 3.29 | +2.49 | +2.49 | 3.16 | 70.7 | No official GARP ≥ 60 yet. Not auto-promoted after a crash. |
| 7 | GDRX | Secondary 20 | Watch | 3.53 | +0.57 | +2.32 | 3.56 | 44.5 | No official GARP ≥ 60 yet. Not auto-promoted after a crash. |
| 8 | TBLA | Secondary 20 | Watch | 3.78 | +0.27 | +1.34 | 4.01 | 34.2 | No official GARP ≥ 60 yet. Not auto-promoted after a crash. |
| 9 | TYGO | Secondary 20 | Watch | 1.09 | -1.80 | +0.00 | 1.24 | 40.0 | No official GARP ≥ 60 yet. Not auto-promoted after a crash. |
| 10 | AMPY | Secondary 20 | Watch | 4.76 | +1.06 | -1.25 | 4.52 | 68.1 | No official GARP ≥ 60 yet. Not auto-promoted after a crash. |
| 11 | SPRO | Secondary 20 | Watch | 1.20 | -0.83 | -1.64 | 1.22 | 44.2 | No official GARP ≥ 60 yet. Not auto-promoted after a crash. |
| 12 | SITC | Secondary 20 | Watch | 2.99 | +0.34 | -2.61 | 3.06 | 47.1 | No official GARP ≥ 60 yet. Not auto-promoted after a crash. |
| 13 | CYH | Secondary 20 | Watch | 2.93 | +0.00 | -2.66 | 2.95 | 49.1 | No official GARP ≥ 60 yet. Not auto-promoted after a crash. |
| 14 | ABUS | Secondary 20 | Watch | 5.07 | -1.93 | -2.69 | 4.80 | 67.7 | No official GARP ≥ 60 yet. Not auto-promoted after a crash. |
| 15 | AISP | Secondary 20 | Watch | 2.09 | -4.13 | -2.79 | 2.04 | 53.7 | No official GARP ≥ 60 yet. Not auto-promoted after a crash. |
| 16 | VRRM | Secondary 20 | Watch | 4.39 | -0.45 | -3.73 | 4.78 | 33.6 | No official GARP ≥ 60 yet. Not auto-promoted after a crash. |
| 17 | HLLY | Secondary 20 | Watch | 2.92 | -1.68 | -5.50 | 3.02 | 39.2 | No official GARP ≥ 60 yet. Not auto-promoted after a crash. |
| 18 | ALTO | Secondary 20 | Watch | 4.07 | -0.49 | -7.08 | 4.33 | 43.1 | No official GARP ≥ 60 yet. Not auto-promoted after a crash. |
| 19 | ARKO | Secondary 20 | Watch | 4.37 | -2.02 | -8.00 | 5.24 | 39.4 | No official GARP ≥ 60 yet. Not auto-promoted after a crash. |
| 20 | AREC | Secondary 20 | Watch | 2.40 | -5.51 | -10.45 | 2.59 | 34.9 | No official GARP ≥ 60 yet. Not auto-promoted after a crash. |

Prices: Yahoo Finance daily bars, 2026-08-28 America/Toronto. SMA20 and RSI14 from the last 3 months of daily closes. Do not use Equibles for this routine price check.


## Rules

- Ranked Buy → Sell → Hold → Watch → Avoid. Max one Buy (paper) per morning.
- `Avoid` never becomes a buy because it bounced. `Sell` only if you already hold that avoid-quality name.
- `Watch` is not auto-promoted after a crash.
- This job never calls wsli and never sets TRADE_APPROVED.
