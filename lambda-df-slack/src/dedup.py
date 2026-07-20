"""
DynamoDB-based Slack event deduplication.
Uses conditional writes for atomic check-and-record across concurrent Lambda instances.
"""
import os
import time
import logging

import boto3
from botocore.exceptions import ClientError

logger = logging.getLogger(__name__)

dynamodb = boto3.resource('dynamodb')
dedup_table = dynamodb.Table(os.environ['CALLBACKS_TABLE_NAME'])

# TTL for dedup entries: 5 minutes
DEDUP_TTL_SECONDS = 300


def is_duplicate_event(event_id: str) -> bool:
    """
    Check if a Slack event has already been processed using DynamoDB conditional write.
    Works correctly across concurrent Lambda instances.

    Uses a conditional PutItem that fails if the item already exists,
    providing atomic deduplication.

    Args:
        event_id: The Slack event_id to check

    Returns:
        True if event was already processed (duplicate), False if new
    """
    try:
        dedup_table.put_item(
            Item={
                'user_id': f'DEDUP#{event_id}',
                'step': 'event',
                'ttl': int(time.time()) + DEDUP_TTL_SECONDS,
            },
            ConditionExpression='attribute_not_exists(user_id)',
        )
        return False  # Successfully wrote — this is a new event
    except ClientError as e:
        if e.response['Error']['Code'] == 'ConditionalCheckFailedException':
            return True  # Already exists — duplicate
        logger.error("DynamoDB error during dedup check: %s", e)
        raise
