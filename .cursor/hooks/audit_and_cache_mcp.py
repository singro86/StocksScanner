#!/usr/bin/env python3
"""beforeMCPExecution: audit and cache MCP calls."""
import hashlib
import json
import sys
from datetime import datetime, timezone
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from hook_utils import CACHE_DIR, audit_log, emit, read_stdin_json

data = read_stdin_json()
tool = data.get("tool_name") or data.get("toolName") or data.get("name") or "unknown"
server = data.get("server_name") or data.get("serverName") or "mcp"
args = data.get("arguments") or data.get("input") or {}

audit_log("mcp_call", f"{server}:{tool}")

CACHE_DIR.mkdir(parents=True, exist_ok=True)
key = hashlib.sha256(json.dumps({"s": server, "t": tool, "a": args}, sort_keys=True).encode()).hexdigest()[:16]
cache_file = CACHE_DIR / f"mcp-{datetime.now(timezone.utc).strftime('%Y%m%d')}-{key}.json"
cache_file.write_text(
    json.dumps(
        {
            "timestamp": datetime.now(timezone.utc).isoformat(),
            "server": server,
            "tool": tool,
            "arguments": args,
        },
        indent=2,
    ),
    encoding="utf-8",
)

emit({"permission": "allow"})
