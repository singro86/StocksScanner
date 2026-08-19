---
name: data-science
description: >-
  Statistical modeling, features, experiments, and timeseries methods on
  portfolio and market datasets. Use when the user asks for data science,
  ML, regression, classification, clustering, A/B or backtest design,
  feature engineering, train/test splits, or hypothesis tests — not for
  simple KPI dashboards (use data-analyst).
---

# Data Science

Build and evaluate models on repo + MCP data. Never invent labels or prices. Cite source + date. Models do **not** override GARP min score 60.

## When to use

User says data science, machine learning, model, features, experiment, hypothesis test, walk-forward, clustering, or “predict.” For KPI reports and EDA-only summaries, use `data-analyst` first (or as a pre-step).

## Defaults

| Choice | Default |
|--------|---------|
| Stack | Python, pandas, scikit-learn; matplotlib/seaborn for diagnostics |
| Split | Time-based walk-forward for market series — never random shuffle of dates |
| Leakage | No future returns in features; no same-day close in a next-day target |
| Baseline | Always beat a naive baseline (last value, equal-weight, QQQ) |
| Metrics | Classification: precision/recall on the positive class. Regression: MAE + directional hit rate |
| Persistence | Scripts under `scripts/` if reused; one-off notebooks only if user asks |

## Workflow

1. State hypothesis, target, and what would falsify it.
2. Inventory features from YAML/CSV/MCP; document look-ahead risk.
3. Fit a simple baseline, then one model. Keep it small until the baseline loses.
4. Report sample size, date range, and whether Rebalance-MCP scores were used.
5. Save memo to `research/reports/YYYY-MM-DD-data-science-{topic}.md`.
6. If the result is used for investing, still require official GARP via `garp-scorer`. If Rebalance-MCP is down: **official GARP pending** — do not promote Buy.

## Memo template

```markdown
# Data science — {topic}

**Hypothesis:**
**Target / horizon:**
**Features:**
**Split:**
**Baseline vs model:**
**Result:**
**Failure modes:** (leakage, tiny n, regime shift)
**Investing implication:** (none / watch only / needs GARP)
```

## Guardrails

- Paper trading active — dry-run only.
- No options/margin/OTC recommendations from a model.
- Penny secondary names stay `watch` even if the model ranks them high.
- Equibles is not for routine quotes; FinanceKit for prices.
