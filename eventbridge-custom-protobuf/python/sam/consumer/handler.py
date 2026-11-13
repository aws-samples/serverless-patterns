# Copyright Amazon.com, Inc. or its affiliates. All Rights Reserved.
# SPDX-License-Identifier: MIT-0

"""Consumer Lambda: log the OrderPlaced events delivered by the subscriber to
CloudWatch, proving the delivered event is the same domain event that was
originally published.

Delivery shape:
  * A subscriber's Lambda target receives a **batch**: the event is a JSON array
    of delivered events, not a single object. The handler iterates it.
  * This subscriber uses a WITH_METADATA transformer, so each delivered event has
    the three-part envelope: `Data` (the payload), `Metadata` (the publisher's
    custom keys), and `SystemMetadata` (service-assigned fields).
  * The payload was published as Protobuf (ContentType application/protobuf)
    against a Glue Schema Registry. **EventBridge decodes the Protobuf server-side
    and delivers `Data` as an already-decoded JSON object** — the handler does NOT
    Protobuf-decode. `SystemMetadata` carries `aws:SchemaId` and
    `aws:RegistryType: Glue` recording the decode.

Because the service does the Protobuf decode, this function needs no Protobuf
library and no bundled schema.
"""

from __future__ import annotations

import json
import logging
from typing import Any, Dict, List

logger = logging.getLogger()
logger.setLevel(logging.INFO)


def _normalize_batch(event: Any) -> List[Dict[str, Any]]:
    """Return the delivered events as a list.

    The subscriber delivers a JSON array; tolerate a single object too so the
    handler is easy to invoke by hand.
    """
    if isinstance(event, list):
        return event
    if isinstance(event, dict):
        return [event]
    raise ValueError(f"unexpected event type: {type(event)!r}")


def _extract_record(item: Dict[str, Any]) -> Dict[str, Any]:
    """Return the decoded domain record from one delivered event.

    `Data` arrives as a JSON object (the service already Protobuf-decoded it). If
    it is delivered as a JSON string, parse it; anything else is unexpected.
    """
    data = item.get("Data")
    if isinstance(data, dict):
        return data
    if isinstance(data, str):
        return json.loads(data)
    raise ValueError(f"unexpected Data type: {type(data)!r}")


def handler(event: Any, context: Any = None) -> Dict[str, Any]:
    """Lambda entry point. Logs each delivered OrderPlaced event."""
    delivered = _normalize_batch(event)
    records: List[Dict[str, Any]] = []

    for index, item in enumerate(delivered):
        record = _extract_record(item)
        metadata = item.get("Metadata", {})
        system_metadata = item.get("SystemMetadata", {})

        logger.info(
            "OrderPlaced[%d]: %s | metadata=%s | schemaId=%s registry=%s",
            index,
            json.dumps(record, default=str),
            json.dumps(metadata, default=str),
            system_metadata.get("aws:SchemaId"),
            system_metadata.get("aws:RegistryType"),
        )
        records.append(record)

    return {"recordCount": len(records)}
