# Secondary penny watchlist scan — 2026-10-07

> I am an AI research assistant, not a licensed financial advisor. This is educational information, not personalized financial advice. Consider a qualified advisor for your situation.

**Paper trading active — dry-run only. Buy lines are paper recommendations, never live Wealthsimple orders.**

## What to buy today (from 20 names)

NONE — no buy today.

Official Rebalance-MCP GARP scores are not computed in this job. Quality flags come from `portfolio/penny-secondary-watchlist.yaml`. A live ticket still needs GARP ≥ 60.

| Rank | Ticker | List | Rec | Close | 1d % | 5d % | SMA20 | RSI14 | Why |
|-----:|--------|------|-----|------:|-----:|-----:|------:|------:|-----|
| 1 | AISP | Secondary 20 | Watch | 2.15 | +1.66 | +15.32 | 1.96 | 59.4 | No official GARP ≥ 60 yet. Not auto-promoted after a crash. |
| 2 | AMPY | Secondary 20 | Watch | 4.46 | -0.34 | +6.06 | 4.47 | 45.3 | No official GARP ≥ 60 yet. Not auto-promoted after a crash. |
| 3 | ARKO | Secondary 20 | Watch | 4.25 | +1.07 | +3.03 | 4.28 | 43.8 | No official GARP ≥ 60 yet. Not auto-promoted after a crash. |
| 4 | GORO | Secondary 20 | Watch | 3.23 | -4.30 | +1.10 | 3.43 | 36.6 | No official GARP ≥ 60 yet. Not auto-promoted after a crash. |
| 5 | TYGO | Secondary 20 | Watch | 0.91 | +5.19 | -0.01 | 0.93 | 40.9 | No official GARP ≥ 60 yet. Not auto-promoted after a crash. |
| 6 | ALTO | Secondary 20 | Watch | 3.69 | -1.73 | -0.14 | 3.83 | 25.9 | No official GARP ≥ 60 yet. Not auto-promoted after a crash. |
| 7 | GDRX | Secondary 20 | Watch | 3.29 | +0.46 | -0.15 | 3.36 | 41.1 | No official GARP ≥ 60 yet. Not auto-promoted after a crash. |
| 8 | HLLY | Secondary 20 | Watch | 2.35 | +1.08 | -0.64 | 2.50 | 33.7 | No official GARP ≥ 60 yet. Not auto-promoted after a crash. |
| 9 | MDXG | Secondary 20 | Watch | 4.63 | +0.22 | -0.64 | 4.68 | 45.8 | No official GARP ≥ 60 yet. Not auto-promoted after a crash. |
| 10 | TBLA | Secondary 20 | Watch | 3.33 | +3.25 | -0.74 | 3.52 | 29.8 | No official GARP ≥ 60 yet. Not auto-promoted after a crash. |
| 11 | UWMC | Secondary 20 | Watch | 1.16 | -3.75 | -2.12 | 1.25 | 37.0 | No official GARP ≥ 60 yet. Not auto-promoted after a crash. |
| 12 | SPRO | Secondary 20 | Watch | 1.17 | -1.68 | -3.31 | 1.18 | 54.0 | No official GARP ≥ 60 yet. Not auto-promoted after a crash. |
| 13 | CYH | Secondary 20 | Watch | 2.74 | +0.00 | -4.20 | 2.88 | 37.5 | No official GARP ≥ 60 yet. Not auto-promoted after a crash. |
| 14 | VRRM | Secondary 20 | Watch | 2.94 | +4.26 | -5.16 | 3.26 | 31.5 | No official GARP ≥ 60 yet. Not auto-promoted after a crash. |
| 15 | SITC | Secondary 20 | Watch | 3.19 | -0.16 | -5.19 | 3.07 | 62.3 | No official GARP ≥ 60 yet. Not auto-promoted after a crash. |
| 16 | NAGE | Secondary 20 | Watch | 2.75 | +2.04 | -5.99 | 2.94 | 36.3 | No official GARP ≥ 60 yet. Not auto-promoted after a crash. |
| 17 | VFF | Secondary 20 | Watch | 2.73 | -2.33 | -6.36 | 2.91 | 43.7 | No official GARP ≥ 60 yet. Not auto-promoted after a crash. |
| 18 | SABR | Secondary 20 | Watch | 1.98 | +2.87 | -6.84 | 2.14 | 27.7 | No official GARP ≥ 60 yet. Not auto-promoted after a crash. |
| 19 | AREC | Secondary 20 | Watch | 1.65 | -3.23 | -8.10 | 1.91 | 16.2 | No official GARP ≥ 60 yet. Not auto-promoted after a crash. |
| 20 | ABUS | Secondary 20 | Watch | 4.36 | -2.79 | -8.89 | 4.85 | 25.1 | No official GARP ≥ 60 yet. Not auto-promoted after a crash. |

Prices: Yahoo Finance daily bars, 2026-10-07 America/Toronto. SMA20 and RSI14 from the last 3 months of daily closes. Do not use Equibles for this routine price check.


## Rules

- Ranked Buy → Sell → Hold → Watch → Avoid. Max one Buy (paper) per morning.
- `Avoid` never becomes a buy because it bounced. `Sell` only if you already hold that avoid-quality name.
- `Watch` is not auto-promoted after a crash.
- This job never calls wsli and never sets TRADE_APPROVED.
