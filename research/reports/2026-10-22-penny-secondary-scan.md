# Secondary penny watchlist scan — 2026-10-22

> I am an AI research assistant, not a licensed financial advisor. This is educational information, not personalized financial advice. Consider a qualified advisor for your situation.

**Paper trading active — dry-run only. Buy lines are paper recommendations, never live Wealthsimple orders.**

## What to buy today (from 20 names)

NONE — no buy today.

Official Rebalance-MCP GARP scores are not computed in this job. Quality flags come from `portfolio/penny-secondary-watchlist.yaml`. A live ticket still needs GARP ≥ 60.

| Rank | Ticker | List | Rec | Close | 1d % | 5d % | SMA20 | RSI14 | Why |
|-----:|--------|------|-----|------:|-----:|-----:|------:|------:|-----|
| 1 | SITC | Secondary 20 | Watch | 3.73 | +0.67 | +24.09 | 3.28 | 63.6 | No official GARP ≥ 60 yet. Not auto-promoted after a crash. |
| 2 | TYGO | Secondary 20 | Watch | 0.96 | +7.85 | +14.82 | 0.87 | 62.9 | No official GARP ≥ 60 yet. Not auto-promoted after a crash. |
| 3 | VRRM | Secondary 20 | Watch | 3.10 | +4.92 | +5.27 | 2.96 | 65.1 | No official GARP ≥ 60 yet. Not auto-promoted after a crash. |
| 4 | VFF | Secondary 20 | Watch | 2.71 | -1.64 | +4.04 | 2.76 | 42.2 | No official GARP ≥ 60 yet. Not auto-promoted after a crash. |
| 5 | GORO | Secondary 20 | Watch | 3.40 | -2.15 | +2.25 | 3.33 | 56.6 | No official GARP ≥ 60 yet. Not auto-promoted after a crash. |
| 6 | GDRX | Secondary 20 | Watch | 3.58 | +0.28 | +2.14 | 3.38 | 64.8 | No official GARP ≥ 60 yet. Not auto-promoted after a crash. |
| 7 | AMPY | Secondary 20 | Watch | 4.43 | -1.23 | +1.95 | 4.41 | 53.5 | No official GARP ≥ 60 yet. Not auto-promoted after a crash. |
| 8 | UWMC | Secondary 20 | Watch | 1.17 | +5.33 | +1.67 | 1.14 | 43.4 | No official GARP ≥ 60 yet. Not auto-promoted after a crash. |
| 9 | AISP | Secondary 20 | Watch | 2.13 | -6.77 | +1.19 | 2.11 | 50.5 | No official GARP ≥ 60 yet. Not auto-promoted after a crash. |
| 10 | SPRO | Secondary 20 | Watch | 1.14 | -2.99 | +0.44 | 1.17 | 44.4 | No official GARP ≥ 60 yet. Not auto-promoted after a crash. |
| 11 | ARKO | Secondary 20 | Watch | 4.06 | +1.75 | -1.22 | 4.13 | 41.3 | No official GARP ≥ 60 yet. Not auto-promoted after a crash. |
| 12 | ABUS | Secondary 20 | Watch | 4.22 | +1.08 | -1.51 | 4.40 | 42.0 | No official GARP ≥ 60 yet. Not auto-promoted after a crash. |
| 13 | ALTO | Secondary 20 | Watch | 3.60 | +0.14 | -1.78 | 3.66 | 40.1 | No official GARP ≥ 60 yet. Not auto-promoted after a crash. |
| 14 | HLLY | Secondary 20 | Watch | 2.56 | +2.61 | -2.11 | 2.45 | 63.5 | No official GARP ≥ 60 yet. Not auto-promoted after a crash. |
| 15 | TBLA | Secondary 20 | Watch | 3.46 | -0.43 | -2.40 | 3.40 | 63.5 | No official GARP ≥ 60 yet. Not auto-promoted after a crash. |
| 16 | NAGE | Secondary 20 | Watch | 2.50 | +1.01 | -3.29 | 2.68 | 26.4 | No official GARP ≥ 60 yet. Not auto-promoted after a crash. |
| 17 | CYH | Secondary 20 | Watch | 2.88 | +1.95 | -3.85 | 2.84 | 60.0 | No official GARP ≥ 60 yet. Not auto-promoted after a crash. |
| 18 | AREC | Secondary 20 | Watch | 1.08 | -1.36 | -9.58 | 1.50 | 2.7 | No official GARP ≥ 60 yet. Not auto-promoted after a crash. |
| 19 | SABR | Secondary 20 | Watch | 1.52 | +0.33 | -14.80 | 1.86 | 6.8 | No official GARP ≥ 60 yet. Not auto-promoted after a crash. |
| 20 | MDXG | Secondary 20 | Watch | 3.85 | +2.94 | -17.73 | 4.53 | 26.3 | No official GARP ≥ 60 yet. Not auto-promoted after a crash. |

Prices: Yahoo Finance daily bars, 2026-10-22 America/Phoenix. SMA20 and RSI14 from the last 3 months of daily closes. Do not use Equibles for this routine price check.


## Rules

- Ranked Buy → Sell → Hold → Watch → Avoid. Max one Buy (paper) per morning.
- Mega-cap core (NVDA / MSFT / GOOGL / AAPL) is display-only in the digest top section — never the morning paper Buy.
- `Avoid` never becomes a buy because it bounced. `Sell` only if you already hold that avoid-quality name.
- `Watch` is not auto-promoted after a crash.
- This job never calls wsli and never sets TRADE_APPROVED.
