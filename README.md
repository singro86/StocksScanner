# 1MillionPortfolio

AI-powered GARP (Growth At Reasonable Price) investment agent for North American markets via Wealthsimple Trade.

**North star:** $1M CAD long-term | **Realistic 2027 milestone:** ~$30K CAD

## Quick start

1. **Configure MCP servers** — see [`config/MCP_SETUP.md`](config/MCP_SETUP.md); merge `config/mcp.template.json` into Cursor MCP settings
2. **Configure wsli** — see [`config/WSLI_SETUP.md`](config/WSLI_SETUP.md); copy `config/wsli.template.env` → `config/wsli.env` (gitignored)
3. **Paper trading (4 weeks)** — live trades blocked until graduation criteria in `portfolio/paper-trading.yaml`
4. **Open in Cursor** — agent uses mandatory rule + `docs/AGENT_SYSTEM.md` automatically

## Architecture

| Layer | Components |
|-------|------------|
| **Docs** | [`docs/AGENT_SYSTEM.md`](docs/AGENT_SYSTEM.md) — full agent specification |
| **Agent** | `AGENTS.md` + mandatory rule `agent-mandatory-workflow.mdc` |
| **Rules** | 6 `.mdc` files (3 always-on + 2 file-scoped) |
| **Skills** | 12 workflows in `.cursor/skills/` |
| **Hooks** | 10 scripts in `.cursor/hooks/` |
| **MCP** | FinanceKit, Equibles, Rebalance-MCP, Portfolio-MCP |
| **Automations** | 5 workflows in `automations/` |

## Key commands

```powershell
# Sync portfolio from Wealthsimple
.\scripts\wsli\sync-portfolio.ps1

# Dry-run trade (always allowed during paper trading)
.\scripts\wsli\dry-run-trade.ps1 -Action buy -Ticker MSFT -AmountCad 1000

# Live trade (after paper graduation + user approval)
$env:TRADE_APPROVED = "true"
.\scripts\wsli\execute-trade.ps1 -Action buy -Ticker MSFT -Shares 1 -GarpScore 78

# Daily scan template (full GARP watchlist — agent completes MCP scoring)
.\scripts\scoring\daily-garp-scan.ps1 -SendEmail

# 9-name penny screen (Yahoo bars, time series, paper recommendation)
# Windows: uv run --python 3.12 --with tzdata --no-project python .\scripts\scoring\daily-penny9-scan.py
python .\scripts\scoring\daily-penny9-scan.py

# 20-name secondary penny watchlist (watch-only tier, same scanner)
python .\scripts\scoring\daily-penny9-scan.py --universe portfolio\penny-secondary-watchlist.yaml
```

Each universe writes its own `research/timeseries/<slug>.csv` and `research/reports/<date>-<slug>-scan.md`, keyed off the `slug` in the universe YAML.

## Paper trading graduation

Complete all criteria in `portfolio/paper-trading.yaml`, confirm with agent, then set `paper_trading_complete: true` in `portfolio/profile.yaml`.

## Cold start (full GARP day 1)

Initial 4 positions: **MSFT, NVDA, GOOGL, AMZN** (~$1K each). See `portfolio/watchlist.yaml` for full 20-stock core.

## Drawdown protocol

At **15% below peak** → review-only mode (no new buys). Tracked in `portfolio/peak-value.yaml`. Email alert via `scripts/notify/drawdown-alert.ps1`.

## Kill switch

```powershell
$env:PAUSE_ALL_TRADING = "true"   # blocks all wsli commands
```

## Prerequisites

- [uv](https://docs.astral.sh/uv/) / `uvx` for MCP servers
- Python 3.10+ for Cursor hooks
- Node 20+ for wsli — install from GitHub (see `config/WSLI_SETUP.md`; `npm install -g wsli` is 404)
- Equibles API key: https://equibles.com/dashboard/apikeys
- Resend API key (optional email): https://resend.com

## Disclaimer

Educational purposes only. Not financial advice. Unofficial Wealthsimple APIs may violate ToS and risk account termination.
