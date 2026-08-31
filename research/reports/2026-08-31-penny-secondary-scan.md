# Secondary penny watchlist scan — 2026-08-31

> I am an AI research assistant, not a licensed financial advisor. This is educational information, not personalized financial advice. Consider a qualified advisor for your situation.

**Paper trading active — dry-run only. Buy lines are paper recommendations, never live Wealthsimple orders.**

## What to buy today (from 20 names)

NONE — no buy today.

Official Rebalance-MCP GARP scores are not computed in this job. Quality flags come from `portfolio/penny-secondary-watchlist.yaml`. A live ticket still needs GARP ≥ 60.

| Rank | Ticker | List | Rec | Close | 1d % | 5d % | SMA20 | RSI14 | Why |
|-----:|--------|------|-----|------:|-----:|-----:|------:|------:|-----|
| 1 | VFF | Secondary 20 | Watch | 2.92 | +0.17 | +7.57 | 2.53 | 80.9 | No official GARP ≥ 60 yet. Not auto-promoted after a crash. |
| 2 | MDXG | Secondary 20 | Watch | 4.50 | -0.11 | +5.27 | 4.32 | 58.5 | No official GARP ≥ 60 yet. Not auto-promoted after a crash. |
| 3 | UWMC | Secondary 20 | Watch | 1.48 | -1.01 | +3.87 | 1.50 | 45.9 | No official GARP ≥ 60 yet. Not auto-promoted after a crash. |
| 4 | GORO | Secondary 20 | Watch | 3.66 | +0.27 | +3.68 | 2.94 | 75.8 | No official GARP ≥ 60 yet. Not auto-promoted after a crash. |
| 5 | AMPY | Secondary 20 | Watch | 4.88 | +2.63 | +2.20 | 4.56 | 63.1 | No official GARP ≥ 60 yet. Not auto-promoted after a crash. |
| 6 | TBLA | Secondary 20 | Watch | 3.71 | -1.72 | +1.78 | 3.94 | 32.6 | No official GARP ≥ 60 yet. Not auto-promoted after a crash. |
| 7 | GDRX | Secondary 20 | Watch | 3.47 | -1.70 | +0.87 | 3.58 | 35.1 | No official GARP ≥ 60 yet. Not auto-promoted after a crash. |
| 8 | NAGE | Secondary 20 | Watch | 3.23 | -1.67 | +0.78 | 3.15 | 62.8 | No official GARP ≥ 60 yet. Not auto-promoted after a crash. |
| 9 | TYGO | Secondary 20 | Watch | 1.05 | -3.21 | +0.48 | 1.20 | 26.5 | No official GARP ≥ 60 yet. Not auto-promoted after a crash. |
| 10 | AISP | Secondary 20 | Watch | 2.15 | +3.11 | +0.23 | 2.06 | 57.7 | No official GARP ≥ 60 yet. Not auto-promoted after a crash. |
| 11 | SPRO | Secondary 20 | Watch | 1.21 | +0.42 | -0.82 | 1.22 | 45.3 | No official GARP ≥ 60 yet. Not auto-promoted after a crash. |
| 12 | VRRM | Secondary 20 | Watch | 4.42 | +0.68 | -1.12 | 4.72 | 33.0 | No official GARP ≥ 60 yet. Not auto-promoted after a crash. |
| 13 | ABUS | Secondary 20 | Watch | 5.07 | +0.00 | -2.50 | 4.84 | 65.6 | No official GARP ≥ 60 yet. Not auto-promoted after a crash. |
| 14 | CYH | Secondary 20 | Watch | 2.92 | -0.51 | -3.16 | 2.95 | 57.4 | No official GARP ≥ 60 yet. Not auto-promoted after a crash. |
| 15 | SABR | Secondary 20 | Watch | 2.18 | -0.91 | -3.54 | 2.14 | 62.3 | No official GARP ≥ 60 yet. Not auto-promoted after a crash. |
| 16 | HLLY | Secondary 20 | Watch | 2.88 | -1.54 | -4.17 | 3.03 | 38.7 | No official GARP ≥ 60 yet. Not auto-promoted after a crash. |
| 17 | SITC | Secondary 20 | Watch | 2.94 | -1.67 | -4.24 | 3.04 | 48.0 | No official GARP ≥ 60 yet. Not auto-promoted after a crash. |
| 18 | ARKO | Secondary 20 | Watch | 4.50 | +3.09 | -4.55 | 5.09 | 53.4 | No official GARP ≥ 60 yet. Not auto-promoted after a crash. |
| 19 | AREC | Secondary 20 | Watch | 2.38 | -0.62 | -4.98 | 2.61 | 32.3 | No official GARP ≥ 60 yet. Not auto-promoted after a crash. |
| 20 | ALTO | Secondary 20 | Watch | 3.90 | -4.18 | -6.92 | 4.28 | 39.4 | No official GARP ≥ 60 yet. Not auto-promoted after a crash. |

Prices: Yahoo Finance daily bars, 2026-08-31 America/Toronto. SMA20 and RSI14 from the last 3 months of daily closes. Do not use Equibles for this routine price check.


## Rules

- Ranked Buy → Sell → Hold → Watch → Avoid. Max one Buy (paper) per morning.
- `Avoid` never becomes a buy because it bounced. `Sell` only if you already hold that avoid-quality name.
- `Watch` is not auto-promoted after a crash.
- This job never calls wsli and never sets TRADE_APPROVED.
