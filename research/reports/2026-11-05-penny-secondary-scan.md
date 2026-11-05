# Secondary penny watchlist scan — 2026-11-05

> I am an AI research assistant, not a licensed financial advisor. This is educational information, not personalized financial advice. Consider a qualified advisor for your situation.

**Paper trading active — dry-run only. Buy lines are paper recommendations, never live Wealthsimple orders.**

## What to buy today (from 20 names)

NONE — no buy today.

Official Rebalance-MCP GARP scores are not computed in this job. Quality flags come from `portfolio/penny-secondary-watchlist.yaml`. A live ticket still needs GARP ≥ 60.

| Rank | Ticker | List | Rec | Close | 1d % | 5d % | SMA20 | RSI14 | Why |
|-----:|--------|------|-----|------:|-----:|-----:|------:|------:|-----|
| 1 | UWMC | Secondary 20 | Watch | 1.60 | -5.03 | +7.72 | 1.31 | 79.4 | No official GARP ≥ 60 yet. Not auto-promoted after a crash. |
| 2 | VFF | Secondary 20 | Watch | 2.77 | -5.29 | +7.14 | 2.64 | 60.4 | No official GARP ≥ 60 yet. Not auto-promoted after a crash. |
| 3 | ARKO | Secondary 20 | Watch | 3.87 | -4.33 | +2.25 | 3.96 | 40.6 | No official GARP ≥ 60 yet. Not auto-promoted after a crash. |
| 4 | SABR | Secondary 20 | Watch | 1.69 | -3.16 | +2.12 | 1.67 | 50.4 | No official GARP ≥ 60 yet. Not auto-promoted after a crash. |
| 5 | ALTO | Secondary 20 | Watch | 3.64 | +4.00 | -0.27 | 3.62 | 63.0 | No official GARP ≥ 60 yet. Not auto-promoted after a crash. |
| 6 | GDRX | Secondary 20 | Watch | 3.52 | -5.38 | -0.56 | 3.50 | 57.1 | No official GARP ≥ 60 yet. Not auto-promoted after a crash. |
| 7 | GORO | Secondary 20 | Watch | 3.15 | +2.27 | -3.96 | 3.25 | 42.0 | No official GARP ≥ 60 yet. Not auto-promoted after a crash. |
| 8 | CYH | Secondary 20 | Watch | 2.27 | -4.41 | -5.60 | 2.69 | 32.0 | No official GARP ≥ 60 yet. Not auto-promoted after a crash. |
| 9 | SITC | Secondary 20 | Watch | 3.60 | -3.36 | -5.89 | 3.53 | 60.9 | No official GARP ≥ 60 yet. Not auto-promoted after a crash. |
| 10 | SPRO | Secondary 20 | Watch | 1.02 | -4.67 | -8.11 | 1.12 | 43.1 | No official GARP ≥ 60 yet. Not auto-promoted after a crash. |
| 11 | ABUS | Secondary 20 | Watch | 3.67 | -9.48 | -14.14 | 4.16 | 30.9 | No official GARP ≥ 60 yet. Not auto-promoted after a crash. |
| 12 | NAGE | Secondary 20 | Watch | 2.08 | -17.46 | -16.80 | 2.48 | 33.3 | No official GARP ≥ 60 yet. Not auto-promoted after a crash. |
| 13 | MDXG | Secondary 20 | Watch | 3.25 | +1.41 | -18.26 | 4.04 | 18.7 | No official GARP ≥ 60 yet. Not auto-promoted after a crash. |
| 14 | HLLY | Secondary 20 | Watch | 2.16 | -25.52 | -18.80 | 2.56 | 39.6 | No official GARP ≥ 60 yet. Not auto-promoted after a crash. |
| 15 | AISP | Secondary 20 | Watch | 1.75 | -5.13 | -22.00 | 2.14 | 37.7 | No official GARP ≥ 60 yet. Not auto-promoted after a crash. |
| 16 | TYGO | Secondary 20 | Watch | 0.73 | -26.35 | -23.03 | 0.90 | 44.6 | No official GARP ≥ 60 yet. Not auto-promoted after a crash. |
| 17 | AREC | Secondary 20 | Watch | 0.96 | -3.36 | -24.51 | 1.18 | 35.9 | No official GARP ≥ 60 yet. Not auto-promoted after a crash. |
| 18 | AMPY | Secondary 20 | Watch | 3.17 | -8.91 | -26.79 | 4.26 | 17.2 | No official GARP ≥ 60 yet. Not auto-promoted after a crash. |
| 19 | VRRM | Secondary 20 | Watch | 2.31 | -7.06 | -30.99 | 2.91 | 34.9 | No official GARP ≥ 60 yet. Not auto-promoted after a crash. |
| 20 | TBLA | Secondary 20 | Watch | 2.19 | -19.89 | -37.64 | 3.35 | 10.7 | No official GARP ≥ 60 yet. Not auto-promoted after a crash. |

Prices: Yahoo Finance daily bars, 2026-11-05 America/Phoenix. SMA20 and RSI14 from the last 3 months of daily closes. Do not use Equibles for this routine price check.


## Rules

- Ranked Buy → Sell → Hold → Watch → Avoid. Max one Buy (paper) per morning.
- Mega-cap core (NVDA / MSFT / GOOGL / AAPL) is display-only in the digest top section — never the morning paper Buy.
- `Avoid` never becomes a buy because it bounced. `Sell` only if you already hold that avoid-quality name.
- `Watch` is not auto-promoted after a crash.
- This job never calls wsli and never sets TRADE_APPROVED.
