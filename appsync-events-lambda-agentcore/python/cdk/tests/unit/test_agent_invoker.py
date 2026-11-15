"""Unit tests for the agent invoker Lambda handler."""

import json
import os
from unittest.mock import patch

from functions.agent_invoker.index import handler


def _make_event(payload, channel="/chat/test-123"):
    """Build a minimal AppSync Events direct Lambda integration event."""
    return {
        "events": [{"id": "evt-1", "payload": payload}],
        "info": {"channel": {"path": channel}},
    }


def _make_multi_event(payloads, channel="/chat/test-123"):
    """Build an event with multiple published messages."""
    return {
        "events": [{"id": f"evt-{i}", "payload": p} for i, p in enumerate(payloads)],
        "info": {"channel": {"path": channel}},
    }


@patch("functions.agent_invoker.index.lambda_client")
def test_valid_message_invokes_stream_relay(mock_client, lambda_context):
    """Valid payload triggers async Lambda invoke with correct relay payload."""
    event = _make_event({"message": "hello", "sessionId": "sess-1"})
    result = handler(event, lambda_context)

    mock_client.invoke.assert_called_once()
    call_kwargs = mock_client.invoke.call_args[1]
    assert call_kwargs["InvocationType"] == "Event"
    assert call_kwargs["FunctionName"] == os.environ["STREAM_RELAY_ARN"]

    relay = json.loads(call_kwargs["Payload"])
    assert relay["content"] == "hello"
    assert relay["sessionId"] == "sess-1"

    assert len(result["events"]) == 1
    assert "error" not in result["events"][0]["payload"]


@patch("functions.agent_invoker.index.lambda_client")
def test_missing_message_returns_error(mock_client, lambda_context):
    """Missing message key returns error without invoking stream relay."""
    event = _make_event({"sessionId": "sess-1"})
    result = handler(event, lambda_context)

    mock_client.invoke.assert_not_called()
    assert "message" in result["events"][0]["payload"]["error"].lower()


@patch("functions.agent_invoker.index.lambda_client")
def test_empty_message_returns_error(mock_client, lambda_context):
    """Whitespace-only message is rejected."""
    event = _make_event({"message": "   ", "sessionId": "sess-1"})
    result = handler(event, lambda_context)

    mock_client.invoke.assert_not_called()
    assert "message" in result["events"][0]["payload"]["error"].lower()


@patch("functions.agent_invoker.index.lambda_client")
def test_missing_session_id_returns_error(mock_client, lambda_context):
    """Missing sessionId returns error without invoking stream relay."""
    event = _make_event({"message": "hello"})
    result = handler(event, lambda_context)

    mock_client.invoke.assert_not_called()
    assert "sessionid" in result["events"][0]["payload"]["error"].lower()


@patch("functions.agent_invoker.index.lambda_client")
def test_empty_session_id_returns_error(mock_client, lambda_context):
    """Whitespace-only sessionId is rejected."""
    event = _make_event({"message": "hello", "sessionId": "  "})
    result = handler(event, lambda_context)

    mock_client.invoke.assert_not_called()
    assert "sessionid" in result["events"][0]["payload"]["error"].lower()


@patch("functions.agent_invoker.index.lambda_client")
def test_empty_payload_returns_error(mock_client, lambda_context):
    """Empty payload returns message error (first validation hit)."""
    event = _make_event({})
    result = handler(event, lambda_context)

    mock_client.invoke.assert_not_called()
    assert "message" in result["events"][0]["payload"]["error"].lower()


@patch("functions.agent_invoker.index.lambda_client")
def test_response_channel_prefixed_with_responses(mock_client, lambda_context):
    """Relay payload channel should be /responses{original_channel}."""
    event = _make_event(
        {"message": "hi", "sessionId": "s1"},
        channel="/chat/conv-abc",
    )
    handler(event, lambda_context)

    relay = json.loads(mock_client.invoke.call_args[1]["Payload"])
    assert relay["channel"] == "/responses/chat/conv-abc"


@patch("functions.agent_invoker.index.lambda_client")
def test_multiple_events_processed_independently(mock_client, lambda_context):
    """Batch with one valid and one invalid event returns mixed results."""
    event = _make_multi_event(
        [
            {"message": "hello", "sessionId": "s1"},
            {"message": "world"},  # missing sessionId
        ]
    )
    result = handler(event, lambda_context)

    assert mock_client.invoke.call_count == 1  # only valid event invoked
    events = result["events"]
    assert "error" not in events[0]["payload"]
    assert "error" in events[1]["payload"]
