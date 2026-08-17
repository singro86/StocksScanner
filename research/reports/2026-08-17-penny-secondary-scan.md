# Secondary penny watchlist scan — 2026-08-17

> I am an AI research assistant, not a licensed financial advisor. This is educational information, not personalized financial advice. Consider a qualified advisor for your situation.

**Paper trading active — dry-run only. Buy lines are paper recommendations, never live Wealthsimple orders.**

## What to buy today (from 20 names)

NONE — no buy today.

Official Rebalance-MCP GARP scores are not computed in this job. Quality flags come from `portfolio/penny-secondary-watchlist.yaml`. A live ticket still needs GARP ≥ 60.

| Rank | Ticker | List | Rec | Close | 1d % | 5d % | SMA20 | RSI14 | Why |
|-----:|--------|------|-----|------:|-----:|-----:|------:|------:|-----|
| 1 | AMPY | Secondary 20 | Watch | 4.84 | +1.25 | +16.34 | 4.13 | 79.1 | No official GARP ≥ 60 yet. Not auto-promoted after a crash. |
| 2 | GORO | Secondary 20 | Watch | 2.83 | +3.09 | +14.78 | 2.36 | 76.7 | No official GARP ≥ 60 yet. Not auto-promoted after a crash. |
| 3 | VFF | Secondary 20 | Watch | 2.62 | +3.75 | +10.76 | 2.14 | 77.5 | No official GARP ≥ 60 yet. Not auto-promoted after a crash. |
| 4 | SABR | Secondary 20 | Watch | 2.21 | -0.67 | +7.00 | 1.96 | 66.0 | No official GARP ≥ 60 yet. Not auto-promoted after a crash. |
| 5 | UWMC | Secondary 20 | Watch | 1.50 | -5.66 | +6.38 | 1.70 | 39.8 | No official GARP ≥ 60 yet. Not auto-promoted after a crash. |
| 6 | ABUS | Secondary 20 | Watch | 4.78 | +2.25 | +4.03 | 4.50 | 65.7 | No official GARP ≥ 60 yet. Not auto-promoted after a crash. |
| 7 | ARKO | Secondary 20 | Watch | 4.75 | -1.96 | +1.17 | 6.74 | 15.7 | No official GARP ≥ 60 yet. Not auto-promoted after a crash. |
| 8 | GDRX | Secondary 20 | Watch | 3.69 | -0.94 | +0.96 | 3.34 | 67.7 | No official GARP ≥ 60 yet. Not auto-promoted after a crash. |
| 9 | AREC | Secondary 20 | Watch | 2.87 | -0.52 | +0.53 | 2.21 | 88.8 | No official GARP ≥ 60 yet. Not auto-promoted after a crash. |
| 10 | CYH | Secondary 20 | Watch | 2.95 | -1.67 | +0.34 | 2.91 | 60.5 | No official GARP ≥ 60 yet. Not auto-promoted after a crash. |
| 11 | AISP | Secondary 20 | Watch | 2.02 | +3.06 | -0.49 | 1.95 | 54.4 | No official GARP ≥ 60 yet. Not auto-promoted after a crash. |
| 12 | MDXG | Secondary 20 | Watch | 4.20 | -1.64 | -1.64 | 4.24 | 42.9 | No official GARP ≥ 60 yet. Not auto-promoted after a crash. |
| 13 | NAGE | Secondary 20 | Watch | 2.99 | -0.99 | -1.97 | 3.21 | 38.5 | No official GARP ≥ 60 yet. Not auto-promoted after a crash. |
| 14 | ALTO | Secondary 20 | Watch | 4.14 | -0.96 | -2.13 | 4.57 | 43.7 | No official GARP ≥ 60 yet. Not auto-promoted after a crash. |
| 15 | SITC | Secondary 20 | Watch | 2.93 | -1.01 | -2.98 | 3.66 | 10.7 | No official GARP ≥ 60 yet. Not auto-promoted after a crash. |
| 16 | VRRM | Secondary 20 | Watch | 4.75 | +0.64 | -3.06 | 4.73 | 60.6 | No official GARP ≥ 60 yet. Not auto-promoted after a crash. |
| 17 | HLLY | Secondary 20 | Watch | 3.06 | -1.45 | -3.31 | 2.84 | 67.2 | No official GARP ≥ 60 yet. Not auto-promoted after a crash. |
| 18 | SPRO | Secondary 20 | Watch | 1.22 | -1.22 | -3.57 | 1.23 | 54.9 | No official GARP ≥ 60 yet. Not auto-promoted after a crash. |
| 19 | TYGO | Secondary 20 | Watch | 1.18 | -3.69 | -3.69 | 1.55 | 34.8 | No official GARP ≥ 60 yet. Not auto-promoted after a crash. |
| 20 | TBLA | Secondary 20 | Watch | 3.84 | -5.18 | -6.34 | 4.63 | 31.7 | No official GARP ≥ 60 yet. Not auto-promoted after a crash. |

Prices: Yahoo Finance daily bars, 2026-08-17 America/Toronto. SMA20 and RSI14 from the last 3 months of daily closes. Do not use Equibles for this routine price check.


## Rules

- Ranked Buy → Sell → Hold → Watch → Avoid. Max one Buy (paper) per morning.
- `Avoid` never becomes a buy because it bounced. `Sell` only if you already hold that avoid-quality name.
- `Watch` is not auto-promoted after a crash.
- This job never calls wsli and never sets TRADE_APPROVED.
