# Secondary penny watchlist scan — 2026-09-16

> I am an AI research assistant, not a licensed financial advisor. This is educational information, not personalized financial advice. Consider a qualified advisor for your situation.

**Paper trading active — dry-run only. Buy lines are paper recommendations, never live Wealthsimple orders.**

## What to buy today (from 20 names)

NONE — no buy today.

Official Rebalance-MCP GARP scores are not computed in this job. Quality flags come from `portfolio/penny-secondary-watchlist.yaml`. A live ticket still needs GARP ≥ 60.

| Rank | Ticker | List | Rec | Close | 1d % | 5d % | SMA20 | RSI14 | Why |
|-----:|--------|------|-----|------:|-----:|-----:|------:|------:|-----|
| 1 | SABR | Secondary 20 | Watch | 2.29 | +9.33 | +6.78 | 2.15 | 55.0 | No official GARP ≥ 60 yet. Not auto-promoted after a crash. |
| 2 | TBLA | Secondary 20 | Watch | 3.85 | +0.13 | +3.91 | 3.78 | 59.4 | No official GARP ≥ 60 yet. Not auto-promoted after a crash. |
| 3 | SITC | Secondary 20 | Watch | 2.90 | +1.57 | +3.38 | 2.93 | 37.9 | No official GARP ≥ 60 yet. Not auto-promoted after a crash. |
| 4 | GDRX | Secondary 20 | Watch | 3.44 | -1.29 | +3.14 | 3.48 | 38.9 | No official GARP ≥ 60 yet. Not auto-promoted after a crash. |
| 5 | ALTO | Secondary 20 | Watch | 4.09 | +0.00 | +1.74 | 4.07 | 50.6 | No official GARP ≥ 60 yet. Not auto-promoted after a crash. |
| 6 | CYH | Secondary 20 | Watch | 3.00 | +0.84 | +1.52 | 2.94 | 59.0 | No official GARP ≥ 60 yet. Not auto-promoted after a crash. |
| 7 | MDXG | Secondary 20 | Watch | 4.72 | +0.00 | +0.85 | 4.52 | 68.3 | No official GARP ≥ 60 yet. Not auto-promoted after a crash. |
| 8 | GORO | Secondary 20 | Watch | 3.58 | +1.85 | -0.97 | 3.60 | 50.7 | No official GARP ≥ 60 yet. Not auto-promoted after a crash. |
| 9 | ARKO | Secondary 20 | Watch | 4.38 | -0.79 | -1.24 | 4.60 | 41.6 | No official GARP ≥ 60 yet. Not auto-promoted after a crash. |
| 10 | NAGE | Secondary 20 | Watch | 3.01 | +0.33 | -1.31 | 3.14 | 28.4 | No official GARP ≥ 60 yet. Not auto-promoted after a crash. |
| 11 | TYGO | Secondary 20 | Watch | 1.02 | -0.48 | -1.44 | 1.06 | 46.5 | No official GARP ≥ 60 yet. Not auto-promoted after a crash. |
| 12 | ABUS | Secondary 20 | Watch | 5.07 | +0.20 | -1.93 | 5.11 | 34.2 | No official GARP ≥ 60 yet. Not auto-promoted after a crash. |
| 13 | VFF | Secondary 20 | Watch | 2.87 | +0.88 | -3.54 | 2.84 | 50.4 | No official GARP ≥ 60 yet. Not auto-promoted after a crash. |
| 14 | SPRO | Secondary 20 | Watch | 1.11 | -1.33 | -4.70 | 1.19 | 26.7 | No official GARP ≥ 60 yet. Not auto-promoted after a crash. |
| 15 | AMPY | Secondary 20 | Watch | 4.62 | -6.24 | -6.05 | 4.84 | 51.8 | No official GARP ≥ 60 yet. Not auto-promoted after a crash. |
| 16 | AISP | Secondary 20 | Watch | 1.90 | +0.84 | -6.61 | 2.06 | 32.4 | No official GARP ≥ 60 yet. Not auto-promoted after a crash. |
| 17 | VRRM | Secondary 20 | Watch | 3.48 | -1.84 | -6.84 | 4.13 | 12.1 | No official GARP ≥ 60 yet. Not auto-promoted after a crash. |
| 18 | HLLY | Secondary 20 | Watch | 2.67 | +1.71 | -8.08 | 2.90 | 42.1 | No official GARP ≥ 60 yet. Not auto-promoted after a crash. |
| 19 | UWMC | Secondary 20 | Watch | 1.25 | -2.34 | -8.76 | 1.41 | 28.6 | No official GARP ≥ 60 yet. Not auto-promoted after a crash. |
| 20 | AREC | Secondary 20 | Watch | 2.01 | -2.43 | -12.99 | 2.40 | 17.0 | No official GARP ≥ 60 yet. Not auto-promoted after a crash. |

Prices: Yahoo Finance daily bars, 2026-09-16 America/Toronto. SMA20 and RSI14 from the last 3 months of daily closes. Do not use Equibles for this routine price check.


## Rules

- Ranked Buy → Sell → Hold → Watch → Avoid. Max one Buy (paper) per morning.
- `Avoid` never becomes a buy because it bounced. `Sell` only if you already hold that avoid-quality name.
- `Watch` is not auto-promoted after a crash.
- This job never calls wsli and never sets TRADE_APPROVED.
