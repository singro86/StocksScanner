---
name: trading-fundamentals
description: Teaches beginner stock trading concepts for Canadian Wealthsimple investors — orders, risk, GARP, technicals, portfolio rules. Use when user wants to learn trading, asks what something means, or requests trading lessons.
---

# Trading Fundamentals (Beginner)

Teach in plain language. One concept per response unless user asks for a full module. Always tie examples to `portfolio/profile.yaml` and North America GARP context.

## Disclaimer (first lesson each session)

> I am an AI research assistant, not a licensed financial advisor. This is educational information, not personalized financial advice.

## Teaching mode

1. **Explain** — simple definition + real example (MSFT, NVDA, GOOGL, etc.)
2. **Connect** — how it applies to their Wealthsimple TFSA + manual mode
3. **Practice** — one question or mini-scenario
4. **Log** — append progress to `research/reports/learning-log.md` when a module is completed

## Module index

| # | Module | File section |
|---|--------|--------------|
| 1 | Markets & accounts | [LEARNING_ROADMAP.md](LEARNING_ROADMAP.md) § Module 1 |
| 2 | Orders & execution | § Module 2 |
| 3 | Reading a stock quote | § Module 3 |
| 4 | GARP & valuation | § Module 4 |
| 5 | Risk & position sizing | § Module 5 |
| 6 | Technical analysis basics | § Module 6 |
| 7 | Portfolio rules (this project) | § Module 7 |
| 8 | Short-term vs long-term | § Module 8 |

## Quick reference — order types (Wealthsimple)

| Order | When to use | Beginner? |
|-------|-------------|-----------|
| **Market** | Buy/sell now at current price | ✅ Default |
| **Limit** | Only buy below X or sell above Y | ✅ After module 2 |
| **Fractional / $ amount** | Can't afford 1 full share (MSFT ~$497) | ✅ Recommended |

## Quick reference — key metrics

| Metric | Plain English | GARP use |
|--------|---------------|----------|
| P/E | Price vs earnings — lower often = cheaper | Valuation guardrail |
| Beta | Volatility vs market — >1 = swings more | Risk check |
| RSI | Overbought (>70) or oversold (<30) | Entry timing |
| Drawdown | Drop from peak | Our 15% pause rule |

## When user asks "what should I learn next?"

Read [LEARNING_ROADMAP.md](LEARNING_ROADMAP.md) and recommend the next unchecked module based on `research/reports/learning-log.md`.

## Related skills

- `portfolio-onboarding` — account setup
- `garp-scorer` — score stocks
- `trade-proposal` — build trade tickets
- `bull-bear-debate` — research before buying

## Output

Lesson notes → `research/reports/learning-YYYY-MM-DD-{topic}.md`
