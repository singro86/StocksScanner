# Secondary penny watchlist scan — 2026-09-17

> I am an AI research assistant, not a licensed financial advisor. This is educational information, not personalized financial advice. Consider a qualified advisor for your situation.

**Paper trading active — dry-run only. Buy lines are paper recommendations, never live Wealthsimple orders.**

## What to buy today (from 20 names)

NONE — no buy today.

Official Rebalance-MCP GARP scores are not computed in this job. Quality flags come from `portfolio/penny-secondary-watchlist.yaml`. A live ticket still needs GARP ≥ 60.

| Rank | Ticker | List | Rec | Close | 1d % | 5d % | SMA20 | RSI14 | Why |
|-----:|--------|------|-----|------:|-----:|-----:|------:|------:|-----|
| 1 | SABR | Secondary 20 | Watch | 2.38 | +2.80 | +11.97 | 2.17 | 61.0 | No official GARP ≥ 60 yet. Not auto-promoted after a crash. |
| 2 | MDXG | Secondary 20 | Watch | 4.75 | +0.53 | +3.37 | 4.53 | 66.0 | No official GARP ≥ 60 yet. Not auto-promoted after a crash. |
| 3 | SITC | Secondary 20 | Watch | 2.92 | +0.52 | +3.36 | 2.93 | 44.3 | No official GARP ≥ 60 yet. Not auto-promoted after a crash. |
| 4 | ALTO | Secondary 20 | Watch | 4.08 | +1.37 | +2.90 | 4.06 | 49.2 | No official GARP ≥ 60 yet. Not auto-promoted after a crash. |
| 5 | GDRX | Secondary 20 | Watch | 3.43 | +1.18 | +2.39 | 3.47 | 45.5 | No official GARP ≥ 60 yet. Not auto-promoted after a crash. |
| 6 | HLLY | Secondary 20 | Watch | 2.67 | +1.55 | +1.94 | 2.87 | 35.9 | No official GARP ≥ 60 yet. Not auto-promoted after a crash. |
| 7 | CYH | Secondary 20 | Watch | 2.92 | -1.85 | +1.21 | 2.94 | 49.4 | No official GARP ≥ 60 yet. Not auto-promoted after a crash. |
| 8 | TBLA | Secondary 20 | Watch | 3.77 | -0.92 | +1.21 | 3.77 | 50.4 | No official GARP ≥ 60 yet. Not auto-promoted after a crash. |
| 9 | VFF | Secondary 20 | Watch | 2.89 | +2.12 | +1.05 | 2.85 | 52.5 | No official GARP ≥ 60 yet. Not auto-promoted after a crash. |
| 10 | GORO | Secondary 20 | Watch | 3.58 | +2.87 | +0.28 | 3.64 | 43.8 | No official GARP ≥ 60 yet. Not auto-promoted after a crash. |
| 11 | SPRO | Secondary 20 | Watch | 1.12 | +0.90 | +0.00 | 1.18 | 30.4 | No official GARP ≥ 60 yet. Not auto-promoted after a crash. |
| 12 | TYGO | Secondary 20 | Watch | 1.03 | +0.00 | +0.00 | 1.06 | 21.4 | No official GARP ≥ 60 yet. Not auto-promoted after a crash. |
| 13 | NAGE | Secondary 20 | Watch | 3.02 | +0.50 | -0.82 | 3.13 | 33.3 | No official GARP ≥ 60 yet. Not auto-promoted after a crash. |
| 14 | ABUS | Secondary 20 | Watch | 5.07 | +0.30 | -1.07 | 5.11 | 36.0 | No official GARP ≥ 60 yet. Not auto-promoted after a crash. |
| 15 | ARKO | Secondary 20 | Watch | 4.36 | +0.23 | -2.46 | 4.58 | 46.8 | No official GARP ≥ 60 yet. Not auto-promoted after a crash. |
| 16 | AISP | Secondary 20 | Watch | 1.96 | +2.62 | -2.74 | 2.06 | 33.3 | No official GARP ≥ 60 yet. Not auto-promoted after a crash. |
| 17 | VRRM | Secondary 20 | Watch | 3.54 | +0.14 | -2.88 | 4.08 | 13.2 | No official GARP ≥ 60 yet. Not auto-promoted after a crash. |
| 18 | AREC | Secondary 20 | Watch | 2.03 | +4.10 | -7.31 | 2.36 | 24.8 | No official GARP ≥ 60 yet. Not auto-promoted after a crash. |
| 19 | UWMC | Secondary 20 | Watch | 1.24 | +0.41 | -7.84 | 1.40 | 25.2 | No official GARP ≥ 60 yet. Not auto-promoted after a crash. |
| 20 | AMPY | Secondary 20 | Watch | 4.55 | -0.11 | -8.16 | 4.83 | 43.2 | No official GARP ≥ 60 yet. Not auto-promoted after a crash. |

Prices: Yahoo Finance daily bars, 2026-09-17 America/Toronto. SMA20 and RSI14 from the last 3 months of daily closes. Do not use Equibles for this routine price check.


## Rules

- Ranked Buy → Sell → Hold → Watch → Avoid. Max one Buy (paper) per morning.
- `Avoid` never becomes a buy because it bounced. `Sell` only if you already hold that avoid-quality name.
- `Watch` is not auto-promoted after a crash.
- This job never calls wsli and never sets TRADE_APPROVED.
