# Secondary penny watchlist scan — 2026-10-16

> I am an AI research assistant, not a licensed financial advisor. This is educational information, not personalized financial advice. Consider a qualified advisor for your situation.

**Paper trading active — dry-run only. Buy lines are paper recommendations, never live Wealthsimple orders.**

## What to buy today (from 20 names)

NONE — no buy today.

Official Rebalance-MCP GARP scores are not computed in this job. Quality flags come from `portfolio/penny-secondary-watchlist.yaml`. A live ticket still needs GARP ≥ 60.

| Rank | Ticker | List | Rec | Close | 1d % | 5d % | SMA20 | RSI14 | Why |
|-----:|--------|------|-----|------:|-----:|-----:|------:|------:|-----|
| 1 | SITC | Secondary 20 | Watch | 3.46 | +14.78 | +11.45 | 3.15 | 64.4 | No official GARP ≥ 60 yet. Not auto-promoted after a crash. |
| 2 | CYH | Secondary 20 | Watch | 2.92 | -2.51 | +5.62 | 2.87 | 51.9 | No official GARP ≥ 60 yet. Not auto-promoted after a crash. |
| 3 | HLLY | Secondary 20 | Watch | 2.60 | -0.43 | +4.37 | 2.45 | 62.1 | No official GARP ≥ 60 yet. Not auto-promoted after a crash. |
| 4 | ABUS | Secondary 20 | Watch | 4.24 | -1.17 | +0.47 | 4.54 | 31.6 | No official GARP ≥ 60 yet. Not auto-promoted after a crash. |
| 5 | TBLA | Secondary 20 | Watch | 3.46 | -2.12 | +0.43 | 3.41 | 53.4 | No official GARP ≥ 60 yet. Not auto-promoted after a crash. |
| 6 | ARKO | Secondary 20 | Watch | 4.12 | +0.12 | +0.12 | 4.17 | 39.3 | No official GARP ≥ 60 yet. Not auto-promoted after a crash. |
| 7 | GORO | Secondary 20 | Watch | 3.40 | +2.25 | -0.15 | 3.36 | 51.9 | No official GARP ≥ 60 yet. Not auto-promoted after a crash. |
| 8 | AMPY | Secondary 20 | Watch | 4.45 | +2.30 | -0.22 | 4.37 | 60.8 | No official GARP ≥ 60 yet. Not auto-promoted after a crash. |
| 9 | VRRM | Secondary 20 | Watch | 2.92 | -0.85 | -0.85 | 3.05 | 45.5 | No official GARP ≥ 60 yet. Not auto-promoted after a crash. |
| 10 | UWMC | Secondary 20 | Watch | 1.07 | -6.95 | -0.92 | 1.17 | 37.1 | No official GARP ≥ 60 yet. Not auto-promoted after a crash. |
| 11 | GDRX | Secondary 20 | Watch | 3.39 | -3.28 | -1.17 | 3.36 | 54.3 | No official GARP ≥ 60 yet. Not auto-promoted after a crash. |
| 12 | MDXG | Secondary 20 | Watch | 4.49 | -4.14 | -3.94 | 4.68 | 37.8 | No official GARP ≥ 60 yet. Not auto-promoted after a crash. |
| 13 | VFF | Secondary 20 | Watch | 2.55 | -1.92 | -4.85 | 2.83 | 16.5 | No official GARP ≥ 60 yet. Not auto-promoted after a crash. |
| 14 | ALTO | Secondary 20 | Watch | 3.51 | -4.10 | -5.90 | 3.72 | 40.9 | No official GARP ≥ 60 yet. Not auto-promoted after a crash. |
| 15 | NAGE | Secondary 20 | Watch | 2.50 | -2.91 | -6.88 | 2.79 | 24.6 | No official GARP ≥ 60 yet. Not auto-promoted after a crash. |
| 16 | SPRO | Secondary 20 | Watch | 1.11 | -1.59 | -7.33 | 1.19 | 40.7 | No official GARP ≥ 60 yet. Not auto-promoted after a crash. |
| 17 | TYGO | Secondary 20 | Watch | 0.82 | -1.89 | -7.74 | 0.89 | 50.0 | No official GARP ≥ 60 yet. Not auto-promoted after a crash. |
| 18 | SABR | Secondary 20 | Watch | 1.70 | -5.31 | -10.79 | 2.00 | 11.4 | No official GARP ≥ 60 yet. Not auto-promoted after a crash. |
| 19 | AISP | Secondary 20 | Watch | 2.00 | -4.98 | -17.15 | 2.06 | 56.7 | No official GARP ≥ 60 yet. Not auto-promoted after a crash. |
| 20 | AREC | Secondary 20 | Watch | 1.14 | -5.00 | -28.30 | 1.67 | 4.0 | No official GARP ≥ 60 yet. Not auto-promoted after a crash. |

Prices: Yahoo Finance daily bars, 2026-10-16 America/Phoenix. SMA20 and RSI14 from the last 3 months of daily closes. Do not use Equibles for this routine price check.


## Rules

- Ranked Buy → Sell → Hold → Watch → Avoid. Max one Buy (paper) per morning.
- Mega-cap core (NVDA / MSFT / GOOGL / AAPL) is display-only in the digest top section — never the morning paper Buy.
- `Avoid` never becomes a buy because it bounced. `Sell` only if you already hold that avoid-quality name.
- `Watch` is not auto-promoted after a crash.
- This job never calls wsli and never sets TRADE_APPROVED.
