# Secondary penny watchlist scan — 2026-10-30

> I am an AI research assistant, not a licensed financial advisor. This is educational information, not personalized financial advice. Consider a qualified advisor for your situation.

**Paper trading active — dry-run only. Buy lines are paper recommendations, never live Wealthsimple orders.**

## What to buy today (from 20 names)

NONE — no buy today.

Official Rebalance-MCP GARP scores are not computed in this job. Quality flags come from `portfolio/penny-secondary-watchlist.yaml`. A live ticket still needs GARP ≥ 60.

| Rank | Ticker | List | Rec | Close | 1d % | 5d % | SMA20 | RSI14 | Why |
|-----:|--------|------|-----|------:|-----:|-----:|------:|------:|-----|
| 1 | AREC | Secondary 20 | Watch | 1.23 | -3.53 | +7.89 | 1.31 | 31.2 | No official GARP ≥ 60 yet. Not auto-promoted after a crash. |
| 2 | UWMC | Secondary 20 | Watch | 1.54 | +3.36 | +6.21 | 1.22 | 76.5 | No official GARP ≥ 60 yet. Not auto-promoted after a crash. |
| 3 | SABR | Secondary 20 | Watch | 1.59 | -3.33 | +4.93 | 1.72 | 31.4 | No official GARP ≥ 60 yet. Not auto-promoted after a crash. |
| 4 | HLLY | Secondary 20 | Watch | 2.59 | -2.58 | +4.07 | 2.51 | 57.2 | No official GARP ≥ 60 yet. Not auto-promoted after a crash. |
| 5 | SITC | Secondary 20 | Watch | 3.81 | -0.39 | +1.74 | 3.44 | 88.8 | No official GARP ≥ 60 yet. Not auto-promoted after a crash. |
| 6 | ALTO | Secondary 20 | Watch | 3.63 | -0.41 | +0.69 | 3.65 | 48.4 | No official GARP ≥ 60 yet. Not auto-promoted after a crash. |
| 7 | TBLA | Secondary 20 | Watch | 3.42 | -2.70 | +0.44 | 3.42 | 51.9 | No official GARP ≥ 60 yet. Not auto-promoted after a crash. |
| 8 | ABUS | Secondary 20 | Watch | 4.14 | -3.15 | -1.31 | 4.26 | 49.7 | No official GARP ≥ 60 yet. Not auto-promoted after a crash. |
| 9 | MDXG | Secondary 20 | Watch | 3.83 | -3.65 | -2.17 | 4.30 | 19.4 | No official GARP ≥ 60 yet. Not auto-promoted after a crash. |
| 10 | ARKO | Secondary 20 | Watch | 3.72 | -1.59 | -2.36 | 4.01 | 29.1 | No official GARP ≥ 60 yet. Not auto-promoted after a crash. |
| 11 | GDRX | Secondary 20 | Watch | 3.42 | -3.25 | -3.25 | 3.45 | 47.3 | No official GARP ≥ 60 yet. Not auto-promoted after a crash. |
| 12 | VFF | Secondary 20 | Watch | 2.48 | -4.05 | -3.50 | 2.63 | 41.7 | No official GARP ≥ 60 yet. Not auto-promoted after a crash. |
| 13 | NAGE | Secondary 20 | Watch | 2.35 | -6.20 | -3.50 | 2.55 | 30.9 | No official GARP ≥ 60 yet. Not auto-promoted after a crash. |
| 14 | AISP | Secondary 20 | Watch | 2.07 | -8.03 | -4.19 | 2.19 | 34.1 | No official GARP ≥ 60 yet. Not auto-promoted after a crash. |
| 15 | SPRO | Secondary 20 | Watch | 1.05 | -5.41 | -5.41 | 1.14 | 39.0 | No official GARP ≥ 60 yet. Not auto-promoted after a crash. |
| 16 | GORO | Secondary 20 | Watch | 3.11 | -5.18 | -5.76 | 3.31 | 37.1 | No official GARP ≥ 60 yet. Not auto-promoted after a crash. |
| 17 | AMPY | Secondary 20 | Watch | 4.25 | -1.96 | -7.52 | 4.45 | 39.9 | No official GARP ≥ 60 yet. Not auto-promoted after a crash. |
| 18 | VRRM | Secondary 20 | Watch | 2.72 | -18.56 | -11.97 | 2.98 | 44.0 | No official GARP ≥ 60 yet. Not auto-promoted after a crash. |
| 19 | TYGO | Secondary 20 | Watch | 0.87 | -8.89 | -15.61 | 0.90 | 48.5 | No official GARP ≥ 60 yet. Not auto-promoted after a crash. |
| 20 | CYH | Secondary 20 | Watch | 2.33 | -3.11 | -20.03 | 2.80 | 24.9 | No official GARP ≥ 60 yet. Not auto-promoted after a crash. |

Prices: Yahoo Finance daily bars, 2026-10-30 America/Phoenix. SMA20 and RSI14 from the last 3 months of daily closes. Do not use Equibles for this routine price check.


## Rules

- Ranked Buy → Sell → Hold → Watch → Avoid. Max one Buy (paper) per morning.
- Mega-cap core (NVDA / MSFT / GOOGL / AAPL) is display-only in the digest top section — never the morning paper Buy.
- `Avoid` never becomes a buy because it bounced. `Sell` only if you already hold that avoid-quality name.
- `Watch` is not auto-promoted after a crash.
- This job never calls wsli and never sets TRADE_APPROVED.
