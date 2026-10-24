"""
S3-backed state persistence for the Sticky Notes Board.
Handles saving/loading board state keyed by clientId.
"""

import json
import logging
import os

import boto3
from botocore.exceptions import ClientError

from app.notes_board import Board

logger = logging.getLogger(__name__)

S3_BUCKET = os.environ.get("STATE_BUCKET", "")
S3_PREFIX = os.environ.get("STATE_PREFIX", "microvm-state/")


def _get_bucket() -> str:
    """Get the current S3 bucket (may be set at runtime by the /run hook)."""
    global S3_BUCKET
    return S3_BUCKET


def set_bucket(bucket: str):
    """Set the S3 bucket at runtime (called from the /run hook)."""
    global S3_BUCKET
    S3_BUCKET = bucket
    logger.info("State bucket set to: %s", bucket)


def _s3_key(client_id: str) -> str:
    """Build the S3 key for a client's board state."""
    return f"{S3_PREFIX}{client_id}/board.json"


def save_state(board: Board) -> bool:
    """Save board state to S3. Returns True on success."""
    bucket = _get_bucket()
    if not bucket:
        logger.warning("STATE_BUCKET not set, skipping state save")
        return False

    key = _s3_key(board.client_id)
    payload = json.dumps(board.to_serializable(), indent=2)

    try:
        s3 = boto3.client("s3")
        s3.put_object(
            Bucket=bucket,
            Key=key,
            Body=payload.encode("utf-8"),
            ContentType="application/json",
        )
        logger.info(
            "State saved to s3://%s/%s (%d notes)",
            bucket,
            key,
            len(board.notes),
        )
        return True
    except ClientError as e:
        logger.error("Failed to save state to S3: %s", e)
        return False


def load_state(client_id: str) -> Board | None:
    """Load board state from S3. Returns None if no state exists."""
    bucket = _get_bucket()
    if not bucket:
        logger.warning("STATE_BUCKET not set, cannot load state")
        return None

    key = _s3_key(client_id)

    try:
        s3 = boto3.client("s3")
        response = s3.get_object(Bucket=bucket, Key=key)
        data = json.loads(response["Body"].read().decode("utf-8"))
        board = Board.from_serialized(data)
        logger.info(
            "State loaded from s3://%s/%s (%d notes)",
            bucket,
            key,
            len(board.notes),
        )
        return board
    except ClientError as e:
        if e.response["Error"]["Code"] == "NoSuchKey":
            logger.info("No existing state for client '%s', starting fresh", client_id)
            return None
        logger.error("Failed to load state from S3: %s", e)
        return None
