# Secondary penny watchlist scan — 2026-11-27

> I am an AI research assistant, not a licensed financial advisor. This is educational information, not personalized financial advice. Consider a qualified advisor for your situation.

**Paper trading active — dry-run only. Buy lines are paper recommendations, never live Wealthsimple orders.**

## What to buy today (from 20 names)

NONE — no buy today.

Official Rebalance-MCP GARP scores are not computed in this job. Quality flags come from `portfolio/penny-secondary-watchlist.yaml`. A live ticket still needs GARP ≥ 60.

| Rank | Ticker | List | Rec | Close | 1d % | 5d % | SMA20 | RSI14 | Why |
|-----:|--------|------|-----|------:|-----:|-----:|------:|------:|-----|
| 1 | CYH | Secondary 20 | Watch | 1.86 | +2.76 | +15.53 | 2.05 | 36.0 | No official GARP ≥ 60 yet. Not auto-promoted after a crash. |
| 2 | VFF | Secondary 20 | Watch | 2.37 | +8.22 | +13.94 | 2.47 | 29.9 | No official GARP ≥ 60 yet. Not auto-promoted after a crash. |
| 3 | TBLA | Secondary 20 | Watch | 2.01 | +2.03 | +8.65 | 2.28 | 50.5 | No official GARP ≥ 60 yet. Not auto-promoted after a crash. |
| 4 | UWMC | Secondary 20 | Watch | 1.18 | -2.48 | +8.26 | 1.33 | 21.7 | No official GARP ≥ 60 yet. Not auto-promoted after a crash. |
| 5 | GORO | Secondary 20 | Watch | 3.04 | +5.19 | +6.29 | 3.12 | 46.8 | No official GARP ≥ 60 yet. Not auto-promoted after a crash. |
| 6 | ARKO | Secondary 20 | Watch | 3.41 | +0.89 | +6.23 | 3.79 | 34.4 | No official GARP ≥ 60 yet. Not auto-promoted after a crash. |
| 7 | AREC | Secondary 20 | Watch | 0.94 | +26.27 | +5.77 | 1.00 | 43.5 | No official GARP ≥ 60 yet. Not auto-promoted after a crash. |
| 8 | NAGE | Secondary 20 | Watch | 1.98 | +3.40 | +5.62 | 2.10 | 46.1 | No official GARP ≥ 60 yet. Not auto-promoted after a crash. |
| 9 | ABUS | Secondary 20 | Watch | 4.25 | +1.68 | +4.42 | 4.01 | 80.4 | No official GARP ≥ 60 yet. Not auto-promoted after a crash. |
| 10 | SPRO | Secondary 20 | Watch | 0.84 | -0.14 | +2.03 | 0.95 | 30.9 | No official GARP ≥ 60 yet. Not auto-promoted after a crash. |
| 11 | VRRM | Secondary 20 | Watch | 1.72 | -2.83 | +1.77 | 2.02 | 24.7 | No official GARP ≥ 60 yet. Not auto-promoted after a crash. |
| 12 | HLLY | Secondary 20 | Watch | 2.52 | +5.00 | +1.61 | 2.49 | 63.5 | No official GARP ≥ 60 yet. Not auto-promoted after a crash. |
| 13 | MDXG | Secondary 20 | Watch | 3.16 | +0.32 | +1.61 | 3.24 | 34.7 | No official GARP ≥ 60 yet. Not auto-promoted after a crash. |
| 14 | SABR | Secondary 20 | Watch | 1.78 | +4.71 | +0.00 | 1.73 | 54.8 | No official GARP ≥ 60 yet. Not auto-promoted after a crash. |
| 15 | AISP | Secondary 20 | Watch | 1.50 | +5.63 | -1.96 | 1.68 | 30.1 | No official GARP ≥ 60 yet. Not auto-promoted after a crash. |
| 16 | ALTO | Secondary 20 | Watch | 3.00 | -0.99 | -2.60 | 3.48 | 24.3 | No official GARP ≥ 60 yet. Not auto-promoted after a crash. |
| 17 | SITC | Secondary 20 | Watch | 0.62 | -3.94 | -8.69 | 1.42 | 43.9 | No official GARP ≥ 60 yet. Not auto-promoted after a crash. |
| 18 | TYGO | Secondary 20 | Watch | 0.51 | +11.52 | -10.78 | 0.66 | 23.1 | No official GARP ≥ 60 yet. Not auto-promoted after a crash. |
| 19 | AMPY | Secondary 20 | Watch | 3.53 | +2.32 | -11.97 | 3.70 | 55.2 | No official GARP ≥ 60 yet. Not auto-promoted after a crash. |
| 20 | GDRX | Secondary 20 | Watch | 2.40 | +0.84 | -20.53 | 3.31 | 21.8 | No official GARP ≥ 60 yet. Not auto-promoted after a crash. |

Prices: Yahoo Finance daily bars, 2026-11-27 America/Phoenix. SMA20 and RSI14 from the last 3 months of daily closes. Do not use Equibles for this routine price check.


## Rules

- Ranked Buy → Sell → Hold → Watch → Avoid. Max one Buy (paper) per morning.
- Mega-cap core (NVDA / MSFT / GOOGL / AAPL) is display-only in the digest top section — never the morning paper Buy.
- `Avoid` never becomes a buy because it bounced. `Sell` only if you already hold that avoid-quality name.
- `Watch` is not auto-promoted after a crash.
- This job never calls wsli and never sets TRADE_APPROVED.
