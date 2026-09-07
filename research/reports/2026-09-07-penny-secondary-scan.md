# Secondary penny watchlist scan — 2026-09-07

> I am an AI research assistant, not a licensed financial advisor. This is educational information, not personalized financial advice. Consider a qualified advisor for your situation.

**Paper trading active — dry-run only. Buy lines are paper recommendations, never live Wealthsimple orders.**

## What to buy today (from 20 names)

NONE — no buy today.

Official Rebalance-MCP GARP scores are not computed in this job. Quality flags come from `portfolio/penny-secondary-watchlist.yaml`. A live ticket still needs GARP ≥ 60.

| Rank | Ticker | List | Rec | Close | 1d % | 5d % | SMA20 | RSI14 | Why |
|-----:|--------|------|-----|------:|-----:|-----:|------:|------:|-----|
| 1 | GORO | Secondary 20 | Watch | 4.15 | +2.47 | +13.70 | 3.27 | 76.2 | No official GARP ≥ 60 yet. Not auto-promoted after a crash. |
| 2 | ARKO | Secondary 20 | Watch | 4.89 | +1.24 | +11.90 | 4.65 | 51.0 | No official GARP ≥ 60 yet. Not auto-promoted after a crash. |
| 3 | HLLY | Secondary 20 | Watch | 3.05 | -1.61 | +4.45 | 3.02 | 50.0 | No official GARP ≥ 60 yet. Not auto-promoted after a crash. |
| 4 | AMPY | Secondary 20 | Watch | 4.90 | +0.00 | +2.94 | 4.75 | 54.0 | No official GARP ≥ 60 yet. Not auto-promoted after a crash. |
| 5 | TBLA | Secondary 20 | Watch | 3.86 | -0.26 | +2.12 | 3.84 | 48.0 | No official GARP ≥ 60 yet. Not auto-promoted after a crash. |
| 6 | ABUS | Secondary 20 | Watch | 5.15 | +0.59 | +1.58 | 4.95 | 69.3 | No official GARP ≥ 60 yet. Not auto-promoted after a crash. |
| 7 | MDXG | Secondary 20 | Watch | 4.57 | +3.16 | +1.56 | 4.38 | 67.3 | No official GARP ≥ 60 yet. Not auto-promoted after a crash. |
| 8 | AREC | Secondary 20 | Watch | 2.43 | -0.41 | +1.25 | 2.63 | 31.7 | No official GARP ≥ 60 yet. Not auto-promoted after a crash. |
| 9 | SPRO | Secondary 20 | Watch | 1.21 | -0.82 | +0.83 | 1.22 | 55.3 | No official GARP ≥ 60 yet. Not auto-promoted after a crash. |
| 10 | VFF | Secondary 20 | Watch | 2.92 | +0.86 | +0.34 | 2.70 | 74.3 | No official GARP ≥ 60 yet. Not auto-promoted after a crash. |
| 11 | ALTO | Secondary 20 | Watch | 4.04 | +0.25 | -0.74 | 4.13 | 42.1 | No official GARP ≥ 60 yet. Not auto-promoted after a crash. |
| 12 | UWMC | Secondary 20 | Watch | 1.47 | +0.69 | -1.34 | 1.47 | 48.3 | No official GARP ≥ 60 yet. Not auto-promoted after a crash. |
| 13 | CYH | Secondary 20 | Watch | 2.89 | -0.69 | -1.36 | 2.94 | 41.7 | No official GARP ≥ 60 yet. Not auto-promoted after a crash. |
| 14 | GDRX | Secondary 20 | Watch | 3.48 | -1.42 | -1.42 | 3.57 | 36.7 | No official GARP ≥ 60 yet. Not auto-promoted after a crash. |
| 15 | TYGO | Secondary 20 | Watch | 1.07 | +0.94 | -1.83 | 1.12 | 32.1 | No official GARP ≥ 60 yet. Not auto-promoted after a crash. |
| 16 | AISP | Secondary 20 | Watch | 2.05 | -2.38 | -1.91 | 2.08 | 51.8 | No official GARP ≥ 60 yet. Not auto-promoted after a crash. |
| 17 | SABR | Secondary 20 | Watch | 2.13 | +3.40 | -3.18 | 2.13 | 48.5 | No official GARP ≥ 60 yet. Not auto-promoted after a crash. |
| 18 | NAGE | Secondary 20 | Watch | 3.17 | +1.93 | -3.65 | 3.14 | 58.2 | No official GARP ≥ 60 yet. Not auto-promoted after a crash. |
| 19 | SITC | Secondary 20 | Watch | 2.87 | +0.00 | -4.01 | 2.98 | 40.0 | No official GARP ≥ 60 yet. Not auto-promoted after a crash. |
| 20 | VRRM | Secondary 20 | Watch | 4.07 | -3.10 | -7.29 | 4.49 | 25.7 | No official GARP ≥ 60 yet. Not auto-promoted after a crash. |

Prices: Yahoo Finance daily bars, 2026-09-07 America/Toronto. SMA20 and RSI14 from the last 3 months of daily closes. Do not use Equibles for this routine price check.


## Rules

- Ranked Buy → Sell → Hold → Watch → Avoid. Max one Buy (paper) per morning.
- `Avoid` never becomes a buy because it bounced. `Sell` only if you already hold that avoid-quality name.
- `Watch` is not auto-promoted after a crash.
- This job never calls wsli and never sets TRADE_APPROVED.
