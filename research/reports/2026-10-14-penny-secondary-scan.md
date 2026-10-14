# Secondary penny watchlist scan — 2026-10-14

> I am an AI research assistant, not a licensed financial advisor. This is educational information, not personalized financial advice. Consider a qualified advisor for your situation.

**Paper trading active — dry-run only. Buy lines are paper recommendations, never live Wealthsimple orders.**

## What to buy today (from 20 names)

NONE — no buy today.

Official Rebalance-MCP GARP scores are not computed in this job. Quality flags come from `portfolio/penny-secondary-watchlist.yaml`. A live ticket still needs GARP ≥ 60.

| Rank | Ticker | List | Rec | Close | 1d % | 5d % | SMA20 | RSI14 | Why |
|-----:|--------|------|-----|------:|-----:|-----:|------:|------:|-----|
| 1 | CYH | Secondary 20 | Watch | 2.99 | +0.00 | +9.93 | 2.86 | 58.2 | No official GARP ≥ 60 yet. Not auto-promoted after a crash. |
| 2 | HLLY | Secondary 20 | Watch | 2.52 | -0.71 | +6.86 | 2.46 | 57.1 | No official GARP ≥ 60 yet. Not auto-promoted after a crash. |
| 3 | GDRX | Secondary 20 | Watch | 3.40 | -1.59 | +4.46 | 3.35 | 52.4 | No official GARP ≥ 60 yet. Not auto-promoted after a crash. |
| 4 | TBLA | Secondary 20 | Watch | 3.38 | -2.35 | +2.70 | 3.43 | 46.1 | No official GARP ≥ 60 yet. Not auto-promoted after a crash. |
| 5 | ALTO | Secondary 20 | Watch | 3.71 | -1.46 | +1.78 | 3.76 | 48.3 | No official GARP ≥ 60 yet. Not auto-promoted after a crash. |
| 6 | MDXG | Secondary 20 | Watch | 4.67 | -0.32 | +1.41 | 4.69 | 47.2 | No official GARP ≥ 60 yet. Not auto-promoted after a crash. |
| 7 | AMPY | Secondary 20 | Watch | 4.43 | -3.80 | -0.56 | 4.39 | 54.1 | No official GARP ≥ 60 yet. Not auto-promoted after a crash. |
| 8 | SPRO | Secondary 20 | Watch | 1.16 | +0.43 | -1.28 | 1.19 | 38.8 | No official GARP ≥ 60 yet. Not auto-promoted after a crash. |
| 9 | ABUS | Secondary 20 | Watch | 4.21 | +2.31 | -1.98 | 4.62 | 28.7 | No official GARP ≥ 60 yet. Not auto-promoted after a crash. |
| 10 | VRRM | Secondary 20 | Watch | 2.85 | -5.48 | -2.57 | 3.09 | 32.6 | No official GARP ≥ 60 yet. Not auto-promoted after a crash. |
| 11 | TYGO | Secondary 20 | Watch | 0.88 | -5.66 | -3.17 | 0.90 | 50.0 | No official GARP ≥ 60 yet. Not auto-promoted after a crash. |
| 12 | AISP | Secondary 20 | Watch | 2.07 | -7.59 | -3.27 | 2.05 | 55.8 | No official GARP ≥ 60 yet. Not auto-promoted after a crash. |
| 13 | GORO | Secondary 20 | Watch | 3.17 | -6.08 | -3.51 | 3.38 | 35.4 | No official GARP ≥ 60 yet. Not auto-promoted after a crash. |
| 14 | VFF | Secondary 20 | Watch | 2.59 | -1.89 | -3.54 | 2.86 | 18.4 | No official GARP ≥ 60 yet. Not auto-promoted after a crash. |
| 15 | SITC | Secondary 20 | Watch | 3.02 | -1.47 | -4.59 | 3.12 | 49.8 | No official GARP ≥ 60 yet. Not auto-promoted after a crash. |
| 16 | ARKO | Secondary 20 | Watch | 4.00 | -2.32 | -5.32 | 4.19 | 34.0 | No official GARP ≥ 60 yet. Not auto-promoted after a crash. |
| 17 | NAGE | Secondary 20 | Watch | 2.54 | -1.74 | -6.80 | 2.83 | 24.0 | No official GARP ≥ 60 yet. Not auto-promoted after a crash. |
| 18 | SABR | Secondary 20 | Watch | 1.77 | -2.21 | -7.33 | 2.06 | 8.6 | No official GARP ≥ 60 yet. Not auto-promoted after a crash. |
| 19 | UWMC | Secondary 20 | Watch | 1.00 | -2.91 | -11.50 | 1.18 | 28.9 | No official GARP ≥ 60 yet. Not auto-promoted after a crash. |
| 20 | AREC | Secondary 20 | Watch | 1.19 | -10.57 | -27.30 | 1.75 | 6.3 | No official GARP ≥ 60 yet. Not auto-promoted after a crash. |

Prices: Yahoo Finance daily bars, 2026-10-14 America/Phoenix. SMA20 and RSI14 from the last 3 months of daily closes. Do not use Equibles for this routine price check.


## Rules

- Ranked Buy → Sell → Hold → Watch → Avoid. Max one Buy (paper) per morning.
- Mega-cap core (NVDA / MSFT / GOOGL / AAPL) is display-only in the digest top section — never the morning paper Buy.
- `Avoid` never becomes a buy because it bounced. `Sell` only if you already hold that avoid-quality name.
- `Watch` is not auto-promoted after a crash.
- This job never calls wsli and never sets TRADE_APPROVED.
