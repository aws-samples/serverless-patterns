"""
Amazon Data Firehose transform: flatten the EventBridge envelope.

EventBridge delivers events to Firehose in their raw envelope form:

    {
      "version": "0",
      "id": "e7c9...",
      "detail-type": "ClaimApproved",
      "source": "agent.claims-processor",
      "account": "111122223333",
      "time": "2026-08-17T10:00:00Z",
      "region": "us-east-1",
      "resources": [],
      "detail": { "claimId": "CLM-001", "decision": "approved" }
    }

Two things make that awkward to query in OpenSearch:

1. ``detail-type`` contains a hyphen, so it needs escaping in DQL/Lucene
   queries and cannot be referenced directly in some aggregations.
2. Business fields are nested one level down under ``detail``, so every
   dashboard filter has to be written as ``detail.claimId`` instead of
   ``claimId``.

This transform renames ``detail-type`` to ``detail_type`` and promotes the
``detail`` keys to the top level, so a search for ``claimId: "CLM-001"``
works directly.

Envelope fields win on collision: if a payload contains its own ``source``
key it is indexed as ``detail_source`` rather than overwriting the
EventBridge envelope value. Without this guard a business payload could
silently mask the real event source.
"""

import base64
import json
import logging

logger = logging.getLogger()
logger.setLevel(logging.INFO)

# Envelope keys that a business payload must never overwrite.
RESERVED_KEYS = frozenset(
    {
        "source",
        "detail_type",
        "time",
        "account",
        "region",
        "id",
        "resources",
        "version",
    }
)


def flatten(payload: dict) -> dict:
    """Flatten one EventBridge envelope into a single-level document."""
    flat = {
        "id": payload.get("id"),
        "source": payload.get("source"),
        "detail_type": payload.get("detail-type"),
        "time": payload.get("time"),
        "account": payload.get("account"),
        "region": payload.get("region"),
        "resources": payload.get("resources", []),
    }

    detail = payload.get("detail")
    if isinstance(detail, dict):
        for key, value in detail.items():
            # Prefix rather than overwrite so envelope metadata stays truthful.
            flat[f"detail_{key}" if key in RESERVED_KEYS else key] = value
    elif detail is not None:
        # Non-object detail (string, list, number) still needs to be indexed.
        flat["detail"] = detail

    # Drop keys the producer never set so OpenSearch does not index nulls.
    return {k: v for k, v in flat.items() if v is not None}


def handler(event, context):
    output = []

    for record in event["records"]:
        record_id = record["recordId"]
        try:
            raw = base64.b64decode(record["data"])
            payload = json.loads(raw)

            if not isinstance(payload, dict):
                raise ValueError(f"expected a JSON object, got {type(payload).__name__}")

            document = json.dumps(flatten(payload)) + "\n"

            output.append(
                {
                    "recordId": record_id,
                    "result": "Ok",
                    "data": base64.b64encode(document.encode("utf-8")).decode("utf-8"),
                }
            )
        except Exception as exc:
            # ProcessingFailed routes just this record to the S3 error prefix
            # and lets the rest of the batch through.
            logger.warning("Record %s failed to transform: %s", record_id, exc)
            output.append(
                {
                    "recordId": record_id,
                    "result": "ProcessingFailed",
                    "data": record["data"],
                }
            )

    ok = sum(1 for r in output if r["result"] == "Ok")
    logger.info("Transformed %d/%d records", ok, len(output))

    return {"records": output}
