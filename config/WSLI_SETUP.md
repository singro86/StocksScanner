# Wealthsimple wsli CLI Setup

**Warning:** Unofficial API. May violate Wealthsimple ToS. Use at your own risk.

## Prerequisites

- Node.js 20+
- Wealthsimple Trade account (TFSA recommended)
- Paper trading graduation (`paper_trading_complete: true`) for live trades

## Install

**Note:** `wsli` is **not published** to the public npm registry (`npm install -g wsli` returns 404). Install from GitHub:

```powershell
# Clone and build (one-time)
git clone https://github.com/Hawkeeeman/wsli.git "$env:LOCALAPPDATA\wsli"
cd "$env:LOCALAPPDATA\wsli"
npm install
npm run build
npm link

# Verify
wsli --help
```

Alternative (may fail if TypeScript build tools missing globally):

```powershell
npm install -g github:Hawkeeeman/wsli
```

If `wsli` is not found after `npm link`, add npm global bin to PATH:

```powershell
npm prefix -g
# Add that path + \node_modules to your user PATH, then restart terminal
```

## Environment variables

Copy `config/wsli.template.env` to your user environment (never commit):

```
WEALTHSIMPLE_ACCESS_TOKEN=your_token
WEALTHSIMPLE_REFRESH_TOKEN=your_token
```

Set in Cursor: Settings → environment or system user variables.

## Scripts

| Script | Purpose |
|--------|---------|
| `scripts/wsli/sync-portfolio.ps1` | Pull positions → `portfolio/holdings.yaml` |
| `scripts/wsli/dry-run-trade.ps1` | Preview order → `research/reports/` |
| `scripts/wsli/execute-trade.ps1` | Live trade (requires `TRADE_APPROVED=true`) |

## Test flow

```powershell
# Read-only
wsli portfolio

# Dry-run (always allowed)
.\scripts\wsli\dry-run-trade.ps1 -Action buy -Ticker MSFT -AmountCad 1000

# Live (only after paper trading + approval)
$env:TRADE_APPROVED = "true"
.\scripts\wsli\execute-trade.ps1 -Action buy -Ticker MSFT -Shares 1
Remove-Item Env:TRADE_APPROVED
```

## Fallback

If wsli breaks: trade manually in Wealthsimple app, then run `sync-portfolio.ps1`.

## Rate limits

- Agent: 3 trades/hour, 5/day
- Wealthsimple server: 7/hour
