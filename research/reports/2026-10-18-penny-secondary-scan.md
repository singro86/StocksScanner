# Secondary penny watchlist scan — 2026-10-18

> I am an AI research assistant, not a licensed financial advisor. This is educational information, not personalized financial advice. Consider a qualified advisor for your situation.

**Paper trading active — dry-run only. Buy lines are paper recommendations, never live Wealthsimple orders.**

## What to buy today (from 20 names)

NONE — no buy today.

Official Rebalance-MCP GARP scores are not computed in this job. Quality flags come from `portfolio/penny-secondary-watchlist.yaml`. A live ticket still needs GARP ≥ 60.

| Rank | Ticker | List | Rec | Close | 1d % | 5d % | SMA20 | RSI14 | Why |
|-----:|--------|------|-----|------:|-----:|-----:|------:|------:|-----|
| 1 | SITC | Secondary 20 | Watch | 3.43 | +13.95 | +10.64 | 3.15 | 63.8 | No official GARP ≥ 60 yet. Not auto-promoted after a crash. |
| 2 | CYH | Secondary 20 | Watch | 2.88 | -3.68 | +4.35 | 2.87 | 49.3 | No official GARP ≥ 60 yet. Not auto-promoted after a crash. |
| 3 | ABUS | Secondary 20 | Watch | 4.22 | -1.63 | +0.00 | 4.54 | 31.2 | No official GARP ≥ 60 yet. Not auto-promoted after a crash. |
| 4 | HLLY | Secondary 20 | Watch | 2.49 | -4.60 | +0.00 | 2.45 | 54.1 | No official GARP ≥ 60 yet. Not auto-promoted after a crash. |
| 5 | ARKO | Secondary 20 | Watch | 4.10 | -0.24 | -0.24 | 4.17 | 38.2 | No official GARP ≥ 60 yet. Not auto-promoted after a crash. |
| 6 | TBLA | Secondary 20 | Watch | 3.44 | -2.83 | -0.29 | 3.41 | 52.0 | No official GARP ≥ 60 yet. Not auto-promoted after a crash. |
| 7 | GORO | Secondary 20 | Watch | 3.39 | +1.80 | -0.59 | 3.36 | 51.3 | No official GARP ≥ 60 yet. Not auto-promoted after a crash. |
| 8 | AMPY | Secondary 20 | Watch | 4.43 | +1.84 | -0.67 | 4.37 | 60.2 | No official GARP ≥ 60 yet. Not auto-promoted after a crash. |
| 9 | GDRX | Secondary 20 | Watch | 3.36 | -4.14 | -2.04 | 3.35 | 52.6 | No official GARP ≥ 60 yet. Not auto-promoted after a crash. |
| 10 | VRRM | Secondary 20 | Watch | 2.86 | -2.72 | -2.72 | 3.04 | 42.7 | No official GARP ≥ 60 yet. Not auto-promoted after a crash. |
| 11 | UWMC | Secondary 20 | Watch | 1.05 | -8.70 | -2.78 | 1.17 | 36.1 | No official GARP ≥ 60 yet. Not auto-promoted after a crash. |
| 12 | MDXG | Secondary 20 | Watch | 4.43 | -5.34 | -5.14 | 4.68 | 35.3 | No official GARP ≥ 60 yet. Not auto-promoted after a crash. |
| 13 | VFF | Secondary 20 | Watch | 2.53 | -2.69 | -5.60 | 2.83 | 16.1 | No official GARP ≥ 60 yet. Not auto-promoted after a crash. |
| 14 | TYGO | Secondary 20 | Watch | 0.82 | -1.32 | -7.20 | 0.89 | 50.7 | No official GARP ≥ 60 yet. Not auto-promoted after a crash. |
| 15 | NAGE | Secondary 20 | Watch | 2.49 | -3.49 | -7.43 | 2.79 | 24.2 | No official GARP ≥ 60 yet. Not auto-promoted after a crash. |
| 16 | ALTO | Secondary 20 | Watch | 3.45 | -5.74 | -7.51 | 3.71 | 38.3 | No official GARP ≥ 60 yet. Not auto-promoted after a crash. |
| 17 | SPRO | Secondary 20 | Watch | 1.10 | -2.65 | -8.33 | 1.19 | 39.5 | No official GARP ≥ 60 yet. Not auto-promoted after a crash. |
| 18 | SABR | Secondary 20 | Watch | 1.68 | -6.14 | -11.58 | 2.00 | 11.1 | No official GARP ≥ 60 yet. Not auto-promoted after a crash. |
| 19 | AISP | Secondary 20 | Watch | 2.05 | -2.84 | -15.29 | 2.07 | 58.4 | No official GARP ≥ 60 yet. Not auto-promoted after a crash. |
| 20 | AREC | Secondary 20 | Watch | 1.14 | -5.00 | -28.30 | 1.67 | 4.0 | No official GARP ≥ 60 yet. Not auto-promoted after a crash. |

Prices: Yahoo Finance daily bars, 2026-10-18 America/Phoenix. SMA20 and RSI14 from the last 3 months of daily closes. Do not use Equibles for this routine price check.


## Rules

- Ranked Buy → Sell → Hold → Watch → Avoid. Max one Buy (paper) per morning.
- Mega-cap core (NVDA / MSFT / GOOGL / AAPL) is display-only in the digest top section — never the morning paper Buy.
- `Avoid` never becomes a buy because it bounced. `Sell` only if you already hold that avoid-quality name.
- `Watch` is not auto-promoted after a crash.
- This job never calls wsli and never sets TRADE_APPROVED.
