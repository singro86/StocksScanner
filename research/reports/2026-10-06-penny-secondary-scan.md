# Secondary penny watchlist scan — 2026-10-06

> I am an AI research assistant, not a licensed financial advisor. This is educational information, not personalized financial advice. Consider a qualified advisor for your situation.

**Paper trading active — dry-run only. Buy lines are paper recommendations, never live Wealthsimple orders.**

## What to buy today (from 20 names)

NONE — no buy today.

Official Rebalance-MCP GARP scores are not computed in this job. Quality flags come from `portfolio/penny-secondary-watchlist.yaml`. A live ticket still needs GARP ≥ 60.

| Rank | Ticker | List | Rec | Close | 1d % | 5d % | SMA20 | RSI14 | Why |
|-----:|--------|------|-----|------:|-----:|-----:|------:|------:|-----|
| 1 | AISP | Secondary 20 | Watch | 2.19 | +8.21 | +19.44 | 1.96 | 62.8 | No official GARP ≥ 60 yet. Not auto-promoted after a crash. |
| 2 | AMPY | Secondary 20 | Watch | 4.50 | +1.69 | +8.55 | 4.49 | 47.3 | No official GARP ≥ 60 yet. Not auto-promoted after a crash. |
| 3 | SITC | Secondary 20 | Watch | 3.26 | +0.62 | +4.82 | 3.05 | 66.4 | No official GARP ≥ 60 yet. Not auto-promoted after a crash. |
| 4 | ALTO | Secondary 20 | Watch | 3.77 | -0.40 | +3.99 | 3.85 | 29.8 | No official GARP ≥ 60 yet. Not auto-promoted after a crash. |
| 5 | GORO | Secondary 20 | Watch | 3.33 | +2.31 | +3.91 | 3.45 | 41.4 | No official GARP ≥ 60 yet. Not auto-promoted after a crash. |
| 6 | TYGO | Secondary 20 | Watch | 0.87 | +1.22 | +3.86 | 0.94 | 31.7 | No official GARP ≥ 60 yet. Not auto-promoted after a crash. |
| 7 | ARKO | Secondary 20 | Watch | 4.25 | +0.83 | +3.29 | 4.29 | 43.0 | No official GARP ≥ 60 yet. Not auto-promoted after a crash. |
| 8 | GDRX | Secondary 20 | Watch | 3.29 | -2.23 | +1.70 | 3.36 | 41.6 | No official GARP ≥ 60 yet. Not auto-promoted after a crash. |
| 9 | SPRO | Secondary 20 | Watch | 1.20 | +3.45 | +0.00 | 1.19 | 57.1 | No official GARP ≥ 60 yet. Not auto-promoted after a crash. |
| 10 | MDXG | Secondary 20 | Watch | 4.57 | +0.44 | -2.14 | 4.68 | 38.6 | No official GARP ≥ 60 yet. Not auto-promoted after a crash. |
| 11 | UWMC | Secondary 20 | Watch | 1.20 | -7.36 | -3.63 | 1.26 | 45.6 | No official GARP ≥ 60 yet. Not auto-promoted after a crash. |
| 12 | ABUS | Secondary 20 | Watch | 4.46 | -4.50 | -4.90 | 4.89 | 28.1 | No official GARP ≥ 60 yet. Not auto-promoted after a crash. |
| 13 | CYH | Secondary 20 | Watch | 2.77 | +0.18 | -4.98 | 2.89 | 36.0 | No official GARP ≥ 60 yet. Not auto-promoted after a crash. |
| 14 | HLLY | Secondary 20 | Watch | 2.33 | +1.53 | -5.10 | 2.53 | 33.7 | No official GARP ≥ 60 yet. Not auto-promoted after a crash. |
| 15 | VRRM | Secondary 20 | Watch | 2.88 | +0.35 | -5.26 | 3.30 | 23.4 | No official GARP ≥ 60 yet. Not auto-promoted after a crash. |
| 16 | AREC | Secondary 20 | Watch | 1.70 | -2.30 | -6.08 | 1.94 | 26.0 | No official GARP ≥ 60 yet. Not auto-promoted after a crash. |
| 17 | TBLA | Secondary 20 | Watch | 3.19 | -2.29 | -6.30 | 3.54 | 16.4 | No official GARP ≥ 60 yet. Not auto-promoted after a crash. |
| 18 | NAGE | Secondary 20 | Watch | 2.69 | +0.56 | -8.64 | 2.95 | 32.2 | No official GARP ≥ 60 yet. Not auto-promoted after a crash. |
| 19 | SABR | Secondary 20 | Watch | 1.93 | -0.26 | -9.62 | 2.15 | 22.4 | No official GARP ≥ 60 yet. Not auto-promoted after a crash. |
| 20 | VFF | Secondary 20 | Watch | 2.76 | +1.47 | -10.97 | 2.92 | 45.8 | No official GARP ≥ 60 yet. Not auto-promoted after a crash. |

Prices: Yahoo Finance daily bars, 2026-10-06 America/Toronto. SMA20 and RSI14 from the last 3 months of daily closes. Do not use Equibles for this routine price check.


## Rules

- Ranked Buy → Sell → Hold → Watch → Avoid. Max one Buy (paper) per morning.
- `Avoid` never becomes a buy because it bounced. `Sell` only if you already hold that avoid-quality name.
- `Watch` is not auto-promoted after a crash.
- This job never calls wsli and never sets TRADE_APPROVED.
