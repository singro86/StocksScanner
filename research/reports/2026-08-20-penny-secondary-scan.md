# Secondary penny watchlist scan — 2026-08-20

> I am an AI research assistant, not a licensed financial advisor. This is educational information, not personalized financial advice. Consider a qualified advisor for your situation.

**Paper trading active — dry-run only. Buy lines are paper recommendations, never live Wealthsimple orders.**

## What to buy today (from 20 names)

NONE — no buy today.

Official Rebalance-MCP GARP scores are not computed in this job. Quality flags come from `portfolio/penny-secondary-watchlist.yaml`. A live ticket still needs GARP ≥ 60.

| Rank | Ticker | List | Rec | Close | 1d % | 5d % | SMA20 | RSI14 | Why |
|-----:|--------|------|-----|------:|-----:|-----:|------:|------:|-----|
| 1 | AMPY | Secondary 20 | Watch | 4.79 | -0.62 | +9.11 | 4.20 | 75.9 | No official GARP ≥ 60 yet. Not auto-promoted after a crash. |
| 2 | ABUS | Secondary 20 | Watch | 4.98 | +2.89 | +8.50 | 4.55 | 78.5 | No official GARP ≥ 60 yet. Not auto-promoted after a crash. |
| 3 | ARKO | Secondary 20 | Watch | 4.70 | -0.42 | +5.38 | 6.40 | 16.7 | No official GARP ≥ 60 yet. Not auto-promoted after a crash. |
| 4 | VFF | Secondary 20 | Watch | 2.61 | +2.76 | +3.98 | 2.20 | 82.7 | No official GARP ≥ 60 yet. Not auto-promoted after a crash. |
| 5 | MDXG | Secondary 20 | Watch | 4.45 | +2.54 | +3.97 | 4.27 | 61.2 | No official GARP ≥ 60 yet. Not auto-promoted after a crash. |
| 6 | NAGE | Secondary 20 | Watch | 3.17 | +3.60 | +3.60 | 3.17 | 48.1 | No official GARP ≥ 60 yet. Not auto-promoted after a crash. |
| 7 | SPRO | Secondary 20 | Watch | 1.23 | +2.50 | +3.36 | 1.21 | 53.9 | No official GARP ≥ 60 yet. Not auto-promoted after a crash. |
| 8 | ALTO | Secondary 20 | Watch | 4.19 | -1.18 | +3.20 | 4.51 | 46.5 | No official GARP ≥ 60 yet. Not auto-promoted after a crash. |
| 9 | SABR | Secondary 20 | Watch | 2.11 | +0.00 | +2.43 | 1.99 | 64.4 | No official GARP ≥ 60 yet. Not auto-promoted after a crash. |
| 10 | SITC | Secondary 20 | Watch | 3.03 | +0.00 | +1.68 | 3.53 | 14.3 | No official GARP ≥ 60 yet. Not auto-promoted after a crash. |
| 11 | GORO | Secondary 20 | Watch | 2.83 | +5.20 | +1.07 | 2.40 | 76.9 | No official GARP ≥ 60 yet. Not auto-promoted after a crash. |
| 12 | CYH | Secondary 20 | Watch | 2.92 | -2.01 | +0.34 | 2.90 | 63.6 | No official GARP ≥ 60 yet. Not auto-promoted after a crash. |
| 13 | AISP | Secondary 20 | Watch | 2.06 | +0.98 | -0.48 | 1.95 | 69.0 | No official GARP ≥ 60 yet. Not auto-promoted after a crash. |
| 14 | TBLA | Secondary 20 | Watch | 3.86 | +0.78 | -0.52 | 4.45 | 25.6 | No official GARP ≥ 60 yet. Not auto-promoted after a crash. |
| 15 | HLLY | Secondary 20 | Watch | 3.14 | +1.62 | -0.95 | 2.91 | 65.8 | No official GARP ≥ 60 yet. Not auto-promoted after a crash. |
| 16 | VRRM | Secondary 20 | Watch | 4.65 | +4.49 | -1.06 | 4.81 | 38.8 | No official GARP ≥ 60 yet. Not auto-promoted after a crash. |
| 17 | UWMC | Secondary 20 | Watch | 1.49 | +3.47 | -1.32 | 1.66 | 38.6 | No official GARP ≥ 60 yet. Not auto-promoted after a crash. |
| 18 | GDRX | Secondary 20 | Watch | 3.54 | -3.01 | -1.39 | 3.40 | 60.7 | No official GARP ≥ 60 yet. Not auto-promoted after a crash. |
| 19 | AREC | Secondary 20 | Watch | 2.64 | -1.49 | -5.71 | 2.30 | 73.7 | No official GARP ≥ 60 yet. Not auto-promoted after a crash. |
| 20 | TYGO | Secondary 20 | Watch | 1.14 | -0.87 | -6.56 | 1.46 | 37.6 | No official GARP ≥ 60 yet. Not auto-promoted after a crash. |

Prices: Yahoo Finance daily bars, 2026-08-20 America/Toronto. SMA20 and RSI14 from the last 3 months of daily closes. Do not use Equibles for this routine price check.


## Rules

- Ranked Buy → Sell → Hold → Watch → Avoid. Max one Buy (paper) per morning.
- `Avoid` never becomes a buy because it bounced. `Sell` only if you already hold that avoid-quality name.
- `Watch` is not auto-promoted after a crash.
- This job never calls wsli and never sets TRADE_APPROVED.
