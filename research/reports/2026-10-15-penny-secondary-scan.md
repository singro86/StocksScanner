# Secondary penny watchlist scan — 2026-10-15

> I am an AI research assistant, not a licensed financial advisor. This is educational information, not personalized financial advice. Consider a qualified advisor for your situation.

**Paper trading active — dry-run only. Buy lines are paper recommendations, never live Wealthsimple orders.**

## What to buy today (from 20 names)

NONE — no buy today.

Official Rebalance-MCP GARP scores are not computed in this job. Quality flags come from `portfolio/penny-secondary-watchlist.yaml`. A live ticket still needs GARP ≥ 60.

| Rank | Ticker | List | Rec | Close | 1d % | 5d % | SMA20 | RSI14 | Why |
|-----:|--------|------|-----|------:|-----:|-----:|------:|------:|-----|
| 1 | CYH | Secondary 20 | Watch | 2.96 | -0.67 | +8.43 | 2.87 | 51.6 | No official GARP ≥ 60 yet. Not auto-promoted after a crash. |
| 2 | HLLY | Secondary 20 | Watch | 2.58 | +4.23 | +5.94 | 2.45 | 57.6 | No official GARP ≥ 60 yet. Not auto-promoted after a crash. |
| 3 | VRRM | Secondary 20 | Watch | 3.00 | +2.21 | +2.91 | 3.08 | 39.6 | No official GARP ≥ 60 yet. Not auto-promoted after a crash. |
| 4 | ABUS | Secondary 20 | Watch | 4.29 | +2.27 | +2.51 | 4.58 | 32.7 | No official GARP ≥ 60 yet. Not auto-promoted after a crash. |
| 5 | GDRX | Secondary 20 | Watch | 3.42 | +1.33 | +1.94 | 3.35 | 54.8 | No official GARP ≥ 60 yet. Not auto-promoted after a crash. |
| 6 | GORO | Secondary 20 | Watch | 3.24 | +0.62 | +1.57 | 3.37 | 38.8 | No official GARP ≥ 60 yet. Not auto-promoted after a crash. |
| 7 | MDXG | Secondary 20 | Watch | 4.67 | -0.74 | +0.97 | 4.69 | 49.6 | No official GARP ≥ 60 yet. Not auto-promoted after a crash. |
| 8 | UWMC | Secondary 20 | Watch | 1.10 | +8.91 | +0.92 | 1.18 | 40.0 | No official GARP ≥ 60 yet. Not auto-promoted after a crash. |
| 9 | TBLA | Secondary 20 | Watch | 3.50 | +2.48 | -0.14 | 3.42 | 51.4 | No official GARP ≥ 60 yet. Not auto-promoted after a crash. |
| 10 | ARKO | Secondary 20 | Watch | 4.09 | +1.36 | -0.61 | 4.18 | 36.3 | No official GARP ≥ 60 yet. Not auto-promoted after a crash. |
| 11 | SPRO | Secondary 20 | Watch | 1.13 | +0.89 | -0.88 | 1.19 | 38.6 | No official GARP ≥ 60 yet. Not auto-promoted after a crash. |
| 12 | ALTO | Secondary 20 | Watch | 3.62 | -2.30 | -3.08 | 3.74 | 43.1 | No official GARP ≥ 60 yet. Not auto-promoted after a crash. |
| 13 | NAGE | Secondary 20 | Watch | 2.56 | +1.38 | -3.57 | 2.81 | 23.5 | No official GARP ≥ 60 yet. Not auto-promoted after a crash. |
| 14 | VFF | Secondary 20 | Watch | 2.58 | +0.78 | -4.44 | 2.84 | 14.9 | No official GARP ≥ 60 yet. Not auto-promoted after a crash. |
| 15 | AMPY | Secondary 20 | Watch | 4.33 | -0.12 | -5.35 | 4.37 | 52.3 | No official GARP ≥ 60 yet. Not auto-promoted after a crash. |
| 16 | SITC | Secondary 20 | Watch | 2.99 | -0.99 | -5.68 | 3.13 | 46.5 | No official GARP ≥ 60 yet. Not auto-promoted after a crash. |
| 17 | TYGO | Secondary 20 | Watch | 0.84 | -4.45 | -6.48 | 0.89 | 46.9 | No official GARP ≥ 60 yet. Not auto-promoted after a crash. |
| 18 | SABR | Secondary 20 | Watch | 1.79 | +0.84 | -7.00 | 2.03 | 12.6 | No official GARP ≥ 60 yet. Not auto-promoted after a crash. |
| 19 | AISP | Secondary 20 | Watch | 2.07 | -1.29 | -9.48 | 2.06 | 58.6 | No official GARP ≥ 60 yet. Not auto-promoted after a crash. |
| 20 | AREC | Secondary 20 | Watch | 1.19 | -2.26 | -27.73 | 1.71 | 3.9 | No official GARP ≥ 60 yet. Not auto-promoted after a crash. |

Prices: Yahoo Finance daily bars, 2026-10-15 America/Phoenix. SMA20 and RSI14 from the last 3 months of daily closes. Do not use Equibles for this routine price check.


## Rules

- Ranked Buy → Sell → Hold → Watch → Avoid. Max one Buy (paper) per morning.
- Mega-cap core (NVDA / MSFT / GOOGL / AAPL) is display-only in the digest top section — never the morning paper Buy.
- `Avoid` never becomes a buy because it bounced. `Sell` only if you already hold that avoid-quality name.
- `Watch` is not auto-promoted after a crash.
- This job never calls wsli and never sets TRADE_APPROVED.
