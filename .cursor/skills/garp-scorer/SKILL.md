---
name: garp-scorer
description: Runs Rebalance-MCP 5-dimension GARP scoring on tickers and outputs composite score with breakdown. Use when user asks to score a stock, GARP analysis, or rate a ticker.
---

# GARP Scorer

## Steps

1. Call Rebalance-MCP `score_tickers` with style preset `garp`
2. Fetch live price via FinanceKit for context
3. Compare score to `min_garp_score` (60) in profile.yaml

## Output format

```markdown
## {TICKER} GARP Score: {XX}/100

| Dimension | Score | Weight |
|-----------|-------|--------|
| Thesis | | 25% |
| Valuation | | 25% |
| Momentum | | 20% |
| Catalyst | | 15% |
| Technical | | 15% |

**Verdict:** Buy candidate / Hold / Below threshold
```

## After scoring

Update `garp_score` in `portfolio/watchlist.yaml` for watchlist tickers.
