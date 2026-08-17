# Live wsli trade execution — requires TRADE_APPROVED=true (hooks enforce)
param(
    [Parameter(Mandatory)][ValidateSet("buy","sell")]
    [string]$Action,
    [Parameter(Mandatory)][string]$Ticker,
    [Parameter(Mandatory)][int]$Shares,
    [double]$GarpScore = 0
)

$ErrorActionPreference = "Stop"
$Root = Split-Path (Split-Path $PSScriptRoot -Parent) -Parent
$LogFile = Join-Path $Root "portfolio\transactions.log.md"

if ($env:TRADE_APPROVED -ne "true") {
    Write-Error "TRADE_APPROVED is not true. Hooks require explicit user approval before live execution."
    exit 1
}

if ($env:PAUSE_ALL_TRADING -eq "true") {
    Write-Error "PAUSE_ALL_TRADING is enabled."
    exit 1
}

if (-not (Get-Command wsli -ErrorAction SilentlyContinue)) {
    Write-Error "wsli not installed. See config/WSLI_SETUP.md"
    exit 1
}

$cmd = "wsli $Action $Ticker --shares $Shares"
Write-Host "Executing: $cmd"
$output = Invoke-Expression $cmd 2>&1 | Out-String
Write-Host $output

$ts = (Get-Date).ToUniversalTime().ToString("yyyy-MM-dd HH:mm")
$entry = "## $ts — $($Action.ToUpper()) $Ticker — $Shares shares — GARP $GarpScore — Approved by user"
Add-Content -Path $LogFile -Value $entry
Add-Content -Path $LogFile -Value "``$output``"
Add-Content -Path $LogFile -Value ""

& (Join-Path $PSScriptRoot "sync-portfolio.ps1")
Write-Host "Logged to $LogFile and synced portfolio."
