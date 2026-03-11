"""Shared fixtures for integration tests."""

import asyncio
import base64
import json
import os
from contextlib import asynccontextmanager
import urllib.request
import uuid

import boto3
import pytest
import websockets

# ---------------------------------------------------------------------------
# Output key prefixes (CDK appends hash suffixes)
# ---------------------------------------------------------------------------
_PREFIX_HTTP = "AppSyncEventsEventApiHttpEndpoint"
_PREFIX_WS = "AppSyncEventsEventApiRealtimeEndpoint"
_PREFIX_KEY = "AppSyncEventsEventApiApiKey"

_DEFAULT_STACK_NAME = "AppsyncLambdaAgentcore"


# ---------------------------------------------------------------------------
# Fixtures
# ---------------------------------------------------------------------------

@pytest.fixture(scope="session")
def stack_outputs():
    """Fetch all CloudFormation stack outputs once for the test session."""
    stack_name = os.environ.get("STACK_NAME") or _DEFAULT_STACK_NAME

    region = os.environ.get("AWS_REGION")
    if not region:
        raise EnvironmentError("AWS_REGION environment variable must be set")

    cfn = boto3.client("cloudformation", region_name=region)
    response = cfn.describe_stacks(StackName=stack_name)
    raw = response["Stacks"][0].get("Outputs", [])
    return {o["OutputKey"]: o["OutputValue"] for o in raw}


@pytest.fixture(scope="session")
def get_output(stack_outputs):
    """Return a callable that looks up a stack output by key prefix."""
    def _lookup(prefix: str) -> str:
        for key, value in stack_outputs.items():
            if key.startswith(prefix):
                return value
        pytest.skip(f"Stack output starting with '{prefix}' not found")
        return ""
    return _lookup


@pytest.fixture(scope="session")
def api_config(get_output):
    """Resolve the three AppSync Events endpoints/key from stack outputs."""
    return {
        "http_endpoint": get_output(_PREFIX_HTTP),
        "realtime_endpoint": get_output(_PREFIX_WS),
        "api_key": get_output(_PREFIX_KEY),
    }


@pytest.fixture(scope="session")
def auth_subprotocol(api_config):
    """Base64-encoded auth subprotocol string for WebSocket connections."""
    header = json.dumps({
        "host": api_config["http_endpoint"],
        "x-api-key": api_config["api_key"],
    }).encode()
    return "header-" + base64.b64encode(header).decode().rstrip("=")


@pytest.fixture(scope="session")
def publish(api_config):
    """Return a callable that publishes to a channel via HTTP."""
    def _do_publish(channel: str, message: dict) -> dict:
        url = f"https://{api_config['http_endpoint']}/event"
        payload = json.dumps({
            "channel": f"/{channel}",
            "events": [json.dumps(message)],
        }).encode()
        req = urllib.request.Request(
            url,
            data=payload,
            method="POST",
            headers={
                "Content-Type": "application/json",
                "x-api-key": api_config["api_key"],
            },
        )
        with urllib.request.urlopen(req) as resp:
            return json.loads(resp.read().decode())
    return _do_publish


@pytest.fixture
def subscribe(api_config, auth_subprotocol):
    """Async context manager that connects, inits, and subscribes to a channel.

    Yields (ws, sub_id) — the WebSocket and subscription ID.

    Usage:
        async with subscribe("/responses/chat/abc") as (ws, sub_id):
            ...
    """
    @asynccontextmanager
    async def _subscribe(channel: str):
        ws_url = (
            f"wss://{api_config['realtime_endpoint']}/event/realtime"
        )
        async with websockets.connect(
            ws_url,
            subprotocols=["aws-appsync-event-ws", auth_subprotocol],
            additional_headers={},
            close_timeout=2,
        ) as ws:
            await ws.send(json.dumps({"type": "connection_init"}))
            ack = json.loads(await ws.recv())
            assert ack["type"] == "connection_ack"

            sub_id = str(uuid.uuid4())
            await ws.send(json.dumps({
                "type": "subscribe",
                "id": sub_id,
                "channel": channel,
                "authorization": {
                    "x-api-key": api_config["api_key"],
                    "host": api_config["http_endpoint"],
                },
            }))

            while True:
                msg = json.loads(
                    await asyncio.wait_for(ws.recv(), timeout=10),
                )
                if msg["type"] == "ka":
                    continue
                assert msg["type"] == "subscribe_success"
                break

            yield ws, sub_id

    return _subscribe
