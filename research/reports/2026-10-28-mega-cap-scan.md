# Mega-cap core scan — 2026-10-28

> I am an AI research assistant, not a licensed financial advisor. This is educational information, not personalized financial advice. Consider a qualified advisor for your situation.

**Paper trading active — dry-run only. Buy lines are paper recommendations, never live Wealthsimple orders.**

## What to buy today (from 4 names)

NONE — no buy today.

Official Rebalance-MCP GARP scores are not computed in this job. Quality flags come from `portfolio/mega-cap-scan-universe.yaml`. A live ticket still needs GARP ≥ 60.

| Rank | Ticker | List | Rec | Close | 1d % | 5d % | SMA20 | RSI14 | Why |
|-----:|--------|------|-----|------:|-----:|-----:|------:|------:|-----|
| 1 | AAPL | Mega-cap | Watch | 344.65 | -0.71 | +0.19 | 340.65 | 56.0 | No official GARP ≥ 60 yet. Not auto-promoted after a crash. |
| 2 | MSFT | Mega-cap | Watch | 528.73 | -0.49 | -0.79 | 529.78 | 53.8 | No official GARP ≥ 60 yet. Not auto-promoted after a crash. |
| 3 | GOOGL | Mega-cap | Watch | 325.20 | +1.44 | -2.86 | 339.83 | 31.1 | No official GARP ≥ 60 yet. Not auto-promoted after a crash. |
| 4 | NVDA | Mega-cap | Watch | 215.62 | -1.06 | -2.86 | 223.80 | 35.2 | No official GARP ≥ 60 yet. Not auto-promoted after a crash. |

Prices: Yahoo Finance daily bars, 2026-10-28 America/Phoenix. SMA20 and RSI14 from the last 3 months of daily closes. Do not use Equibles for this routine price check.


## Rules

- Ranked Buy → Sell → Hold → Watch → Avoid. Max one Buy (paper) per morning.
- Mega-cap core (NVDA / MSFT / GOOGL / AAPL) is display-only in the digest top section — never the morning paper Buy.
- `Avoid` never becomes a buy because it bounced. `Sell` only if you already hold that avoid-quality name.
- `Watch` is not auto-promoted after a crash.
- This job never calls wsli and never sets TRADE_APPROVED.
