# Secondary penny watchlist scan — 2026-11-06

> I am an AI research assistant, not a licensed financial advisor. This is educational information, not personalized financial advice. Consider a qualified advisor for your situation.

**Paper trading active — dry-run only. Buy lines are paper recommendations, never live Wealthsimple orders.**

## What to buy today (from 20 names)

NONE — no buy today.

Official Rebalance-MCP GARP scores are not computed in this job. Quality flags come from `portfolio/penny-secondary-watchlist.yaml`. A live ticket still needs GARP ≥ 60.

| Rank | Ticker | List | Rec | Close | 1d % | 5d % | SMA20 | RSI14 | Why |
|-----:|--------|------|-----|------:|-----:|-----:|------:|------:|-----|
| 1 | VFF | Secondary 20 | Watch | 2.88 | +3.05 | +15.00 | 2.65 | 63.6 | No official GARP ≥ 60 yet. Not auto-promoted after a crash. |
| 2 | ARKO | Secondary 20 | Watch | 3.92 | +1.68 | +3.56 | 3.95 | 45.8 | No official GARP ≥ 60 yet. Not auto-promoted after a crash. |
| 3 | GORO | Secondary 20 | Watch | 3.23 | +2.71 | +2.06 | 3.24 | 44.4 | No official GARP ≥ 60 yet. Not auto-promoted after a crash. |
| 4 | ALTO | Secondary 20 | Watch | 3.69 | +0.68 | +1.23 | 3.62 | 63.8 | No official GARP ≥ 60 yet. Not auto-promoted after a crash. |
| 5 | UWMC | Secondary 20 | Watch | 1.57 | -3.68 | +0.00 | 1.34 | 76.3 | No official GARP ≥ 60 yet. Not auto-promoted after a crash. |
| 6 | SABR | Secondary 20 | Watch | 1.61 | -3.87 | -0.31 | 1.66 | 48.3 | No official GARP ≥ 60 yet. Not auto-promoted after a crash. |
| 7 | GDRX | Secondary 20 | Watch | 3.48 | -0.43 | -0.43 | 3.50 | 54.5 | No official GARP ≥ 60 yet. Not auto-promoted after a crash. |
| 8 | SPRO | Secondary 20 | Watch | 1.03 | +1.36 | -2.46 | 1.11 | 42.5 | No official GARP ≥ 60 yet. Not auto-promoted after a crash. |
| 9 | CYH | Secondary 20 | Watch | 2.15 | -5.48 | -10.21 | 2.66 | 32.0 | No official GARP ≥ 60 yet. Not auto-promoted after a crash. |
| 10 | NAGE | Secondary 20 | Watch | 2.07 | -1.70 | -10.98 | 2.45 | 32.6 | No official GARP ≥ 60 yet. Not auto-promoted after a crash. |
| 11 | AREC | Secondary 20 | Watch | 1.08 | +13.94 | -11.47 | 1.16 | 46.7 | No official GARP ≥ 60 yet. Not auto-promoted after a crash. |
| 12 | ABUS | Secondary 20 | Watch | 3.69 | +0.41 | -12.47 | 4.14 | 31.0 | No official GARP ≥ 60 yet. Not auto-promoted after a crash. |
| 13 | AISP | Secondary 20 | Watch | 1.80 | +3.45 | -13.46 | 2.11 | 41.1 | No official GARP ≥ 60 yet. Not auto-promoted after a crash. |
| 14 | MDXG | Secondary 20 | Watch | 3.33 | +1.52 | -14.18 | 3.97 | 22.8 | No official GARP ≥ 60 yet. Not auto-promoted after a crash. |
| 15 | TYGO | Secondary 20 | Watch | 0.75 | +3.56 | -15.32 | 0.89 | 45.5 | No official GARP ≥ 60 yet. Not auto-promoted after a crash. |
| 16 | HLLY | Secondary 20 | Watch | 2.13 | -0.23 | -18.82 | 2.54 | 39.0 | No official GARP ≥ 60 yet. Not auto-promoted after a crash. |
| 17 | AMPY | Secondary 20 | Watch | 3.38 | +6.13 | -20.96 | 4.21 | 21.2 | No official GARP ≥ 60 yet. Not auto-promoted after a crash. |
| 18 | VRRM | Secondary 20 | Watch | 2.21 | -4.74 | -21.07 | 2.88 | 34.0 | No official GARP ≥ 60 yet. Not auto-promoted after a crash. |
| 19 | TBLA | Secondary 20 | Watch | 2.02 | -7.14 | -41.85 | 3.27 | 9.1 | No official GARP ≥ 60 yet. Not auto-promoted after a crash. |
| 20 | SITC | Secondary 20 | Watch | 0.67 | -81.31 | -82.11 | 3.41 | 9.3 | No official GARP ≥ 60 yet. Not auto-promoted after a crash. |

Prices: Yahoo Finance daily bars, 2026-11-06 America/Phoenix. SMA20 and RSI14 from the last 3 months of daily closes. Do not use Equibles for this routine price check.


## Rules

- Ranked Buy → Sell → Hold → Watch → Avoid. Max one Buy (paper) per morning.
- Mega-cap core (NVDA / MSFT / GOOGL / AAPL) is display-only in the digest top section — never the morning paper Buy.
- `Avoid` never becomes a buy because it bounced. `Sell` only if you already hold that avoid-quality name.
- `Watch` is not auto-promoted after a crash.
- This job never calls wsli and never sets TRADE_APPROVED.
