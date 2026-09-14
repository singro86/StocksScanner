# Secondary penny watchlist scan — 2026-09-14

> I am an AI research assistant, not a licensed financial advisor. This is educational information, not personalized financial advice. Consider a qualified advisor for your situation.

**Paper trading active — dry-run only. Buy lines are paper recommendations, never live Wealthsimple orders.**

## What to buy today (from 20 names)

NONE — no buy today.

Official Rebalance-MCP GARP scores are not computed in this job. Quality flags come from `portfolio/penny-secondary-watchlist.yaml`. A live ticket still needs GARP ≥ 60.

| Rank | Ticker | List | Rec | Close | 1d % | 5d % | SMA20 | RSI14 | Why |
|-----:|--------|------|-----|------:|-----:|-----:|------:|------:|-----|
| 1 | SABR | Secondary 20 | Watch | 2.17 | +0.23 | +2.11 | 2.15 | 45.0 | No official GARP ≥ 60 yet. Not auto-promoted after a crash. |
| 2 | CYH | Secondary 20 | Watch | 2.93 | +0.34 | +1.38 | 2.93 | 40.9 | No official GARP ≥ 60 yet. Not auto-promoted after a crash. |
| 3 | GDRX | Secondary 20 | Watch | 3.52 | +3.83 | +1.15 | 3.50 | 54.1 | No official GARP ≥ 60 yet. Not auto-promoted after a crash. |
| 4 | VFF | Secondary 20 | Watch | 2.94 | +2.26 | +0.86 | 2.82 | 65.6 | No official GARP ≥ 60 yet. Not auto-promoted after a crash. |
| 5 | MDXG | Secondary 20 | Watch | 4.59 | +0.55 | +0.55 | 4.47 | 69.2 | No official GARP ≥ 60 yet. Not auto-promoted after a crash. |
| 6 | TBLA | Secondary 20 | Watch | 3.88 | +1.97 | +0.39 | 3.78 | 67.4 | No official GARP ≥ 60 yet. Not auto-promoted after a crash. |
| 7 | SITC | Secondary 20 | Watch | 2.88 | +2.13 | +0.35 | 2.95 | 32.7 | No official GARP ≥ 60 yet. Not auto-promoted after a crash. |
| 8 | TYGO | Secondary 20 | Watch | 1.07 | +4.90 | +0.00 | 1.08 | 53.9 | No official GARP ≥ 60 yet. Not auto-promoted after a crash. |
| 9 | AMPY | Secondary 20 | Watch | 4.89 | -0.71 | -0.10 | 4.85 | 56.5 | No official GARP ≥ 60 yet. Not auto-promoted after a crash. |
| 10 | ABUS | Secondary 20 | Watch | 5.12 | +0.10 | -0.48 | 5.08 | 37.7 | No official GARP ≥ 60 yet. Not auto-promoted after a crash. |
| 11 | ALTO | Secondary 20 | Watch | 3.96 | +1.67 | -1.86 | 4.09 | 38.9 | No official GARP ≥ 60 yet. Not auto-promoted after a crash. |
| 12 | NAGE | Secondary 20 | Watch | 3.06 | +0.49 | -3.63 | 3.15 | 39.3 | No official GARP ≥ 60 yet. Not auto-promoted after a crash. |
| 13 | SPRO | Secondary 20 | Watch | 1.16 | +2.21 | -4.54 | 1.20 | 37.5 | No official GARP ≥ 60 yet. Not auto-promoted after a crash. |
| 14 | AISP | Secondary 20 | Watch | 1.96 | +0.77 | -4.63 | 2.08 | 38.2 | No official GARP ≥ 60 yet. Not auto-promoted after a crash. |
| 15 | ARKO | Secondary 20 | Watch | 4.61 | +1.99 | -5.73 | 4.64 | 46.6 | No official GARP ≥ 60 yet. Not auto-promoted after a crash. |
| 16 | UWMC | Secondary 20 | Watch | 1.35 | +0.00 | -8.16 | 1.43 | 43.4 | No official GARP ≥ 60 yet. Not auto-promoted after a crash. |
| 17 | HLLY | Secondary 20 | Watch | 2.70 | +0.37 | -11.47 | 2.94 | 37.1 | No official GARP ≥ 60 yet. Not auto-promoted after a crash. |
| 18 | VRRM | Secondary 20 | Watch | 3.58 | +0.99 | -11.92 | 4.23 | 9.6 | No official GARP ≥ 60 yet. Not auto-promoted after a crash. |
| 19 | GORO | Secondary 20 | Watch | 3.60 | +0.14 | -13.13 | 3.52 | 51.6 | No official GARP ≥ 60 yet. Not auto-promoted after a crash. |
| 20 | AREC | Secondary 20 | Watch | 2.09 | -2.44 | -14.09 | 2.48 | 31.5 | No official GARP ≥ 60 yet. Not auto-promoted after a crash. |

Prices: Yahoo Finance daily bars, 2026-09-14 America/Toronto. SMA20 and RSI14 from the last 3 months of daily closes. Do not use Equibles for this routine price check.


## Rules

- Ranked Buy → Sell → Hold → Watch → Avoid. Max one Buy (paper) per morning.
- `Avoid` never becomes a buy because it bounced. `Sell` only if you already hold that avoid-quality name.
- `Watch` is not auto-promoted after a crash.
- This job never calls wsli and never sets TRADE_APPROVED.
