# Secondary penny watchlist scan — 2026-09-25

> I am an AI research assistant, not a licensed financial advisor. This is educational information, not personalized financial advice. Consider a qualified advisor for your situation.

**Paper trading active — dry-run only. Buy lines are paper recommendations, never live Wealthsimple orders.**

## What to buy today (from 20 names)

NONE — no buy today.

Official Rebalance-MCP GARP scores are not computed in this job. Quality flags come from `portfolio/penny-secondary-watchlist.yaml`. A live ticket still needs GARP ≥ 60.

| Rank | Ticker | List | Rec | Close | 1d % | 5d % | SMA20 | RSI14 | Why |
|-----:|--------|------|-----|------:|-----:|-----:|------:|------:|-----|
| 1 | VFF | Secondary 20 | Watch | 3.16 | +1.28 | +11.27 | 2.92 | 67.7 | No official GARP ≥ 60 yet. Not auto-promoted after a crash. |
| 2 | SPRO | Secondary 20 | Watch | 1.22 | -2.19 | +8.20 | 1.19 | 51.2 | No official GARP ≥ 60 yet. Not auto-promoted after a crash. |
| 3 | SITC | Secondary 20 | Watch | 3.02 | -0.17 | +2.20 | 2.92 | 62.6 | No official GARP ≥ 60 yet. Not auto-promoted after a crash. |
| 4 | CYH | Secondary 20 | Watch | 2.92 | +1.39 | +1.74 | 2.92 | 52.0 | No official GARP ≥ 60 yet. Not auto-promoted after a crash. |
| 5 | NAGE | Secondary 20 | Watch | 3.04 | +1.00 | +1.67 | 3.07 | 34.1 | No official GARP ≥ 60 yet. Not auto-promoted after a crash. |
| 6 | ARKO | Secondary 20 | Watch | 4.26 | +0.71 | +0.95 | 4.46 | 24.0 | No official GARP ≥ 60 yet. Not auto-promoted after a crash. |
| 7 | GDRX | Secondary 20 | Watch | 3.38 | +0.74 | +0.15 | 3.43 | 44.6 | No official GARP ≥ 60 yet. Not auto-promoted after a crash. |
| 8 | SABR | Secondary 20 | Watch | 2.25 | -0.22 | -0.66 | 2.19 | 56.0 | No official GARP ≥ 60 yet. Not auto-promoted after a crash. |
| 9 | UWMC | Secondary 20 | Watch | 1.24 | +1.43 | -1.01 | 1.33 | 18.4 | No official GARP ≥ 60 yet. Not auto-promoted after a crash. |
| 10 | HLLY | Secondary 20 | Watch | 2.50 | +3.09 | -1.38 | 2.73 | 28.6 | No official GARP ≥ 60 yet. Not auto-promoted after a crash. |
| 11 | AISP | Secondary 20 | Watch | 1.89 | +0.00 | -1.56 | 1.99 | 33.3 | No official GARP ≥ 60 yet. Not auto-promoted after a crash. |
| 12 | ABUS | Secondary 20 | Watch | 4.90 | +0.41 | -2.20 | 5.06 | 24.5 | No official GARP ≥ 60 yet. Not auto-promoted after a crash. |
| 13 | AREC | Secondary 20 | Watch | 1.93 | +2.39 | -2.78 | 2.16 | 21.5 | No official GARP ≥ 60 yet. Not auto-promoted after a crash. |
| 14 | TBLA | Secondary 20 | Watch | 3.49 | +1.16 | -3.06 | 3.71 | 31.3 | No official GARP ≥ 60 yet. Not auto-promoted after a crash. |
| 15 | GORO | Secondary 20 | Watch | 3.47 | -1.42 | -3.34 | 3.65 | 21.7 | No official GARP ≥ 60 yet. Not auto-promoted after a crash. |
| 16 | MDXG | Secondary 20 | Watch | 4.50 | -4.35 | -5.56 | 4.65 | 47.0 | No official GARP ≥ 60 yet. Not auto-promoted after a crash. |
| 17 | AMPY | Secondary 20 | Watch | 4.23 | -2.54 | -6.00 | 4.70 | 24.0 | No official GARP ≥ 60 yet. Not auto-promoted after a crash. |
| 18 | ALTO | Secondary 20 | Watch | 3.75 | +0.27 | -6.25 | 3.96 | 32.9 | No official GARP ≥ 60 yet. Not auto-promoted after a crash. |
| 19 | VRRM | Secondary 20 | Watch | 3.25 | -0.15 | -6.75 | 3.74 | 15.8 | No official GARP ≥ 60 yet. Not auto-promoted after a crash. |
| 20 | TYGO | Secondary 20 | Watch | 0.87 | -0.89 | -10.54 | 1.01 | 15.6 | No official GARP ≥ 60 yet. Not auto-promoted after a crash. |

Prices: Yahoo Finance daily bars, 2026-09-25 America/Toronto. SMA20 and RSI14 from the last 3 months of daily closes. Do not use Equibles for this routine price check.


## Rules

- Ranked Buy → Sell → Hold → Watch → Avoid. Max one Buy (paper) per morning.
- `Avoid` never becomes a buy because it bounced. `Sell` only if you already hold that avoid-quality name.
- `Watch` is not auto-promoted after a crash.
- This job never calls wsli and never sets TRADE_APPROVED.
