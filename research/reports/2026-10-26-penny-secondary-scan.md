# Secondary penny watchlist scan — 2026-10-26

> I am an AI research assistant, not a licensed financial advisor. This is educational information, not personalized financial advice. Consider a qualified advisor for your situation.

**Paper trading active — dry-run only. Buy lines are paper recommendations, never live Wealthsimple orders.**

## What to buy today (from 20 names)

NONE — no buy today.

Official Rebalance-MCP GARP scores are not computed in this job. Quality flags come from `portfolio/penny-secondary-watchlist.yaml`. A live ticket still needs GARP ≥ 60.

| Rank | Ticker | List | Rec | Close | 1d % | 5d % | SMA20 | RSI14 | Why |
|-----:|--------|------|-----|------:|-----:|-----:|------:|------:|-----|
| 1 | UWMC | Secondary 20 | Watch | 1.43 | -1.38 | +34.91 | 1.16 | 63.2 | No official GARP ≥ 60 yet. Not auto-promoted after a crash. |
| 2 | TYGO | Secondary 20 | Watch | 0.93 | -9.56 | +12.64 | 0.89 | 56.4 | No official GARP ≥ 60 yet. Not auto-promoted after a crash. |
| 3 | VRRM | Secondary 20 | Watch | 3.08 | -0.48 | +9.43 | 2.96 | 63.5 | No official GARP ≥ 60 yet. Not auto-promoted after a crash. |
| 4 | AISP | Secondary 20 | Watch | 2.18 | +0.93 | +7.92 | 2.15 | 52.8 | No official GARP ≥ 60 yet. Not auto-promoted after a crash. |
| 5 | CYH | Secondary 20 | Watch | 2.94 | +0.51 | +6.34 | 2.85 | 62.6 | No official GARP ≥ 60 yet. Not auto-promoted after a crash. |
| 6 | GDRX | Secondary 20 | Watch | 3.55 | +0.28 | +5.34 | 3.40 | 64.4 | No official GARP ≥ 60 yet. Not auto-promoted after a crash. |
| 7 | SITC | Secondary 20 | Watch | 3.73 | -0.13 | +4.92 | 3.35 | 78.3 | No official GARP ≥ 60 yet. Not auto-promoted after a crash. |
| 8 | ALTO | Secondary 20 | Watch | 3.64 | +0.83 | +4.30 | 3.66 | 43.7 | No official GARP ≥ 60 yet. Not auto-promoted after a crash. |
| 9 | HLLY | Secondary 20 | Watch | 2.56 | +3.01 | +3.01 | 2.46 | 63.0 | No official GARP ≥ 60 yet. Not auto-promoted after a crash. |
| 10 | SABR | Secondary 20 | Watch | 1.67 | +9.54 | +1.52 | 1.81 | 30.2 | No official GARP ≥ 60 yet. Not auto-promoted after a crash. |
| 11 | ABUS | Secondary 20 | Watch | 4.21 | +0.36 | -0.35 | 4.33 | 37.0 | No official GARP ≥ 60 yet. Not auto-promoted after a crash. |
| 12 | VFF | Secondary 20 | Watch | 2.52 | -1.94 | -0.59 | 2.70 | 34.5 | No official GARP ≥ 60 yet. Not auto-promoted after a crash. |
| 13 | AMPY | Secondary 20 | Watch | 4.47 | -2.61 | -1.32 | 4.44 | 49.6 | No official GARP ≥ 60 yet. Not auto-promoted after a crash. |
| 14 | AREC | Secondary 20 | Watch | 1.11 | -2.62 | -1.76 | 1.43 | 8.4 | No official GARP ≥ 60 yet. Not auto-promoted after a crash. |
| 15 | TBLA | Secondary 20 | Watch | 3.38 | -1.03 | -2.17 | 3.40 | 58.7 | No official GARP ≥ 60 yet. Not auto-promoted after a crash. |
| 16 | NAGE | Secondary 20 | Watch | 2.44 | +0.62 | -2.20 | 2.62 | 30.7 | No official GARP ≥ 60 yet. Not auto-promoted after a crash. |
| 17 | ARKO | Secondary 20 | Watch | 3.87 | +1.44 | -4.09 | 4.09 | 32.5 | No official GARP ≥ 60 yet. Not auto-promoted after a crash. |
| 18 | SPRO | Secondary 20 | Watch | 1.06 | -4.50 | -5.36 | 1.16 | 37.2 | No official GARP ≥ 60 yet. Not auto-promoted after a crash. |
| 19 | GORO | Secondary 20 | Watch | 3.12 | -5.46 | -8.23 | 3.31 | 40.0 | No official GARP ≥ 60 yet. Not auto-promoted after a crash. |
| 20 | MDXG | Secondary 20 | Watch | 3.85 | -1.41 | -11.99 | 4.45 | 26.2 | No official GARP ≥ 60 yet. Not auto-promoted after a crash. |

Prices: Yahoo Finance daily bars, 2026-10-26 America/Phoenix. SMA20 and RSI14 from the last 3 months of daily closes. Do not use Equibles for this routine price check.


## Rules

- Ranked Buy → Sell → Hold → Watch → Avoid. Max one Buy (paper) per morning.
- Mega-cap core (NVDA / MSFT / GOOGL / AAPL) is display-only in the digest top section — never the morning paper Buy.
- `Avoid` never becomes a buy because it bounced. `Sell` only if you already hold that avoid-quality name.
- `Watch` is not auto-promoted after a crash.
- This job never calls wsli and never sets TRADE_APPROVED.
