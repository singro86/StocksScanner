# Secondary penny watchlist scan — 2026-09-09

> I am an AI research assistant, not a licensed financial advisor. This is educational information, not personalized financial advice. Consider a qualified advisor for your situation.

**Paper trading active — dry-run only. Buy lines are paper recommendations, never live Wealthsimple orders.**

## What to buy today (from 20 names)

NONE — no buy today.

Official Rebalance-MCP GARP scores are not computed in this job. Quality flags come from `portfolio/penny-secondary-watchlist.yaml`. A live ticket still needs GARP ≥ 60.

| Rank | Ticker | List | Rec | Close | 1d % | 5d % | SMA20 | RSI14 | Why |
|-----:|--------|------|-----|------:|-----:|-----:|------:|------:|-----|
| 1 | SABR | Secondary 20 | Watch | 2.25 | -0.22 | +12.19 | 2.15 | 58.1 | No official GARP ≥ 60 yet. Not auto-promoted after a crash. |
| 2 | VFF | Secondary 20 | Watch | 2.98 | -1.49 | +5.11 | 2.76 | 75.2 | No official GARP ≥ 60 yet. Not auto-promoted after a crash. |
| 3 | AREC | Secondary 20 | Watch | 2.42 | -1.02 | +4.98 | 2.59 | 40.7 | No official GARP ≥ 60 yet. Not auto-promoted after a crash. |
| 4 | HLLY | Secondary 20 | Watch | 2.97 | -0.17 | +3.65 | 3.00 | 41.5 | No official GARP ≥ 60 yet. Not auto-promoted after a crash. |
| 5 | MDXG | Secondary 20 | Watch | 4.63 | -0.88 | +2.41 | 4.42 | 59.1 | No official GARP ≥ 60 yet. Not auto-promoted after a crash. |
| 6 | GORO | Secondary 20 | Watch | 3.66 | -4.62 | +2.31 | 3.40 | 64.2 | No official GARP ≥ 60 yet. Not auto-promoted after a crash. |
| 7 | UWMC | Secondary 20 | Watch | 1.39 | +0.00 | +1.46 | 1.47 | 41.4 | No official GARP ≥ 60 yet. Not auto-promoted after a crash. |
| 8 | ABUS | Secondary 20 | Watch | 5.15 | -0.58 | +1.18 | 5.00 | 59.1 | No official GARP ≥ 60 yet. Not auto-promoted after a crash. |
| 9 | ALTO | Secondary 20 | Watch | 4.03 | -2.07 | +0.12 | 4.12 | 43.3 | No official GARP ≥ 60 yet. Not auto-promoted after a crash. |
| 10 | CYH | Secondary 20 | Watch | 2.93 | +3.17 | +0.00 | 2.94 | 51.2 | No official GARP ≥ 60 yet. Not auto-promoted after a crash. |
| 11 | AMPY | Secondary 20 | Watch | 4.97 | +0.71 | -0.30 | 4.81 | 58.9 | No official GARP ≥ 60 yet. Not auto-promoted after a crash. |
| 12 | TBLA | Secondary 20 | Watch | 3.71 | -2.75 | -0.40 | 3.80 | 40.8 | No official GARP ≥ 60 yet. Not auto-promoted after a crash. |
| 13 | SPRO | Secondary 20 | Watch | 1.20 | +0.42 | -0.42 | 1.21 | 40.0 | No official GARP ≥ 60 yet. Not auto-promoted after a crash. |
| 14 | TYGO | Secondary 20 | Watch | 1.05 | -0.94 | -0.94 | 1.11 | 33.3 | No official GARP ≥ 60 yet. Not auto-promoted after a crash. |
| 15 | ARKO | Secondary 20 | Watch | 4.46 | -5.31 | -1.00 | 4.65 | 42.9 | No official GARP ≥ 60 yet. Not auto-promoted after a crash. |
| 16 | GDRX | Secondary 20 | Watch | 3.41 | -3.12 | -1.45 | 3.55 | 42.5 | No official GARP ≥ 60 yet. Not auto-promoted after a crash. |
| 17 | AISP | Secondary 20 | Watch | 2.02 | -2.88 | -1.46 | 2.08 | 47.7 | No official GARP ≥ 60 yet. Not auto-promoted after a crash. |
| 18 | NAGE | Secondary 20 | Watch | 3.07 | -0.97 | -1.92 | 3.15 | 43.4 | No official GARP ≥ 60 yet. Not auto-promoted after a crash. |
| 19 | SITC | Secondary 20 | Watch | 2.83 | -1.74 | -2.41 | 2.97 | 30.0 | No official GARP ≥ 60 yet. Not auto-promoted after a crash. |
| 20 | VRRM | Secondary 20 | Watch | 3.81 | -2.69 | -8.75 | 4.40 | 8.0 | No official GARP ≥ 60 yet. Not auto-promoted after a crash. |

Prices: Yahoo Finance daily bars, 2026-09-09 America/Toronto. SMA20 and RSI14 from the last 3 months of daily closes. Do not use Equibles for this routine price check.


## Rules

- Ranked Buy → Sell → Hold → Watch → Avoid. Max one Buy (paper) per morning.
- `Avoid` never becomes a buy because it bounced. `Sell` only if you already hold that avoid-quality name.
- `Watch` is not auto-promoted after a crash.
- This job never calls wsli and never sets TRADE_APPROVED.
