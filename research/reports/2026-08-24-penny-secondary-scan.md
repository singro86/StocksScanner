# Secondary penny watchlist scan — 2026-08-24

> I am an AI research assistant, not a licensed financial advisor. This is educational information, not personalized financial advice. Consider a qualified advisor for your situation.

**Paper trading active — dry-run only. Buy lines are paper recommendations, never live Wealthsimple orders.**

## What to buy today (from 20 names)

NONE — no buy today.

Official Rebalance-MCP GARP scores are not computed in this job. Quality flags come from `portfolio/penny-secondary-watchlist.yaml`. A live ticket still needs GARP ≥ 60.

| Rank | Ticker | List | Rec | Close | 1d % | 5d % | SMA20 | RSI14 | Why |
|-----:|--------|------|-----|------:|-----:|-----:|------:|------:|-----|
| 1 | GORO | Secondary 20 | Watch | 3.22 | +0.94 | +16.67 | 2.53 | 82.4 | No official GARP ≥ 60 yet. Not auto-promoted after a crash. |
| 2 | ABUS | Secondary 20 | Watch | 5.23 | +0.38 | +11.04 | 4.64 | 74.5 | No official GARP ≥ 60 yet. Not auto-promoted after a crash. |
| 3 | NAGE | Secondary 20 | Watch | 3.23 | +0.62 | +6.25 | 3.17 | 38.9 | No official GARP ≥ 60 yet. Not auto-promoted after a crash. |
| 4 | VFF | Secondary 20 | Watch | 2.72 | +0.00 | +5.43 | 2.30 | 84.8 | No official GARP ≥ 60 yet. Not auto-promoted after a crash. |
| 5 | AISP | Secondary 20 | Watch | 2.11 | -1.86 | +4.46 | 1.96 | 59.6 | No official GARP ≥ 60 yet. Not auto-promoted after a crash. |
| 6 | MDXG | Secondary 20 | Watch | 4.37 | +0.92 | +4.30 | 4.28 | 54.3 | No official GARP ≥ 60 yet. Not auto-promoted after a crash. |
| 7 | SITC | Secondary 20 | Watch | 3.07 | +0.00 | +3.37 | 3.34 | 43.1 | No official GARP ≥ 60 yet. Not auto-promoted after a crash. |
| 8 | CYH | Secondary 20 | Watch | 3.03 | +0.66 | +2.71 | 2.92 | 55.6 | No official GARP ≥ 60 yet. Not auto-promoted after a crash. |
| 9 | SPRO | Secondary 20 | Watch | 1.22 | +0.00 | +2.52 | 1.22 | 48.3 | No official GARP ≥ 60 yet. Not auto-promoted after a crash. |
| 10 | ALTO | Secondary 20 | Watch | 4.31 | -1.60 | +2.13 | 4.43 | 22.5 | No official GARP ≥ 60 yet. Not auto-promoted after a crash. |
| 11 | HLLY | Secondary 20 | Watch | 3.08 | -0.32 | +0.98 | 2.99 | 61.3 | No official GARP ≥ 60 yet. Not auto-promoted after a crash. |
| 12 | AMPY | Secondary 20 | Watch | 4.82 | -0.01 | -0.01 | 4.34 | 74.4 | No official GARP ≥ 60 yet. Not auto-promoted after a crash. |
| 13 | VRRM | Secondary 20 | Watch | 4.55 | -0.22 | -1.09 | 4.89 | 21.6 | No official GARP ≥ 60 yet. Not auto-promoted after a crash. |
| 14 | ARKO | Secondary 20 | Watch | 4.75 | +0.00 | -2.26 | 5.92 | 15.4 | No official GARP ≥ 60 yet. Not auto-promoted after a crash. |
| 15 | SABR | Secondary 20 | Watch | 2.10 | -0.24 | -2.78 | 2.06 | 48.4 | No official GARP ≥ 60 yet. Not auto-promoted after a crash. |
| 16 | TBLA | Secondary 20 | Watch | 3.73 | +0.13 | -3.98 | 4.28 | 20.7 | No official GARP ≥ 60 yet. Not auto-promoted after a crash. |
| 17 | UWMC | Secondary 20 | Watch | 1.43 | +2.14 | -4.03 | 1.60 | 33.5 | No official GARP ≥ 60 yet. Not auto-promoted after a crash. |
| 18 | TYGO | Secondary 20 | Watch | 1.09 | +0.37 | -6.50 | 1.37 | 9.7 | No official GARP ≥ 60 yet. Not auto-promoted after a crash. |
| 19 | GDRX | Secondary 20 | Watch | 3.45 | +0.00 | -7.26 | 3.48 | 54.0 | No official GARP ≥ 60 yet. Not auto-promoted after a crash. |
| 20 | AREC | Secondary 20 | Watch | 2.65 | -0.93 | -10.00 | 2.43 | 69.1 | No official GARP ≥ 60 yet. Not auto-promoted after a crash. |

Prices: Yahoo Finance daily bars, 2026-08-24 America/Toronto. SMA20 and RSI14 from the last 3 months of daily closes. Do not use Equibles for this routine price check.


## Rules

- Ranked Buy → Sell → Hold → Watch → Avoid. Max one Buy (paper) per morning.
- `Avoid` never becomes a buy because it bounced. `Sell` only if you already hold that avoid-quality name.
- `Watch` is not auto-promoted after a crash.
- This job never calls wsli and never sets TRADE_APPROVED.
