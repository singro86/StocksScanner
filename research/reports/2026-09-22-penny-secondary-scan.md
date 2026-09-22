# Secondary penny watchlist scan — 2026-09-22

> I am an AI research assistant, not a licensed financial advisor. This is educational information, not personalized financial advice. Consider a qualified advisor for your situation.

**Paper trading active — dry-run only. Buy lines are paper recommendations, never live Wealthsimple orders.**

## What to buy today (from 20 names)

NONE — no buy today.

Official Rebalance-MCP GARP scores are not computed in this job. Quality flags come from `portfolio/penny-secondary-watchlist.yaml`. A live ticket still needs GARP ≥ 60.

| Rank | Ticker | List | Rec | Close | 1d % | 5d % | SMA20 | RSI14 | Why |
|-----:|--------|------|-----|------:|-----:|-----:|------:|------:|-----|
| 1 | SPRO | Secondary 20 | Watch | 1.34 | +17.64 | +18.68 | 1.18 | 67.6 | No official GARP ≥ 60 yet. Not auto-promoted after a crash. |
| 2 | SABR | Secondary 20 | Watch | 2.27 | -2.36 | +8.85 | 2.19 | 63.5 | No official GARP ≥ 60 yet. Not auto-promoted after a crash. |
| 3 | VFF | Secondary 20 | Watch | 3.04 | +5.38 | +6.87 | 2.89 | 65.3 | No official GARP ≥ 60 yet. Not auto-promoted after a crash. |
| 4 | SITC | Secondary 20 | Watch | 3.02 | +0.17 | +5.77 | 2.92 | 62.9 | No official GARP ≥ 60 yet. Not auto-promoted after a crash. |
| 5 | AISP | Secondary 20 | Watch | 1.99 | +1.79 | +5.58 | 2.03 | 44.2 | No official GARP ≥ 60 yet. Not auto-promoted after a crash. |
| 6 | MDXG | Secondary 20 | Watch | 4.88 | +1.35 | +3.28 | 4.61 | 69.8 | No official GARP ≥ 60 yet. Not auto-promoted after a crash. |
| 7 | NAGE | Secondary 20 | Watch | 3.06 | +0.82 | +2.17 | 3.11 | 42.2 | No official GARP ≥ 60 yet. Not auto-promoted after a crash. |
| 8 | HLLY | Secondary 20 | Watch | 2.65 | +5.80 | +0.57 | 2.80 | 40.7 | No official GARP ≥ 60 yet. Not auto-promoted after a crash. |
| 9 | CYH | Secondary 20 | Watch | 2.98 | +3.11 | +0.34 | 2.92 | 54.2 | No official GARP ≥ 60 yet. Not auto-promoted after a crash. |
| 10 | ABUS | Secondary 20 | Watch | 5.01 | +0.20 | -0.99 | 5.10 | 38.2 | No official GARP ≥ 60 yet. Not auto-promoted after a crash. |
| 11 | GORO | Secondary 20 | Watch | 3.48 | -1.42 | -1.14 | 3.68 | 46.7 | No official GARP ≥ 60 yet. Not auto-promoted after a crash. |
| 12 | UWMC | Secondary 20 | Watch | 1.26 | +0.00 | -1.56 | 1.37 | 36.6 | No official GARP ≥ 60 yet. Not auto-promoted after a crash. |
| 13 | VRRM | Secondary 20 | Watch | 3.47 | -1.42 | -1.98 | 3.91 | 19.3 | No official GARP ≥ 60 yet. Not auto-promoted after a crash. |
| 14 | GDRX | Secondary 20 | Watch | 3.40 | +0.15 | -2.72 | 3.46 | 45.9 | No official GARP ≥ 60 yet. Not auto-promoted after a crash. |
| 15 | AREC | Secondary 20 | Watch | 2.00 | +1.27 | -2.91 | 2.27 | 30.6 | No official GARP ≥ 60 yet. Not auto-promoted after a crash. |
| 16 | ARKO | Secondary 20 | Watch | 4.28 | +0.94 | -3.17 | 4.51 | 42.0 | No official GARP ≥ 60 yet. Not auto-promoted after a crash. |
| 17 | TYGO | Secondary 20 | Watch | 1.00 | -1.39 | -3.30 | 1.04 | 33.5 | No official GARP ≥ 60 yet. Not auto-promoted after a crash. |
| 18 | ALTO | Secondary 20 | Watch | 3.85 | -1.53 | -5.87 | 4.01 | 40.5 | No official GARP ≥ 60 yet. Not auto-promoted after a crash. |
| 19 | TBLA | Secondary 20 | Watch | 3.56 | -1.80 | -7.66 | 3.75 | 40.2 | No official GARP ≥ 60 yet. Not auto-promoted after a crash. |
| 20 | AMPY | Secondary 20 | Watch | 4.29 | -0.58 | -13.08 | 4.76 | 18.7 | No official GARP ≥ 60 yet. Not auto-promoted after a crash. |

Prices: Yahoo Finance daily bars, 2026-09-22 America/Toronto. SMA20 and RSI14 from the last 3 months of daily closes. Do not use Equibles for this routine price check.


## Rules

- Ranked Buy → Sell → Hold → Watch → Avoid. Max one Buy (paper) per morning.
- `Avoid` never becomes a buy because it bounced. `Sell` only if you already hold that avoid-quality name.
- `Watch` is not auto-promoted after a crash.
- This job never calls wsli and never sets TRADE_APPROVED.
