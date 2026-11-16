# Copyright Amazon.com, Inc. or its affiliates. All Rights Reserved.
# SPDX-License-Identifier: MIT-0

"""Round-trip test for the shared Avro encode/decode helper."""

from datetime import datetime, timezone

from common import avroio


def _sample_record():
    # timestamp-millis logical type round-trips as a timezone-aware datetime,
    # so build the expected value the same way fastavro will return it.
    placed_at = datetime(2026, 9, 14, 12, 0, 0, tzinfo=timezone.utc)
    return {
        "orderId": "order-123",
        "customerId": "cust-987",
        "amount": 129.95,
        "currency": "USD",
        "items": [
            {"sku": "SKU-1", "qty": 2},
            {"sku": "SKU-2", "qty": 1},
        ],
        "placedAt": placed_at,
    }


def test_encode_produces_bytes():
    encoded = avroio.encode(_sample_record())
    assert isinstance(encoded, bytes)
    assert len(encoded) > 0


def test_glue_frame_round_trip():
    version_id = "e424651b-7a41-405d-bf05-2cae8cdf5aea"
    framed = avroio.encode_framed(_sample_record(), version_id)
    # Header: 0x03, 0x00, then the 16-byte UUID.
    assert framed[0] == 0x03
    assert framed[1] == 0x00
    got_version, _avro = avroio.glue_unframe(framed)
    assert got_version == version_id
    decoded = avroio.decode_framed(framed)
    assert decoded["orderId"] == _sample_record()["orderId"]


def test_round_trip_is_lossless():
    original = _sample_record()
    decoded = avroio.decode(avroio.encode(original))

    assert decoded["orderId"] == original["orderId"]
    assert decoded["customerId"] == original["customerId"]
    assert decoded["amount"] == original["amount"]
    assert decoded["currency"] == original["currency"]
    assert decoded["items"] == original["items"]
    # fastavro returns timestamp-millis as an aware datetime equal to the input.
    assert decoded["placedAt"] == original["placedAt"]
