# Secondary penny watchlist scan — 2026-10-08

> I am an AI research assistant, not a licensed financial advisor. This is educational information, not personalized financial advice. Consider a qualified advisor for your situation.

**Paper trading active — dry-run only. Buy lines are paper recommendations, never live Wealthsimple orders.**

## What to buy today (from 20 names)

NONE — no buy today.

Official Rebalance-MCP GARP scores are not computed in this job. Quality flags come from `portfolio/penny-secondary-watchlist.yaml`. A live ticket still needs GARP ≥ 60.

| Rank | Ticker | List | Rec | Close | 1d % | 5d % | SMA20 | RSI14 | Why |
|-----:|--------|------|-----|------:|-----:|-----:|------:|------:|-----|
| 1 | AISP | Secondary 20 | Watch | 2.37 | +10.75 | +6.76 | 1.98 | 68.8 | No official GARP ≥ 60 yet. Not auto-promoted after a crash. |
| 2 | AMPY | Secondary 20 | Watch | 4.62 | +3.70 | +5.59 | 4.45 | 55.6 | No official GARP ≥ 60 yet. Not auto-promoted after a crash. |
| 3 | TBLA | Secondary 20 | Watch | 3.48 | +5.62 | +4.67 | 3.51 | 43.2 | No official GARP ≥ 60 yet. Not auto-promoted after a crash. |
| 4 | GDRX | Secondary 20 | Watch | 3.37 | +3.54 | +2.90 | 3.35 | 49.0 | No official GARP ≥ 60 yet. Not auto-promoted after a crash. |
| 5 | HLLY | Secondary 20 | Watch | 2.42 | +2.54 | +1.68 | 2.49 | 43.3 | No official GARP ≥ 60 yet. Not auto-promoted after a crash. |
| 6 | TYGO | Secondary 20 | Watch | 0.91 | -0.36 | +1.54 | 0.93 | 41.6 | No official GARP ≥ 60 yet. Not auto-promoted after a crash. |
| 7 | ARKO | Secondary 20 | Watch | 4.16 | -1.77 | +1.09 | 4.27 | 45.4 | No official GARP ≥ 60 yet. Not auto-promoted after a crash. |
| 8 | ALTO | Secondary 20 | Watch | 3.68 | +0.82 | +0.00 | 3.81 | 28.4 | No official GARP ≥ 60 yet. Not auto-promoted after a crash. |
| 9 | CYH | Secondary 20 | Watch | 2.73 | +0.55 | -0.55 | 2.87 | 40.4 | No official GARP ≥ 60 yet. Not auto-promoted after a crash. |
| 10 | MDXG | Secondary 20 | Watch | 4.59 | -0.33 | -0.97 | 4.68 | 36.6 | No official GARP ≥ 60 yet. Not auto-promoted after a crash. |
| 11 | GORO | Secondary 20 | Watch | 3.12 | -4.73 | -2.04 | 3.41 | 28.6 | No official GARP ≥ 60 yet. Not auto-promoted after a crash. |
| 12 | VRRM | Secondary 20 | Watch | 2.91 | -0.26 | -2.60 | 3.22 | 26.1 | No official GARP ≥ 60 yet. Not auto-promoted after a crash. |
| 13 | NAGE | Secondary 20 | Watch | 2.61 | -4.04 | -2.61 | 2.91 | 30.6 | No official GARP ≥ 60 yet. Not auto-promoted after a crash. |
| 14 | SABR | Secondary 20 | Watch | 1.90 | -0.47 | -4.47 | 2.13 | 23.6 | No official GARP ≥ 60 yet. Not auto-promoted after a crash. |
| 15 | VFF | Secondary 20 | Watch | 2.67 | -0.56 | -6.32 | 2.90 | 41.2 | No official GARP ≥ 60 yet. Not auto-promoted after a crash. |
| 16 | ABUS | Secondary 20 | Watch | 4.19 | -2.33 | -8.11 | 4.80 | 23.4 | No official GARP ≥ 60 yet. Not auto-promoted after a crash. |
| 17 | SITC | Secondary 20 | Watch | 3.19 | +0.79 | -9.00 | 3.09 | 60.5 | No official GARP ≥ 60 yet. Not auto-promoted after a crash. |
| 18 | AREC | Secondary 20 | Watch | 1.64 | +0.31 | -9.17 | 1.88 | 17.1 | No official GARP ≥ 60 yet. Not auto-promoted after a crash. |
| 19 | UWMC | Secondary 20 | Watch | 1.09 | -3.54 | -9.17 | 1.24 | 32.6 | No official GARP ≥ 60 yet. Not auto-promoted after a crash. |
| 20 | SPRO | Secondary 20 | Watch | 1.14 | -2.56 | -9.52 | 1.19 | 50.8 | No official GARP ≥ 60 yet. Not auto-promoted after a crash. |

Prices: Yahoo Finance daily bars, 2026-10-08 America/Toronto. SMA20 and RSI14 from the last 3 months of daily closes. Do not use Equibles for this routine price check.


## Rules

- Ranked Buy → Sell → Hold → Watch → Avoid. Max one Buy (paper) per morning.
- `Avoid` never becomes a buy because it bounced. `Sell` only if you already hold that avoid-quality name.
- `Watch` is not auto-promoted after a crash.
- This job never calls wsli and never sets TRADE_APPROVED.
