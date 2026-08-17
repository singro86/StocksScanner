# Send email via Resend API
param(
    [Parameter(Mandatory)][string]$Subject,
    [Parameter(Mandatory)][string]$Body,
    [ValidateSet("daily_scan","trade_approval","drawdown_alert")]
    [string]$Type = "daily_scan"
)

$ErrorActionPreference = "Stop"

$apiKey = $env:RESEND_API_KEY
$to = $env:NOTIFY_EMAIL_TO
$from = if ($env:NOTIFY_EMAIL_FROM) { $env:NOTIFY_EMAIL_FROM } else { "portfolio@yourdomain.com" }

if (-not $apiKey -or -not $to) {
    Write-Warning "RESEND_API_KEY or NOTIFY_EMAIL_TO not set. Email skipped. Configure per config/wsli.template.env"
    $Root = Split-Path (Split-Path $PSScriptRoot -Parent) -Parent
    $Outbox = Join-Path $Root "portfolio\cache\email-outbox"
    New-Item -ItemType Directory -Force -Path $Outbox | Out-Null
    $file = Join-Path $Outbox "$(Get-Date -Format 'yyyyMMdd-HHmmss')-$Type.md"
    @("# $Subject", "", $Body) | Set-Content -Path $file -Encoding UTF8
    Write-Host "Saved to outbox: $file"
    exit 0
}

$payload = @{
    from = $from
    to = @($to)
    subject = $Subject
    text = $Body
} | ConvertTo-Json

$headers = @{
    "Authorization" = "Bearer $apiKey"
    "Content-Type" = "application/json"
}

try {
    Invoke-RestMethod -Uri "https://api.resend.com/emails" -Method Post -Headers $headers -Body $payload | Out-Null
    Write-Host "Email sent: $Subject"
} catch {
    Write-Error "Resend API failed: $_"
    exit 1
}
