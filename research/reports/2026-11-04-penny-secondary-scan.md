# Secondary penny watchlist scan — 2026-11-04

> I am an AI research assistant, not a licensed financial advisor. This is educational information, not personalized financial advice. Consider a qualified advisor for your situation.

**Paper trading active — dry-run only. Buy lines are paper recommendations, never live Wealthsimple orders.**

## What to buy today (from 20 names)

NONE — no buy today.

Official Rebalance-MCP GARP scores are not computed in this job. Quality flags come from `portfolio/penny-secondary-watchlist.yaml`. A live ticket still needs GARP ≥ 60.

| Rank | Ticker | List | Rec | Close | 1d % | 5d % | SMA20 | RSI14 | Why |
|-----:|--------|------|-----|------:|-----:|-----:|------:|------:|-----|
| 1 | VFF | Secondary 20 | Watch | 2.97 | +4.21 | +15.12 | 2.64 | 66.4 | No official GARP ≥ 60 yet. Not auto-promoted after a crash. |
| 2 | UWMC | Secondary 20 | Watch | 1.72 | +7.86 | +14.33 | 1.29 | 78.7 | No official GARP ≥ 60 yet. Not auto-promoted after a crash. |
| 3 | SABR | Secondary 20 | Watch | 1.76 | +5.39 | +10.00 | 1.69 | 48.0 | No official GARP ≥ 60 yet. Not auto-promoted after a crash. |
| 4 | HLLY | Secondary 20 | Watch | 2.90 | +7.22 | +9.66 | 2.58 | 64.8 | No official GARP ≥ 60 yet. Not auto-promoted after a crash. |
| 5 | TYGO | Secondary 20 | Watch | 1.01 | +10.93 | +9.49 | 0.91 | 64.9 | No official GARP ≥ 60 yet. Not auto-promoted after a crash. |
| 6 | ARKO | Secondary 20 | Watch | 4.01 | +4.43 | +8.67 | 3.97 | 45.2 | No official GARP ≥ 60 yet. Not auto-promoted after a crash. |
| 7 | GDRX | Secondary 20 | Watch | 3.75 | +7.31 | +7.92 | 3.50 | 61.0 | No official GARP ≥ 60 yet. Not auto-promoted after a crash. |
| 8 | NAGE | Secondary 20 | Watch | 2.55 | +8.05 | +0.39 | 2.51 | 48.4 | No official GARP ≥ 60 yet. Not auto-promoted after a crash. |
| 9 | SITC | Secondary 20 | Watch | 3.67 | +0.00 | -3.17 | 3.50 | 83.0 | No official GARP ≥ 60 yet. Not auto-promoted after a crash. |
| 10 | ALTO | Secondary 20 | Watch | 3.52 | -0.99 | -3.96 | 3.62 | 40.8 | No official GARP ≥ 60 yet. Not auto-promoted after a crash. |
| 11 | ABUS | Secondary 20 | Watch | 4.04 | +4.00 | -6.60 | 4.19 | 38.2 | No official GARP ≥ 60 yet. Not auto-promoted after a crash. |
| 12 | GORO | Secondary 20 | Watch | 3.06 | +7.92 | -7.68 | 3.25 | 41.0 | No official GARP ≥ 60 yet. Not auto-promoted after a crash. |
| 13 | SPRO | Secondary 20 | Watch | 1.06 | +2.40 | -8.97 | 1.12 | 44.1 | No official GARP ≥ 60 yet. Not auto-promoted after a crash. |
| 14 | CYH | Secondary 20 | Watch | 2.35 | +14.63 | -11.65 | 2.71 | 30.7 | No official GARP ≥ 60 yet. Not auto-promoted after a crash. |
| 15 | AISP | Secondary 20 | Watch | 1.89 | -8.05 | -16.96 | 2.17 | 40.0 | No official GARP ≥ 60 yet. Not auto-promoted after a crash. |
| 16 | AREC | Secondary 20 | Watch | 1.00 | -6.10 | -18.03 | 1.22 | 34.6 | No official GARP ≥ 60 yet. Not auto-promoted after a crash. |
| 17 | MDXG | Secondary 20 | Watch | 3.17 | -2.31 | -19.62 | 4.10 | 14.6 | No official GARP ≥ 60 yet. Not auto-promoted after a crash. |
| 18 | VRRM | Secondary 20 | Watch | 2.52 | -5.26 | -19.75 | 2.94 | 37.6 | No official GARP ≥ 60 yet. Not auto-promoted after a crash. |
| 19 | AMPY | Secondary 20 | Watch | 3.52 | -6.44 | -19.86 | 4.34 | 24.8 | No official GARP ≥ 60 yet. Not auto-promoted after a crash. |
| 20 | TBLA | Secondary 20 | Watch | 2.77 | -18.68 | -20.55 | 3.42 | 15.2 | No official GARP ≥ 60 yet. Not auto-promoted after a crash. |

Prices: Yahoo Finance daily bars, 2026-11-04 America/Phoenix. SMA20 and RSI14 from the last 3 months of daily closes. Do not use Equibles for this routine price check.


## Rules

- Ranked Buy → Sell → Hold → Watch → Avoid. Max one Buy (paper) per morning.
- Mega-cap core (NVDA / MSFT / GOOGL / AAPL) is display-only in the digest top section — never the morning paper Buy.
- `Avoid` never becomes a buy because it bounced. `Sell` only if you already hold that avoid-quality name.
- `Watch` is not auto-promoted after a crash.
- This job never calls wsli and never sets TRADE_APPROVED.
