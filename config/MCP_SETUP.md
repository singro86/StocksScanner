# MCP Server Setup

Copy entries from `config/mcp.template.json` into your Cursor MCP config.

**Windows path:** `%USERPROFILE%\.cursor\mcp.json`  
**Or:** Cursor Settings → MCP → Edit config

## Prerequisites

```powershell
# Install uv (for Rebalance-MCP, Portfolio-MCP, FinanceKit)
powershell -ExecutionPolicy ByPass -c "irm https://astral.sh/uv/install.ps1 | iex"

# Verify
uvx --version
```

## Servers

| Server | Purpose | Auth |
|--------|---------|------|
| rebalance-mcp | GARP scoring, swaps, backtests | None |
| equibles | SEC, earnings, screener | API key from [equibles.com/dashboard/apikeys](https://equibles.com/dashboard/apikeys) |
| portfolio-mcp | Sharpe, Monte Carlo, optimization | None |
| financekit | Live quotes | None |

## Install steps

1. Merge `config/mcp.template.json` into `~/.cursor/mcp.json`
2. Replace `eq_YOUR_KEY_HERE` with your Equibles API key
3. Restart Cursor
4. Verify each server shows tools in MCP panel

## Routing policy

- **Daily scans:** Rebalance-MCP + FinanceKit only
- **Deep research:** Equibles (reserve 100/day quota)
- **Goal tracking:** Portfolio-MCP Monte Carlo
- **Never** use Equibles for routine price checks

## Troubleshooting

| Issue | Fix |
|-------|-----|
| `uvx` not found | Reinstall uv; restart terminal |
| Equibles auth error | Regenerate API key; check Bearer header |
| Rebalance-MCP timeout | Retry; check network; use `uvx rebalance-mcp` manually |
| MCP not loading | Restart Cursor; validate JSON syntax |
