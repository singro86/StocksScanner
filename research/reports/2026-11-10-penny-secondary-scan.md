# Secondary penny watchlist scan — 2026-11-10

> I am an AI research assistant, not a licensed financial advisor. This is educational information, not personalized financial advice. Consider a qualified advisor for your situation.

**Paper trading active — dry-run only. Buy lines are paper recommendations, never live Wealthsimple orders.**

## What to buy today (from 20 names)

NONE — no buy today.

Official Rebalance-MCP GARP scores are not computed in this job. Quality flags come from `portfolio/penny-secondary-watchlist.yaml`. A live ticket still needs GARP ≥ 60.

| Rank | Ticker | List | Rec | Close | 1d % | 5d % | SMA20 | RSI14 | Why |
|-----:|--------|------|-----|------:|-----:|-----:|------:|------:|-----|
| 1 | GORO | Secondary 20 | Watch | 3.46 | +1.92 | +21.66 | 3.24 | 49.3 | No official GARP ≥ 60 yet. Not auto-promoted after a crash. |
| 2 | ARKO | Secondary 20 | Watch | 4.17 | -0.59 | +8.72 | 3.95 | 56.1 | No official GARP ≥ 60 yet. Not auto-promoted after a crash. |
| 3 | ALTO | Secondary 20 | Watch | 3.79 | -0.66 | +6.90 | 3.63 | 62.9 | No official GARP ≥ 60 yet. Not auto-promoted after a crash. |
| 4 | SABR | Secondary 20 | Watch | 1.77 | -1.67 | +5.99 | 1.66 | 68.1 | No official GARP ≥ 60 yet. Not auto-promoted after a crash. |
| 5 | CYH | Secondary 20 | Watch | 2.16 | -4.42 | +5.37 | 2.59 | 30.1 | No official GARP ≥ 60 yet. Not auto-promoted after a crash. |
| 6 | MDXG | Secondary 20 | Watch | 3.33 | +0.30 | +2.46 | 3.83 | 34.1 | No official GARP ≥ 60 yet. Not auto-promoted after a crash. |
| 7 | GDRX | Secondary 20 | Watch | 3.54 | -2.88 | +1.58 | 3.52 | 49.0 | No official GARP ≥ 60 yet. Not auto-promoted after a crash. |
| 8 | AREC | Secondary 20 | Watch | 1.06 | -8.97 | +0.00 | 1.13 | 48.1 | No official GARP ≥ 60 yet. Not auto-promoted after a crash. |
| 9 | SPRO | Secondary 20 | Watch | 1.03 | -3.74 | -0.96 | 1.10 | 36.0 | No official GARP ≥ 60 yet. Not auto-promoted after a crash. |
| 10 | ABUS | Secondary 20 | Watch | 3.80 | +2.15 | -2.06 | 4.10 | 35.6 | No official GARP ≥ 60 yet. Not auto-promoted after a crash. |
| 11 | VFF | Secondary 20 | Watch | 2.68 | -5.63 | -5.96 | 2.67 | 47.1 | No official GARP ≥ 60 yet. Not auto-promoted after a crash. |
| 12 | AMPY | Secondary 20 | Watch | 3.50 | +9.53 | -6.78 | 4.09 | 29.1 | No official GARP ≥ 60 yet. Not auto-promoted after a crash. |
| 13 | HLLY | Secondary 20 | Watch | 2.51 | -3.83 | -7.04 | 2.55 | 50.5 | No official GARP ≥ 60 yet. Not auto-promoted after a crash. |
| 14 | NAGE | Secondary 20 | Watch | 2.15 | -5.92 | -9.11 | 2.41 | 39.3 | No official GARP ≥ 60 yet. Not auto-promoted after a crash. |
| 15 | UWMC | Secondary 20 | Watch | 1.36 | -7.77 | -14.15 | 1.37 | 61.3 | No official GARP ≥ 60 yet. Not auto-promoted after a crash. |
| 16 | AISP | Secondary 20 | Watch | 1.68 | -3.18 | -18.29 | 2.05 | 21.4 | No official GARP ≥ 60 yet. Not auto-promoted after a crash. |
| 17 | VRRM | Secondary 20 | Watch | 2.03 | -4.70 | -23.68 | 2.79 | 24.4 | No official GARP ≥ 60 yet. Not auto-promoted after a crash. |
| 18 | TYGO | Secondary 20 | Watch | 0.69 | -9.20 | -24.58 | 0.87 | 38.8 | No official GARP ≥ 60 yet. Not auto-promoted after a crash. |
| 19 | TBLA | Secondary 20 | Watch | 1.99 | -7.44 | -41.47 | 3.14 | 14.1 | No official GARP ≥ 60 yet. Not auto-promoted after a crash. |
| 20 | SITC | Secondary 20 | Watch | 0.69 | +3.05 | -81.09 | 3.17 | 6.0 | No official GARP ≥ 60 yet. Not auto-promoted after a crash. |

Prices: Yahoo Finance daily bars, 2026-11-10 America/Phoenix. SMA20 and RSI14 from the last 3 months of daily closes. Do not use Equibles for this routine price check.


## Rules

- Ranked Buy → Sell → Hold → Watch → Avoid. Max one Buy (paper) per morning.
- Mega-cap core (NVDA / MSFT / GOOGL / AAPL) is display-only in the digest top section — never the morning paper Buy.
- `Avoid` never becomes a buy because it bounced. `Sell` only if you already hold that avoid-quality name.
- `Watch` is not auto-promoted after a crash.
- This job never calls wsli and never sets TRADE_APPROVED.
