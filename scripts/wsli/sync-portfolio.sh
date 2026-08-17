#!/usr/bin/env bash
# Bash wrapper — sync portfolio via wsli
set -euo pipefail
SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
powershell.exe -NoProfile -ExecutionPolicy Bypass -File "$SCRIPT_DIR/sync-portfolio.ps1" "$@"
