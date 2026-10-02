# Secondary penny watchlist scan — 2026-10-02

> I am an AI research assistant, not a licensed financial advisor. This is educational information, not personalized financial advice. Consider a qualified advisor for your situation.

**Paper trading active — dry-run only. Buy lines are paper recommendations, never live Wealthsimple orders.**

## What to buy today (from 20 names)

NONE — no buy today.

Official Rebalance-MCP GARP scores are not computed in this job. Quality flags come from `portfolio/penny-secondary-watchlist.yaml`. A live ticket still needs GARP ≥ 60.

| Rank | Ticker | List | Rec | Close | 1d % | 5d % | SMA20 | RSI14 | Why |
|-----:|--------|------|-----|------:|-----:|-----:|------:|------:|-----|
| 1 | AISP | Secondary 20 | Watch | 2.12 | -4.28 | +16.76 | 1.96 | 61.5 | No official GARP ≥ 60 yet. Not auto-promoted after a crash. |
| 2 | SITC | Secondary 20 | Watch | 3.49 | -0.29 | +14.05 | 3.02 | 83.2 | No official GARP ≥ 60 yet. Not auto-promoted after a crash. |
| 3 | ALTO | Secondary 20 | Watch | 3.81 | +3.67 | +2.28 | 3.88 | 41.1 | No official GARP ≥ 60 yet. Not auto-promoted after a crash. |
| 4 | TYGO | Secondary 20 | Watch | 0.88 | -1.86 | +1.79 | 0.96 | 30.9 | No official GARP ≥ 60 yet. Not auto-promoted after a crash. |
| 5 | AMPY | Secondary 20 | Watch | 4.33 | -1.14 | +1.17 | 4.53 | 32.9 | No official GARP ≥ 60 yet. Not auto-promoted after a crash. |
| 6 | UWMC | Secondary 20 | Watch | 1.23 | +2.50 | +0.82 | 1.28 | 35.3 | No official GARP ≥ 60 yet. Not auto-promoted after a crash. |
| 7 | MDXG | Secondary 20 | Watch | 4.58 | -1.29 | -1.93 | 4.69 | 46.0 | No official GARP ≥ 60 yet. Not auto-promoted after a crash. |
| 8 | SPRO | Secondary 20 | Watch | 1.21 | -4.37 | -2.03 | 1.19 | 55.6 | No official GARP ≥ 60 yet. Not auto-promoted after a crash. |
| 9 | ARKO | Secondary 20 | Watch | 4.16 | +1.09 | -2.92 | 4.35 | 26.6 | No official GARP ≥ 60 yet. Not auto-promoted after a crash. |
| 10 | GDRX | Secondary 20 | Watch | 3.25 | -0.77 | -3.13 | 3.38 | 25.9 | No official GARP ≥ 60 yet. Not auto-promoted after a crash. |
| 11 | HLLY | Secondary 20 | Watch | 2.35 | -1.26 | -4.86 | 2.60 | 30.1 | No official GARP ≥ 60 yet. Not auto-promoted after a crash. |
| 12 | TBLA | Secondary 20 | Watch | 3.29 | -0.90 | -5.46 | 3.60 | 13.1 | No official GARP ≥ 60 yet. Not auto-promoted after a crash. |
| 13 | AREC | Secondary 20 | Watch | 1.78 | -1.11 | -6.32 | 2.01 | 27.2 | No official GARP ≥ 60 yet. Not auto-promoted after a crash. |
| 14 | CYH | Secondary 20 | Watch | 2.72 | -1.09 | -7.48 | 2.90 | 34.7 | No official GARP ≥ 60 yet. Not auto-promoted after a crash. |
| 15 | GORO | Secondary 20 | Watch | 3.23 | +1.41 | -7.57 | 3.52 | 31.1 | No official GARP ≥ 60 yet. Not auto-promoted after a crash. |
| 16 | VFF | Secondary 20 | Watch | 2.91 | +2.10 | -8.20 | 2.95 | 54.8 | No official GARP ≥ 60 yet. Not auto-promoted after a crash. |
| 17 | ABUS | Secondary 20 | Watch | 4.44 | -2.63 | -8.45 | 4.95 | 15.8 | No official GARP ≥ 60 yet. Not auto-promoted after a crash. |
| 18 | SABR | Secondary 20 | Watch | 1.97 | -1.00 | -9.63 | 2.18 | 39.6 | No official GARP ≥ 60 yet. Not auto-promoted after a crash. |
| 19 | VRRM | Secondary 20 | Watch | 2.92 | -2.34 | -9.88 | 3.42 | 19.1 | No official GARP ≥ 60 yet. Not auto-promoted after a crash. |
| 20 | NAGE | Secondary 20 | Watch | 2.70 | +0.75 | -11.47 | 2.99 | 25.0 | No official GARP ≥ 60 yet. Not auto-promoted after a crash. |

Prices: Yahoo Finance daily bars, 2026-10-02 America/Toronto. SMA20 and RSI14 from the last 3 months of daily closes. Do not use Equibles for this routine price check.


## Rules

- Ranked Buy → Sell → Hold → Watch → Avoid. Max one Buy (paper) per morning.
- `Avoid` never becomes a buy because it bounced. `Sell` only if you already hold that avoid-quality name.
- `Watch` is not auto-promoted after a crash.
- This job never calls wsli and never sets TRADE_APPROVED.
