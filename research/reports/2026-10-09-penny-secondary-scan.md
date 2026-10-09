# Secondary penny watchlist scan — 2026-10-09

> I am an AI research assistant, not a licensed financial advisor. This is educational information, not personalized financial advice. Consider a qualified advisor for your situation.

**Paper trading active — dry-run only. Buy lines are paper recommendations, never live Wealthsimple orders.**

## What to buy today (from 20 names)

NONE — no buy today.

Official Rebalance-MCP GARP scores are not computed in this job. Quality flags come from `portfolio/penny-secondary-watchlist.yaml`. A live ticket still needs GARP ≥ 60.

| Rank | Ticker | List | Rec | Close | 1d % | 5d % | SMA20 | RSI14 | Why |
|-----:|--------|------|-----|------:|-----:|-----:|------:|------:|-----|
| 1 | AISP | Secondary 20 | Watch | 2.42 | +5.68 | +14.15 | 2.00 | 69.3 | No official GARP ≥ 60 yet. Not auto-promoted after a crash. |
| 2 | TBLA | Secondary 20 | Watch | 3.48 | -1.00 | +7.58 | 3.49 | 42.5 | No official GARP ≥ 60 yet. Not auto-promoted after a crash. |
| 3 | GORO | Secondary 20 | Watch | 3.42 | +7.05 | +4.75 | 3.41 | 45.1 | No official GARP ≥ 60 yet. Not auto-promoted after a crash. |
| 4 | TYGO | Secondary 20 | Watch | 0.90 | +1.14 | +4.29 | 0.92 | 36.7 | No official GARP ≥ 60 yet. Not auto-promoted after a crash. |
| 5 | GDRX | Secondary 20 | Watch | 3.40 | +1.34 | +3.81 | 3.36 | 51.0 | No official GARP ≥ 60 yet. Not auto-promoted after a crash. |
| 6 | VRRM | Secondary 20 | Watch | 2.90 | -0.51 | +3.38 | 3.19 | 23.4 | No official GARP ≥ 60 yet. Not auto-promoted after a crash. |
| 7 | AMPY | Secondary 20 | Watch | 4.49 | -2.07 | +2.87 | 4.42 | 58.9 | No official GARP ≥ 60 yet. Not auto-promoted after a crash. |
| 8 | MDXG | Secondary 20 | Watch | 4.67 | +1.19 | +1.85 | 4.69 | 39.9 | No official GARP ≥ 60 yet. Not auto-promoted after a crash. |
| 9 | HLLY | Secondary 20 | Watch | 2.38 | -2.46 | +1.71 | 2.47 | 43.6 | No official GARP ≥ 60 yet. Not auto-promoted after a crash. |
| 10 | CYH | Secondary 20 | Watch | 2.76 | +1.10 | +1.47 | 2.86 | 40.9 | No official GARP ≥ 60 yet. Not auto-promoted after a crash. |
| 11 | SPRO | Secondary 20 | Watch | 1.21 | +5.70 | +1.26 | 1.19 | 54.6 | No official GARP ≥ 60 yet. Not auto-promoted after a crash. |
| 12 | ALTO | Secondary 20 | Watch | 3.76 | +0.84 | -0.23 | 3.81 | 39.8 | No official GARP ≥ 60 yet. Not auto-promoted after a crash. |
| 13 | ARKO | Secondary 20 | Watch | 4.13 | +0.24 | -0.96 | 4.24 | 42.5 | No official GARP ≥ 60 yet. Not auto-promoted after a crash. |
| 14 | SABR | Secondary 20 | Watch | 1.90 | -1.55 | -3.55 | 2.11 | 16.9 | No official GARP ≥ 60 yet. Not auto-promoted after a crash. |
| 15 | NAGE | Secondary 20 | Watch | 2.69 | +1.13 | -3.58 | 2.90 | 30.8 | No official GARP ≥ 60 yet. Not auto-promoted after a crash. |
| 16 | ABUS | Secondary 20 | Watch | 4.26 | +1.91 | -4.27 | 4.76 | 27.2 | No official GARP ≥ 60 yet. Not auto-promoted after a crash. |
| 17 | VFF | Secondary 20 | Watch | 2.67 | -1.11 | -5.99 | 2.89 | 39.1 | No official GARP ≥ 60 yet. Not auto-promoted after a crash. |
| 18 | SITC | Secondary 20 | Watch | 3.12 | -1.42 | -8.63 | 3.10 | 54.9 | No official GARP ≥ 60 yet. Not auto-promoted after a crash. |
| 19 | AREC | Secondary 20 | Watch | 1.60 | -2.78 | -10.38 | 1.85 | 18.1 | No official GARP ≥ 60 yet. Not auto-promoted after a crash. |
| 20 | UWMC | Secondary 20 | Watch | 1.07 | -1.79 | -15.04 | 1.22 | 29.8 | No official GARP ≥ 60 yet. Not auto-promoted after a crash. |

Prices: Yahoo Finance daily bars, 2026-10-09 America/Toronto. SMA20 and RSI14 from the last 3 months of daily closes. Do not use Equibles for this routine price check.


## Rules

- Ranked Buy → Sell → Hold → Watch → Avoid. Max one Buy (paper) per morning.
- `Avoid` never becomes a buy because it bounced. `Sell` only if you already hold that avoid-quality name.
- `Watch` is not auto-promoted after a crash.
- This job never calls wsli and never sets TRADE_APPROVED.
