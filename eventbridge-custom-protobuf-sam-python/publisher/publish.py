# Copyright Amazon.com, Inc. or its affiliates. All Rights Reserved.
# SPDX-License-Identifier: MIT-0

"""Publish a rich OrderPlaced domain event to an EventBridge custom event bus
in Protobuf binary format, decoded against an AWS Glue Schema Registry.

Usage:
    python publisher/publish.py \
        --bus-arn arn:aws:events:<region>:<account>:event-busv2/proto-orders-bus/<id> \
        --registry-arn arn:aws:glue:<region>:<account>:registry/proto-orders-registry \
        [--region <region>] [--order-id order-123]

Both ARNs can also be supplied via the BUS_ARN and REGISTRY_ARN environment
variables (see scripts/run_publish.sh, which reads them from stack outputs).

How Protobuf decoding is wired:
  * Protobuf is an open format, so the service decodes it against a schema
    registry named **on the publish request itself** via
    `SchemaRegistryConfiguration.RegistryUri`. It is not configured on the bus.
  * The registry is read with THIS caller's credentials, so the publishing IAM
    identity must be allowed to read the Glue registry (see README).

Other rules this script follows:
  * PutRawEvents carries the payload in `Data` as RAW BYTES. Do not base64-encode
    before handing to boto3 — the SDK does the wire encoding itself.
  * `ContentType` goes inside each entry's `SystemMetadata`; for Protobuf it is
    `application/protobuf`.
  * Custom keys go in a per-entry `Metadata` map (up to 100 keys); a METADATA
    subscriber filter routes on these, since a DATA filter cannot see inside
    Protobuf binary.
  * The response is a single `Entries` list aligned by index, each carrying a
    `SuccessCode` (PUBLISHED or DEDUPLICATED) or an `ErrorCode`; also check
    `FailedEntryCount`. `DEDUPLICATED` is a success, not an error.
  * The IAM namespace is `events:`, never `eventsv2:`.

The OrderPlaced message and the Glue Protobuf wire framing live in
common/protoio.py; the Protobuf bindings must be generated first with
scripts/generate.sh.
"""

from __future__ import annotations

import argparse
import os
import random
import sys
import time
from typing import Any, Dict, List, Optional

import boto3
from botocore.exceptions import ClientError

# Make the sibling `common` package importable when run as a script.
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), ".."))

from common import protoio  # noqa: E402

CONTENT_TYPE_PROTOBUF = "application/protobuf"


def build_entry(message: Any, schema_version_id: str) -> Dict[str, Any]:
    """Build a single PutRawEvents entry from an OrderPlaced protobuf message.

    `Data` is Protobuf bytes wrapped in the Glue Schema Registry wire format (a
    header naming the schema-version UUID plus a message-index element, then the
    Protobuf binary). Bare Protobuf is rejected by the service. `Metadata`
    carries the "enhanced" custom keys a METADATA-scoped subscriber filter can
    route on.
    """
    return {
        "Data": protoio.encode_framed(message, schema_version_id),
        "SystemMetadata": {"ContentType": CONTENT_TYPE_PROTOBUF},
        "Metadata": {
            "eventType": "OrderPlaced",
            "source": "com.example.orders",
            "schemaVersion": "1",
        },
    }


def resolve_schema_version_id(registry_arn: str, region: Optional[str]) -> str:
    """Look up the latest AVAILABLE schema-version UUID for OrderPlaced.

    The registry ARN's name is used to address the schema; the version id is what
    the Glue wire header must carry so EventBridge can decode the payload.
    """
    registry_name = registry_arn.split("/")[-1]
    glue = boto3.client("glue", region_name=region)
    resp = glue.get_schema_version(
        SchemaId={"RegistryName": registry_name, "SchemaName": "OrderPlaced"},
        SchemaVersionNumber={"LatestVersion": True},
    )
    return resp["SchemaVersionId"]


def find_failures(response: Dict[str, Any]) -> List[Dict[str, Any]]:
    """Return the failed per-entry results.

    The response is a single `Entries` list aligned by request index; an entry
    with an `ErrorCode` failed. A `SuccessCode` of PUBLISHED or DEDUPLICATED is a
    success, so it is not counted here.
    """
    failures: List[Dict[str, Any]] = []
    for index, entry in enumerate(response.get("Entries", [])):
        if entry.get("ErrorCode"):
            failures.append({"index": index, **entry})
    return failures


def put_raw_with_backoff(
    client,
    bus_arn: str,
    registry_arn: str,
    entries: List[Dict[str, Any]],
    attempts: int = 5,
) -> Dict[str, Any]:
    """Call put_raw_events, retrying ThrottlingException with backoff + jitter.

    Targets the bus directly via `EventBusArn` and names the Glue registry on the
    request so the service can decode the Protobuf payload.
    """
    delay = 0.2
    for attempt in range(attempts):
        try:
            return client.put_raw_events(
                EventBusArn=bus_arn,
                Entries=entries,
                SchemaRegistryConfiguration={"RegistryUri": registry_arn},
            )
        except ClientError as error:
            code = error.response["Error"]["Code"]
            if code != "ThrottlingException" or attempt == attempts - 1:
                raise
            time.sleep(delay + random.uniform(0, delay))
            delay *= 2
    raise RuntimeError("exhausted retry attempts without a response")


def publish(
    client,
    bus_arn: str,
    registry_arn: str,
    message: Any,
    schema_version_id: str,
) -> Dict[str, Any]:
    """Encode one message and publish it to the bus; raise on any failure."""
    entries = [build_entry(message, schema_version_id)]
    response = put_raw_with_backoff(client, bus_arn, registry_arn, entries)

    failures = find_failures(response)
    if failures or response.get("FailedEntryCount"):
        raise RuntimeError(f"publish had failed entries: {failures}")
    return response


def _parse_args(argv: List[str]) -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Publish a Protobuf OrderPlaced event.")
    parser.add_argument("--bus-arn", default=os.environ.get("BUS_ARN"))
    parser.add_argument("--registry-arn", default=os.environ.get("REGISTRY_ARN"))
    parser.add_argument("--region", default=os.environ.get("AWS_REGION"))
    parser.add_argument("--order-id", default=f"order-{int(time.time())}")
    return parser.parse_args(argv)


def main(argv: List[str]) -> int:
    args = _parse_args(argv)
    if not args.bus_arn or not args.registry_arn:
        print(
            "error: --bus-arn and --registry-arn are required "
            "(or set BUS_ARN and REGISTRY_ARN).",
            file=sys.stderr,
        )
        return 2

    client = boto3.client("eventsv2", region_name=args.region)
    schema_version_id = resolve_schema_version_id(args.registry_arn, args.region)
    message = protoio.build_order(args.order_id)
    response = publish(
        client, args.bus_arn, args.registry_arn, message, schema_version_id
    )

    entry = response["Entries"][0]
    print(
        f"Published orderId={message.order_id} "
        f"-> SuccessCode={entry.get('SuccessCode')} EventId={entry.get('EventId')}"
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main(sys.argv[1:]))
