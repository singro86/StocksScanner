# Send drawdown alert when portfolio drops 15% from peak
param([switch]$Force)

$Root = Split-Path (Split-Path $PSScriptRoot -Parent) -Parent
$PeakFile = Join-Path $Root "portfolio\peak-value.yaml"

if (-not (Test-Path $PeakFile)) { exit 0 }
$content = Get-Content $PeakFile -Raw
$mode = "normal"
if ($content -match "mode:\s*(\w+)") { $mode = $Matches[1] }

if ($mode -ne "review_only" -and -not $Force) { exit 0 }

$drawdown = 0
if ($content -match "drawdown_pct:\s*([\d.]+)") { $drawdown = $Matches[1] }

$body = @"
DRAWDOWN ALERT — Review-only mode active

Portfolio has dropped $drawdown% from peak (15% threshold).
New buys are blocked. Agent is in review-only mode.

Open Cursor to review holdings and GARP scores.
"@

& (Join-Path $PSScriptRoot "send-email.ps1") `
    -Subject "1M Portfolio — Drawdown Alert ($drawdown%)" `
    -Body $body `
    -Type drawdown_alert
