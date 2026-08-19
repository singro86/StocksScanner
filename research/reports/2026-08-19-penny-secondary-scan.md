# Secondary penny watchlist scan — 2026-08-19

> I am an AI research assistant, not a licensed financial advisor. This is educational information, not personalized financial advice. Consider a qualified advisor for your situation.

**Paper trading active — dry-run only. Buy lines are paper recommendations, never live Wealthsimple orders.**

## What to buy today (from 20 names)

NONE — no buy today.

Official Rebalance-MCP GARP scores are not computed in this job. Quality flags come from `portfolio/penny-secondary-watchlist.yaml`. A live ticket still needs GARP ≥ 60.

| Rank | Ticker | List | Rec | Close | 1d % | 5d % | SMA20 | RSI14 | Why |
|-----:|--------|------|-----|------:|-----:|-----:|------:|------:|-----|
| 1 | GORO | Secondary 20 | Watch | 2.69 | -2.54 | +10.25 | 2.39 | 75.4 | No official GARP ≥ 60 yet. Not auto-promoted after a crash. |
| 2 | ARKO | Secondary 20 | Watch | 4.72 | -2.88 | +7.03 | 6.57 | 15.7 | No official GARP ≥ 60 yet. Not auto-promoted after a crash. |
| 3 | AMPY | Secondary 20 | Watch | 4.82 | +0.00 | +6.87 | 4.16 | 78.9 | No official GARP ≥ 60 yet. Not auto-promoted after a crash. |
| 4 | SABR | Secondary 20 | Watch | 2.11 | -2.09 | +6.03 | 1.97 | 60.4 | No official GARP ≥ 60 yet. Not auto-promoted after a crash. |
| 5 | CYH | Secondary 20 | Watch | 2.98 | +1.02 | +4.93 | 2.91 | 62.0 | No official GARP ≥ 60 yet. Not auto-promoted after a crash. |
| 6 | VFF | Secondary 20 | Watch | 2.54 | -1.55 | +4.53 | 2.17 | 74.5 | No official GARP ≥ 60 yet. Not auto-promoted after a crash. |
| 7 | ABUS | Secondary 20 | Watch | 4.84 | +2.76 | +3.64 | 4.53 | 68.1 | No official GARP ≥ 60 yet. Not auto-promoted after a crash. |
| 8 | SITC | Secondary 20 | Watch | 3.03 | +2.02 | +2.37 | 3.59 | 13.1 | No official GARP ≥ 60 yet. Not auto-promoted after a crash. |
| 9 | ALTO | Secondary 20 | Watch | 4.24 | +0.47 | +1.68 | 4.55 | 45.8 | No official GARP ≥ 60 yet. Not auto-promoted after a crash. |
| 10 | AISP | Secondary 20 | Watch | 2.04 | +0.99 | +0.99 | 1.95 | 70.1 | No official GARP ≥ 60 yet. Not auto-promoted after a crash. |
| 11 | MDXG | Secondary 20 | Watch | 4.34 | +3.58 | +0.46 | 4.26 | 49.0 | No official GARP ≥ 60 yet. Not auto-promoted after a crash. |
| 12 | NAGE | Secondary 20 | Watch | 3.06 | +0.66 | -0.65 | 3.18 | 41.2 | No official GARP ≥ 60 yet. Not auto-promoted after a crash. |
| 13 | HLLY | Secondary 20 | Watch | 3.09 | +1.31 | -0.96 | 2.89 | 63.6 | No official GARP ≥ 60 yet. Not auto-promoted after a crash. |
| 14 | SPRO | Secondary 20 | Watch | 1.20 | +0.84 | -2.44 | 1.21 | 51.4 | No official GARP ≥ 60 yet. Not auto-promoted after a crash. |
| 15 | GDRX | Secondary 20 | Watch | 3.65 | -1.88 | -3.95 | 3.38 | 67.8 | No official GARP ≥ 60 yet. Not auto-promoted after a crash. |
| 16 | UWMC | Secondary 20 | Watch | 1.44 | -3.36 | -5.88 | 1.68 | 34.1 | No official GARP ≥ 60 yet. Not auto-promoted after a crash. |
| 17 | VRRM | Secondary 20 | Watch | 4.45 | -3.26 | -6.90 | 4.77 | 34.0 | No official GARP ≥ 60 yet. Not auto-promoted after a crash. |
| 18 | TBLA | Secondary 20 | Watch | 3.83 | -1.54 | -7.04 | 4.52 | 28.9 | No official GARP ≥ 60 yet. Not auto-promoted after a crash. |
| 19 | AREC | Secondary 20 | Watch | 2.68 | -9.15 | -7.59 | 2.26 | 77.1 | No official GARP ≥ 60 yet. Not auto-promoted after a crash. |
| 20 | TYGO | Secondary 20 | Watch | 1.15 | -1.71 | -8.00 | 1.49 | 36.8 | No official GARP ≥ 60 yet. Not auto-promoted after a crash. |

Prices: Yahoo Finance daily bars, 2026-08-19 America/Toronto. SMA20 and RSI14 from the last 3 months of daily closes. Do not use Equibles for this routine price check.


## Rules

- Ranked Buy → Sell → Hold → Watch → Avoid. Max one Buy (paper) per morning.
- `Avoid` never becomes a buy because it bounced. `Sell` only if you already hold that avoid-quality name.
- `Watch` is not auto-promoted after a crash.
- This job never calls wsli and never sets TRADE_APPROVED.
