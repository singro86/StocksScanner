# Secondary penny watchlist scan — 2026-11-25

> I am an AI research assistant, not a licensed financial advisor. This is educational information, not personalized financial advice. Consider a qualified advisor for your situation.

**Paper trading active — dry-run only. Buy lines are paper recommendations, never live Wealthsimple orders.**

## What to buy today (from 20 names)

NONE — no buy today.

Official Rebalance-MCP GARP scores are not computed in this job. Quality flags come from `portfolio/penny-secondary-watchlist.yaml`. A live ticket still needs GARP ≥ 60.

| Rank | Ticker | List | Rec | Close | 1d % | 5d % | SMA20 | RSI14 | Why |
|-----:|--------|------|-----|------:|-----:|-----:|------:|------:|-----|
| 1 | UWMC | Secondary 20 | Watch | 1.21 | +5.22 | +3.42 | 1.35 | 19.1 | No official GARP ≥ 60 yet. Not auto-promoted after a crash. |
| 2 | VRRM | Secondary 20 | Watch | 1.77 | +2.91 | +2.91 | 2.10 | 22.8 | No official GARP ≥ 60 yet. Not auto-promoted after a crash. |
| 3 | ABUS | Secondary 20 | Watch | 4.18 | -1.18 | +1.70 | 4.01 | 78.0 | No official GARP ≥ 60 yet. Not auto-promoted after a crash. |
| 4 | VFF | Secondary 20 | Watch | 2.19 | +2.82 | +0.92 | 2.48 | 24.6 | No official GARP ≥ 60 yet. Not auto-promoted after a crash. |
| 5 | SABR | Secondary 20 | Watch | 1.70 | +1.80 | -0.58 | 1.73 | 51.1 | No official GARP ≥ 60 yet. Not auto-promoted after a crash. |
| 6 | MDXG | Secondary 20 | Watch | 3.15 | +0.96 | -0.94 | 3.28 | 37.2 | No official GARP ≥ 60 yet. Not auto-promoted after a crash. |
| 7 | NAGE | Secondary 20 | Watch | 1.91 | -7.07 | -1.80 | 2.13 | 41.4 | No official GARP ≥ 60 yet. Not auto-promoted after a crash. |
| 8 | TBLA | Secondary 20 | Watch | 1.97 | +0.00 | -2.48 | 2.35 | 41.4 | No official GARP ≥ 60 yet. Not auto-promoted after a crash. |
| 9 | CYH | Secondary 20 | Watch | 1.81 | +2.26 | -2.69 | 2.07 | 31.5 | No official GARP ≥ 60 yet. Not auto-promoted after a crash. |
| 10 | HLLY | Secondary 20 | Watch | 2.40 | +0.42 | -2.83 | 2.50 | 58.8 | No official GARP ≥ 60 yet. Not auto-promoted after a crash. |
| 11 | SPRO | Secondary 20 | Watch | 0.84 | +5.78 | -3.42 | 0.96 | 32.4 | No official GARP ≥ 60 yet. Not auto-promoted after a crash. |
| 12 | SITC | Secondary 20 | Watch | 0.65 | -4.20 | -4.38 | 1.58 | 4.9 | No official GARP ≥ 60 yet. Not auto-promoted after a crash. |
| 13 | ALTO | Secondary 20 | Watch | 3.03 | -4.72 | -9.01 | 3.51 | 28.4 | No official GARP ≥ 60 yet. Not auto-promoted after a crash. |
| 14 | ARKO | Secondary 20 | Watch | 3.38 | +1.81 | -9.38 | 3.81 | 37.2 | No official GARP ≥ 60 yet. Not auto-promoted after a crash. |
| 15 | AISP | Secondary 20 | Watch | 1.42 | -1.39 | -11.25 | 1.72 | 27.1 | No official GARP ≥ 60 yet. Not auto-promoted after a crash. |
| 16 | GORO | Secondary 20 | Watch | 2.89 | -4.93 | -12.95 | 3.13 | 42.0 | No official GARP ≥ 60 yet. Not auto-promoted after a crash. |
| 17 | AREC | Secondary 20 | Watch | 0.74 | -30.61 | -13.06 | 1.02 | 40.7 | No official GARP ≥ 60 yet. Not auto-promoted after a crash. |
| 18 | AMPY | Secondary 20 | Watch | 3.45 | -0.58 | -13.32 | 3.74 | 56.8 | No official GARP ≥ 60 yet. Not auto-promoted after a crash. |
| 19 | TYGO | Secondary 20 | Watch | 0.46 | -4.15 | -18.85 | 0.68 | 14.8 | No official GARP ≥ 60 yet. Not auto-promoted after a crash. |
| 20 | GDRX | Secondary 20 | Watch | 2.38 | -20.67 | -29.17 | 3.37 | 21.8 | No official GARP ≥ 60 yet. Not auto-promoted after a crash. |

Prices: Yahoo Finance daily bars, 2026-11-25 America/Phoenix. SMA20 and RSI14 from the last 3 months of daily closes. Do not use Equibles for this routine price check.


## Rules

- Ranked Buy → Sell → Hold → Watch → Avoid. Max one Buy (paper) per morning.
- Mega-cap core (NVDA / MSFT / GOOGL / AAPL) is display-only in the digest top section — never the morning paper Buy.
- `Avoid` never becomes a buy because it bounced. `Sell` only if you already hold that avoid-quality name.
- `Watch` is not auto-promoted after a crash.
- This job never calls wsli and never sets TRADE_APPROVED.
