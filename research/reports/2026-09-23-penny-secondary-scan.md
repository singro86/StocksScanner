# Secondary penny watchlist scan — 2026-09-23

> I am an AI research assistant, not a licensed financial advisor. This is educational information, not personalized financial advice. Consider a qualified advisor for your situation.

**Paper trading active — dry-run only. Buy lines are paper recommendations, never live Wealthsimple orders.**

## What to buy today (from 20 names)

NONE — no buy today.

Official Rebalance-MCP GARP scores are not computed in this job. Quality flags come from `portfolio/penny-secondary-watchlist.yaml`. A live ticket still needs GARP ≥ 60.

| Rank | Ticker | List | Rec | Close | 1d % | 5d % | SMA20 | RSI14 | Why |
|-----:|--------|------|-----|------:|-----:|-----:|------:|------:|-----|
| 1 | SPRO | Secondary 20 | Watch | 1.26 | +10.53 | +11.50 | 1.18 | 59.4 | No official GARP ≥ 60 yet. Not auto-promoted after a crash. |
| 2 | VFF | Secondary 20 | Watch | 3.02 | +5.04 | +6.51 | 2.89 | 64.8 | No official GARP ≥ 60 yet. Not auto-promoted after a crash. |
| 3 | SABR | Secondary 20 | Watch | 2.19 | -6.22 | +4.54 | 2.18 | 58.1 | No official GARP ≥ 60 yet. Not auto-promoted after a crash. |
| 4 | AISP | Secondary 20 | Watch | 1.97 | +0.77 | +4.52 | 2.03 | 42.2 | No official GARP ≥ 60 yet. Not auto-promoted after a crash. |
| 5 | SITC | Secondary 20 | Watch | 3.00 | -1.80 | +3.27 | 2.92 | 56.9 | No official GARP ≥ 60 yet. Not auto-promoted after a crash. |
| 6 | NAGE | Secondary 20 | Watch | 3.05 | +0.38 | +1.72 | 3.11 | 40.2 | No official GARP ≥ 60 yet. Not auto-promoted after a crash. |
| 7 | CYH | Secondary 20 | Watch | 3.02 | +4.50 | +1.68 | 2.92 | 57.1 | No official GARP ≥ 60 yet. Not auto-promoted after a crash. |
| 8 | MDXG | Secondary 20 | Watch | 4.78 | -0.62 | +1.27 | 4.60 | 65.1 | No official GARP ≥ 60 yet. Not auto-promoted after a crash. |
| 9 | GORO | Secondary 20 | Watch | 3.48 | -1.56 | -1.28 | 3.68 | 46.6 | No official GARP ≥ 60 yet. Not auto-promoted after a crash. |
| 10 | ARKO | Secondary 20 | Watch | 4.30 | +1.53 | -2.60 | 4.51 | 43.1 | No official GARP ≥ 60 yet. Not auto-promoted after a crash. |
| 11 | ABUS | Secondary 20 | Watch | 4.92 | -1.70 | -2.87 | 5.10 | 28.9 | No official GARP ≥ 60 yet. Not auto-promoted after a crash. |
| 12 | VRRM | Secondary 20 | Watch | 3.42 | -2.70 | -3.25 | 3.91 | 18.6 | No official GARP ≥ 60 yet. Not auto-promoted after a crash. |
| 13 | GDRX | Secondary 20 | Watch | 3.34 | -1.48 | -4.30 | 3.46 | 42.9 | No official GARP ≥ 60 yet. Not auto-promoted after a crash. |
| 14 | UWMC | Secondary 20 | Watch | 1.22 | -3.13 | -4.65 | 1.37 | 33.4 | No official GARP ≥ 60 yet. Not auto-promoted after a crash. |
| 15 | HLLY | Secondary 20 | Watch | 2.50 | +0.00 | -4.94 | 2.79 | 32.7 | No official GARP ≥ 60 yet. Not auto-promoted after a crash. |
| 16 | AREC | Secondary 20 | Watch | 1.93 | -2.28 | -6.32 | 2.27 | 26.8 | No official GARP ≥ 60 yet. Not auto-promoted after a crash. |
| 17 | ALTO | Secondary 20 | Watch | 3.73 | -4.48 | -8.68 | 4.01 | 35.8 | No official GARP ≥ 60 yet. Not auto-promoted after a crash. |
| 18 | TYGO | Secondary 20 | Watch | 0.94 | -6.92 | -8.73 | 1.04 | 26.0 | No official GARP ≥ 60 yet. Not auto-promoted after a crash. |
| 19 | TBLA | Secondary 20 | Watch | 3.38 | -6.49 | -12.08 | 3.75 | 33.8 | No official GARP ≥ 60 yet. Not auto-promoted after a crash. |
| 20 | AMPY | Secondary 20 | Watch | 4.23 | -1.74 | -14.10 | 4.75 | 17.9 | No official GARP ≥ 60 yet. Not auto-promoted after a crash. |

Prices: Yahoo Finance daily bars, 2026-09-23 America/Toronto. SMA20 and RSI14 from the last 3 months of daily closes. Do not use Equibles for this routine price check.


## Rules

- Ranked Buy → Sell → Hold → Watch → Avoid. Max one Buy (paper) per morning.
- `Avoid` never becomes a buy because it bounced. `Sell` only if you already hold that avoid-quality name.
- `Watch` is not auto-promoted after a crash.
- This job never calls wsli and never sets TRADE_APPROVED.
