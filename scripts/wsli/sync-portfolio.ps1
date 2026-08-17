# Sync Wealthsimple portfolio to portfolio/holdings.yaml via wsli
param(
    [switch]$DryRun
)

$ErrorActionPreference = "Stop"
$Root = Split-Path (Split-Path $PSScriptRoot -Parent) -Parent
$HoldingsFile = Join-Path $Root "portfolio\holdings.yaml"
$PeakFile = Join-Path $Root "portfolio\peak-value.yaml"

function Write-YamlHoldings {
    param($TotalCad, $CashCad, $Positions, $Timestamp)
    $lines = @(
        "# Synced from wsli",
        "currency: CAD",
        "total_value_cad: $TotalCad",
        "cash_cad: $CashCad",
        "last_sync: `"$Timestamp`"",
        "source: wsli",
        "",
        "positions:"
    )
    if ($Positions.Count -eq 0) {
        $lines += "  []"
    } else {
        foreach ($p in $Positions) {
            $lines += "  - ticker: $($p.ticker)"
            $lines += "    shares: $($p.shares)"
            $lines += "    avg_cost_cad: $($p.avg_cost_cad)"
            $lines += "    current_price_cad: $($p.current_price_cad)"
            $lines += "    market_value_cad: $($p.market_value_cad)"
            $lines += "    weight_pct: $($p.weight_pct)"
            $lines += "    garp_score: null"
            $lines += "    sleeve: unknown"
        }
    }
    $lines | Set-Content -Path $HoldingsFile -Encoding UTF8
}

function Update-PeakValue {
    param([double]$CurrentValue)
    $now = (Get-Date).ToUniversalTime().ToString("yyyy-MM-dd")
    $peak = 0.0
    $peakDate = "null"
    if (Test-Path $PeakFile) {
        $content = Get-Content $PeakFile -Raw
        if ($content -match "peak_value_cad:\s*([\d.]+)") { $peak = [double]$Matches[1] }
    }
    if ($CurrentValue -gt $peak) { $peak = $CurrentValue; $peakDate = "`"$now`"" }
    $drawdown = 0.0
    if ($peak -gt 0) { $drawdown = [math]::Round((($peak - $CurrentValue) / $peak) * 100, 2) }
    $mode = if ($drawdown -ge 15) { "review_only" } else { "normal" }
    @"
# Tracks portfolio peak for 15% drawdown protocol

peak_value_cad: $peak
peak_date: $peakDate
current_value_cad: $CurrentValue
current_date: "$now"
drawdown_pct: $drawdown
mode: $mode

benchmark:
  ticker: QQQ
  peak_value: null
  current_value: null
  drawdown_pct: null

history: []
"@ | Set-Content -Path $PeakFile -Encoding UTF8
}

$timestamp = (Get-Date).ToUniversalTime().ToString("yyyy-MM-ddTHH:mm:ssZ")

if ($DryRun) {
    Write-Host "[DRY RUN] Would sync wsli portfolio to $HoldingsFile"
    exit 0
}

if (-not (Get-Command wsli -ErrorAction SilentlyContinue)) {
    Write-Warning "wsli not installed. See config/WSLI_SETUP.md. Writing empty holdings with source: wsli-unavailable."
    Write-YamlHoldings 0 0 @() $timestamp
    exit 1
}

try {
    $output = wsli portfolio 2>&1 | Out-String
    Write-Host $output
    # wsli human-readable output — store raw + placeholder parse
    # User/agent should verify positions; full JSON parsing depends on wsli version
    $positions = @()
    $total = 0.0
    $cash = 0.0
    Write-YamlHoldings $total $cash $positions $timestamp
    Update-PeakValue $total
    Write-Host "Synced to $HoldingsFile (review wsli output and update holdings if needed)"
} catch {
    Write-Error "wsli sync failed: $_"
    exit 1
}
