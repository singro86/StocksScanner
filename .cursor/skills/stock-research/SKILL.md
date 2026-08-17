---
name: stock-research
description: Generates full investment memo with business analysis, GARP score, reverse DCF, and portfolio fit. Use when user asks to analyze or research a ticker.
---

# Stock Research

## Steps

1. `garp-scorer` → composite score
2. Equibles → business fundamentals, recent SEC/earnings
3. FinanceKit → current price, 52-week range
4. Write memo per `research-standards.mdc` template
5. Assess fit vs `portfolio/holdings.yaml` and constraints

## Save to

`research/reports/YYYY-MM-DD-{TICKER}-research.md`

## Include

- Business model (beginner-friendly)
- GARP valuation (P/E, PEG vs sector)
- Reverse DCF implied growth
- Key risks
- Portfolio fit and suggested weight
