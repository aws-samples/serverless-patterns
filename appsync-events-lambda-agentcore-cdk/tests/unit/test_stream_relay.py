"""Unit tests for the stream relay Lambda handler."""

import json
from unittest.mock import MagicMock, patch

from functions.stream_relay.index import handler


def _make_event(content="hello", channel="/responses/chat/conv-1", event_id="evt-1", session_id="sess-1"):
    return {
        "content": content,
        "channel": channel,
        "eventId": event_id,
        "sessionId": session_id,
    }


def _mock_sse_response(lines):
    """Create a mock AgentCore response with SSE streaming."""
    encoded_lines = [line.encode("utf-8") for line in lines]
    stream = MagicMock()
    stream.iter_lines.return_value = encoded_lines
    return {
        "contentType": "text/event-stream",
        "response": stream,
    }


@patch("functions.stream_relay.index._publish_to_channel")
@patch("functions.stream_relay.index.agentcore_client")
def test_streaming_sse_publishes_chunks(mock_ac, mock_publish, lambda_context):
    """SSE stream with data events publishes chunks to AppSync channel."""
    mock_ac.invoke_agent_runtime.return_value = _mock_sse_response(
        [
            'data: {"data": "Hello, "}',
            'data: {"data": "how are you?"}',
        ]
    )

    result = handler(_make_event(), lambda_context)

    assert result["status"] == "success"
    assert mock_publish.call_count >= 1
    last_call = mock_publish.call_args_list[-1]
    completion = last_call[0][1]
    assert completion["type"] == "complete"
    assert "Hello, " in completion["response"]
    assert "how are you?" in completion["response"]


@patch("functions.stream_relay.index._publish_to_channel")
@patch("functions.stream_relay.index.agentcore_client")
def test_completion_event_includes_full_response(mock_ac, mock_publish, lambda_context):
    """Final publish contains the assembled full response text."""
    mock_ac.invoke_agent_runtime.return_value = _mock_sse_response(
        [
            'data: {"data": "Part one. "}',
            'data: {"data": "Part two."}',
        ]
    )

    handler(_make_event(), lambda_context)

    completion = mock_publish.call_args_list[-1][0][1]
    assert completion["type"] == "complete"
    assert completion["response"] == "Part one. Part two."
    assert completion["eventId"] == "evt-1"


@patch("functions.stream_relay.index._publish_to_channel")
@patch("functions.stream_relay.index.agentcore_client")
def test_control_events_are_skipped(mock_ac, mock_publish, lambda_context):
    """Strands control events should not produce chunk publishes."""
    mock_ac.invoke_agent_runtime.return_value = _mock_sse_response(
        [
            'data: {"init_event_loop": true}',
            'data: {"start": true}',
            'data: {"data": "actual text."}',
            'data: {"complete": true}',
        ]
    )

    handler(_make_event(), lambda_context)

    completion = mock_publish.call_args_list[-1][0][1]
    assert completion["response"] == "actual text."
    for c in mock_publish.call_args_list:
        payload = c[0][1]
        if payload["type"] == "chunk":
            assert "init_event_loop" not in payload["content"]
            assert "start" not in payload["content"]


@patch("functions.stream_relay.index._publish_to_channel")
@patch("functions.stream_relay.index.agentcore_client")
def test_non_streaming_response_handled(mock_ac, mock_publish, lambda_context):
    """Non-SSE response is read and published as completion."""
    stream = MagicMock()
    stream.read.return_value = json.dumps({"message": "static reply"}).encode()
    mock_ac.invoke_agent_runtime.return_value = {
        "contentType": "application/json",
        "response": stream,
    }

    handler(_make_event(), lambda_context)

    completion = mock_publish.call_args_list[-1][0][1]
    assert completion["type"] == "complete"
    assert completion["response"] == "static reply"


@patch("functions.stream_relay.index._publish_to_channel")
@patch("functions.stream_relay.index.agentcore_client")
def test_chunk_batching_on_punctuation(mock_ac, mock_publish, lambda_context):
    """Chunks should flush on sentence-ending punctuation."""
    mock_ac.invoke_agent_runtime.return_value = _mock_sse_response(
        [
            'data: {"data": "Short."}',
            'data: {"data": " More text after."}',
        ]
    )

    handler(_make_event(), lambda_context)

    chunk_publishes = [c[0][1] for c in mock_publish.call_args_list if c[0][1]["type"] == "chunk"]
    assert len(chunk_publishes) >= 1
    assert chunk_publishes[0]["content"] == "Short."
