# Secondary penny watchlist scan — 2026-09-01

> I am an AI research assistant, not a licensed financial advisor. This is educational information, not personalized financial advice. Consider a qualified advisor for your situation.

**Paper trading active — dry-run only. Buy lines are paper recommendations, never live Wealthsimple orders.**

## What to buy today (from 20 names)

NONE — no buy today.

Official Rebalance-MCP GARP scores are not computed in this job. Quality flags come from `portfolio/penny-secondary-watchlist.yaml`. A live ticket still needs GARP ≥ 60.

| Rank | Ticker | List | Rec | Close | 1d % | 5d % | SMA20 | RSI14 | Why |
|-----:|--------|------|-----|------:|-----:|-----:|------:|------:|-----|
| 1 | AMPY | Secondary 20 | Watch | 4.95 | +0.61 | +6.00 | 4.61 | 70.3 | No official GARP ≥ 60 yet. Not auto-promoted after a crash. |
| 2 | MDXG | Secondary 20 | Watch | 4.53 | -0.33 | +4.26 | 4.34 | 61.8 | No official GARP ≥ 60 yet. Not auto-promoted after a crash. |
| 3 | GDRX | Secondary 20 | Watch | 3.54 | +1.43 | +1.87 | 3.59 | 47.3 | No official GARP ≥ 60 yet. Not auto-promoted after a crash. |
| 4 | TYGO | Secondary 20 | Watch | 1.06 | -0.47 | +1.43 | 1.15 | 29.3 | No official GARP ≥ 60 yet. Not auto-promoted after a crash. |
| 5 | HLLY | Secondary 20 | Watch | 2.91 | +1.75 | +0.69 | 3.03 | 38.2 | No official GARP ≥ 60 yet. Not auto-promoted after a crash. |
| 6 | TBLA | Secondary 20 | Watch | 3.72 | -0.27 | +0.54 | 3.86 | 41.3 | No official GARP ≥ 60 yet. Not auto-promoted after a crash. |
| 7 | SITC | Secondary 20 | Watch | 2.98 | +1.19 | +0.17 | 3.03 | 50.5 | No official GARP ≥ 60 yet. Not auto-promoted after a crash. |
| 8 | VFF | Secondary 20 | Watch | 2.88 | +0.00 | +0.00 | 2.57 | 75.3 | No official GARP ≥ 60 yet. Not auto-promoted after a crash. |
| 9 | ALTO | Secondary 20 | Watch | 3.98 | +0.50 | -0.25 | 4.22 | 46.4 | No official GARP ≥ 60 yet. Not auto-promoted after a crash. |
| 10 | ARKO | Secondary 20 | Watch | 4.63 | +1.65 | -0.75 | 4.95 | 55.9 | No official GARP ≥ 60 yet. Not auto-promoted after a crash. |
| 11 | CYH | Secondary 20 | Watch | 2.90 | -0.69 | -2.36 | 2.95 | 48.9 | No official GARP ≥ 60 yet. Not auto-promoted after a crash. |
| 12 | SPRO | Secondary 20 | Watch | 1.20 | -1.64 | -2.44 | 1.22 | 51.9 | No official GARP ≥ 60 yet. Not auto-promoted after a crash. |
| 13 | ABUS | Secondary 20 | Watch | 5.06 | -0.39 | -2.69 | 4.87 | 69.1 | No official GARP ≥ 60 yet. Not auto-promoted after a crash. |
| 14 | NAGE | Secondary 20 | Watch | 3.12 | -0.33 | -4.59 | 3.13 | 54.3 | No official GARP ≥ 60 yet. Not auto-promoted after a crash. |
| 15 | VRRM | Secondary 20 | Watch | 4.21 | -4.85 | -4.85 | 4.65 | 29.9 | No official GARP ≥ 60 yet. Not auto-promoted after a crash. |
| 16 | UWMC | Secondary 20 | Watch | 1.43 | -1.72 | -5.63 | 1.47 | 44.0 | No official GARP ≥ 60 yet. Not auto-promoted after a crash. |
| 17 | GORO | Secondary 20 | Watch | 3.59 | -2.71 | -7.24 | 3.01 | 68.5 | No official GARP ≥ 60 yet. Not auto-promoted after a crash. |
| 18 | SABR | Secondary 20 | Watch | 2.06 | -5.02 | -8.80 | 2.14 | 50.1 | No official GARP ≥ 60 yet. Not auto-promoted after a crash. |
| 19 | AISP | Secondary 20 | Watch | 2.03 | -4.66 | -9.74 | 2.06 | 47.8 | No official GARP ≥ 60 yet. Not auto-promoted after a crash. |
| 20 | AREC | Secondary 20 | Watch | 2.30 | -2.55 | -15.45 | 2.62 | 32.6 | No official GARP ≥ 60 yet. Not auto-promoted after a crash. |

Prices: Yahoo Finance daily bars, 2026-09-01 America/Toronto. SMA20 and RSI14 from the last 3 months of daily closes. Do not use Equibles for this routine price check.


## Rules

- Ranked Buy → Sell → Hold → Watch → Avoid. Max one Buy (paper) per morning.
- `Avoid` never becomes a buy because it bounced. `Sell` only if you already hold that avoid-quality name.
- `Watch` is not auto-promoted after a crash.
- This job never calls wsli and never sets TRADE_APPROVED.
