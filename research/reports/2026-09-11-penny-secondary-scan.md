# Secondary penny watchlist scan — 2026-09-11

> I am an AI research assistant, not a licensed financial advisor. This is educational information, not personalized financial advice. Consider a qualified advisor for your situation.

**Paper trading active — dry-run only. Buy lines are paper recommendations, never live Wealthsimple orders.**

## What to buy today (from 20 names)

NONE — no buy today.

Official Rebalance-MCP GARP scores are not computed in this job. Quality flags come from `portfolio/penny-secondary-watchlist.yaml`. A live ticket still needs GARP ≥ 60.

| Rank | Ticker | List | Rec | Close | 1d % | 5d % | SMA20 | RSI14 | Why |
|-----:|--------|------|-----|------:|-----:|-----:|------:|------:|-----|
| 1 | SABR | Secondary 20 | Watch | 2.17 | +2.11 | +5.58 | 2.15 | 53.7 | No official GARP ≥ 60 yet. Not auto-promoted after a crash. |
| 2 | MDXG | Secondary 20 | Watch | 4.54 | -1.41 | +2.37 | 4.45 | 61.2 | No official GARP ≥ 60 yet. Not auto-promoted after a crash. |
| 3 | AMPY | Secondary 20 | Watch | 4.95 | -0.20 | +1.02 | 4.85 | 57.5 | No official GARP ≥ 60 yet. Not auto-promoted after a crash. |
| 4 | CYH | Secondary 20 | Watch | 2.92 | +1.21 | +0.52 | 2.94 | 40.2 | No official GARP ≥ 60 yet. Not auto-promoted after a crash. |
| 5 | ABUS | Secondary 20 | Watch | 5.12 | +0.10 | +0.10 | 5.06 | 36.5 | No official GARP ≥ 60 yet. Not auto-promoted after a crash. |
| 6 | VFF | Secondary 20 | Watch | 2.88 | +0.70 | -0.52 | 2.80 | 61.4 | No official GARP ≥ 60 yet. Not auto-promoted after a crash. |
| 7 | TBLA | Secondary 20 | Watch | 3.81 | +2.28 | -1.42 | 3.79 | 56.4 | No official GARP ≥ 60 yet. Not auto-promoted after a crash. |
| 8 | SITC | Secondary 20 | Watch | 2.83 | -0.18 | -1.57 | 2.95 | 24.7 | No official GARP ≥ 60 yet. Not auto-promoted after a crash. |
| 9 | NAGE | Secondary 20 | Watch | 3.06 | +0.49 | -1.77 | 3.14 | 39.3 | No official GARP ≥ 60 yet. Not auto-promoted after a crash. |
| 10 | ALTO | Secondary 20 | Watch | 3.96 | -0.13 | -1.86 | 4.10 | 30.4 | No official GARP ≥ 60 yet. Not auto-promoted after a crash. |
| 11 | TYGO | Secondary 20 | Watch | 1.03 | +0.48 | -2.36 | 1.08 | 38.8 | No official GARP ≥ 60 yet. Not auto-promoted after a crash. |
| 12 | GDRX | Secondary 20 | Watch | 3.40 | +1.34 | -3.82 | 3.51 | 46.8 | No official GARP ≥ 60 yet. Not auto-promoted after a crash. |
| 13 | ARKO | Secondary 20 | Watch | 4.57 | +2.12 | -5.49 | 4.65 | 44.2 | No official GARP ≥ 60 yet. Not auto-promoted after a crash. |
| 14 | AISP | Secondary 20 | Watch | 1.98 | -1.74 | -5.95 | 2.08 | 38.7 | No official GARP ≥ 60 yet. Not auto-promoted after a crash. |
| 15 | SPRO | Secondary 20 | Watch | 1.14 | +1.79 | -6.56 | 1.20 | 32.6 | No official GARP ≥ 60 yet. Not auto-promoted after a crash. |
| 16 | UWMC | Secondary 20 | Watch | 1.34 | +0.37 | -7.88 | 1.44 | 45.0 | No official GARP ≥ 60 yet. Not auto-promoted after a crash. |
| 17 | AREC | Secondary 20 | Watch | 2.17 | -1.14 | -11.27 | 2.52 | 29.1 | No official GARP ≥ 60 yet. Not auto-promoted after a crash. |
| 18 | GORO | Secondary 20 | Watch | 3.58 | +0.42 | -11.48 | 3.48 | 57.4 | No official GARP ≥ 60 yet. Not auto-promoted after a crash. |
| 19 | HLLY | Secondary 20 | Watch | 2.69 | +2.86 | -13.06 | 2.96 | 34.1 | No official GARP ≥ 60 yet. Not auto-promoted after a crash. |
| 20 | VRRM | Secondary 20 | Watch | 3.54 | -2.88 | -15.60 | 4.28 | 6.1 | No official GARP ≥ 60 yet. Not auto-promoted after a crash. |

Prices: Yahoo Finance daily bars, 2026-09-11 America/Toronto. SMA20 and RSI14 from the last 3 months of daily closes. Do not use Equibles for this routine price check.


## Rules

- Ranked Buy → Sell → Hold → Watch → Avoid. Max one Buy (paper) per morning.
- `Avoid` never becomes a buy because it bounced. `Sell` only if you already hold that avoid-quality name.
- `Watch` is not auto-promoted after a crash.
- This job never calls wsli and never sets TRADE_APPROVED.
