# Secondary penny watchlist scan — 2026-09-30

> I am an AI research assistant, not a licensed financial advisor. This is educational information, not personalized financial advice. Consider a qualified advisor for your situation.

**Paper trading active — dry-run only. Buy lines are paper recommendations, never live Wealthsimple orders.**

## What to buy today (from 20 names)

NONE — no buy today.

Official Rebalance-MCP GARP scores are not computed in this job. Quality flags come from `portfolio/penny-secondary-watchlist.yaml`. A live ticket still needs GARP ≥ 60.

| Rank | Ticker | List | Rec | Close | 1d % | 5d % | SMA20 | RSI14 | Why |
|-----:|--------|------|-----|------:|-----:|-----:|------:|------:|-----|
| 1 | SITC | Secondary 20 | Watch | 3.25 | +4.66 | +9.60 | 2.96 | 79.3 | No official GARP ≥ 60 yet. Not auto-promoted after a crash. |
| 2 | TYGO | Secondary 20 | Watch | 0.92 | +8.85 | +2.85 | 0.98 | 35.5 | No official GARP ≥ 60 yet. Not auto-promoted after a crash. |
| 3 | TBLA | Secondary 20 | Watch | 3.45 | +1.17 | +1.47 | 3.66 | 35.1 | No official GARP ≥ 60 yet. Not auto-promoted after a crash. |
| 4 | ABUS | Secondary 20 | Watch | 4.88 | +4.16 | +0.72 | 5.02 | 35.0 | No official GARP ≥ 60 yet. Not auto-promoted after a crash. |
| 5 | UWMC | Secondary 20 | Watch | 1.23 | -1.21 | +0.41 | 1.30 | 29.1 | No official GARP ≥ 60 yet. Not auto-promoted after a crash. |
| 6 | GDRX | Secondary 20 | Watch | 3.33 | +2.94 | +0.15 | 3.40 | 48.5 | No official GARP ≥ 60 yet. Not auto-promoted after a crash. |
| 7 | ALTO | Secondary 20 | Watch | 3.71 | +2.34 | -0.40 | 3.91 | 35.0 | No official GARP ≥ 60 yet. Not auto-promoted after a crash. |
| 8 | AMPY | Secondary 20 | Watch | 4.21 | +1.32 | -0.59 | 4.59 | 21.5 | No official GARP ≥ 60 yet. Not auto-promoted after a crash. |
| 9 | NAGE | Secondary 20 | Watch | 2.95 | -0.05 | -1.72 | 3.04 | 38.3 | No official GARP ≥ 60 yet. Not auto-promoted after a crash. |
| 10 | SPRO | Secondary 20 | Watch | 1.24 | +2.92 | -1.98 | 1.19 | 61.2 | No official GARP ≥ 60 yet. Not auto-promoted after a crash. |
| 11 | HLLY | Secondary 20 | Watch | 2.43 | -0.82 | -2.02 | 2.67 | 39.6 | No official GARP ≥ 60 yet. Not auto-promoted after a crash. |
| 12 | SABR | Secondary 20 | Watch | 2.13 | +0.23 | -2.51 | 2.19 | 50.3 | No official GARP ≥ 60 yet. Not auto-promoted after a crash. |
| 13 | MDXG | Secondary 20 | Watch | 4.63 | -0.86 | -2.94 | 4.67 | 51.9 | No official GARP ≥ 60 yet. Not auto-promoted after a crash. |
| 14 | AREC | Secondary 20 | Watch | 1.82 | +0.83 | -3.18 | 2.08 | 23.4 | No official GARP ≥ 60 yet. Not auto-promoted after a crash. |
| 15 | AISP | Secondary 20 | Watch | 1.88 | +2.46 | -3.35 | 1.95 | 37.6 | No official GARP ≥ 60 yet. Not auto-promoted after a crash. |
| 16 | CYH | Secondary 20 | Watch | 2.90 | -0.17 | -3.49 | 2.92 | 51.2 | No official GARP ≥ 60 yet. Not auto-promoted after a crash. |
| 17 | ARKO | Secondary 20 | Watch | 4.08 | -0.85 | -3.66 | 4.41 | 29.3 | No official GARP ≥ 60 yet. Not auto-promoted after a crash. |
| 18 | VFF | Secondary 20 | Watch | 2.92 | -5.81 | -3.79 | 2.95 | 54.5 | No official GARP ≥ 60 yet. Not auto-promoted after a crash. |
| 19 | VRRM | Secondary 20 | Watch | 3.12 | +2.63 | -7.69 | 3.54 | 27.4 | No official GARP ≥ 60 yet. Not auto-promoted after a crash. |
| 20 | GORO | Secondary 20 | Watch | 3.23 | +1.09 | -11.37 | 3.60 | 31.9 | No official GARP ≥ 60 yet. Not auto-promoted after a crash. |

Prices: Yahoo Finance daily bars, 2026-09-30 America/Toronto. SMA20 and RSI14 from the last 3 months of daily closes. Do not use Equibles for this routine price check.


## Rules

- Ranked Buy → Sell → Hold → Watch → Avoid. Max one Buy (paper) per morning.
- `Avoid` never becomes a buy because it bounced. `Sell` only if you already hold that avoid-quality name.
- `Watch` is not auto-promoted after a crash.
- This job never calls wsli and never sets TRADE_APPROVED.
