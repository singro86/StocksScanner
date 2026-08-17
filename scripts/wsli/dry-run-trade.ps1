# Dry-run trade preview via wsli — saves report to research/reports/
param(
    [Parameter(Mandatory)][ValidateSet("buy","sell")]
    [string]$Action,
    [Parameter(Mandatory)][string]$Ticker,
    [int]$Shares = 0,
    [double]$AmountCad = 0
)

$ErrorActionPreference = "Stop"
$Root = Split-Path (Split-Path $PSScriptRoot -Parent) -Parent
$ReportsDir = Join-Path $Root "research\reports"
$PaperFile = Join-Path $Root "portfolio\paper-trading.yaml"
New-Item -ItemType Directory -Force -Path $ReportsDir | Out-Null

$timestamp = (Get-Date).ToUniversalTime().ToString("yyyy-MM-ddTHH:mm:ssZ")
$dateSlug = (Get-Date).ToUniversalTime().ToString("yyyy-MM-dd")
$reportFile = Join-Path $ReportsDir "$dateSlug-dry-run-$Action-$Ticker.md"

$cmd = "wsli $Action $Ticker --dry-run"
if ($Shares -gt 0) { $cmd += " --shares $Shares" }

$output = ""
if (Get-Command wsli -ErrorAction SilentlyContinue) {
    try { $output = Invoke-Expression $cmd 2>&1 | Out-String } catch { $output = "wsli error: $_" }
} else {
    $output = "wsli not installed — simulated dry-run. Install per config/WSLI_SETUP.md"
}

$report = @"
# Dry-Run Trade Ticket

**Date:** $timestamp
**Action:** $($Action.ToUpper())
**Ticker:** $Ticker
**Shares:** $Shares
**Amount CAD:** $AmountCad
**Command:** ``$cmd``

## wsli output

``````
$output
``````

## Status

Paper trading mode — live execution blocked until graduation.

**Approve in chat to proceed (live still requires paper_trading_complete + TRADE_APPROVED).**
"@

$report | Set-Content -Path $reportFile -Encoding UTF8
Write-Host "Dry-run report saved: $reportFile"

# Append to paper-trading dry_run_log if file exists
if (Test-Path $PaperFile) {
    Add-Content -Path $PaperFile -Value "- date: `"$timestamp`" ticker: $Ticker action: $Action report: `"$reportFile`""
}
