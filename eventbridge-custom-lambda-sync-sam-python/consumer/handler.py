# Copyright Amazon.com, Inc. or its affiliates. All Rights Reserved.
# SPDX-License-Identifier: MIT-0

"""Consumer Lambda: the SYNCHRONOUS, ordered target of an EventBridge
custom-event-bus subscriber. It logs each delivered order to CloudWatch in the
order it is processed.

Why this demonstrates ordered processing:
  * The subscriber is FIFO (Type = FIFO) and invokes this function synchronously
    (InvocationType = REQUEST_RESPONSE). EventBridge waits for the function to
    confirm successful processing of each event before acknowledging it and
    moving on to the next event in the same event group.
  * That synchronous confirmation is what makes ordered, reliable, direct-to-
    Lambda processing possible — it removes the pattern of putting an SQS queue
    between the bus and Lambda just to get reliability and back-pressure.
  * The publisher sends a sequence of orders that share one EventGroupId, each
    carrying a monotonically increasing `seq`. This handler logs `seq` as it
    processes each one; the log shows them in order (1, 2, 3, ...), proving the
    bus delivered and confirmed them one at a time, in sequence.

Delivery shape:
  * A Lambda target receives a BATCH — a JSON array of delivered events — so the
    handler iterates it.
  * With the default RAW transformer and a PutEvents publish, each element is the
    classic envelope, so the order fields are under `detail`. The handler
    tolerates top-level fields too, for easy hand-invocation.

boto3 is provided by the Lambda runtime; this function needs no bundled deps.
"""

from __future__ import annotations

import json
import logging
from typing import Any, Dict, List

logger = logging.getLogger()
logger.setLevel(logging.INFO)


def _normalize_batch(event: Any) -> List[Dict[str, Any]]:
    if isinstance(event, list):
        return event
    if isinstance(event, dict):
        return [event]
    raise ValueError(f"unexpected event type: {type(event)!r}")


def _extract_order(item: Dict[str, Any]) -> Dict[str, Any]:
    """Return the order fields from one delivered event.

    A RAW PutEvents payload is the classic envelope, so the order is under
    `detail`. Fall back to the top level for hand-invocation.
    """
    if isinstance(item.get("detail"), dict):
        return item["detail"]
    return item


def handler(event: Any, context: Any = None) -> Dict[str, Any]:
    """Lambda entry point. Logs each delivered order in processing order."""
    delivered = _normalize_batch(event)
    processed = []

    for batch_index, raw in enumerate(delivered):
        order = _extract_order(raw)
        order_id = order.get("orderId")
        group = order.get("orderGroup")
        seq = order.get("seq")

        logger.info(
            "Processing order group=%s seq=%s orderId=%s (batchIndex=%d)",
            group, seq, order_id, batch_index,
        )
        processed.append({"orderId": order_id, "group": group, "seq": seq})

    logger.info("Processed %d order(s): %s", len(processed), json.dumps(processed, default=str))
    return {"processed": len(processed)}
