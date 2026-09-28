# Secondary penny watchlist scan — 2026-09-28

> I am an AI research assistant, not a licensed financial advisor. This is educational information, not personalized financial advice. Consider a qualified advisor for your situation.

**Paper trading active — dry-run only. Buy lines are paper recommendations, never live Wealthsimple orders.**

## What to buy today (from 20 names)

NONE — no buy today.

Official Rebalance-MCP GARP scores are not computed in this job. Quality flags come from `portfolio/penny-secondary-watchlist.yaml`. A live ticket still needs GARP ≥ 60.

| Rank | Ticker | List | Rec | Close | 1d % | 5d % | SMA20 | RSI14 | Why |
|-----:|--------|------|-----|------:|-----:|-----:|------:|------:|-----|
| 1 | VFF | Secondary 20 | Watch | 3.13 | -1.26 | +8.68 | 2.93 | 58.1 | No official GARP ≥ 60 yet. Not auto-promoted after a crash. |
| 2 | SPRO | Secondary 20 | Watch | 1.20 | -2.85 | +4.83 | 1.19 | 50.5 | No official GARP ≥ 60 yet. Not auto-promoted after a crash. |
| 3 | SITC | Secondary 20 | Watch | 3.05 | -0.33 | +0.99 | 2.93 | 63.9 | No official GARP ≥ 60 yet. Not auto-promoted after a crash. |
| 4 | CYH | Secondary 20 | Watch | 2.92 | -0.85 | +0.86 | 2.92 | 55.0 | No official GARP ≥ 60 yet. Not auto-promoted after a crash. |
| 5 | ARKO | Secondary 20 | Watch | 4.26 | -0.47 | +0.47 | 4.46 | 29.1 | No official GARP ≥ 60 yet. Not auto-promoted after a crash. |
| 6 | UWMC | Secondary 20 | Watch | 1.24 | +1.23 | -1.98 | 1.32 | 22.8 | No official GARP ≥ 60 yet. Not auto-promoted after a crash. |
| 7 | NAGE | Secondary 20 | Watch | 2.98 | -2.36 | -2.04 | 3.06 | 35.5 | No official GARP ≥ 60 yet. Not auto-promoted after a crash. |
| 8 | AMPY | Secondary 20 | Watch | 4.22 | -1.50 | -2.18 | 4.67 | 21.4 | No official GARP ≥ 60 yet. Not auto-promoted after a crash. |
| 9 | ABUS | Secondary 20 | Watch | 4.86 | +0.21 | -2.80 | 5.04 | 16.7 | No official GARP ≥ 60 yet. Not auto-promoted after a crash. |
| 10 | GDRX | Secondary 20 | Watch | 3.29 | -1.94 | -3.10 | 3.42 | 36.9 | No official GARP ≥ 60 yet. Not auto-promoted after a crash. |
| 11 | HLLY | Secondary 20 | Watch | 2.42 | -2.02 | -3.20 | 2.71 | 27.1 | No official GARP ≥ 60 yet. Not auto-promoted after a crash. |
| 12 | MDXG | Secondary 20 | Watch | 4.64 | -0.64 | -3.53 | 4.66 | 48.2 | No official GARP ≥ 60 yet. Not auto-promoted after a crash. |
| 13 | GORO | Secondary 20 | Watch | 3.35 | -4.14 | -4.96 | 3.64 | 25.9 | No official GARP ≥ 60 yet. Not auto-promoted after a crash. |
| 14 | TBLA | Secondary 20 | Watch | 3.40 | -2.30 | -6.08 | 3.69 | 29.4 | No official GARP ≥ 60 yet. Not auto-promoted after a crash. |
| 15 | AISP | Secondary 20 | Watch | 1.82 | -0.06 | -6.72 | 1.97 | 24.9 | No official GARP ≥ 60 yet. Not auto-promoted after a crash. |
| 16 | ALTO | Secondary 20 | Watch | 3.65 | -2.28 | -6.78 | 3.94 | 23.1 | No official GARP ≥ 60 yet. Not auto-promoted after a crash. |
| 17 | AREC | Secondary 20 | Watch | 1.83 | -3.68 | -7.34 | 2.13 | 15.9 | No official GARP ≥ 60 yet. Not auto-promoted after a crash. |
| 18 | SABR | Secondary 20 | Watch | 2.11 | -3.21 | -9.44 | 2.18 | 42.2 | No official GARP ≥ 60 yet. Not auto-promoted after a crash. |
| 19 | VRRM | Secondary 20 | Watch | 3.01 | -7.10 | -14.49 | 3.67 | 14.8 | No official GARP ≥ 60 yet. Not auto-promoted after a crash. |
| 20 | TYGO | Secondary 20 | Watch | 0.82 | -4.65 | -18.81 | 1.00 | 13.6 | No official GARP ≥ 60 yet. Not auto-promoted after a crash. |

Prices: Yahoo Finance daily bars, 2026-09-28 America/Toronto. SMA20 and RSI14 from the last 3 months of daily closes. Do not use Equibles for this routine price check.


## Rules

- Ranked Buy → Sell → Hold → Watch → Avoid. Max one Buy (paper) per morning.
- `Avoid` never becomes a buy because it bounced. `Sell` only if you already hold that avoid-quality name.
- `Watch` is not auto-promoted after a crash.
- This job never calls wsli and never sets TRADE_APPROVED.
