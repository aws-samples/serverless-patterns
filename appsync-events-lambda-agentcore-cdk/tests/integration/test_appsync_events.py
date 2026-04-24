"""Integration tests for the deployed AppSync Event API.

Tests HTTP publish, streaming responses, tool use (http_request,
calculator, current_time), multi-turn conversations, and error
handling for the full end-to-end flow.
"""

import asyncio
import json
import re
import uuid
from datetime import datetime, timezone

import pytest


async def _collect_response(ws, sub_id, timeout=180):
    """Collect streaming events until a completion event arrives."""
    events = []
    complete = None
    deadline = asyncio.get_event_loop().time() + timeout

    while asyncio.get_event_loop().time() < deadline:
        try:
            raw = await asyncio.wait_for(ws.recv(), timeout=10)
        except asyncio.TimeoutError:
            break
        msg = json.loads(raw)
        if msg["type"] == "ka":
            continue
        if msg["type"] == "data" and msg["id"] == sub_id:
            event_data = msg["event"]
            if isinstance(event_data, str):
                event_data = json.loads(event_data)
            events.append(event_data)
            print(f"Chunk {len(events)}: {event_data}")

            payload = event_data.get("payload", event_data)
            if payload.get("type") == "complete":
                complete = payload
                break

    return events, complete


def test_publish_returns_success(publish):
    """Publish a chat message and verify the API accepts it."""
    body = publish("chat/test", {"message": "ping", "sessionId": str(uuid.uuid4())})

    assert "successful" in body, f"Expected 'successful' key: {body}"
    assert len(body["successful"]) == 1
    assert len(body["failed"]) == 0


@pytest.mark.asyncio
async def test_http_request_tool(subscribe, publish):
    """Ask the agent to fetch a URL using http_request and verify
    it streams a summarised response back via the channel."""
    conversation_id = str(uuid.uuid4())
    publish_channel = f"chat/{conversation_id}"

    async with subscribe(f"/responses/{publish_channel}") as (ws, sub_id):
        publish(
            publish_channel,
            {
                "message": ("Fetch the AWS blog homepage at https://aws.amazon.com/blogs/ and show me the latest 5 blog posts titles."),
                "sessionId": conversation_id,
            },
        )

        received, complete = await _collect_response(ws, sub_id)

        assert len(received) > 0, "Did not receive any data messages"
        assert complete is not None, "Did not receive a completion event"
        assert complete.get("response"), "Completion should contain a response"


@pytest.mark.asyncio
async def test_conversation_with_session(subscribe, publish):
    """Test multi-turn conversation using sessionId for continuity.

    Turn 1: Ask the agent to compute 347 * 29 using the calculator tool.
    Turn 2: Ask the agent to divide the previous result by 7 — it must
    recall 10063 from session history to produce the correct answer.
    """
    session_id = str(uuid.uuid4())
    publish_channel = f"chat/{session_id}"

    async with subscribe(f"/responses/{publish_channel}") as (ws, sub_id):
        # Turn 1: deterministic calculator call
        publish(
            publish_channel,
            {
                "message": (
                    "Use the calculator to compute 347 * 29. "
                    "Reply with only the result."
                ),
                "sessionId": session_id,
            },
        )

        _, complete_1 = await _collect_response(ws, sub_id)
        assert complete_1 is not None, "Turn 1 did not complete"
        assert "10063" in complete_1.get("response", ""), (
            "Turn 1 should contain 10063"
        )

        # Small delay to allow session persistence to flush
        await asyncio.sleep(2)

        # Turn 2: follow-up that requires session recall
        publish(
            publish_channel,
            {
                "message": (
                    "Take the number you just calculated and divide it by 7 "
                    "using the calculator. Reply with only the result."
                ),
                "sessionId": session_id,
            },
        )

        _, complete_2 = await _collect_response(ws, sub_id)
        assert complete_2 is not None, "Turn 2 did not complete"
        response_2 = complete_2.get("response", "")

        assert "1437" in response_2, (
            f"Turn 2 should contain 1437 (10063/7): {response_2}"
        )


@pytest.mark.asyncio
async def test_unsubscribe_stops_receiving_events(subscribe, publish):
    """After unsubscribing, the client should stop receiving events
    on that channel while the WebSocket remains open."""
    conversation_id = str(uuid.uuid4())
    publish_channel = f"chat/{conversation_id}"
    response_channel = f"/responses/{publish_channel}"

    async with subscribe(response_channel) as (ws, sub_id):
        # Verify subscription works — publish and collect response
        publish(
            publish_channel,
            {
                "message": "Say hello",
                "sessionId": conversation_id,
            },
        )
        _, complete = await _collect_response(ws, sub_id, timeout=30)
        assert complete is not None, "Should receive response while subscribed"

        # Unsubscribe from the channel
        await ws.send(
            json.dumps(
                {
                    "type": "unsubscribe",
                    "id": sub_id,
                }
            )
        )

        # Wait for unsubscribe ack
        deadline = asyncio.get_event_loop().time() + 5
        while asyncio.get_event_loop().time() < deadline:
            raw = await asyncio.wait_for(ws.recv(), timeout=5)
            msg = json.loads(raw)
            if msg["type"] == "ka":
                continue
            if msg["type"] == "unsubscribe_success":
                break

        # Publish again — should NOT receive anything on this sub
        new_session = str(uuid.uuid4())
        publish(
            publish_channel,
            {
                "message": "Say goodbye",
                "sessionId": new_session,
            },
        )

        # Wait briefly — we should only see keepalives, no data
        got_data = False
        deadline = asyncio.get_event_loop().time() + 10
        while asyncio.get_event_loop().time() < deadline:
            try:
                raw = await asyncio.wait_for(ws.recv(), timeout=5)
            except asyncio.TimeoutError:
                break
            msg = json.loads(raw)
            if msg["type"] == "ka":
                continue
            if msg["type"] == "data" and msg["id"] == sub_id:
                got_data = True
                break

        assert not got_data, "Should not receive data after unsubscribing"


