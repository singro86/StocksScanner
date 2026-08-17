---
name: earnings-watch
description: Flags upcoming earnings for holdings and watchlist, triggers pre-earnings GARP re-score checklist. Use before earnings season or when user asks about earnings.
---

# Earnings Watch

## Steps

1. Read tickers from `portfolio/holdings.yaml` and `portfolio/watchlist.yaml`
2. Query Equibles for upcoming earnings dates (holdings + watchlist)
3. For earnings within 14 days: run GARP re-score on affected tickers
4. Produce checklist per ticker

## Checklist template

```markdown
## {TICKER} — Earnings {DATE}

- [ ] Re-score GARP (Rebalance-MCP)
- [ ] Review last quarter via Equibles earnings transcript
- [ ] Check implied move vs historical
- [ ] Decision: Hold through / Trim / No action
```

Save to `research/reports/YYYY-MM-DD-earnings-watch.md`.

Reserve Equibles calls — batch tickers in one session.
