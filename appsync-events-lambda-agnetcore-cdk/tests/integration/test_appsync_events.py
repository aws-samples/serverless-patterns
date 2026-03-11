"""Integration tests for the deployed AppSync Event API.

Tests HTTP publish, streaming responses, multi-turn conversations,
and error handling for the full end-to-end flow.
"""

import asyncio
import json
import uuid

import pytest


async def _collect_response(ws, sub_id, timeout=60):
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
async def test_subscribe_receives_agent_response(subscribe, publish):
    """Subscribe via WebSocket, publish via HTTP, and verify
    the agent streams chunks back via the channel."""
    conversation_id = str(uuid.uuid4())
    publish_channel = f"chat/{conversation_id}"

    async with subscribe(f"/responses/{publish_channel}") as (ws, sub_id):
        publish(publish_channel, {
            "message": "Write a short nursery rhyme about goats",
            "sessionId": conversation_id,
        })

        received, complete = await _collect_response(ws, sub_id)

        assert len(received) > 0, "Did not receive any data messages"
        assert complete is not None, "Did not receive a completion event"
        assert complete.get("response"), "Completion should contain a response"


@pytest.mark.asyncio
async def test_conversation_with_session(subscribe, publish):
    """Test multi-turn conversation using sessionId for continuity.

    Turn 1: Ask for a short nursery rhyme about goats (< 100 words).
    Turn 2: Ask to make it longer (250-300 words) — the agent should
    remember the first request via session persistence.
    """
    session_id = str(uuid.uuid4())
    publish_channel = f"chat/{session_id}"

    async with subscribe(f"/responses/{publish_channel}") as (ws, sub_id):
        # Turn 1: short nursery rhyme
        publish(publish_channel, {
            "message": (
                "Write a short nursery rhyme about goats. "
                "Keep it under 100 words."
            ),
            "sessionId": session_id,
        })

        _, complete_1 = await _collect_response(ws, sub_id)
        assert complete_1 is not None, "Turn 1 did not complete"
        response_1 = complete_1.get("response", "")
        word_count_1 = len(response_1.split())
        print(f"\n[turn 1] {word_count_1} words: {response_1[:200]}...")
        assert word_count_1 < 150, f"Turn 1 too long: {word_count_1} words"

        # Turn 2: ask to make it longer — agent should remember the rhyme
        publish(publish_channel, {
            "message": (
                "That was great! Now make the nursery rhyme longer, "
                "between 250 and 300 words."
            ),
            "sessionId": session_id,
        })

        _, complete_2 = await _collect_response(ws, sub_id)
        assert complete_2 is not None, "Turn 2 did not complete"
        response_2 = complete_2.get("response", "")
        word_count_2 = len(response_2.split())
        print(f"\n[turn 2] {word_count_2} words: {response_2[:200]}...")

        assert word_count_2 > word_count_1, (
            f"Turn 2 ({word_count_2} words) should be longer "
            f"than turn 1 ({word_count_1} words)"
        )
        assert "goat" in response_2.lower(), (
            "Turn 2 should reference goats from the conversation context"
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
        publish(publish_channel, {
            "message": "Say hello",
            "sessionId": conversation_id,
        })
        _, complete = await _collect_response(ws, sub_id, timeout=30)
        assert complete is not None, "Should receive response while subscribed"

        # Unsubscribe from the channel
        await ws.send(json.dumps({
            "type": "unsubscribe",
            "id": sub_id,
        }))

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
        publish(publish_channel, {
            "message": "Say goodbye",
            "sessionId": new_session,
        })

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
            publish(f"chat/{id_a}", {
                "message": "Say hello from channel A",
                "sessionId": id_a,
            })

            # Channel A should receive the response
            _, complete_a = await _collect_response(
                ws_a, sub_a, timeout=30,
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

            assert not got_data_b, (
                "Channel B should not receive events from channel A"
            )



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
                    assert expected_text in error.lower(), (
                        f"Expected '{expected_text}' in error: {error}"
                    )
                    return

        pytest.fail(f"Did not receive error event for payload: {payload}")


@pytest.mark.asyncio
async def test_missing_session_id_returns_error(subscribe, publish):
    """Publishing without a sessionId should return an error via WebSocket."""
    await _expect_error_event(
        subscribe, publish,
        channel_id=str(uuid.uuid4()),
        payload={"message": "hello"},
        expected_text="sessionid",
    )




