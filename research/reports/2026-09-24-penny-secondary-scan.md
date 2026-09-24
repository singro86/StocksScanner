# Secondary penny watchlist scan — 2026-09-24

> I am an AI research assistant, not a licensed financial advisor. This is educational information, not personalized financial advice. Consider a qualified advisor for your situation.

**Paper trading active — dry-run only. Buy lines are paper recommendations, never live Wealthsimple orders.**

## What to buy today (from 20 names)

NONE — no buy today.

Official Rebalance-MCP GARP scores are not computed in this job. Quality flags come from `portfolio/penny-secondary-watchlist.yaml`. A live ticket still needs GARP ≥ 60.

| Rank | Ticker | List | Rec | Close | 1d % | 5d % | SMA20 | RSI14 | Why |
|-----:|--------|------|-----|------:|-----:|-----:|------:|------:|-----|
| 1 | SPRO | Secondary 20 | Watch | 1.25 | -0.79 | +12.61 | 1.18 | 54.8 | No official GARP ≥ 60 yet. Not auto-promoted after a crash. |
| 2 | VFF | Secondary 20 | Watch | 3.12 | +2.64 | +10.07 | 2.90 | 66.9 | No official GARP ≥ 60 yet. Not auto-promoted after a crash. |
| 3 | SITC | Secondary 20 | Watch | 3.04 | +2.19 | +3.58 | 2.92 | 64.1 | No official GARP ≥ 60 yet. Not auto-promoted after a crash. |
| 4 | MDXG | Secondary 20 | Watch | 4.75 | -0.31 | +0.53 | 4.62 | 62.0 | No official GARP ≥ 60 yet. Not auto-promoted after a crash. |
| 5 | GORO | Secondary 20 | Watch | 3.50 | -4.25 | +0.43 | 3.67 | 37.1 | No official GARP ≥ 60 yet. Not auto-promoted after a crash. |
| 6 | NAGE | Secondary 20 | Watch | 3.00 | +0.17 | +0.17 | 3.09 | 29.1 | No official GARP ≥ 60 yet. Not auto-promoted after a crash. |
| 7 | GDRX | Secondary 20 | Watch | 3.33 | +0.45 | -1.62 | 3.45 | 43.4 | No official GARP ≥ 60 yet. Not auto-promoted after a crash. |
| 8 | CYH | Secondary 20 | Watch | 2.92 | -3.16 | -2.18 | 2.92 | 51.1 | No official GARP ≥ 60 yet. Not auto-promoted after a crash. |
| 9 | ARKO | Secondary 20 | Watch | 4.24 | +0.12 | -2.64 | 4.49 | 27.4 | No official GARP ≥ 60 yet. Not auto-promoted after a crash. |
| 10 | ABUS | Secondary 20 | Watch | 4.86 | +0.10 | -3.86 | 5.08 | 24.2 | No official GARP ≥ 60 yet. Not auto-promoted after a crash. |
| 11 | AISP | Secondary 20 | Watch | 1.88 | -3.35 | -4.09 | 2.01 | 29.4 | No official GARP ≥ 60 yet. Not auto-promoted after a crash. |
| 12 | SABR | Secondary 20 | Watch | 2.21 | +0.69 | -4.96 | 2.18 | 55.7 | No official GARP ≥ 60 yet. Not auto-promoted after a crash. |
| 13 | AMPY | Secondary 20 | Watch | 4.33 | +2.32 | -5.09 | 4.74 | 23.5 | No official GARP ≥ 60 yet. Not auto-promoted after a crash. |
| 14 | AREC | Secondary 20 | Watch | 1.85 | -1.86 | -5.13 | 2.22 | 11.7 | No official GARP ≥ 60 yet. Not auto-promoted after a crash. |
| 15 | UWMC | Secondary 20 | Watch | 1.20 | -2.05 | -5.16 | 1.35 | 15.6 | No official GARP ≥ 60 yet. Not auto-promoted after a crash. |
| 16 | VRRM | Secondary 20 | Watch | 3.31 | -2.13 | -6.55 | 3.85 | 14.9 | No official GARP ≥ 60 yet. Not auto-promoted after a crash. |
| 17 | ALTO | Secondary 20 | Watch | 3.75 | +0.40 | -6.84 | 3.99 | 30.5 | No official GARP ≥ 60 yet. Not auto-promoted after a crash. |
| 18 | HLLY | Secondary 20 | Watch | 2.42 | -2.22 | -7.79 | 2.77 | 26.7 | No official GARP ≥ 60 yet. Not auto-promoted after a crash. |
| 19 | TBLA | Secondary 20 | Watch | 3.42 | +0.73 | -10.11 | 3.73 | 29.9 | No official GARP ≥ 60 yet. Not auto-promoted after a crash. |
| 20 | TYGO | Secondary 20 | Watch | 0.89 | +0.53 | -13.14 | 1.03 | 20.3 | No official GARP ≥ 60 yet. Not auto-promoted after a crash. |

Prices: Yahoo Finance daily bars, 2026-09-24 America/Toronto. SMA20 and RSI14 from the last 3 months of daily closes. Do not use Equibles for this routine price check.


## Rules

- Ranked Buy → Sell → Hold → Watch → Avoid. Max one Buy (paper) per morning.
- `Avoid` never becomes a buy because it bounced. `Sell` only if you already hold that avoid-quality name.
- `Watch` is not auto-promoted after a crash.
- This job never calls wsli and never sets TRADE_APPROVED.
