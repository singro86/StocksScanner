# Secondary penny watchlist scan — 2026-11-01

> I am an AI research assistant, not a licensed financial advisor. This is educational information, not personalized financial advice. Consider a qualified advisor for your situation.

**Paper trading active — dry-run only. Buy lines are paper recommendations, never live Wealthsimple orders.**

## What to buy today (from 20 names)

NONE — no buy today.

Official Rebalance-MCP GARP scores are not computed in this job. Quality flags come from `portfolio/penny-secondary-watchlist.yaml`. A live ticket still needs GARP ≥ 60.

| Rank | Ticker | List | Rec | Close | 1d % | 5d % | SMA20 | RSI14 | Why |
|-----:|--------|------|-----|------:|-----:|-----:|------:|------:|-----|
| 1 | UWMC | Secondary 20 | Watch | 1.57 | +5.37 | +8.28 | 1.22 | 77.2 | No official GARP ≥ 60 yet. Not auto-promoted after a crash. |
| 2 | AREC | Secondary 20 | Watch | 1.22 | -4.31 | +7.02 | 1.31 | 30.8 | No official GARP ≥ 60 yet. Not auto-promoted after a crash. |
| 3 | SABR | Secondary 20 | Watch | 1.62 | -1.82 | +6.58 | 1.72 | 32.4 | No official GARP ≥ 60 yet. Not auto-promoted after a crash. |
| 4 | HLLY | Secondary 20 | Watch | 2.63 | -1.13 | +5.62 | 2.51 | 59.8 | No official GARP ≥ 60 yet. Not auto-promoted after a crash. |
| 5 | TBLA | Secondary 20 | Watch | 3.46 | -1.56 | +1.61 | 3.42 | 55.1 | No official GARP ≥ 60 yet. Not auto-promoted after a crash. |
| 6 | ALTO | Secondary 20 | Watch | 3.65 | +0.00 | +1.11 | 3.65 | 49.4 | No official GARP ≥ 60 yet. Not auto-promoted after a crash. |
| 7 | ABUS | Secondary 20 | Watch | 4.21 | -1.64 | +0.24 | 4.26 | 53.7 | No official GARP ≥ 60 yet. Not auto-promoted after a crash. |
| 8 | SITC | Secondary 20 | Watch | 3.73 | -2.36 | -0.27 | 3.43 | 82.2 | No official GARP ≥ 60 yet. Not auto-promoted after a crash. |
| 9 | ARKO | Secondary 20 | Watch | 3.79 | +0.27 | -0.53 | 4.01 | 31.5 | No official GARP ≥ 60 yet. Not auto-promoted after a crash. |
| 10 | MDXG | Secondary 20 | Watch | 3.88 | -2.27 | -0.77 | 4.31 | 20.1 | No official GARP ≥ 60 yet. Not auto-promoted after a crash. |
| 11 | GDRX | Secondary 20 | Watch | 3.49 | -1.41 | -1.41 | 3.45 | 50.5 | No official GARP ≥ 60 yet. Not auto-promoted after a crash. |
| 12 | VFF | Secondary 20 | Watch | 2.50 | -3.48 | -2.91 | 2.63 | 42.5 | No official GARP ≥ 60 yet. Not auto-promoted after a crash. |
| 13 | AISP | Secondary 20 | Watch | 2.08 | -7.56 | -3.70 | 2.19 | 34.4 | No official GARP ≥ 60 yet. Not auto-promoted after a crash. |
| 14 | NAGE | Secondary 20 | Watch | 2.33 | -6.80 | -4.12 | 2.55 | 30.3 | No official GARP ≥ 60 yet. Not auto-promoted after a crash. |
| 15 | GORO | Secondary 20 | Watch | 3.16 | -3.66 | -4.24 | 3.31 | 38.7 | No official GARP ≥ 60 yet. Not auto-promoted after a crash. |
| 16 | SPRO | Secondary 20 | Watch | 1.06 | -4.50 | -4.50 | 1.14 | 39.7 | No official GARP ≥ 60 yet. Not auto-promoted after a crash. |
| 17 | AMPY | Secondary 20 | Watch | 4.27 | -1.39 | -6.97 | 4.45 | 40.6 | No official GARP ≥ 60 yet. Not auto-promoted after a crash. |
| 18 | VRRM | Secondary 20 | Watch | 2.80 | -16.17 | -9.38 | 2.98 | 46.2 | No official GARP ≥ 60 yet. Not auto-promoted after a crash. |
| 19 | TYGO | Secondary 20 | Watch | 0.88 | -7.44 | -14.27 | 0.90 | 49.6 | No official GARP ≥ 60 yet. Not auto-promoted after a crash. |
| 20 | CYH | Secondary 20 | Watch | 2.40 | -0.41 | -17.81 | 2.80 | 26.4 | No official GARP ≥ 60 yet. Not auto-promoted after a crash. |

Prices: Yahoo Finance daily bars, 2026-11-01 America/Phoenix. SMA20 and RSI14 from the last 3 months of daily closes. Do not use Equibles for this routine price check.


## Rules

- Ranked Buy → Sell → Hold → Watch → Avoid. Max one Buy (paper) per morning.
- Mega-cap core (NVDA / MSFT / GOOGL / AAPL) is display-only in the digest top section — never the morning paper Buy.
- `Avoid` never becomes a buy because it bounced. `Sell` only if you already hold that avoid-quality name.
- `Watch` is not auto-promoted after a crash.
- This job never calls wsli and never sets TRADE_APPROVED.
