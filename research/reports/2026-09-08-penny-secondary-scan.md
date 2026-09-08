# Secondary penny watchlist scan — 2026-09-08

> I am an AI research assistant, not a licensed financial advisor. This is educational information, not personalized financial advice. Consider a qualified advisor for your situation.

**Paper trading active — dry-run only. Buy lines are paper recommendations, never live Wealthsimple orders.**

## What to buy today (from 20 names)

NONE — no buy today.

Official Rebalance-MCP GARP scores are not computed in this job. Quality flags come from `portfolio/penny-secondary-watchlist.yaml`. A live ticket still needs GARP ≥ 60.

| Rank | Ticker | List | Rec | Close | 1d % | 5d % | SMA20 | RSI14 | Why |
|-----:|--------|------|-----|------:|-----:|-----:|------:|------:|-----|
| 1 | HLLY | Secondary 20 | Watch | 3.05 | +0.00 | +6.64 | 3.02 | 47.9 | No official GARP ≥ 60 yet. Not auto-promoted after a crash. |
| 2 | AREC | Secondary 20 | Watch | 2.48 | +2.06 | +5.08 | 2.61 | 41.7 | No official GARP ≥ 60 yet. Not auto-promoted after a crash. |
| 3 | VFF | Secondary 20 | Watch | 3.02 | +3.42 | +4.86 | 2.73 | 81.6 | No official GARP ≥ 60 yet. Not auto-promoted after a crash. |
| 4 | ARKO | Secondary 20 | Watch | 4.72 | -3.37 | +3.62 | 4.65 | 50.2 | No official GARP ≥ 60 yet. Not auto-promoted after a crash. |
| 5 | ALTO | Secondary 20 | Watch | 4.08 | +1.11 | +3.16 | 4.12 | 43.4 | No official GARP ≥ 60 yet. Not auto-promoted after a crash. |
| 6 | TBLA | Secondary 20 | Watch | 3.83 | -0.78 | +2.68 | 3.82 | 50.0 | No official GARP ≥ 60 yet. Not auto-promoted after a crash. |
| 7 | TYGO | Secondary 20 | Watch | 1.09 | +2.34 | +2.34 | 1.12 | 40.4 | No official GARP ≥ 60 yet. Not auto-promoted after a crash. |
| 8 | ABUS | Secondary 20 | Watch | 5.19 | +0.76 | +2.15 | 4.98 | 66.6 | No official GARP ≥ 60 yet. Not auto-promoted after a crash. |
| 9 | UWMC | Secondary 20 | Watch | 1.47 | -0.34 | +1.03 | 1.48 | 52.2 | No official GARP ≥ 60 yet. Not auto-promoted after a crash. |
| 10 | MDXG | Secondary 20 | Watch | 4.57 | -0.08 | +0.58 | 4.39 | 61.9 | No official GARP ≥ 60 yet. Not auto-promoted after a crash. |
| 11 | AMPY | Secondary 20 | Watch | 4.95 | +0.92 | +0.51 | 4.79 | 56.0 | No official GARP ≥ 60 yet. Not auto-promoted after a crash. |
| 12 | NAGE | Secondary 20 | Watch | 3.15 | -0.79 | +0.48 | 3.15 | 55.4 | No official GARP ≥ 60 yet. Not auto-promoted after a crash. |
| 13 | GDRX | Secondary 20 | Watch | 3.50 | +0.72 | +0.43 | 3.56 | 41.5 | No official GARP ≥ 60 yet. Not auto-promoted after a crash. |
| 14 | GORO | Secondary 20 | Watch | 3.70 | -10.85 | +0.27 | 3.33 | 66.7 | No official GARP ≥ 60 yet. Not auto-promoted after a crash. |
| 15 | SABR | Secondary 20 | Watch | 2.17 | +2.11 | +0.23 | 2.14 | 54.0 | No official GARP ≥ 60 yet. Not auto-promoted after a crash. |
| 16 | SPRO | Secondary 20 | Watch | 1.21 | -0.41 | -1.23 | 1.21 | 51.4 | No official GARP ≥ 60 yet. Not auto-promoted after a crash. |
| 17 | AISP | Secondary 20 | Watch | 2.08 | +1.66 | -2.15 | 2.08 | 52.6 | No official GARP ≥ 60 yet. Not auto-promoted after a crash. |
| 18 | SITC | Secondary 20 | Watch | 2.87 | +0.00 | -2.71 | 2.97 | 31.8 | No official GARP ≥ 60 yet. Not auto-promoted after a crash. |
| 19 | CYH | Secondary 20 | Watch | 2.83 | -2.25 | -3.25 | 2.93 | 30.4 | No official GARP ≥ 60 yet. Not auto-promoted after a crash. |
| 20 | VRRM | Secondary 20 | Watch | 3.92 | -3.67 | -11.50 | 4.45 | 25.7 | No official GARP ≥ 60 yet. Not auto-promoted after a crash. |

Prices: Yahoo Finance daily bars, 2026-09-08 America/Toronto. SMA20 and RSI14 from the last 3 months of daily closes. Do not use Equibles for this routine price check.


## Rules

- Ranked Buy → Sell → Hold → Watch → Avoid. Max one Buy (paper) per morning.
- `Avoid` never becomes a buy because it bounced. `Sell` only if you already hold that avoid-quality name.
- `Watch` is not auto-promoted after a crash.
- This job never calls wsli and never sets TRADE_APPROVED.
