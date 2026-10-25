# Secondary penny watchlist scan — 2026-10-25

> I am an AI research assistant, not a licensed financial advisor. This is educational information, not personalized financial advice. Consider a qualified advisor for your situation.

**Paper trading active — dry-run only. Buy lines are paper recommendations, never live Wealthsimple orders.**

## What to buy today (from 20 names)

NONE — no buy today.

Official Rebalance-MCP GARP scores are not computed in this job. Quality flags come from `portfolio/penny-secondary-watchlist.yaml`. A live ticket still needs GARP ≥ 60.

| Rank | Ticker | List | Rec | Close | 1d % | 5d % | SMA20 | RSI14 | Why |
|-----:|--------|------|-----|------:|-----:|-----:|------:|------:|-----|
| 1 | UWMC | Secondary 20 | Watch | 1.45 | +26.09 | +38.09 | 1.15 | 58.5 | No official GARP ≥ 60 yet. Not auto-promoted after a crash. |
| 2 | TYGO | Secondary 20 | Watch | 1.03 | +11.23 | +24.85 | 0.88 | 69.7 | No official GARP ≥ 60 yet. Not auto-promoted after a crash. |
| 3 | SITC | Secondary 20 | Watch | 3.74 | +0.00 | +9.04 | 3.32 | 75.5 | No official GARP ≥ 60 yet. Not auto-promoted after a crash. |
| 4 | VRRM | Secondary 20 | Watch | 3.09 | -1.59 | +8.04 | 2.95 | 61.2 | No official GARP ≥ 60 yet. Not auto-promoted after a crash. |
| 5 | AISP | Secondary 20 | Watch | 2.16 | +0.47 | +5.37 | 2.13 | 55.3 | No official GARP ≥ 60 yet. Not auto-promoted after a crash. |
| 6 | GDRX | Secondary 20 | Watch | 3.54 | -2.21 | +5.36 | 3.39 | 58.6 | No official GARP ≥ 60 yet. Not auto-promoted after a crash. |
| 7 | ALTO | Secondary 20 | Watch | 3.61 | +0.56 | +4.64 | 3.66 | 39.8 | No official GARP ≥ 60 yet. Not auto-promoted after a crash. |
| 8 | AMPY | Secondary 20 | Watch | 4.59 | +3.61 | +3.61 | 4.42 | 56.8 | No official GARP ≥ 60 yet. Not auto-promoted after a crash. |
| 9 | VFF | Secondary 20 | Watch | 2.58 | -4.98 | +1.78 | 2.73 | 41.7 | No official GARP ≥ 60 yet. Not auto-promoted after a crash. |
| 10 | CYH | Secondary 20 | Watch | 2.92 | +0.34 | +1.39 | 2.84 | 60.3 | No official GARP ≥ 60 yet. Not auto-promoted after a crash. |
| 11 | SPRO | Secondary 20 | Watch | 1.11 | -1.77 | +0.91 | 1.17 | 44.9 | No official GARP ≥ 60 yet. Not auto-promoted after a crash. |
| 12 | AREC | Secondary 20 | Watch | 1.14 | +2.70 | +0.00 | 1.46 | 8.3 | No official GARP ≥ 60 yet. Not auto-promoted after a crash. |
| 13 | HLLY | Secondary 20 | Watch | 2.49 | -4.23 | +0.00 | 2.45 | 61.1 | No official GARP ≥ 60 yet. Not auto-promoted after a crash. |
| 14 | ABUS | Secondary 20 | Watch | 4.20 | -0.24 | -0.47 | 4.36 | 30.2 | No official GARP ≥ 60 yet. Not auto-promoted after a crash. |
| 15 | TBLA | Secondary 20 | Watch | 3.41 | -1.73 | -0.87 | 3.40 | 58.3 | No official GARP ≥ 60 yet. Not auto-promoted after a crash. |
| 16 | NAGE | Secondary 20 | Watch | 2.43 | -3.57 | -2.41 | 2.65 | 30.2 | No official GARP ≥ 60 yet. Not auto-promoted after a crash. |
| 17 | GORO | Secondary 20 | Watch | 3.30 | -1.49 | -2.65 | 3.32 | 52.1 | No official GARP ≥ 60 yet. Not auto-promoted after a crash. |
| 18 | ARKO | Secondary 20 | Watch | 3.81 | -6.96 | -7.07 | 4.11 | 28.0 | No official GARP ≥ 60 yet. Not auto-promoted after a crash. |
| 19 | SABR | Secondary 20 | Watch | 1.52 | -1.30 | -9.52 | 1.83 | 9.8 | No official GARP ≥ 60 yet. Not auto-promoted after a crash. |
| 20 | MDXG | Secondary 20 | Watch | 3.91 | -0.51 | -11.74 | 4.49 | 30.2 | No official GARP ≥ 60 yet. Not auto-promoted after a crash. |

Prices: Yahoo Finance daily bars, 2026-10-25 America/Phoenix. SMA20 and RSI14 from the last 3 months of daily closes. Do not use Equibles for this routine price check.


## Rules

- Ranked Buy → Sell → Hold → Watch → Avoid. Max one Buy (paper) per morning.
- Mega-cap core (NVDA / MSFT / GOOGL / AAPL) is display-only in the digest top section — never the morning paper Buy.
- `Avoid` never becomes a buy because it bounced. `Sell` only if you already hold that avoid-quality name.
- `Watch` is not auto-promoted after a crash.
- This job never calls wsli and never sets TRADE_APPROVED.
