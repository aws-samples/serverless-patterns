# Copyright Amazon.com, Inc. or its affiliates. All Rights Reserved.
# SPDX-License-Identifier: MIT-0

"""Shared Avro encode/decode helpers used by both the publisher and the consumer.

The same ``order_placed.avsc`` schema is loaded here and used to encode on the
publish side and decode on the consume side. Using one schema on both ends is
what proves the delivered event is byte-for-byte the same domain event that was
originally published.

Encoding uses Avro binary (the plain binary encoding, no container framing),
which is what EventBridge decodes against the Glue Schema Registry when the
payload is published with ``ContentType: application/avro``.
"""

from __future__ import annotations

import io
import json
import os
from typing import Any, Dict

import fastavro

# Resolve the schema relative to this file so it works regardless of the caller's
# working directory (the publisher runs from a checkout, the Lambda bundles it).
_SCHEMA_PATH = os.path.join(
    os.path.dirname(os.path.abspath(__file__)),
    "..",
    "schema",
    "order_placed.avsc",
)


def load_schema(path: str = _SCHEMA_PATH) -> Dict[str, Any]:
    """Load and parse the OrderPlaced Avro schema."""
    with open(path, "r", encoding="utf-8") as handle:
        return fastavro.parse_schema(json.load(handle))


# Parse once at import time; the schema does not change at runtime.
SCHEMA = load_schema()


def encode(record: Dict[str, Any], schema: Dict[str, Any] = SCHEMA) -> bytes:
    """Serialize a domain record to Avro binary bytes.

    Returns raw bytes. Do NOT base64-encode these before handing them to boto3's
    ``put_raw_events``; the SDK does the wire encoding itself.
    """
    buffer = io.BytesIO()
    fastavro.schemaless_writer(buffer, schema, record)
    return buffer.getvalue()


def decode(data: bytes, schema: Dict[str, Any] = SCHEMA) -> Dict[str, Any]:
    """Deserialize Avro binary bytes back into a domain record."""
    return fastavro.schemaless_reader(io.BytesIO(data), schema)


# --- AWS Glue Schema Registry wire format ---------------------------------
#
# When a payload is published to EventBridge with ContentType application/avro
# and decoded against a Glue registry, the bytes must carry the Glue wire
# header, not bare Avro. The frame is:
#
#     byte 0      header version, always 0x03
#     byte 1      compression: 0x00 = none, 0x05 = zlib
#     bytes 2-17  16-byte schema-version UUID (big-endian)
#     bytes 18+   the Avro binary payload
#
# EventBridge reads the header to look up the schema version, so bare Avro is
# rejected with "Malformed Glue wire format".

GLUE_HEADER_VERSION = 0x03
GLUE_COMPRESSION_NONE = 0x00


def glue_frame(avro_bytes: bytes, schema_version_id: str) -> bytes:
    """Wrap Avro bytes in the Glue Schema Registry wire format.

    `schema_version_id` is the Glue SchemaVersionId (a UUID string), obtained
    from glue:GetSchemaVersion / RegisterSchemaVersion.
    """
    import uuid as _uuid

    header = bytes([GLUE_HEADER_VERSION, GLUE_COMPRESSION_NONE])
    version_bytes = _uuid.UUID(schema_version_id).bytes  # 16 bytes, big-endian
    return header + version_bytes + avro_bytes


def glue_unframe(framed: bytes) -> "tuple[str, bytes]":
    """Split a Glue-framed payload into (schema_version_id, avro_bytes).

    Validates the header version and compression byte; raises ValueError on a
    frame that is not uncompressed Glue-format.
    """
    import uuid as _uuid

    if len(framed) < 18:
        raise ValueError("payload too short to be Glue-framed")
    if framed[0] != GLUE_HEADER_VERSION:
        raise ValueError(f"unexpected Glue header version: {framed[0]:#x}")
    if framed[1] != GLUE_COMPRESSION_NONE:
        raise ValueError(f"compressed Glue payloads are not supported here: {framed[1]:#x}")
    schema_version_id = str(_uuid.UUID(bytes=framed[2:18]))
    return schema_version_id, framed[18:]


def encode_framed(
    record: Dict[str, Any], schema_version_id: str, schema: Dict[str, Any] = SCHEMA
) -> bytes:
    """Avro-encode a record and wrap it in the Glue wire format."""
    return glue_frame(encode(record, schema), schema_version_id)


def decode_framed(framed: bytes, schema: Dict[str, Any] = SCHEMA) -> Dict[str, Any]:
    """Strip the Glue wire header and Avro-decode the payload."""
    _version_id, avro_bytes = glue_unframe(framed)
    return decode(avro_bytes, schema)
