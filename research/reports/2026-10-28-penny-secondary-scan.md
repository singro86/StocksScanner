# Secondary penny watchlist scan — 2026-10-28

> I am an AI research assistant, not a licensed financial advisor. This is educational information, not personalized financial advice. Consider a qualified advisor for your situation.

**Paper trading active — dry-run only. Buy lines are paper recommendations, never live Wealthsimple orders.**

## What to buy today (from 20 names)

NONE — no buy today.

Official Rebalance-MCP GARP scores are not computed in this job. Quality flags come from `portfolio/penny-secondary-watchlist.yaml`. A live ticket still needs GARP ≥ 60.

| Rank | Ticker | List | Rec | Close | 1d % | 5d % | SMA20 | RSI14 | Why |
|-----:|--------|------|-----|------:|-----:|-----:|------:|------:|-----|
| 1 | UWMC | Secondary 20 | Watch | 1.51 | -2.88 | +36.49 | 1.19 | 71.8 | No official GARP ≥ 60 yet. Not auto-promoted after a crash. |
| 2 | AREC | Secondary 20 | Watch | 1.19 | +1.28 | +7.73 | 1.37 | 18.4 | No official GARP ≥ 60 yet. Not auto-promoted after a crash. |
| 3 | VRRM | Secondary 20 | Watch | 3.11 | -0.95 | +5.42 | 2.96 | 60.4 | No official GARP ≥ 60 yet. Not auto-promoted after a crash. |
| 4 | MDXG | Secondary 20 | Watch | 3.90 | +0.00 | +4.28 | 4.37 | 28.1 | No official GARP ≥ 60 yet. Not auto-promoted after a crash. |
| 5 | HLLY | Secondary 20 | Watch | 2.59 | +0.39 | +4.02 | 2.48 | 58.8 | No official GARP ≥ 60 yet. Not auto-promoted after a crash. |
| 6 | SABR | Secondary 20 | Watch | 1.56 | +0.32 | +2.96 | 1.75 | 23.0 | No official GARP ≥ 60 yet. Not auto-promoted after a crash. |
| 7 | NAGE | Secondary 20 | Watch | 2.54 | +1.40 | +2.63 | 2.58 | 40.2 | No official GARP ≥ 60 yet. Not auto-promoted after a crash. |
| 8 | TYGO | Secondary 20 | Watch | 0.91 | -4.60 | +2.47 | 0.89 | 51.7 | No official GARP ≥ 60 yet. Not auto-promoted after a crash. |
| 9 | ABUS | Secondary 20 | Watch | 4.28 | -0.23 | +2.39 | 4.29 | 56.2 | No official GARP ≥ 60 yet. Not auto-promoted after a crash. |
| 10 | SITC | Secondary 20 | Watch | 3.77 | +0.13 | +1.48 | 3.40 | 81.2 | No official GARP ≥ 60 yet. Not auto-promoted after a crash. |
| 11 | ALTO | Secondary 20 | Watch | 3.62 | -2.82 | +0.70 | 3.66 | 43.4 | No official GARP ≥ 60 yet. Not auto-promoted after a crash. |
| 12 | TBLA | Secondary 20 | Watch | 3.44 | +1.62 | -0.72 | 3.40 | 44.7 | No official GARP ≥ 60 yet. Not auto-promoted after a crash. |
| 13 | SPRO | Secondary 20 | Watch | 1.16 | +1.75 | -0.85 | 1.16 | 51.9 | No official GARP ≥ 60 yet. Not auto-promoted after a crash. |
| 14 | AMPY | Secondary 20 | Watch | 4.40 | +1.77 | -2.08 | 4.46 | 43.1 | No official GARP ≥ 60 yet. Not auto-promoted after a crash. |
| 15 | AISP | Secondary 20 | Watch | 2.23 | -2.62 | -2.62 | 2.19 | 47.6 | No official GARP ≥ 60 yet. Not auto-promoted after a crash. |
| 16 | GDRX | Secondary 20 | Watch | 3.46 | -0.43 | -2.94 | 3.43 | 55.6 | No official GARP ≥ 60 yet. Not auto-promoted after a crash. |
| 17 | GORO | Secondary 20 | Watch | 3.31 | +3.28 | -5.03 | 3.31 | 54.6 | No official GARP ≥ 60 yet. Not auto-promoted after a crash. |
| 18 | CYH | Secondary 20 | Watch | 2.67 | -6.16 | -5.50 | 2.83 | 46.8 | No official GARP ≥ 60 yet. Not auto-promoted after a crash. |
| 19 | VFF | Secondary 20 | Watch | 2.57 | -0.77 | -6.54 | 2.66 | 41.8 | No official GARP ≥ 60 yet. Not auto-promoted after a crash. |
| 20 | ARKO | Secondary 20 | Watch | 3.71 | -3.51 | -6.89 | 4.05 | 28.3 | No official GARP ≥ 60 yet. Not auto-promoted after a crash. |

Prices: Yahoo Finance daily bars, 2026-10-28 America/Phoenix. SMA20 and RSI14 from the last 3 months of daily closes. Do not use Equibles for this routine price check.


## Rules

- Ranked Buy → Sell → Hold → Watch → Avoid. Max one Buy (paper) per morning.
- Mega-cap core (NVDA / MSFT / GOOGL / AAPL) is display-only in the digest top section — never the morning paper Buy.
- `Avoid` never becomes a buy because it bounced. `Sell` only if you already hold that avoid-quality name.
- `Watch` is not auto-promoted after a crash.
- This job never calls wsli and never sets TRADE_APPROVED.
