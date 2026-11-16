# Secondary penny watchlist scan — 2026-11-16

> I am an AI research assistant, not a licensed financial advisor. This is educational information, not personalized financial advice. Consider a qualified advisor for your situation.

**Paper trading active — dry-run only. Buy lines are paper recommendations, never live Wealthsimple orders.**

## What to buy today (from 20 names)

NONE — no buy today.

Official Rebalance-MCP GARP scores are not computed in this job. Quality flags come from `portfolio/penny-secondary-watchlist.yaml`. A live ticket still needs GARP ≥ 60.

| Rank | Ticker | List | Rec | Close | 1d % | 5d % | SMA20 | RSI14 | Why |
|-----:|--------|------|-----|------:|-----:|-----:|------:|------:|-----|
| 1 | AMPY | Secondary 20 | Watch | 4.03 | -0.98 | +25.94 | 4.00 | 44.1 | No official GARP ≥ 60 yet. Not auto-promoted after a crash. |
| 2 | ABUS | Secondary 20 | Watch | 4.04 | -1.22 | +8.60 | 4.05 | 41.8 | No official GARP ≥ 60 yet. Not auto-promoted after a crash. |
| 3 | SITC | Secondary 20 | Watch | 0.71 | +8.03 | +5.45 | 2.65 | 5.6 | No official GARP ≥ 60 yet. Not auto-promoted after a crash. |
| 4 | TBLA | Secondary 20 | Watch | 2.10 | -5.83 | -2.33 | 2.87 | 21.6 | No official GARP ≥ 60 yet. Not auto-promoted after a crash. |
| 5 | ALTO | Secondary 20 | Watch | 3.68 | +0.55 | -3.67 | 3.66 | 47.7 | No official GARP ≥ 60 yet. Not auto-promoted after a crash. |
| 6 | HLLY | Secondary 20 | Watch | 2.51 | +1.21 | -3.83 | 2.54 | 48.4 | No official GARP ≥ 60 yet. Not auto-promoted after a crash. |
| 7 | GDRX | Secondary 20 | Watch | 3.51 | -1.40 | -3.84 | 3.55 | 51.1 | No official GARP ≥ 60 yet. Not auto-promoted after a crash. |
| 8 | GORO | Secondary 20 | Watch | 3.25 | +0.93 | -4.13 | 3.23 | 51.6 | No official GARP ≥ 60 yet. Not auto-promoted after a crash. |
| 9 | ARKO | Secondary 20 | Watch | 4.03 | +0.62 | -4.17 | 3.96 | 56.5 | No official GARP ≥ 60 yet. Not auto-promoted after a crash. |
| 10 | MDXG | Secondary 20 | Watch | 3.18 | -0.94 | -4.22 | 3.57 | 20.0 | No official GARP ≥ 60 yet. Not auto-promoted after a crash. |
| 11 | SABR | Secondary 20 | Watch | 1.72 | -7.53 | -4.44 | 1.68 | 60.5 | No official GARP ≥ 60 yet. Not auto-promoted after a crash. |
| 12 | CYH | Secondary 20 | Watch | 2.13 | -4.91 | -5.75 | 2.45 | 29.9 | No official GARP ≥ 60 yet. Not auto-promoted after a crash. |
| 13 | AISP | Secondary 20 | Watch | 1.61 | +0.62 | -6.94 | 1.96 | 11.4 | No official GARP ≥ 60 yet. Not auto-promoted after a crash. |
| 14 | SPRO | Secondary 20 | Watch | 0.95 | -5.36 | -11.55 | 1.07 | 27.7 | No official GARP ≥ 60 yet. Not auto-promoted after a crash. |
| 15 | NAGE | Secondary 20 | Watch | 2.01 | -2.90 | -11.84 | 2.32 | 34.0 | No official GARP ≥ 60 yet. Not auto-promoted after a crash. |
| 16 | VRRM | Secondary 20 | Watch | 1.74 | -5.43 | -18.31 | 2.59 | 11.1 | No official GARP ≥ 60 yet. Not auto-promoted after a crash. |
| 17 | VFF | Secondary 20 | Watch | 2.31 | -4.54 | -18.66 | 2.65 | 39.9 | No official GARP ≥ 60 yet. Not auto-promoted after a crash. |
| 18 | UWMC | Secondary 20 | Watch | 1.19 | -5.56 | -19.59 | 1.41 | 26.0 | No official GARP ≥ 60 yet. Not auto-promoted after a crash. |
| 19 | AREC | Secondary 20 | Watch | 0.90 | -12.62 | -23.08 | 1.09 | 35.4 | No official GARP ≥ 60 yet. Not auto-promoted after a crash. |
| 20 | TYGO | Secondary 20 | Watch | 0.56 | -6.66 | -26.18 | 0.83 | 24.2 | No official GARP ≥ 60 yet. Not auto-promoted after a crash. |

Prices: Yahoo Finance daily bars, 2026-11-16 America/Phoenix. SMA20 and RSI14 from the last 3 months of daily closes. Do not use Equibles for this routine price check.


## Rules

- Ranked Buy → Sell → Hold → Watch → Avoid. Max one Buy (paper) per morning.
- Mega-cap core (NVDA / MSFT / GOOGL / AAPL) is display-only in the digest top section — never the morning paper Buy.
- `Avoid` never becomes a buy because it bounced. `Sell` only if you already hold that avoid-quality name.
- `Watch` is not auto-promoted after a crash.
- This job never calls wsli and never sets TRADE_APPROVED.
