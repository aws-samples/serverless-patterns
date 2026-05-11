"""
Slack Event Handler - Entry point for Slack webhooks
Handles Slack events and initiates Durable Function orchestrations
"""
import json
import os
import hashlib
import hmac
import time
import boto3
import boto3.dynamodb.conditions
from datetime import datetime
from typing import Dict, Any

from utils.slack_client import SlackClient

SLACK_SIGNING_SECRET = os.environ['SLACK_SIGNING_SECRET']
ORCHESTRATOR_FUNCTION_ARN = os.environ['ORCHESTRATOR_FUNCTION_ARN']

lambda_client = boto3.client('lambda')
dynamodb = boto3.resource('dynamodb')
callbacks_table = dynamodb.Table(os.environ['CALLBACKS_TABLE_NAME'])

# Simple in-memory dedup cache (persists across warm Lambda invocations)
_processed_events = {}


def verify_slack_request(event: Dict[str, Any]) -> bool:
    """Verify request is from Slack using signing secret"""
    # Normalize headers to lowercase for API Gateway proxy integration
    headers = {k.lower(): v for k, v in event.get('headers', {}).items()}
    timestamp = headers.get('x-slack-request-timestamp', '')
    signature = headers.get('x-slack-signature', '')

    if not timestamp or not signature:
        print("Missing Slack headers - timestamp or signature not found")
        return False

    # Prevent replay attacks
    try:
        if abs(time.time() - int(timestamp)) > 60 * 5:
            return False
    except ValueError:
        print(f"Invalid timestamp format: {timestamp}")
        return False

    body = event.get('body', '')
    sig_basestring = f"v0:{timestamp}:{body}"

    my_signature = 'v0=' + hmac.new(
        SLACK_SIGNING_SECRET.encode(),
        sig_basestring.encode(),
        hashlib.sha256
    ).hexdigest()

    return hmac.compare_digest(my_signature, signature)


def is_duplicate_event(event_id: str) -> bool:
    """Check if we've already processed this Slack event (prevents retry duplicates)"""
    global _processed_events

    # Clean old entries (keep last 5 minutes)
    now = time.time()
    _processed_events = {k: v for k, v in _processed_events.items() if now - v < 300}

    if event_id in _processed_events:
        return True

    _processed_events[event_id] = now
    return False


def lambda_handler(event: Dict[str, Any], context: Any) -> Dict[str, Any]:
    """
    Main Lambda handler for Slack events
    """
    print(f"Received event: {json.dumps(event)}")

    body = json.loads(event.get('body', '{}'))

    # Handle Slack URL verification challenge FIRST
    if body.get('type') == 'url_verification':
        return {
            'statusCode': 200,
            'headers': {'Content-Type': 'application/json'},
            'body': json.dumps({'challenge': body['challenge']})
        }

    # Verify Slack signature
    if not verify_slack_request(event):
        return {
            'statusCode': 401,
            'body': json.dumps({'error': 'Invalid signature'})
        }

    # Handle events
    if body.get('type') == 'event_callback':
        # Deduplicate Slack retries
        event_id = body.get('event_id', '')
        if event_id and is_duplicate_event(event_id):
            print(f"Duplicate event {event_id}, skipping")
            return {'statusCode': 200, 'body': json.dumps({'ok': True})}

        slack_event = body.get('event', {})
        event_type = slack_event.get('type')

        # Ignore bot messages to prevent loops
        if slack_event.get('bot_id'):
            return {'statusCode': 200, 'body': json.dumps({'ok': True})}

        # Ignore message subtypes (edits, deletes, etc.)
        if slack_event.get('subtype'):
            return {'statusCode': 200, 'body': json.dumps({'ok': True})}

        if event_type in ['message', 'app_mention']:
            handle_message_event(slack_event)

        return {'statusCode': 200, 'body': json.dumps({'ok': True})}

    return {'statusCode': 200, 'body': json.dumps({'ok': True})}


def handle_message_event(event: Dict[str, Any]):
    """Handle new Slack messages"""
    user_id = event.get('user')
    channel = event.get('channel')
    text = event.get('text', '').strip().lower()

    if not user_id or not text:
        return

    print(f"Message from {user_id} in {channel}: {text}")

    # Check if this is a new trip planning request
    if any(keyword in text for keyword in ['plan a trip', 'plan trip', 'travel planning', 'help me plan']):
        # Check if user already has an active orchestration
        response = callbacks_table.query(
            KeyConditionExpression=boto3.dynamodb.conditions.Key('user_id').eq(user_id)
        )
        if response.get('Items'):
            slack_client = SlackClient()
            slack_client.post_message(
                channel=channel,
                text="You already have a trip planning session in progress. Please answer the current question or say 'cancel' to start over."
            )
            return

        # Start new durable function orchestration
        execution_id = f"{user_id}_{int(datetime.now().timestamp())}"
        print(f"Starting new orchestration: {execution_id}")

        slack_client = SlackClient()
        slack_client.post_message(
            channel=channel,
            text="Great! I'll help you plan an amazing trip. Let me ask you a few questions..."
        )

        try:
            response = lambda_client.invoke(
                FunctionName=ORCHESTRATOR_FUNCTION_ARN,
                InvocationType='Event',
                Payload=json.dumps({
                    'execution_id': execution_id,
                    'user_id': user_id,
                    'channel': channel
                })
            )
            print(f"Invoked orchestrator: {response['StatusCode']}")
        except Exception as e:
            print(f"Error invoking orchestrator: {e}")
            slack_client.post_message(
                channel=channel,
                text="Sorry, I encountered an error starting the trip planning. Please try again."
            )
    elif text == 'cancel':
        # Cancel active orchestration by clearing callbacks
        response = callbacks_table.query(
            KeyConditionExpression=boto3.dynamodb.conditions.Key('user_id').eq(user_id)
        )
        for item in response.get('Items', []):
            callbacks_table.delete_item(Key={'user_id': user_id, 'step': item['step']})

        slack_client = SlackClient()
        slack_client.post_message(
            channel=channel,
            text="Trip planning cancelled. Say 'plan a trip' to start over."
        )
    else:
        # This is a response to an ongoing conversation
        send_callback_to_orchestration(user_id, channel, text)


def send_callback_to_orchestration(user_id: str, channel: str, message: str):
    """Send user's message as callback to waiting orchestration"""

    try:
        # Query all callbacks for this user, get the most recent one
        response = callbacks_table.query(
            KeyConditionExpression=boto3.dynamodb.conditions.Key('user_id').eq(user_id),
            ScanIndexForward=False
        )

        items = response.get('Items', [])
        if not items:
            print(f"No active callback for user {user_id}")
            return

        # Use the most recently written callback (last item by timestamp)
        item = max(items, key=lambda x: x.get('timestamp', 0))
        callback_id = item['callback_id']
        step = item.get('step', 'unknown')
        print(f"Found callback_id for {user_id} (step: {step}): {callback_id[:50]}...")

        # Send callback to resume orchestration
        lambda_client.send_durable_execution_callback_success(
            CallbackId=callback_id,
            Result=json.dumps(message)
        )

        print(f"Sent callback successfully for {user_id}")

        # Delete the callback entry (it's been used)
        callbacks_table.delete_item(Key={'user_id': user_id, 'step': step})

    except Exception as e:
        print(f"Error sending callback: {e}")
