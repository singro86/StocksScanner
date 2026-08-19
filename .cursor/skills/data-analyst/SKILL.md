---
name: data-analyst
description: >-
  Exploratory analysis, dashboards, and stakeholder reports on tabular
  portfolio data (YAML, CSV, timeseries). Use when the user asks for data
  analysis, EDA, KPIs, charts, pivot tables, SQL-style questions, trends,
  or a business-friendly summary of holdings, scans, or research CSVs.
---

# Data Analyst

Business-facing analysis of this repo’s data. Do not invent prices or fundamentals — use FinanceKit / Equibles / existing files and cite source + date.

## When to use

User says data analysis, EDA, dashboard, KPI, trend, concentration, “summarize the CSV,” or wants a non-model report. For predictive models, feature pipelines, or experiments, use `data-science` instead.

## Sources (this repo)

| Data | Path |
|------|------|
| Holdings, weights | `portfolio/holdings.yaml` |
| Profile / constraints | `portfolio/profile.yaml` |
| Watchlist scores | `portfolio/watchlist.yaml` |
| Penny-9 / secondary scans | `research/timeseries/penny9.csv`, `penny-secondary.csv` |
| Memos | `research/reports/` |

Prefer pandas (or PowerShell + Python) over guessing. CAD for portfolio totals.

## Workflow

1. Confirm the question in one sentence (metric, grain, date range).
2. Load files; print row counts, dtypes, nulls, date range.
3. Compute KPIs with a defined numerator/denominator.
4. Show 1–2 charts or tables max unless asked for more (bar, line, heatmap).
5. Write a beginner-friendly finding: what changed, why it might matter, what to check next.
6. Save to `research/reports/YYYY-MM-DD-data-analyst-{topic}.md`.

## Report template

```markdown
# Data analyst — {topic}

**Question:**
**Grain / window:**
**Source + date:**

## KPIs
| Metric | Value | vs prior |

## Findings
1.
2.

## Caveats
(missing data, survivorship, FX USD vs CAD)

## Next action
```

## Guardrails

- Paper trading active — dry-run only; this skill does not place trades.
- Do not promote a ticker to Buy. Hand off to `garp-scorer` / `trade-proposal`.
- Flag 20% single-name and 40% sector caps if weights breach `profile.yaml`.
