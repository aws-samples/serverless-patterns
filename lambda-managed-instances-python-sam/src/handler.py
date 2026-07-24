"""
API handler running on Lambda Managed Instances.

This function runs on EC2 instances managed by AWS, enabling:
- Multi-concurrent invocations per execution environment
- EC2 Savings Plans / Reserved Instance pricing
- Access to Graviton4, network-optimized, and specialized instance types

Important: With multi-concurrency, your code must be thread-safe.
Global state is shared across concurrent invocations.
"""

import json
import logging
import threading
from datetime import datetime, timezone

logger = logging.getLogger()
logger.setLevel(logging.INFO)

# Thread-safe counter for demonstrating multi-concurrency
_lock = threading.Lock()
_invocation_count = 0


def lambda_handler(event: dict, context) -> dict:
    """
    Handle API request on a Managed Instance.

    Input event:
    {
        "name": "World",
        "operation": "greet"
    }
    """
    global _invocation_count

    with _lock:
        _invocation_count += 1
        count = _invocation_count

    name = event.get("name", "Managed Instances")
    operation = event.get("operation", "greet")

    response = {
        "message": f"Hello, {name}! Running on Lambda Managed Instances.",
        "operation": operation,
        "invocation_count": count,
        "timestamp": datetime.now(timezone.utc).isoformat(),
        "environment": {
            "function_name": context.function_name,
            "function_version": context.function_version,
            "memory_limit_mb": context.memory_limit_in_mb,
            "remaining_time_ms": context.get_remaining_time_in_millis(),
        },
    }

    logger.info(
        "Processed request #%d for operation=%s on version=%s",
        count,
        operation,
        context.function_version,
    )

    return {
        "statusCode": 200,
        "headers": {"Content-Type": "application/json"},
        "body": json.dumps(response),
    }
