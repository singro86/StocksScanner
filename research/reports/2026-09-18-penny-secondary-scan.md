# Secondary penny watchlist scan — 2026-09-18

> I am an AI research assistant, not a licensed financial advisor. This is educational information, not personalized financial advice. Consider a qualified advisor for your situation.

**Paper trading active — dry-run only. Buy lines are paper recommendations, never live Wealthsimple orders.**

## What to buy today (from 20 names)

NONE — no buy today.

Official Rebalance-MCP GARP scores are not computed in this job. Quality flags come from `portfolio/penny-secondary-watchlist.yaml`. A live ticket still needs GARP ≥ 60.

| Rank | Ticker | List | Rec | Close | 1d % | 5d % | SMA20 | RSI14 | Why |
|-----:|--------|------|-----|------:|-----:|-----:|------:|------:|-----|
| 1 | MDXG | Secondary 20 | Watch | 4.77 | +1.71 | +4.38 | 4.55 | 65.9 | No official GARP ≥ 60 yet. Not auto-promoted after a crash. |
| 2 | SITC | Secondary 20 | Watch | 2.94 | +0.17 | +4.08 | 2.93 | 44.3 | No official GARP ≥ 60 yet. Not auto-promoted after a crash. |
| 3 | SABR | Secondary 20 | Watch | 2.25 | -3.23 | +3.46 | 2.17 | 52.1 | No official GARP ≥ 60 yet. Not auto-promoted after a crash. |
| 4 | ALTO | Secondary 20 | Watch | 3.98 | -1.12 | +1.92 | 4.05 | 44.9 | No official GARP ≥ 60 yet. Not auto-promoted after a crash. |
| 5 | SPRO | Secondary 20 | Watch | 1.12 | +0.00 | -0.89 | 1.18 | 31.8 | No official GARP ≥ 60 yet. Not auto-promoted after a crash. |
| 6 | NAGE | Secondary 20 | Watch | 3.01 | +0.67 | -0.99 | 3.12 | 23.1 | No official GARP ≥ 60 yet. Not auto-promoted after a crash. |
| 7 | AISP | Secondary 20 | Watch | 1.92 | -1.79 | -1.03 | 2.05 | 36.3 | No official GARP ≥ 60 yet. Not auto-promoted after a crash. |
| 8 | GDRX | Secondary 20 | Watch | 3.35 | -1.47 | -1.18 | 3.46 | 39.8 | No official GARP ≥ 60 yet. Not auto-promoted after a crash. |
| 9 | VFF | Secondary 20 | Watch | 2.85 | +0.18 | -1.22 | 2.87 | 43.7 | No official GARP ≥ 60 yet. Not auto-promoted after a crash. |
| 10 | ABUS | Secondary 20 | Watch | 5.01 | -1.08 | -2.05 | 5.12 | 41.8 | No official GARP ≥ 60 yet. Not auto-promoted after a crash. |
| 11 | CYH | Secondary 20 | Watch | 2.85 | -2.38 | -2.38 | 2.93 | 42.3 | No official GARP ≥ 60 yet. Not auto-promoted after a crash. |
| 12 | GORO | Secondary 20 | Watch | 3.51 | -0.01 | -2.51 | 3.66 | 45.3 | No official GARP ≥ 60 yet. Not auto-promoted after a crash. |
| 13 | TBLA | Secondary 20 | Watch | 3.66 | -0.54 | -3.68 | 3.77 | 42.5 | No official GARP ≥ 60 yet. Not auto-promoted after a crash. |
| 14 | HLLY | Secondary 20 | Watch | 2.59 | -2.26 | -3.72 | 2.85 | 34.3 | No official GARP ≥ 60 yet. Not auto-promoted after a crash. |
| 15 | UWMC | Secondary 20 | Watch | 1.29 | +2.78 | -4.07 | 1.39 | 32.1 | No official GARP ≥ 60 yet. Not auto-promoted after a crash. |
| 16 | TYGO | Secondary 20 | Watch | 0.97 | -1.26 | -4.55 | 1.05 | 17.0 | No official GARP ≥ 60 yet. Not auto-promoted after a crash. |
| 17 | VRRM | Secondary 20 | Watch | 3.38 | -0.88 | -4.79 | 4.00 | 11.4 | No official GARP ≥ 60 yet. Not auto-promoted after a crash. |
| 18 | ARKO | Secondary 20 | Watch | 4.29 | -1.27 | -5.20 | 4.56 | 47.2 | No official GARP ≥ 60 yet. Not auto-promoted after a crash. |
| 19 | AREC | Secondary 20 | Watch | 1.99 | -0.75 | -7.24 | 2.33 | 25.7 | No official GARP ≥ 60 yet. Not auto-promoted after a crash. |
| 20 | AMPY | Secondary 20 | Watch | 4.53 | -0.77 | -8.21 | 4.81 | 39.5 | No official GARP ≥ 60 yet. Not auto-promoted after a crash. |

Prices: Yahoo Finance daily bars, 2026-09-18 America/Toronto. SMA20 and RSI14 from the last 3 months of daily closes. Do not use Equibles for this routine price check.


## Rules

- Ranked Buy → Sell → Hold → Watch → Avoid. Max one Buy (paper) per morning.
- `Avoid` never becomes a buy because it bounced. `Sell` only if you already hold that avoid-quality name.
- `Watch` is not auto-promoted after a crash.
- This job never calls wsli and never sets TRADE_APPROVED.
