# Copyright Amazon.com, Inc. or its affiliates. All Rights Reserved.
# SPDX-License-Identifier: MIT-0

"""Shared Protobuf encode/decode + Glue wire-format helpers.

The publisher uses these to turn an OrderPlaced domain object into the bytes
EventBridge expects in a PutRawEvents `Data` field (ContentType
application/protobuf), decoded server-side against the Glue Schema Registry.

The generated bindings (common/gen/order_placed_pb.py) are produced by
scripts/generate.sh from proto/order_placed.proto. Import them lazily with a
clear error if they are missing, so a fresh clone that forgot to generate gets
an actionable message instead of an ImportError.

    Inner encoding : OrderPlaced.to_binary()  (bufbuild protobuf-py)
    Wire framing   : the AWS Glue Schema Registry Protobuf frame (see below)

IMPORTANT — the exact Glue Protobuf wire frame is verified against the live
service (see README "Glue wire format"). The Avro frame is
`0x03` + compression byte + 16-byte schema-version UUID + Avro bytes. The Glue
*Protobuf* SerDe additionally writes a message-index element between the header
and the payload. The layout below is applied and confirmed end-to-end in the
sample's live verification; if AWS changes the framing, this is the one place to
adjust.
"""

from __future__ import annotations

import uuid as _uuid
from typing import Any, Tuple


def _load_generated():
    """Import the generated bindings, or raise a helpful error if not built."""
    try:
        from common.gen import order_placed_pb  # type: ignore
    except ModuleNotFoundError as exc:  # pragma: no cover - exercised via message
        raise ModuleNotFoundError(
            "Protobuf bindings not found. Generate them first:\n"
            "  scripts/generate.sh\n"
            "(see the README prerequisites)."
        ) from exc
    return order_placed_pb


# --- inner Protobuf encode / decode ---------------------------------------

def build_order(order_id: str) -> Any:
    """Construct a sample OrderPlaced protobuf message."""
    m = _load_generated()
    return m.OrderPlaced(
        order_id=order_id,
        customer_id="cust-987",
        amount=129.95,
        currency="USD",
        items=[m.OrderItem(sku="SKU-1", qty=2), m.OrderItem(sku="SKU-2", qty=1)],
        placed_at=1_790_000_000_000,
    )


def encode(message: Any) -> bytes:
    """Serialize an OrderPlaced message to raw Protobuf wire bytes."""
    return message.to_binary()


def decode(data: bytes) -> Any:
    """Deserialize raw Protobuf wire bytes into an OrderPlaced message."""
    m = _load_generated()
    return m.OrderPlaced.from_binary(data)


# --- AWS Glue Schema Registry wire format (Protobuf) ----------------------
#
# Frame layout (uncompressed):
#   byte 0        header version, always 0x03
#   byte 1        compression: 0x00 = none, 0x05 = zlib
#   bytes 2-17    16-byte schema-version UUID (big-endian)
#   bytes 18..    message-index (unsigned varint), then the Protobuf payload
#
# The message-index identifies WHICH message type in the .proto the payload is.
# Glue assigns indices by: breadth-first (level-order) traversal of all message
# types in the file, sorted lexicographically by full name, position in that
# list. It is written as a plain unsigned varint (CodedOutputStream
# writeUInt32NoTag) — NOT zig-zag, despite a misleading comment in the AWS SerDe.
# Ref: awslabs/aws-glue-schema-registry MessageIndexFinder + ProtobufWireFormatEncoder.
#
# Getting this wrong does not fail the publish — the service decodes the bytes
# against the WRONG message type and delivers a garbled record. (Our first live
# test framed index 0, which is OrderItem, so OrderPlaced arrived as
# {"sku": "<orderId>", "qty": 0}.) So we compute the index the same way Glue does
# rather than hardcode it.

GLUE_HEADER_VERSION = 0x03
GLUE_COMPRESSION_NONE = 0x00

# The full names of the two messages in order_placed.proto, used to compute the
# Glue message index for OrderPlaced without importing protobuf descriptor APIs.
_MESSAGE_FULL_NAMES = [
    "com.example.orders.OrderItem",
    "com.example.orders.OrderPlaced",
]
_ORDER_PLACED_FULL_NAME = "com.example.orders.OrderPlaced"


def _message_index(full_name: str) -> int:
    """Replicate Glue's message-index assignment: lexicographically sorted
    full names, index = position. (Level-order traversal is irrelevant here
    because there are no nested message types.)"""
    ordered = sorted(_MESSAGE_FULL_NAMES)
    return ordered.index(full_name)


def _encode_varint(value: int) -> bytes:
    """Encode a non-negative int as an unsigned LEB128 varint."""
    out = bytearray()
    while True:
        byte = value & 0x7F
        value >>= 7
        if value:
            out.append(byte | 0x80)
        else:
            out.append(byte)
            return bytes(out)


def _decode_varint(data: bytes, offset: int) -> Tuple[int, int]:
    """Decode an unsigned varint at `offset`; return (value, new_offset)."""
    result = 0
    shift = 0
    pos = offset
    while True:
        byte = data[pos]
        result |= (byte & 0x7F) << shift
        pos += 1
        if not (byte & 0x80):
            return result, pos
        shift += 7


def glue_frame(proto_bytes: bytes, schema_version_id: str) -> bytes:
    """Wrap raw Protobuf bytes in the Glue Schema Registry Protobuf wire format.

    `schema_version_id` is the Glue SchemaVersionId (a UUID string) from
    glue:GetSchemaVersion. The message index for OrderPlaced is computed the way
    Glue assigns it.
    """
    header = bytes([GLUE_HEADER_VERSION, GLUE_COMPRESSION_NONE])
    version_bytes = _uuid.UUID(schema_version_id).bytes  # 16 bytes, big-endian
    index_bytes = _encode_varint(_message_index(_ORDER_PLACED_FULL_NAME))
    return header + version_bytes + index_bytes + proto_bytes


def glue_unframe(framed: bytes) -> Tuple[str, bytes]:
    """Split a Glue-framed Protobuf payload into (schema_version_id, proto_bytes).

    Validates the header, reads the schema-version UUID, and strips the
    message-index varint. Raises ValueError on an unexpected frame.
    """
    if len(framed) < 19:
        raise ValueError("payload too short to be a Glue Protobuf frame")
    if framed[0] != GLUE_HEADER_VERSION:
        raise ValueError(f"unexpected Glue header version: {framed[0]:#x}")
    if framed[1] != GLUE_COMPRESSION_NONE:
        raise ValueError(f"compressed Glue payloads are not supported here: {framed[1]:#x}")
    schema_version_id = str(_uuid.UUID(bytes=framed[2:18]))
    _index, payload_offset = _decode_varint(framed, 18)
    return schema_version_id, framed[payload_offset:]


def encode_framed(message: Any, schema_version_id: str) -> bytes:
    """Protobuf-encode a message and wrap it in the Glue Protobuf wire format."""
    return glue_frame(encode(message), schema_version_id)


def decode_framed(framed: bytes) -> Any:
    """Strip the Glue wire header/index and Protobuf-decode the payload."""
    _version_id, proto_bytes = glue_unframe(framed)
    return decode(proto_bytes)
