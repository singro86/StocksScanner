#!/usr/bin/env python3
"""beforeSubmitPrompt: block secrets and flag reckless trading prompts."""
import re
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from hook_utils import ask_shell, emit, read_stdin_json

data = read_stdin_json()
prompt = data.get("prompt") or data.get("text") or ""
if isinstance(prompt, list):
    prompt = " ".join(str(p) for p in prompt)

SECRET_PATTERNS = [
    r"eq_[a-zA-Z0-9]{20,}",
    r"Bearer\s+[a-zA-Z0-9._-]{20,}",
    r"WEALTHSIMPLE_ACCESS_TOKEN\s*=",
    r"WEALTHSIMPLE_REFRESH_TOKEN\s*=",
    r"RESEND_API_KEY\s*=",
    r"sk-[a-zA-Z0-9]{20,}",
]

for pat in SECRET_PATTERNS:
    if re.search(pat, prompt, re.I):
        emit(
            {
                "permission": "deny",
                "user_message": "Prompt appears to contain API keys or secrets. Remove credentials from chat.",
                "agent_message": "Secret detected in prompt. Never paste API keys — use environment variables.",
            }
        )

RISKY = [r"\byolo\b", r"\ball[\s-]?in\b", r"\bmargin\b", r"\b100%\b.*\b(?:stock|position)\b"]
for pat in RISKY:
    if re.search(pat, prompt, re.I):
        ask_shell(
            "This prompt suggests high-risk behavior. Confirm you want to proceed against GARP guardrails.",
            "Risky prompt flagged. Verify against profile.yaml constraints before recommending.",
        )

emit({"permission": "allow"})
