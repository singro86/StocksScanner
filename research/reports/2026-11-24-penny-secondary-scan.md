# Secondary penny watchlist scan — 2026-11-24

> I am an AI research assistant, not a licensed financial advisor. This is educational information, not personalized financial advice. Consider a qualified advisor for your situation.

**Paper trading active — dry-run only. Buy lines are paper recommendations, never live Wealthsimple orders.**

## What to buy today (from 20 names)

NONE — no buy today.

Official Rebalance-MCP GARP scores are not computed in this job. Quality flags come from `portfolio/penny-secondary-watchlist.yaml`. A live ticket still needs GARP ≥ 60.

| Rank | Ticker | List | Rec | Close | 1d % | 5d % | SMA20 | RSI14 | Why |
|-----:|--------|------|-----|------:|-----:|-----:|------:|------:|-----|
| 1 | AREC | Secondary 20 | Watch | 1.07 | +2.88 | +27.38 | 1.04 | 54.5 | No official GARP ≥ 60 yet. Not auto-promoted after a crash. |
| 2 | ABUS | Secondary 20 | Watch | 4.23 | +1.20 | +4.44 | 4.02 | 56.8 | No official GARP ≥ 60 yet. Not auto-promoted after a crash. |
| 3 | VRRM | Secondary 20 | Watch | 1.72 | +2.99 | +3.61 | 2.17 | 16.1 | No official GARP ≥ 60 yet. Not auto-promoted after a crash. |
| 4 | NAGE | Secondary 20 | Watch | 2.05 | +7.33 | +0.49 | 2.16 | 33.8 | No official GARP ≥ 60 yet. Not auto-promoted after a crash. |
| 5 | SITC | Secondary 20 | Watch | 0.68 | -6.44 | +0.28 | 1.74 | 4.7 | No official GARP ≥ 60 yet. Not auto-promoted after a crash. |
| 6 | SABR | Secondary 20 | Watch | 1.67 | -3.47 | -0.59 | 1.72 | 46.3 | No official GARP ≥ 60 yet. Not auto-promoted after a crash. |
| 7 | UWMC | Secondary 20 | Watch | 1.15 | +2.68 | -0.86 | 1.36 | 10.3 | No official GARP ≥ 60 yet. Not auto-promoted after a crash. |
| 8 | MDXG | Secondary 20 | Watch | 3.12 | +1.30 | -1.89 | 3.32 | 42.9 | No official GARP ≥ 60 yet. Not auto-promoted after a crash. |
| 9 | HLLY | Secondary 20 | Watch | 2.39 | -3.24 | -2.85 | 2.51 | 38.6 | No official GARP ≥ 60 yet. Not auto-promoted after a crash. |
| 10 | TBLA | Secondary 20 | Watch | 1.97 | +3.68 | -3.90 | 2.43 | 27.8 | No official GARP ≥ 60 yet. Not auto-promoted after a crash. |
| 11 | GORO | Secondary 20 | Watch | 3.04 | +4.11 | -5.30 | 3.15 | 48.6 | No official GARP ≥ 60 yet. Not auto-promoted after a crash. |
| 12 | VFF | Secondary 20 | Watch | 2.13 | +1.43 | -6.99 | 2.50 | 18.2 | No official GARP ≥ 60 yet. Not auto-promoted after a crash. |
| 13 | AMPY | Secondary 20 | Watch | 3.47 | -0.29 | -11.03 | 3.79 | 49.8 | No official GARP ≥ 60 yet. Not auto-promoted after a crash. |
| 14 | SPRO | Secondary 20 | Watch | 0.80 | +1.79 | -11.43 | 0.98 | 23.0 | No official GARP ≥ 60 yet. Not auto-promoted after a crash. |
| 15 | ALTO | Secondary 20 | Watch | 3.18 | -0.94 | -11.67 | 3.54 | 39.3 | No official GARP ≥ 60 yet. Not auto-promoted after a crash. |
| 16 | CYH | Secondary 20 | Watch | 1.77 | +7.27 | -12.38 | 2.12 | 27.1 | No official GARP ≥ 60 yet. Not auto-promoted after a crash. |
| 17 | AISP | Secondary 20 | Watch | 1.44 | -5.26 | -13.25 | 1.76 | 24.1 | No official GARP ≥ 60 yet. Not auto-promoted after a crash. |
| 18 | GDRX | Secondary 20 | Watch | 3.00 | -0.99 | -13.54 | 3.42 | 27.2 | No official GARP ≥ 60 yet. Not auto-promoted after a crash. |
| 19 | ARKO | Secondary 20 | Watch | 3.32 | -3.49 | -15.31 | 3.82 | 31.9 | No official GARP ≥ 60 yet. Not auto-promoted after a crash. |
| 20 | TYGO | Secondary 20 | Watch | 0.48 | -0.33 | -15.72 | 0.71 | 8.8 | No official GARP ≥ 60 yet. Not auto-promoted after a crash. |

Prices: Yahoo Finance daily bars, 2026-11-24 America/Phoenix. SMA20 and RSI14 from the last 3 months of daily closes. Do not use Equibles for this routine price check.


## Rules

- Ranked Buy → Sell → Hold → Watch → Avoid. Max one Buy (paper) per morning.
- Mega-cap core (NVDA / MSFT / GOOGL / AAPL) is display-only in the digest top section — never the morning paper Buy.
- `Avoid` never becomes a buy because it bounced. `Sell` only if you already hold that avoid-quality name.
- `Watch` is not auto-promoted after a crash.
- This job never calls wsli and never sets TRADE_APPROVED.
