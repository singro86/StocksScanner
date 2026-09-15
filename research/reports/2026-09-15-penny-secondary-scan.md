# Secondary penny watchlist scan — 2026-09-15

> I am an AI research assistant, not a licensed financial advisor. This is educational information, not personalized financial advice. Consider a qualified advisor for your situation.

**Paper trading active — dry-run only. Buy lines are paper recommendations, never live Wealthsimple orders.**

## What to buy today (from 20 names)

NONE — no buy today.

Official Rebalance-MCP GARP scores are not computed in this job. Quality flags come from `portfolio/penny-secondary-watchlist.yaml`. A live ticket still needs GARP ≥ 60.

| Rank | Ticker | List | Rec | Close | 1d % | 5d % | SMA20 | RSI14 | Why |
|-----:|--------|------|-----|------:|-----:|-----:|------:|------:|-----|
| 1 | CYH | Secondary 20 | Watch | 2.94 | -0.17 | +3.70 | 2.93 | 47.1 | No official GARP ≥ 60 yet. Not auto-promoted after a crash. |
| 2 | MDXG | Secondary 20 | Watch | 4.79 | +3.12 | +2.46 | 4.50 | 73.1 | No official GARP ≥ 60 yet. Not auto-promoted after a crash. |
| 3 | TBLA | Secondary 20 | Watch | 3.85 | -1.41 | +0.92 | 3.78 | 61.3 | No official GARP ≥ 60 yet. Not auto-promoted after a crash. |
| 4 | SITC | Secondary 20 | Watch | 2.90 | -0.17 | +0.52 | 2.94 | 41.2 | No official GARP ≥ 60 yet. Not auto-promoted after a crash. |
| 5 | AMPY | Secondary 20 | Watch | 4.96 | +3.22 | +0.51 | 4.85 | 64.5 | No official GARP ≥ 60 yet. Not auto-promoted after a crash. |
| 6 | GDRX | Secondary 20 | Watch | 3.53 | -0.84 | +0.28 | 3.50 | 52.7 | No official GARP ≥ 60 yet. Not auto-promoted after a crash. |
| 7 | ALTO | Secondary 20 | Watch | 4.00 | +1.14 | -2.56 | 4.08 | 50.9 | No official GARP ≥ 60 yet. Not auto-promoted after a crash. |
| 8 | ABUS | Secondary 20 | Watch | 5.04 | -1.66 | -2.61 | 5.10 | 30.4 | No official GARP ≥ 60 yet. Not auto-promoted after a crash. |
| 9 | NAGE | Secondary 20 | Watch | 2.98 | -1.81 | -3.71 | 3.14 | 29.8 | No official GARP ≥ 60 yet. Not auto-promoted after a crash. |
| 10 | SABR | Secondary 20 | Watch | 2.17 | -0.46 | -4.20 | 2.15 | 44.5 | No official GARP ≥ 60 yet. Not auto-promoted after a crash. |
| 11 | TYGO | Secondary 20 | Watch | 1.01 | -1.94 | -4.72 | 1.07 | 41.7 | No official GARP ≥ 60 yet. Not auto-promoted after a crash. |
| 12 | VFF | Secondary 20 | Watch | 2.88 | +1.38 | -4.98 | 2.83 | 49.9 | No official GARP ≥ 60 yet. Not auto-promoted after a crash. |
| 13 | SPRO | Secondary 20 | Watch | 1.12 | -1.75 | -5.88 | 1.19 | 26.1 | No official GARP ≥ 60 yet. Not auto-promoted after a crash. |
| 14 | ARKO | Secondary 20 | Watch | 4.41 | -3.61 | -6.38 | 4.61 | 42.1 | No official GARP ≥ 60 yet. Not auto-promoted after a crash. |
| 15 | UWMC | Secondary 20 | Watch | 1.30 | -2.26 | -6.47 | 1.42 | 28.6 | No official GARP ≥ 60 yet. Not auto-promoted after a crash. |
| 16 | AISP | Secondary 20 | Watch | 1.92 | +0.00 | -7.69 | 2.07 | 27.4 | No official GARP ≥ 60 yet. Not auto-promoted after a crash. |
| 17 | GORO | Secondary 20 | Watch | 3.49 | -2.24 | -9.12 | 3.56 | 41.0 | No official GARP ≥ 60 yet. Not auto-promoted after a crash. |
| 18 | VRRM | Secondary 20 | Watch | 3.54 | -2.34 | -9.34 | 4.18 | 12.7 | No official GARP ≥ 60 yet. Not auto-promoted after a crash. |
| 19 | HLLY | Secondary 20 | Watch | 2.61 | -4.04 | -12.42 | 2.92 | 38.1 | No official GARP ≥ 60 yet. Not auto-promoted after a crash. |
| 20 | AREC | Secondary 20 | Watch | 2.04 | -0.24 | -16.94 | 2.43 | 15.2 | No official GARP ≥ 60 yet. Not auto-promoted after a crash. |

Prices: Yahoo Finance daily bars, 2026-09-15 America/Toronto. SMA20 and RSI14 from the last 3 months of daily closes. Do not use Equibles for this routine price check.


## Rules

- Ranked Buy → Sell → Hold → Watch → Avoid. Max one Buy (paper) per morning.
- `Avoid` never becomes a buy because it bounced. `Sell` only if you already hold that avoid-quality name.
- `Watch` is not auto-promoted after a crash.
- This job never calls wsli and never sets TRADE_APPROVED.
