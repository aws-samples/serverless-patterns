"""Show the prompts the agent received, the code it ran in the Code Interpreter and the results.

Reads the structured events that agent/log_events.py writes to the runtime's CloudWatch Logs log group.

Usage: python logs.py [--minutes N] [--session-id ID ...] [--stack-name NAME]
"""
import argparse
import json
import sys
import time
from collections.abc import Iterator
from datetime import datetime, timezone
from typing import Any

import boto3
from botocore.exceptions import ClientError

from invoke import DEFAULT_STACK_NAME, get_stack_output

INDENT = "    "


def read_records(group: str, start_ms: int, session_ids: list[str]) -> Iterator[dict[str, Any]]:
    """Yield the JSON records that the agent wrote, oldest first, for the given sessions or all of them."""
    kwargs = {"logGroupName": group, "startTime": start_ms}
    if session_ids:
        # https://docs.aws.amazon.com/AmazonCloudWatch/latest/logs/FilterAndPatternSyntax.html
        condition = " || ".join(f'($.sessionId = "{session_id}")' for session_id in session_ids)
        kwargs["filterPattern"] = f"{{ {condition} }}"
    events = []
    for page in boto3.client("logs").get_paginator("filter_log_events").paginate(**kwargs):
        events.extend(page["events"])
    for event in sorted(events, key=lambda e: e["timestamp"]):
        try:
            record = json.loads(event["message"])
        except json.JSONDecodeError:
            continue  # Lines that the SDK's JSON formatter didn't write, such as server startup output.
        if isinstance(record, dict):
            yield record


def parse_event(record: dict[str, Any]) -> dict[str, Any] | None:
    """Return the structured event in a record's message, or None if the message isn't one."""
    try:
        event = json.loads(record.get("message", ""))
    except json.JSONDecodeError:
        return None
    return event if isinstance(event, dict) and "event" in event else None


def indent(text: str) -> str:
    return "\n".join(INDENT + line for line in text.rstrip("\n").splitlines()) or INDENT + "(empty)"


def print_record(record: dict[str, Any], state: dict[str, Any]) -> None:
    event = parse_event(record)
    is_error = record.get("level") in ("ERROR", "CRITICAL")
    if event is None and not is_error:
        return  # Other agent and SDK messages, such as session start and stop.

    request_id = record.get("requestId", "")
    if request_id != state["request_id"]:
        state.update(request_id=request_id, runs=0)
        print(f"\n=== Request {request_id or '(none)'}")
        print(f"Time: {record.get('timestamp', '')}  Session: {record.get('sessionId', '(none)')}")

    if event is None:
        details = f": {record['errorMessage']}" if record.get("errorMessage") else ""
        print(f"\nError: {record.get('message', '')}{details}")
        return

    kind = event["event"]
    if kind == "prompt":
        print(f"\nPrompt:\n{indent(event.get('prompt', ''))}")
    elif kind == "run":
        state["runs"] += 1
        print(f"\n--- Run {state['runs']} ({event.get('operation')})")
        print(indent(event.get("input") or ""))
    elif kind == "result":
        print(f"Exit code {event.get('exitCode')}")
        print(f"stdout:\n{indent(event.get('stdout', ''))}")
        if event.get("stderr"):
            print(f"stderr:\n{indent(event['stderr'])}")
    elif kind == "timeout":
        print(f"Timed out after {event.get('timeoutSeconds')} seconds")


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    parser.add_argument("--minutes", type=int, default=30, help="How far back to read, in minutes. Defaults to 30.")
    parser.add_argument(
        "--session-id", dest="session_ids", action="append", default=[],
        help="Show only this runtime session, as printed by invoke.py. Repeat to show several sessions.",
    )
    parser.add_argument("--stack-name", default=DEFAULT_STACK_NAME)
    args = parser.parse_args()
    # Session IDs go into a CloudWatch Logs filter pattern, so allow only the characters that IDs use.
    for session_id in args.session_ids:
        if not session_id.replace("-", "").replace("_", "").isalnum():
            sys.exit(f"Invalid --session-id {session_id!r}: use only letters, digits, hyphens and underscores.")

    group = get_stack_output(args.stack_name, "AgentLogGroupName")
    start_ms = int((time.time() - args.minutes * 60) * 1000)
    state: dict[str, Any] = {"request_id": None, "runs": 0}
    try:
        for record in read_records(group, start_ms, args.session_ids):
            print_record(record, state)
    except ClientError as error:
        if error.response["Error"]["Code"] != "ResourceNotFoundException":
            sys.exit(f"Can't read log group {group}: {error}")
        print(f"Log group {group} doesn't exist yet. It appears after the agent is first invoked.")
        return
    if state["request_id"] is None:
        since = datetime.fromtimestamp(start_ms / 1000, timezone.utc).strftime("%Y-%m-%d %H:%M:%S UTC")
        print(f"No agent log records in {group} since {since}. Use --minutes to read further back.")


if __name__ == "__main__":
    main()
