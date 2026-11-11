"""Structured log events that client/logs.py reads back to show what the agent ran.

Each event is one log record whose message is a JSON object with an "event" field:

- prompt: {"event": "prompt", "prompt": str}
- run: {"event": "run", "operation": "executeCode" | "executeCommand", "input": str}
- result: {"event": "result", "operation": str, "exitCode": int, "stdout": str, "stderr": str}
- timeout: {"event": "timeout", "operation": str, "timeoutSeconds": float}

The AgentCore SDK's log formatter wraps the message in its own JSON record, which adds the
timestamp, level, request ID and session ID:
https://github.com/aws/bedrock-agentcore-sdk-python/blob/v1.25.4/src/bedrock_agentcore/runtime/app.py#L124
"""

import json
import logging
from typing import Any

MAX_LOGGED_CHARS = 2000


def log_event(logger: logging.Logger, event: str, **fields: Any) -> None:
    """Log one structured event at INFO level."""
    logger.info(json.dumps({"event": event, **fields}, ensure_ascii=False))


def truncate(text: str) -> str:
    """Shorten long output so that one log record stays small, and say that it was shortened."""
    if len(text) <= MAX_LOGGED_CHARS:
        return text
    return f"{text[:MAX_LOGGED_CHARS]}\n... (truncated, {len(text):,} characters in total)"
