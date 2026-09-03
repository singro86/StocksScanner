# Secondary penny watchlist scan — 2026-09-03

> I am an AI research assistant, not a licensed financial advisor. This is educational information, not personalized financial advice. Consider a qualified advisor for your situation.

**Paper trading active — dry-run only. Buy lines are paper recommendations, never live Wealthsimple orders.**

## What to buy today (from 20 names)

NONE — no buy today.

Official Rebalance-MCP GARP scores are not computed in this job. Quality flags come from `portfolio/penny-secondary-watchlist.yaml`. A live ticket still needs GARP ≥ 60.

| Rank | Ticker | List | Rec | Close | 1d % | 5d % | SMA20 | RSI14 | Why |
|-----:|--------|------|-----|------:|-----:|-----:|------:|------:|-----|
| 1 | GORO | Secondary 20 | Watch | 4.10 | +5.92 | +8.16 | 3.19 | 75.8 | No official GARP ≥ 60 yet. Not auto-promoted after a crash. |
| 2 | ARKO | Secondary 20 | Watch | 4.77 | +0.63 | +6.95 | 4.68 | 47.0 | No official GARP ≥ 60 yet. Not auto-promoted after a crash. |
| 3 | AMPY | Secondary 20 | Watch | 4.91 | -1.90 | +4.14 | 4.71 | 56.0 | No official GARP ≥ 60 yet. Not auto-promoted after a crash. |
| 4 | TBLA | Secondary 20 | Watch | 3.85 | +0.92 | +2.25 | 3.85 | 38.7 | No official GARP ≥ 60 yet. Not auto-promoted after a crash. |
| 5 | SPRO | Secondary 20 | Watch | 1.23 | +0.41 | +1.24 | 1.22 | 48.9 | No official GARP ≥ 60 yet. Not auto-promoted after a crash. |
| 6 | GDRX | Secondary 20 | Watch | 3.52 | +1.88 | +0.14 | 3.58 | 37.3 | No official GARP ≥ 60 yet. Not auto-promoted after a crash. |
| 7 | AISP | Secondary 20 | Watch | 2.18 | +2.35 | +0.00 | 2.08 | 62.8 | No official GARP ≥ 60 yet. Not auto-promoted after a crash. |
| 8 | HLLY | Secondary 20 | Watch | 2.97 | +1.36 | +0.00 | 3.02 | 41.9 | No official GARP ≥ 60 yet. Not auto-promoted after a crash. |
| 9 | CYH | Secondary 20 | Watch | 2.92 | +0.86 | -0.17 | 2.95 | 40.7 | No official GARP ≥ 60 yet. Not auto-promoted after a crash. |
| 10 | ABUS | Secondary 20 | Watch | 5.13 | +0.59 | -0.77 | 4.92 | 69.8 | No official GARP ≥ 60 yet. Not auto-promoted after a crash. |
| 11 | ALTO | Secondary 20 | Watch | 4.04 | -1.58 | -1.10 | 4.15 | 44.2 | No official GARP ≥ 60 yet. Not auto-promoted after a crash. |
| 12 | VFF | Secondary 20 | Watch | 2.83 | -2.25 | -1.22 | 2.65 | 68.8 | No official GARP ≥ 60 yet. Not auto-promoted after a crash. |
| 13 | UWMC | Secondary 20 | Watch | 1.46 | +0.34 | -1.69 | 1.46 | 40.1 | No official GARP ≥ 60 yet. Not auto-promoted after a crash. |
| 14 | NAGE | Secondary 20 | Watch | 3.13 | -1.10 | -2.34 | 3.14 | 57.9 | No official GARP ≥ 60 yet. Not auto-promoted after a crash. |
| 15 | MDXG | Secondary 20 | Watch | 4.38 | -3.63 | -2.77 | 4.37 | 55.3 | No official GARP ≥ 60 yet. Not auto-promoted after a crash. |
| 16 | SITC | Secondary 20 | Watch | 2.89 | -1.36 | -3.02 | 3.00 | 42.9 | No official GARP ≥ 60 yet. Not auto-promoted after a crash. |
| 17 | TYGO | Secondary 20 | Watch | 1.07 | +0.47 | -3.15 | 1.13 | 27.0 | No official GARP ≥ 60 yet. Not auto-promoted after a crash. |
| 18 | SABR | Secondary 20 | Watch | 2.06 | -1.20 | -3.50 | 2.13 | 39.8 | No official GARP ≥ 60 yet. Not auto-promoted after a crash. |
| 19 | AREC | Secondary 20 | Watch | 2.44 | -0.20 | -4.13 | 2.64 | 35.0 | No official GARP ≥ 60 yet. Not auto-promoted after a crash. |
| 20 | VRRM | Secondary 20 | Watch | 4.16 | -1.07 | -5.78 | 4.53 | 24.9 | No official GARP ≥ 60 yet. Not auto-promoted after a crash. |

Prices: Yahoo Finance daily bars, 2026-09-03 America/Toronto. SMA20 and RSI14 from the last 3 months of daily closes. Do not use Equibles for this routine price check.


## Rules

- Ranked Buy → Sell → Hold → Watch → Avoid. Max one Buy (paper) per morning.
- `Avoid` never becomes a buy because it bounced. `Sell` only if you already hold that avoid-quality name.
- `Watch` is not auto-promoted after a crash.
- This job never calls wsli and never sets TRADE_APPROVED.
