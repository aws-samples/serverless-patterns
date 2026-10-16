# Copyright Amazon.com, Inc. or its affiliates. All Rights Reserved.
# SPDX-License-Identifier: MIT-0

"""Publish a sequence of OrderPlaced events (JSON) that share one event group,
to an EventBridge custom event bus whose FIFO subscriber invokes a Lambda
synchronously and processes the group in order.

Usage:
    python publisher/publish.py \
        --bus-arn arn:aws:events:<region>:<account>:event-busv2/sync-orders-bus/<id> \
        [--region <region>] [--count 5] [--group order-group-<ts>]

The bus ARN can also come from the BUS_ARN environment variable (see
scripts/run_publish.sh, which looks the bus up by name).

Ordered processing:
  * Every event in one run shares a single `EventGroupId` (SystemMetadata), so
    the FIFO subscriber processes them in order within that group.
  * Each event carries a monotonically increasing `seq` (1..count). The consumer
    logs `seq` as it processes, so the CloudWatch log shows 1, 2, 3, ... in
    order — proof the synchronous FIFO subscriber confirmed each event before
    delivering the next.

Notes:
  * This publishes JSON with `PutEvents`; no schema registry is involved.
  * The response is a single `Entries` list; check `FailedEntryCount` and each
    entry's `SuccessCode`/`ErrorCode`. `DEDUPLICATED` is a success.
  * The IAM namespace is `events:`, never `eventsv2:`.
"""

from __future__ import annotations

import argparse
import json
import os
import random
import sys
import time
from typing import Any, Dict, List

import boto3
from botocore.exceptions import ClientError

SOURCE = "com.example.orders"
DETAIL_TYPE = "OrderPlaced"


def build_order(group: str, seq: int) -> Dict[str, Any]:
    """Construct one OrderPlaced record in a group with a sequence number."""
    return {
        "orderId": f"{group}-{seq:03d}",
        "orderGroup": group,
        "seq": seq,
        "customerId": "cust-987",
        "amount": 100.0 + seq,
        "currency": "USD",
        "placedAt": "2026-09-21T12:00:00Z",
    }


def build_entry(order: Dict[str, Any], group: str) -> Dict[str, Any]:
    """Build a PutEvents entry, grouping the event for FIFO ordering.

    SystemMetadata.EventGroupId is what the FIFO subscriber orders within.
    """
    return {
        "Source": SOURCE,
        "DetailType": DETAIL_TYPE,
        "Detail": json.dumps(order),
        "SystemMetadata": {"EventGroupId": group},
    }


def find_failures(response: Dict[str, Any]) -> List[Dict[str, Any]]:
    """Return the failed per-entry results (an entry with an ErrorCode)."""
    failures: List[Dict[str, Any]] = []
    for index, entry in enumerate(response.get("Entries", [])):
        if entry.get("ErrorCode"):
            failures.append({"index": index, **entry})
    return failures


def put_events_with_backoff(
    client, bus_arn: str, entries: List[Dict[str, Any]], attempts: int = 5
) -> Dict[str, Any]:
    """Call put_events, retrying ThrottlingException with backoff + jitter."""
    delay = 0.2
    for attempt in range(attempts):
        try:
            return client.put_events(EventBusArn=bus_arn, Entries=entries)
        except ClientError as error:
            code = error.response["Error"]["Code"]
            if code != "ThrottlingException" or attempt == attempts - 1:
                raise
            time.sleep(delay + random.uniform(0, delay))
            delay *= 2
    raise RuntimeError("exhausted retry attempts without a response")


def publish_one(client, bus_arn: str, order: Dict[str, Any], group: str) -> Dict[str, Any]:
    """Publish a single grouped order; raise on a per-entry failure."""
    response = put_events_with_backoff(client, bus_arn, [build_entry(order, group)])
    failures = find_failures(response)
    if failures or response.get("FailedEntryCount"):
        raise RuntimeError(f"publish had failed entries: {failures}")
    return response


def publish_sequence(client, bus_arn: str, group: str, count: int) -> List[str]:
    """Publish `count` ordered events sharing `group`. Returns the event ids."""
    event_ids = []
    for seq in range(1, count + 1):
        order = build_order(group, seq)
        response = publish_one(client, bus_arn, order, group)
        entry = response["Entries"][0]
        event_ids.append(entry.get("EventId"))
        print(f"Published seq={seq} orderId={order['orderId']} "
              f"-> SuccessCode={entry.get('SuccessCode')} EventId={entry.get('EventId')}")
    return event_ids


def _parse_args(argv: List[str]) -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Publish an ordered sequence of OrderPlaced events.")
    parser.add_argument("--bus-arn", default=os.environ.get("BUS_ARN"))
    parser.add_argument("--region", default=os.environ.get("AWS_REGION"))
    parser.add_argument("--count", type=int, default=5, help="Number of ordered events to publish.")
    parser.add_argument("--group", default=None, help="EventGroupId shared by the sequence.")
    return parser.parse_args(argv)


def main(argv: List[str]) -> int:
    args = _parse_args(argv)
    if not args.bus_arn:
        print("error: --bus-arn is required (or set BUS_ARN).", file=sys.stderr)
        return 2
    if args.count < 1:
        print("error: --count must be >= 1.", file=sys.stderr)
        return 2

    group = args.group or f"order-group-{int(time.time())}"
    client = boto3.client("eventsv2", region_name=args.region)

    print(f"Publishing {args.count} ordered events in group '{group}'...")
    publish_sequence(client, args.bus_arn, group, args.count)
    print(f"\nThe FIFO subscriber invokes the consumer synchronously and processes "
          f"group '{group}' in order. Check the consumer log to see seq=1..{args.count} "
          f"processed in sequence.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main(sys.argv[1:]))