@pytest.mark.asyncio
async def test_channel_isolation(subscribe, publish):
    """Messages published to one conversation channel should not
    leak to a subscriber on a different conversation channel."""
    id_a = str(uuid.uuid4())
    id_b = str(uuid.uuid4())

    async with subscribe(f"/responses/chat/{id_a}") as (ws_a, sub_a):
        async with subscribe(f"/responses/chat/{id_b}") as (ws_b, sub_b):
            # Publish only to channel A
            publish(
                f"chat/{id_a}",
                {
                    "message": "Say hello from channel A",
                    "sessionId": id_a,
                },
            )

            # Channel A should receive the response
            _, complete_a = await _collect_response(
                ws_a,
                sub_a,
                timeout=30,
            )
            assert complete_a is not None, "Channel A should receive a response"

            # Channel B should NOT receive anything
            got_data_b = False
            deadline = asyncio.get_event_loop().time() + 10
            while asyncio.get_event_loop().time() < deadline:
                try:
                    raw = await asyncio.wait_for(ws_b.recv(), timeout=5)
                except asyncio.TimeoutError:
                    break
                msg = json.loads(raw)
                if msg["type"] == "ka":
                    continue
                if msg["type"] == "data" and msg["id"] == sub_b:
                    got_data_b = True
                    break

            assert not got_data_b, "Channel B should not receive events from channel A"


async def _expect_error_event(subscribe, publish, channel_id, payload, expected_text):
    """Publish an invalid payload and verify the Lambda returns an error
    event to WebSocket subscribers on the chat channel."""
    publish_channel = f"chat/{channel_id}"

    async with subscribe(f"/{publish_channel}") as (ws, sub_id):
        publish(publish_channel, payload)

        deadline = asyncio.get_event_loop().time() + 15
        while asyncio.get_event_loop().time() < deadline:
            try:
                raw = await asyncio.wait_for(ws.recv(), timeout=5)
            except asyncio.TimeoutError:
                break
            msg = json.loads(raw)
            if msg["type"] == "ka":
                continue
            if msg["type"] == "data" and msg["id"] == sub_id:
                event_data = msg["event"]
                if isinstance(event_data, str):
                    event_data = json.loads(event_data)
                error = event_data.get("payload", event_data).get("error", "")
                if error:
                    assert expected_text in error.lower(), f"Expected '{expected_text}' in error: {error}"
                    return

        pytest.fail(f"Did not receive error event for payload: {payload}")


@pytest.mark.asyncio
async def test_calculator_tool(subscribe, publish):
    """Ask the agent to perform a calculation and verify it uses the
    calculator tool and returns the correct result."""
    conversation_id = str(uuid.uuid4())
    publish_channel = f"chat/{conversation_id}"

    async with subscribe(f"/responses/{publish_channel}") as (ws, sub_id):
        publish(
            publish_channel,
            {
                "message": "Use the calculator to compute 347 * 29. Reply with only the number.",
                "sessionId": conversation_id,
            },
        )

        _, complete = await _collect_response(ws, sub_id)
        assert complete is not None, "Did not receive a completion event"
        response = complete.get("response", "")
        assert "10063" in response, f"Expected calculator result 10063 in response: {response}"


@pytest.mark.asyncio
async def test_current_time_tool(subscribe, publish):
    """Ask the agent for the current UTC time and verify the response
    matches the actual time to the minute (±2 min grace)."""
    conversation_id = str(uuid.uuid4())
    publish_channel = f"chat/{conversation_id}"

    async with subscribe(f"/responses/{publish_channel}") as (ws, sub_id):
        publish(
            publish_channel,
            {
                "message": (
                    "Get the current time in UTC. " "Reply with ONLY the time in this exact format: YYYY-MM-DD HH:MM " "For example: 2026-03-11 14:05"
                ),
                "sessionId": conversation_id,
            },
        )

        now_utc = datetime.now(timezone.utc)
        _, complete = await _collect_response(ws, sub_id)
        assert complete is not None, "Did not receive a completion event"
        response = complete.get("response", "")

        match = re.search(r"\d{4}-\d{2}-\d{2}\s+\d{2}:\d{2}", response)
        assert match, f"Could not find YYYY-MM-DD HH:MM in response: {response}"

        reported = datetime.strptime(match.group(), "%Y-%m-%d %H:%M").replace(
            tzinfo=timezone.utc,
        )
        diff = abs((reported - now_utc).total_seconds())
        assert diff <= 120, f"Reported time {match.group()} differs from actual " f"{now_utc.strftime('%Y-%m-%d %H:%M')} by {diff:.0f}s (max 120s)"


@pytest.mark.asyncio
async def test_missing_session_id_returns_error(subscribe, publish):
    """Publishing without a sessionId should return an error via WebSocket."""
    await _expect_error_event(
        subscribe,
        publish,
        channel_id=str(uuid.uuid4()),
        payload={"message": "hello"},
        expected_text="sessionid",
    )
