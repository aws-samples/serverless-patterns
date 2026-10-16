# Copyright Amazon.com, Inc. or its affiliates. All Rights Reserved.
# SPDX-License-Identifier: MIT-0

"""Tests for the consumer Lambda handler.

Builds a synthetic delivery batch the way the live subscriber does: a
WITH_METADATA envelope whose `Data` is the already-decoded JSON record (the
service Protobuf-decodes against Glue before delivery), with `SystemMetadata`
carrying the Glue schema id.
"""

from consumer import handler


def _sample_record():
    return {
        "orderId": "order-xyz",
        "customerId": "cust-1",
        "amount": 42.5,
        "currency": "USD",
        "items": [{"sku": "A", "qty": 3}],
        "placedAt": "1790000000000",
    }


def _delivered_event(record, metadata):
    return {
        "Data": record,
        "Metadata": metadata,
        "SystemMetadata": {
            "ContentType": "application/protobuf",
            "aws:SchemaId": "e424651b-7a41-405d-bf05-2cae8cdf5aea",
            "aws:RegistryType": "Glue",
            "aws:DeliveryType": "LIVE",
        },
    }


def test_handler_processes_batch():
    metadata = {"eventType": "OrderPlaced", "source": "com.example.orders"}
    batch = [_delivered_event(_sample_record(), metadata)]
    result = handler.handler(batch)
    assert result["recordCount"] == 1


def test_handler_logs_record_and_metadata(caplog):
    metadata = {"eventType": "OrderPlaced", "source": "com.example.orders"}
    with caplog.at_level("INFO"):
        handler.handler([_delivered_event(_sample_record(), metadata)])
    logged = " ".join(r.getMessage() for r in caplog.records)
    assert "order-xyz" in logged            # the originating orderId
    assert "OrderPlaced" in logged          # the custom metadata
    assert "e424651b" in logged             # the Glue schema id from SystemMetadata


def test_handler_accepts_data_as_json_string():
    import json
    ev = _delivered_event(_sample_record(), {})
    ev["Data"] = json.dumps(ev["Data"])
    result = handler.handler(ev)
    assert result["recordCount"] == 1


def test_handler_accepts_single_object():
    result = handler.handler(_delivered_event(_sample_record(), {}))
    assert result["recordCount"] == 1
