# Secondary penny watchlist scan — 2026-10-19

> I am an AI research assistant, not a licensed financial advisor. This is educational information, not personalized financial advice. Consider a qualified advisor for your situation.

**Paper trading active — dry-run only. Buy lines are paper recommendations, never live Wealthsimple orders.**

## What to buy today (from 20 names)

NONE — no buy today.

Official Rebalance-MCP GARP scores are not computed in this job. Quality flags come from `portfolio/penny-secondary-watchlist.yaml`. A live ticket still needs GARP ≥ 60.

| Rank | Ticker | List | Rec | Close | 1d % | 5d % | SMA20 | RSI14 | Why |
|-----:|--------|------|-----|------:|-----:|-----:|------:|------:|-----|
| 1 | SITC | Secondary 20 | Watch | 3.56 | +3.79 | +15.58 | 3.18 | 65.5 | No official GARP ≥ 60 yet. Not auto-promoted after a crash. |
| 2 | UWMC | Secondary 20 | Watch | 1.05 | +0.48 | +3.43 | 1.16 | 37.1 | No official GARP ≥ 60 yet. Not auto-promoted after a crash. |
| 3 | HLLY | Secondary 20 | Watch | 2.52 | +1.21 | +2.44 | 2.45 | 54.1 | No official GARP ≥ 60 yet. Not auto-promoted after a crash. |
| 4 | ABUS | Secondary 20 | Watch | 4.22 | +0.12 | +1.81 | 4.50 | 34.9 | No official GARP ≥ 60 yet. Not auto-promoted after a crash. |
| 5 | TBLA | Secondary 20 | Watch | 3.44 | +0.14 | +1.32 | 3.40 | 51.8 | No official GARP ≥ 60 yet. Not auto-promoted after a crash. |
| 6 | AMPY | Secondary 20 | Watch | 4.50 | +1.58 | -0.22 | 4.38 | 64.5 | No official GARP ≥ 60 yet. Not auto-promoted after a crash. |
| 7 | GORO | Secondary 20 | Watch | 3.40 | +0.15 | -1.02 | 3.35 | 59.6 | No official GARP ≥ 60 yet. Not auto-promoted after a crash. |
| 8 | VFF | Secondary 20 | Watch | 2.56 | +0.99 | -2.48 | 2.81 | 19.2 | No official GARP ≥ 60 yet. Not auto-promoted after a crash. |
| 9 | ARKO | Secondary 20 | Watch | 4.03 | -1.83 | -3.25 | 4.16 | 43.0 | No official GARP ≥ 60 yet. Not auto-promoted after a crash. |
| 10 | GDRX | Secondary 20 | Watch | 3.37 | +0.15 | -3.31 | 3.35 | 57.6 | No official GARP ≥ 60 yet. Not auto-promoted after a crash. |
| 11 | VRRM | Secondary 20 | Watch | 2.81 | -1.92 | -3.94 | 3.01 | 36.9 | No official GARP ≥ 60 yet. Not auto-promoted after a crash. |
| 12 | ALTO | Secondary 20 | Watch | 3.48 | +0.87 | -4.92 | 3.69 | 41.9 | No official GARP ≥ 60 yet. Not auto-promoted after a crash. |
| 13 | CYH | Secondary 20 | Watch | 2.77 | -3.82 | -5.14 | 2.86 | 41.0 | No official GARP ≥ 60 yet. Not auto-promoted after a crash. |
| 14 | NAGE | Secondary 20 | Watch | 2.49 | +0.05 | -5.28 | 2.76 | 25.1 | No official GARP ≥ 60 yet. Not auto-promoted after a crash. |
| 15 | SPRO | Secondary 20 | Watch | 1.11 | +1.36 | -5.51 | 1.19 | 40.2 | No official GARP ≥ 60 yet. Not auto-promoted after a crash. |
| 16 | TYGO | Secondary 20 | Watch | 0.83 | +0.41 | -6.71 | 0.88 | 48.1 | No official GARP ≥ 60 yet. Not auto-promoted after a crash. |
| 17 | MDXG | Secondary 20 | Watch | 4.38 | -1.24 | -9.42 | 4.65 | 33.5 | No official GARP ≥ 60 yet. Not auto-promoted after a crash. |
| 18 | SABR | Secondary 20 | Watch | 1.64 | -2.68 | -13.03 | 1.97 | 5.4 | No official GARP ≥ 60 yet. Not auto-promoted after a crash. |
| 19 | AISP | Secondary 20 | Watch | 2.05 | +0.00 | -16.67 | 2.07 | 57.5 | No official GARP ≥ 60 yet. Not auto-promoted after a crash. |
| 20 | AREC | Secondary 20 | Watch | 1.16 | +1.93 | -22.53 | 1.63 | 6.9 | No official GARP ≥ 60 yet. Not auto-promoted after a crash. |

Prices: Yahoo Finance daily bars, 2026-10-19 America/Phoenix. SMA20 and RSI14 from the last 3 months of daily closes. Do not use Equibles for this routine price check.


## Rules

- Ranked Buy → Sell → Hold → Watch → Avoid. Max one Buy (paper) per morning.
- Mega-cap core (NVDA / MSFT / GOOGL / AAPL) is display-only in the digest top section — never the morning paper Buy.
- `Avoid` never becomes a buy because it bounced. `Sell` only if you already hold that avoid-quality name.
- `Watch` is not auto-promoted after a crash.
- This job never calls wsli and never sets TRADE_APPROVED.
