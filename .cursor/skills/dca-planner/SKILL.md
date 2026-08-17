---
name: dca-planner
description: Creates GARP-ranked dollar-cost averaging plan for monthly contributions across watchlist and core holdings. Use when user says I have $X this month or plans monthly DCA.
---

# DCA Planner

## Steps

1. Read monthly amount from user (default: midpoint of profile `monthly_range`)
2. Score watchlist via Rebalance-MCP
3. Prioritize: lowest-scored holding needing boost OR highest-scored watchlist candidate not yet held
4. Respect cash buffer (~10%) and drawdown mode (no buys if review-only)
5. Split across 1–2 names max per month to minimize trades

## Output

```markdown
# DCA Plan — {DATE} — ${amount} CAD

| Allocation | Ticker | Amount CAD | GARP Score | Rationale |
|------------|--------|------------|------------|-----------|

**Dry-run commands:** [list]
```

Hand off to `trade-proposal` for dry-run tickets.
