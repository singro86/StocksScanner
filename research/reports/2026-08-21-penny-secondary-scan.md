# Secondary penny watchlist scan — 2026-08-21

> I am an AI research assistant, not a licensed financial advisor. This is educational information, not personalized financial advice. Consider a qualified advisor for your situation.

**Paper trading active — dry-run only. Buy lines are paper recommendations, never live Wealthsimple orders.**

## What to buy today (from 20 names)

NONE — no buy today.

Official Rebalance-MCP GARP scores are not computed in this job. Quality flags come from `portfolio/penny-secondary-watchlist.yaml`. A live ticket still needs GARP ≥ 60.

| Rank | Ticker | List | Rec | Close | 1d % | 5d % | SMA20 | RSI14 | Why |
|-----:|--------|------|-----|------:|-----:|-----:|------:|------:|-----|
| 1 | GORO | Secondary 20 | Watch | 3.00 | +6.01 | +7.14 | 2.41 | 81.1 | No official GARP ≥ 60 yet. Not auto-promoted after a crash. |
| 2 | AISP | Secondary 20 | Watch | 2.03 | -1.46 | +4.64 | 1.95 | 67.3 | No official GARP ≥ 60 yet. Not auto-promoted after a crash. |
| 3 | ABUS | Secondary 20 | Watch | 4.77 | -4.22 | +4.15 | 4.56 | 66.9 | No official GARP ≥ 60 yet. Not auto-promoted after a crash. |
| 4 | VFF | Secondary 20 | Watch | 2.57 | -1.53 | +4.05 | 2.22 | 83.5 | No official GARP ≥ 60 yet. Not auto-promoted after a crash. |
| 5 | NAGE | Secondary 20 | Watch | 3.15 | -0.63 | +3.28 | 3.17 | 39.5 | No official GARP ≥ 60 yet. Not auto-promoted after a crash. |
| 6 | MDXG | Secondary 20 | Watch | 4.30 | -3.37 | +2.38 | 4.26 | 56.9 | No official GARP ≥ 60 yet. Not auto-promoted after a crash. |
| 7 | ARKO | Secondary 20 | Watch | 4.59 | -2.34 | +2.00 | 6.25 | 10.5 | No official GARP ≥ 60 yet. Not auto-promoted after a crash. |
| 8 | HLLY | Secondary 20 | Watch | 3.04 | -3.19 | +1.67 | 2.94 | 65.3 | No official GARP ≥ 60 yet. Not auto-promoted after a crash. |
| 9 | AMPY | Secondary 20 | Watch | 4.91 | +2.50 | +1.66 | 4.24 | 78.4 | No official GARP ≥ 60 yet. Not auto-promoted after a crash. |
| 10 | CYH | Secondary 20 | Watch | 2.98 | +2.06 | +0.34 | 2.89 | 62.7 | No official GARP ≥ 60 yet. Not auto-promoted after a crash. |
| 11 | SITC | Secondary 20 | Watch | 3.02 | -0.33 | +0.00 | 3.47 | 14.6 | No official GARP ≥ 60 yet. Not auto-promoted after a crash. |
| 12 | ALTO | Secondary 20 | Watch | 4.18 | -0.24 | -0.48 | 4.46 | 35.8 | No official GARP ≥ 60 yet. Not auto-promoted after a crash. |
| 13 | SPRO | Secondary 20 | Watch | 1.21 | -1.63 | -2.42 | 1.21 | 55.3 | No official GARP ≥ 60 yet. Not auto-promoted after a crash. |
| 14 | VRRM | Secondary 20 | Watch | 4.66 | +0.21 | -3.12 | 4.84 | 34.6 | No official GARP ≥ 60 yet. Not auto-promoted after a crash. |
| 15 | GDRX | Secondary 20 | Watch | 3.56 | +0.56 | -4.30 | 3.44 | 65.8 | No official GARP ≥ 60 yet. Not auto-promoted after a crash. |
| 16 | SABR | Secondary 20 | Watch | 2.08 | -1.42 | -5.88 | 2.02 | 61.2 | No official GARP ≥ 60 yet. Not auto-promoted after a crash. |
| 17 | TBLA | Secondary 20 | Watch | 3.68 | -4.66 | -6.60 | 4.39 | 26.9 | No official GARP ≥ 60 yet. Not auto-promoted after a crash. |
| 18 | AREC | Secondary 20 | Watch | 2.57 | -2.65 | -8.87 | 2.34 | 72.4 | No official GARP ≥ 60 yet. Not auto-promoted after a crash. |
| 19 | UWMC | Secondary 20 | Watch | 1.42 | -4.70 | -12.88 | 1.64 | 38.0 | No official GARP ≥ 60 yet. Not auto-promoted after a crash. |
| 20 | TYGO | Secondary 20 | Watch | 1.09 | -4.39 | -13.49 | 1.43 | 18.5 | No official GARP ≥ 60 yet. Not auto-promoted after a crash. |

Prices: Yahoo Finance daily bars, 2026-08-21 America/Toronto. SMA20 and RSI14 from the last 3 months of daily closes. Do not use Equibles for this routine price check.


## Rules

- Ranked Buy → Sell → Hold → Watch → Avoid. Max one Buy (paper) per morning.
- `Avoid` never becomes a buy because it bounced. `Sell` only if you already hold that avoid-quality name.
- `Watch` is not auto-promoted after a crash.
- This job never calls wsli and never sets TRADE_APPROVED.
