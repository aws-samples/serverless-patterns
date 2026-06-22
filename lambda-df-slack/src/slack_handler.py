"""
Slack Event Handler - Entry point for Slack webhooks
Handles Slack events and initiates Durable Function orchestrations
"""
import json
import os
import hashlib
import hmac
import time
import logging
import boto3
import boto3.dynamodb.conditions
from typing import Dict, Any

from utils.slack_client import SlackClient
from secrets import get_slack_secrets
from dedup import is_duplicate_event

logger = logging.getLogger(__name__)

ORCHESTRATOR_FUNCTION_ARN = os.environ['ORCHESTRATOR_FUNCTION_ARN']

lambda_client = boto3.client('lambda')
dynamodb = boto3.resource('dynamodb')
callbacks_table = dynamodb.Table(os.environ['CALLBACKS_TABLE_NAME'])


def verify_slack_request(event: Dict[str, Any]) -> bool:
    """Verify request is from Slack using signing secret"""
    secrets = get_slack_secrets()
    signing_secret = secrets['SLACK_SIGNING_SECRET']

    # Normalize headers to lowercase for API Gateway proxy integration
    headers = {k.lower(): v for k, v in event.get('headers', {}).items()}
    timestamp = headers.get('x-slack-request-timestamp', '')
    signature = headers.get('x-slack-signature', '')

    if not timestamp or not signature:
        logger.warning("Missing Slack headers - timestamp or signature not found")
        return False

    # Prevent replay attacks
    try:
        if abs(time.time() - int(timestamp)) > 60 * 5:
            return False
    except ValueError:
        logger.warning("Invalid timestamp format: %s", timestamp)
        return False

    body = event.get('body', '')
    sig_basestring = f"v0:{timestamp}:{body}"

    my_signature = 'v0=' + hmac.new(
        signing_secret.encode(),
        sig_basestring.encode(),
        hashlib.sha256
    ).hexdigest()

    return hmac.compare_digest(my_signature, signature)


def lambda_handler(event: Dict[str, Any], context: Any) -> Dict[str, Any]:
    """
    Main Lambda handler for Slack events
    """
    logger.info("Received event: %s", json.dumps(event))

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
            logger.info("Duplicate event %s, skipping", event_id)
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

    logger.info("Message from %s in %s: %s", user_id, channel, text)

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
        execution_id = f"{user_id}_{int(time.time())}"
        logger.info("Starting new orchestration: %s", execution_id)

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
            logger.info("Invoked orchestrator: %s", response['StatusCode'])
        except Exception as e:
            logger.error("Error invoking orchestrator: %s", e)
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
            logger.warning("No active callback for user %s", user_id)
            return

        # Use the most recently written callback (last item by timestamp)
        item = max(items, key=lambda x: x.get('timestamp', 0))
        callback_id = item['callback_id']
        step = item.get('step', 'unknown')
        logger.info("Found callback_id for %s (step: %s): %s...", user_id, step, callback_id[:50])

        # Send callback to resume orchestration
        lambda_client.send_durable_execution_callback_success(
            CallbackId=callback_id,
            Result=json.dumps(message)
        )

        logger.info("Sent callback successfully for %s", user_id)

        # Delete the callback entry (it's been used)
        callbacks_table.delete_item(Key={'user_id': user_id, 'step': step})

    except Exception:
        logger.exception("Failed to send callback for user %s", user_id)
        raise
