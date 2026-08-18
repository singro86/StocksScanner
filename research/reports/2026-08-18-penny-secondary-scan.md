# Secondary penny watchlist scan — 2026-08-18

> I am an AI research assistant, not a licensed financial advisor. This is educational information, not personalized financial advice. Consider a qualified advisor for your situation.

**Paper trading active — dry-run only. Buy lines are paper recommendations, never live Wealthsimple orders.**

## What to buy today (from 20 names)

NONE — no buy today.

Official Rebalance-MCP GARP scores are not computed in this job. Quality flags come from `portfolio/penny-secondary-watchlist.yaml`. A live ticket still needs GARP ≥ 60.

| Rank | Ticker | List | Rec | Close | 1d % | 5d % | SMA20 | RSI14 | Why |
|-----:|--------|------|-----|------:|-----:|-----:|------:|------:|-----|
| 1 | UWMC | Secondary 20 | Watch | 1.59 | -2.45 | +24.22 | 1.72 | 42.6 | No official GARP ≥ 60 yet. Not auto-promoted after a crash. |
| 2 | VFF | Secondary 20 | Watch | 2.53 | +2.43 | +21.64 | 2.10 | 75.8 | No official GARP ≥ 60 yet. Not auto-promoted after a crash. |
| 3 | AMPY | Secondary 20 | Watch | 4.78 | -1.03 | +18.61 | 4.08 | 75.4 | No official GARP ≥ 60 yet. Not auto-promoted after a crash. |
| 4 | GORO | Secondary 20 | Watch | 2.75 | -1.79 | +8.70 | 2.38 | 68.8 | No official GARP ≥ 60 yet. Not auto-promoted after a crash. |
| 5 | SABR | Secondary 20 | Watch | 2.23 | +0.91 | +7.73 | 1.94 | 73.5 | No official GARP ≥ 60 yet. Not auto-promoted after a crash. |
| 6 | AREC | Secondary 20 | Watch | 2.88 | +2.13 | +5.11 | 2.14 | 87.3 | No official GARP ≥ 60 yet. Not auto-promoted after a crash. |
| 7 | GDRX | Secondary 20 | Watch | 3.73 | +0.27 | +1.36 | 3.32 | 74.5 | No official GARP ≥ 60 yet. Not auto-promoted after a crash. |
| 8 | ABUS | Secondary 20 | Watch | 4.67 | +1.97 | +0.86 | 4.52 | 63.8 | No official GARP ≥ 60 yet. Not auto-promoted after a crash. |
| 9 | CYH | Secondary 20 | Watch | 3.00 | +1.01 | +0.00 | 2.95 | 67.1 | No official GARP ≥ 60 yet. Not auto-promoted after a crash. |
| 10 | TYGO | Secondary 20 | Watch | 1.22 | -3.17 | +0.00 | 1.55 | 36.3 | No official GARP ≥ 60 yet. Not auto-promoted after a crash. |
| 11 | TBLA | Secondary 20 | Watch | 4.05 | +2.79 | -1.22 | 4.67 | 36.1 | No official GARP ≥ 60 yet. Not auto-promoted after a crash. |
| 12 | MDXG | Secondary 20 | Watch | 4.27 | +1.67 | -1.61 | 4.27 | 53.8 | No official GARP ≥ 60 yet. Not auto-promoted after a crash. |
| 13 | SITC | Secondary 20 | Watch | 2.97 | +0.34 | -1.66 | 3.66 | 11.3 | No official GARP ≥ 60 yet. Not auto-promoted after a crash. |
| 14 | HLLY | Secondary 20 | Watch | 3.11 | +4.01 | -1.89 | 2.84 | 68.8 | No official GARP ≥ 60 yet. Not auto-promoted after a crash. |
| 15 | SPRO | Secondary 20 | Watch | 1.23 | -0.81 | -2.38 | 1.23 | 57.4 | No official GARP ≥ 60 yet. Not auto-promoted after a crash. |
| 16 | NAGE | Secondary 20 | Watch | 3.02 | -0.98 | -3.21 | 3.22 | 43.0 | No official GARP ≥ 60 yet. Not auto-promoted after a crash. |
| 17 | VRRM | Secondary 20 | Watch | 4.72 | -1.87 | -3.67 | 4.73 | 59.9 | No official GARP ≥ 60 yet. Not auto-promoted after a crash. |
| 18 | ALTO | Secondary 20 | Watch | 4.18 | -0.48 | -4.78 | 4.70 | 41.1 | No official GARP ≥ 60 yet. Not auto-promoted after a crash. |
| 19 | AISP | Secondary 20 | Watch | 1.96 | +1.03 | -5.31 | 1.95 | 49.5 | No official GARP ≥ 60 yet. Not auto-promoted after a crash. |
| 20 | ARKO | Secondary 20 | Watch | 4.85 | +7.78 | -14.31 | 6.87 | 17.8 | No official GARP ≥ 60 yet. Not auto-promoted after a crash. |

Prices: Yahoo Finance daily bars, 2026-08-18 America/Toronto. SMA20 and RSI14 from the last 3 months of daily closes. Do not use Equibles for this routine price check.


## Rules

- Ranked Buy → Sell → Hold → Watch → Avoid. Max one Buy (paper) per morning.
- `Avoid` never becomes a buy because it bounced. `Sell` only if you already hold that avoid-quality name.
- `Watch` is not auto-promoted after a crash.
- This job never calls wsli and never sets TRADE_APPROVED.
