# Copyright Amazon.com, Inc. or its affiliates. All Rights Reserved.
# SPDX-License-Identifier: MIT-0

"""Round-trip and Glue-framing tests for the shared Protobuf helper.

Skipped automatically (see tests/conftest.py) if the bindings have not been
generated or protobuf-py is not installed.
"""

from common import protoio

SCHEMA_VERSION_ID = "e424651b-7a41-405d-bf05-2cae8cdf5aea"


def test_encode_produces_bytes():
    encoded = protoio.encode(protoio.build_order("order-1"))
    assert isinstance(encoded, bytes)
    assert len(encoded) > 0


def test_round_trip_is_lossless():
    original = protoio.build_order("order-abc")
    decoded = protoio.decode(protoio.encode(original))

    assert decoded.order_id == "order-abc"
    assert decoded.customer_id == original.customer_id
    assert decoded.amount == original.amount
    assert decoded.currency == original.currency
    assert [(i.sku, i.qty) for i in decoded.items] == [(i.sku, i.qty) for i in original.items]
    assert decoded.placed_at == original.placed_at


def test_glue_frame_layout():
    framed = protoio.encode_framed(protoio.build_order("order-1"), SCHEMA_VERSION_ID)
    assert framed[0] == 0x03            # header version
    assert framed[1] == 0x00            # no compression
    # Message index for OrderPlaced. In order_placed.proto the messages sort
    # lexicographically as OrderItem(0) < OrderPlaced(1), so the index is 1.
    assert framed[18] == 0x01


def test_message_index_matches_glue_rule():
    # Glue sorts message full names lexicographically; OrderPlaced is second.
    assert protoio._message_index("com.example.orders.OrderPlaced") == 1
    assert protoio._message_index("com.example.orders.OrderItem") == 0


def test_glue_frame_round_trip():
    original = protoio.build_order("order-xyz")
    framed = protoio.encode_framed(original, SCHEMA_VERSION_ID)
    version_id, proto_bytes = protoio.glue_unframe(framed)
    assert version_id == SCHEMA_VERSION_ID
    # The stripped payload is exactly the inner protobuf encoding.
    assert proto_bytes == protoio.encode(original)
    decoded = protoio.decode_framed(framed)
    assert decoded.order_id == "order-xyz"
