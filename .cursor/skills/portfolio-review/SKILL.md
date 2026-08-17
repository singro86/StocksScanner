---
name: portfolio-review
description: Syncs wsli portfolio, scores all holdings, reports drift vs target allocation, swap candidates, and benchmark alpha vs QQQ. Use for weekly portfolio review or review my portfolio.
---

# Portfolio Review

## Steps

1. Run `scripts/wsli/sync-portfolio.ps1` (or .sh) to refresh holdings
2. Score all holdings via Rebalance-MCP
3. Read `portfolio/peak-value.yaml` — check drawdown status
4. Compare weights vs GARP target sleeves in AGENTS.md
5. Flag drift > 5%; list swap candidates (delta >= 15)
6. Compare portfolio return vs QQQ benchmark (FinanceKit)

## Output format

```markdown
# Portfolio Review — {DATE}

**Total value (CAD):** $X | **Drawdown mode:** Normal / Review-only
**vs QQQ:** [alpha or underperformance]

## Holdings
| Ticker | Weight | GARP Score | Action |
|--------|--------|------------|--------|

## Drift alerts
## Swap candidates
## Action items
```

Save to `research/reports/YYYY-MM-DD-portfolio-review.md`.
