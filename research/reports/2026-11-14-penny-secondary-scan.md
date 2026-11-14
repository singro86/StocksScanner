# Secondary penny watchlist scan — 2026-11-14

> I am an AI research assistant, not a licensed financial advisor. This is educational information, not personalized financial advice. Consider a qualified advisor for your situation.

**Paper trading active — dry-run only. Buy lines are paper recommendations, never live Wealthsimple orders.**

## What to buy today (from 20 names)

NONE — no buy today.

Official Rebalance-MCP GARP scores are not computed in this job. Quality flags come from `portfolio/penny-secondary-watchlist.yaml`. A live ticket still needs GARP ≥ 60.

| Rank | Ticker | List | Rec | Close | 1d % | 5d % | SMA20 | RSI14 | Why |
|-----:|--------|------|-----|------:|-----:|-----:|------:|------:|-----|
| 1 | AMPY | Secondary 20 | Watch | 4.07 | +1.24 | +22.22 | 4.03 | 42.6 | No official GARP ≥ 60 yet. Not auto-promoted after a crash. |
| 2 | HLLY | Secondary 20 | Watch | 2.48 | +5.08 | +18.09 | 2.54 | 48.2 | No official GARP ≥ 60 yet. Not auto-promoted after a crash. |
| 3 | ABUS | Secondary 20 | Watch | 4.09 | +1.49 | +11.75 | 4.06 | 46.5 | No official GARP ≥ 60 yet. Not auto-promoted after a crash. |
| 4 | TBLA | Secondary 20 | Watch | 2.23 | +4.70 | +11.50 | 2.94 | 23.3 | No official GARP ≥ 60 yet. Not auto-promoted after a crash. |
| 5 | SABR | Secondary 20 | Watch | 1.86 | -2.10 | +10.39 | 1.68 | 65.7 | No official GARP ≥ 60 yet. Not auto-promoted after a crash. |
| 6 | GORO | Secondary 20 | Watch | 3.22 | -1.83 | +2.22 | 3.24 | 53.0 | No official GARP ≥ 60 yet. Not auto-promoted after a crash. |
| 7 | GDRX | Secondary 20 | Watch | 3.56 | +1.43 | +1.43 | 3.54 | 50.0 | No official GARP ≥ 60 yet. Not auto-promoted after a crash. |
| 8 | CYH | Secondary 20 | Watch | 2.24 | +1.36 | +1.36 | 2.48 | 30.1 | No official GARP ≥ 60 yet. Not auto-promoted after a crash. |
| 9 | ARKO | Secondary 20 | Watch | 4.00 | -2.44 | +0.76 | 3.96 | 56.0 | No official GARP ≥ 60 yet. Not auto-promoted after a crash. |
| 10 | NAGE | Secondary 20 | Watch | 2.07 | -3.27 | +0.00 | 2.35 | 37.9 | No official GARP ≥ 60 yet. Not auto-promoted after a crash. |
| 11 | SITC | Secondary 20 | Watch | 0.66 | -5.36 | -1.62 | 2.79 | 5.2 | No official GARP ≥ 60 yet. Not auto-promoted after a crash. |
| 12 | ALTO | Secondary 20 | Watch | 3.66 | -1.35 | -2.14 | 3.65 | 50.0 | No official GARP ≥ 60 yet. Not auto-promoted after a crash. |
| 13 | SPRO | Secondary 20 | Watch | 1.00 | +0.00 | -2.91 | 1.08 | 42.2 | No official GARP ≥ 60 yet. Not auto-promoted after a crash. |
| 14 | MDXG | Secondary 20 | Watch | 3.21 | -0.93 | -3.02 | 3.63 | 23.8 | No official GARP ≥ 60 yet. Not auto-promoted after a crash. |
| 15 | AREC | Secondary 20 | Watch | 1.03 | +0.00 | -5.50 | 1.11 | 46.6 | No official GARP ≥ 60 yet. Not auto-promoted after a crash. |
| 16 | AISP | Secondary 20 | Watch | 1.60 | -4.19 | -10.62 | 1.98 | 22.0 | No official GARP ≥ 60 yet. Not auto-promoted after a crash. |
| 17 | VFF | Secondary 20 | Watch | 2.42 | -4.72 | -15.97 | 2.66 | 45.5 | No official GARP ≥ 60 yet. Not auto-promoted after a crash. |
| 18 | VRRM | Secondary 20 | Watch | 1.84 | -6.12 | -15.98 | 2.64 | 14.3 | No official GARP ≥ 60 yet. Not auto-promoted after a crash. |
| 19 | UWMC | Secondary 20 | Watch | 1.26 | -0.79 | -17.11 | 1.41 | 41.2 | No official GARP ≥ 60 yet. Not auto-promoted after a crash. |
| 20 | TYGO | Secondary 20 | Watch | 0.60 | -5.50 | -18.23 | 0.84 | 27.5 | No official GARP ≥ 60 yet. Not auto-promoted after a crash. |

Prices: Yahoo Finance daily bars, 2026-11-14 America/Phoenix. SMA20 and RSI14 from the last 3 months of daily closes. Do not use Equibles for this routine price check.


## Rules

- Ranked Buy → Sell → Hold → Watch → Avoid. Max one Buy (paper) per morning.
- Mega-cap core (NVDA / MSFT / GOOGL / AAPL) is display-only in the digest top section — never the morning paper Buy.
- `Avoid` never becomes a buy because it bounced. `Sell` only if you already hold that avoid-quality name.
- `Watch` is not auto-promoted after a crash.
- This job never calls wsli and never sets TRADE_APPROVED.
