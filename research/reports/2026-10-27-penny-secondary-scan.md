# Secondary penny watchlist scan — 2026-10-27

> I am an AI research assistant, not a licensed financial advisor. This is educational information, not personalized financial advice. Consider a qualified advisor for your situation.

**Paper trading active — dry-run only. Buy lines are paper recommendations, never live Wealthsimple orders.**

## What to buy today (from 20 names)

NONE — no buy today.

Official Rebalance-MCP GARP scores are not computed in this job. Quality flags come from `portfolio/penny-secondary-watchlist.yaml`. A live ticket still needs GARP ≥ 60.

| Rank | Ticker | List | Rec | Close | 1d % | 5d % | SMA20 | RSI14 | Why |
|-----:|--------|------|-----|------:|-----:|-----:|------:|------:|-----|
| 1 | UWMC | Secondary 20 | Watch | 1.62 | +14.89 | +47.27 | 1.18 | 73.8 | No official GARP ≥ 60 yet. Not auto-promoted after a crash. |
| 2 | TYGO | Secondary 20 | Watch | 0.96 | +2.06 | +12.79 | 0.89 | 54.7 | No official GARP ≥ 60 yet. Not auto-promoted after a crash. |
| 3 | AREC | Secondary 20 | Watch | 1.17 | +7.34 | +6.36 | 1.40 | 18.9 | No official GARP ≥ 60 yet. Not auto-promoted after a crash. |
| 4 | VRRM | Secondary 20 | Watch | 3.17 | +2.43 | +5.15 | 2.96 | 63.5 | No official GARP ≥ 60 yet. Not auto-promoted after a crash. |
| 5 | AISP | Secondary 20 | Watch | 2.27 | +4.86 | +4.86 | 2.17 | 54.8 | No official GARP ≥ 60 yet. Not auto-promoted after a crash. |
| 6 | SITC | Secondary 20 | Watch | 3.77 | +1.34 | +3.57 | 3.38 | 81.4 | No official GARP ≥ 60 yet. Not auto-promoted after a crash. |
| 7 | ALTO | Secondary 20 | Watch | 3.66 | -0.08 | +2.73 | 3.66 | 50.5 | No official GARP ≥ 60 yet. Not auto-promoted after a crash. |
| 8 | SABR | Secondary 20 | Watch | 1.60 | -2.13 | +2.23 | 1.78 | 26.4 | No official GARP ≥ 60 yet. Not auto-promoted after a crash. |
| 9 | HLLY | Secondary 20 | Watch | 2.56 | +0.20 | +1.79 | 2.46 | 61.3 | No official GARP ≥ 60 yet. Not auto-promoted after a crash. |
| 10 | NAGE | Secondary 20 | Watch | 2.50 | +2.66 | -0.20 | 2.60 | 33.8 | No official GARP ≥ 60 yet. Not auto-promoted after a crash. |
| 11 | ABUS | Secondary 20 | Watch | 4.29 | +2.02 | -1.04 | 4.31 | 49.7 | No official GARP ≥ 60 yet. Not auto-promoted after a crash. |
| 12 | TBLA | Secondary 20 | Watch | 3.40 | +0.74 | -1.30 | 3.40 | 57.2 | No official GARP ≥ 60 yet. Not auto-promoted after a crash. |
| 13 | CYH | Secondary 20 | Watch | 2.78 | -5.44 | -2.46 | 2.84 | 53.3 | No official GARP ≥ 60 yet. Not auto-promoted after a crash. |
| 14 | GDRX | Secondary 20 | Watch | 3.43 | -3.65 | -2.56 | 3.41 | 58.3 | No official GARP ≥ 60 yet. Not auto-promoted after a crash. |
| 15 | VFF | Secondary 20 | Watch | 2.59 | +1.97 | -2.63 | 2.67 | 44.0 | No official GARP ≥ 60 yet. Not auto-promoted after a crash. |
| 16 | AMPY | Secondary 20 | Watch | 4.29 | -3.48 | -4.77 | 4.44 | 44.1 | No official GARP ≥ 60 yet. Not auto-promoted after a crash. |
| 17 | ARKO | Secondary 20 | Watch | 3.77 | -1.82 | -6.45 | 4.07 | 26.3 | No official GARP ≥ 60 yet. Not auto-promoted after a crash. |
| 18 | GORO | Secondary 20 | Watch | 3.15 | +0.96 | -7.62 | 3.30 | 44.5 | No official GARP ≥ 60 yet. Not auto-promoted after a crash. |
| 19 | MDXG | Secondary 20 | Watch | 3.87 | +0.52 | -8.51 | 4.41 | 27.2 | No official GARP ≥ 60 yet. Not auto-promoted after a crash. |
| 20 | SPRO | Secondary 20 | Watch | 1.11 | +3.74 | -9.02 | 1.16 | 44.2 | No official GARP ≥ 60 yet. Not auto-promoted after a crash. |

Prices: Yahoo Finance daily bars, 2026-10-27 America/Phoenix. SMA20 and RSI14 from the last 3 months of daily closes. Do not use Equibles for this routine price check.


## Rules

- Ranked Buy → Sell → Hold → Watch → Avoid. Max one Buy (paper) per morning.
- Mega-cap core (NVDA / MSFT / GOOGL / AAPL) is display-only in the digest top section — never the morning paper Buy.
- `Avoid` never becomes a buy because it bounced. `Sell` only if you already hold that avoid-quality name.
- `Watch` is not auto-promoted after a crash.
- This job never calls wsli and never sets TRADE_APPROVED.
