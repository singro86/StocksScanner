---
name: portfolio-onboarding
description: Walks new investors through TFSA setup, wsli config, GARP profile, and cold-start allocation on Wealthsimple. Use when user says they are starting out, first session, or onboarding.
---

# Portfolio Onboarding

## Checklist

- [ ] Read `portfolio/profile.yaml`
- [ ] Confirm TFSA contribution room (ask user)
- [ ] Verify paper trading status (`paper_trading_complete`)
- [ ] Guide wsli setup if not done (see `config/wsli.template.env`)
- [ ] Explain GARP methodology in plain language
- [ ] Propose cold-start 4 positions: MSFT, NVDA, GOOGL, AMZN (~$1K each)

## TFSA first (Canada)

Explain: tax-free growth; US dividend 15% withholding still applies; ideal for aggressive GARP stocks.

## Cold start allocation

With $5K–$10K, deploy into 4 GARP positions. Use `trade-proposal` skill for dry-run tickets.

## Paper trading

If Phase 0 active: explain 4-week graduation criteria in `portfolio/paper-trading.yaml`.

## Output

Onboarding summary saved to `research/reports/YYYY-MM-DD-onboarding.md`.
