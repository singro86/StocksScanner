# Secondary penny watchlist scan — 2026-09-04

> I am an AI research assistant, not a licensed financial advisor. This is educational information, not personalized financial advice. Consider a qualified advisor for your situation.

**Paper trading active — dry-run only. Buy lines are paper recommendations, never live Wealthsimple orders.**

## What to buy today (from 20 names)

NONE — no buy today.

Official Rebalance-MCP GARP scores are not computed in this job. Quality flags come from `portfolio/penny-secondary-watchlist.yaml`. A live ticket still needs GARP ≥ 60.

| Rank | Ticker | List | Rec | Close | 1d % | 5d % | SMA20 | RSI14 | Why |
|-----:|--------|------|-----|------:|-----:|-----:|------:|------:|-----|
| 1 | GORO | Secondary 20 | Watch | 4.11 | +1.36 | +12.47 | 3.27 | 75.8 | No official GARP ≥ 60 yet. Not auto-promoted after a crash. |
| 2 | ARKO | Secondary 20 | Watch | 4.85 | +0.41 | +10.98 | 4.65 | 49.6 | No official GARP ≥ 60 yet. Not auto-promoted after a crash. |
| 3 | HLLY | Secondary 20 | Watch | 3.11 | +0.32 | +6.51 | 3.02 | 53.2 | No official GARP ≥ 60 yet. Not auto-promoted after a crash. |
| 4 | TBLA | Secondary 20 | Watch | 3.88 | +0.26 | +2.65 | 3.84 | 49.3 | No official GARP ≥ 60 yet. Not auto-promoted after a crash. |
| 5 | AMPY | Secondary 20 | Watch | 4.87 | -0.61 | +2.31 | 4.75 | 52.4 | No official GARP ≥ 60 yet. Not auto-promoted after a crash. |
| 6 | AREC | Secondary 20 | Watch | 2.46 | +0.61 | +2.29 | 2.63 | 32.6 | No official GARP ≥ 60 yet. Not auto-promoted after a crash. |
| 7 | ABUS | Secondary 20 | Watch | 5.15 | +0.59 | +1.58 | 4.95 | 69.3 | No official GARP ≥ 60 yet. Not auto-promoted after a crash. |
| 8 | MDXG | Secondary 20 | Watch | 4.53 | +2.14 | +0.56 | 4.38 | 65.9 | No official GARP ≥ 60 yet. Not auto-promoted after a crash. |
| 9 | ALTO | Secondary 20 | Watch | 4.08 | +1.36 | +0.37 | 4.13 | 44.3 | No official GARP ≥ 60 yet. Not auto-promoted after a crash. |
| 10 | VFF | Secondary 20 | Watch | 2.92 | +0.86 | +0.34 | 2.70 | 74.3 | No official GARP ≥ 60 yet. Not auto-promoted after a crash. |
| 11 | SPRO | Secondary 20 | Watch | 1.20 | -1.64 | +0.00 | 1.22 | 52.5 | No official GARP ≥ 60 yet. Not auto-promoted after a crash. |
| 12 | GDRX | Secondary 20 | Watch | 3.50 | -0.85 | -0.85 | 3.57 | 37.5 | No official GARP ≥ 60 yet. Not auto-promoted after a crash. |
| 13 | TYGO | Secondary 20 | Watch | 1.08 | +1.89 | -0.92 | 1.12 | 34.5 | No official GARP ≥ 60 yet. Not auto-promoted after a crash. |
| 14 | CYH | Secondary 20 | Watch | 2.90 | -0.34 | -1.02 | 2.94 | 42.9 | No official GARP ≥ 60 yet. Not auto-promoted after a crash. |
| 15 | UWMC | Secondary 20 | Watch | 1.45 | -0.69 | -2.69 | 1.47 | 46.7 | No official GARP ≥ 60 yet. Not auto-promoted after a crash. |
| 16 | SABR | Secondary 20 | Watch | 2.13 | +3.64 | -2.96 | 2.13 | 48.8 | No official GARP ≥ 60 yet. Not auto-promoted after a crash. |
| 17 | AISP | Secondary 20 | Watch | 2.02 | -3.72 | -3.26 | 2.08 | 50.1 | No official GARP ≥ 60 yet. Not auto-promoted after a crash. |
| 18 | SITC | Secondary 20 | Watch | 2.85 | -0.70 | -4.68 | 2.98 | 38.5 | No official GARP ≥ 60 yet. Not auto-promoted after a crash. |
| 19 | NAGE | Secondary 20 | Watch | 3.13 | +0.67 | -4.84 | 3.14 | 56.0 | No official GARP ≥ 60 yet. Not auto-promoted after a crash. |
| 20 | VRRM | Secondary 20 | Watch | 4.10 | -2.29 | -6.51 | 4.49 | 26.5 | No official GARP ≥ 60 yet. Not auto-promoted after a crash. |

Prices: Yahoo Finance daily bars, 2026-09-04 America/Toronto. SMA20 and RSI14 from the last 3 months of daily closes. Do not use Equibles for this routine price check.


## Rules

- Ranked Buy → Sell → Hold → Watch → Avoid. Max one Buy (paper) per morning.
- `Avoid` never becomes a buy because it bounced. `Sell` only if you already hold that avoid-quality name.
- `Watch` is not auto-promoted after a crash.
- This job never calls wsli and never sets TRADE_APPROVED.
