# Copyright Amazon.com, Inc. or its affiliates. All Rights Reserved.
# SPDX-License-Identifier: MIT-0

"""Unit tests for the publisher's entry-building and result-checking logic.

These use botocore's Stubber, which validates request parameters against the
real eventsv2 service model — so a wrong field name or shape fails the test
without any live AWS call.
"""

import boto3
import pytest
from botocore.stub import Stubber

from publisher import publish

# Test-only placeholders. The region and account are arbitrary: these tests run
# fully offline against a botocore stubber and never call AWS.
TEST_REGION = "aws-region-1"
BUS_ARN = f"arn:aws:events:{TEST_REGION}:111122223333:event-busv2/avro-orders-bus/abc123def456ghi789jkl012m"
REGISTRY_ARN = f"arn:aws:glue:{TEST_REGION}:111122223333:registry/avro-orders-registry"
SCHEMA_VERSION_ID = "e424651b-7a41-405d-bf05-2cae8cdf5aea"


def _client():
    return boto3.client(
        "eventsv2",
        region_name=TEST_REGION,
        aws_access_key_id="test",
        aws_secret_access_key="test",
    )


def test_build_entry_shape():
    entry = publish.build_entry(publish.build_order("order-abc"), SCHEMA_VERSION_ID)
    assert isinstance(entry["Data"], bytes)  # raw bytes, not base64 text
    # Data is Glue-framed: 0x03, 0x00, then the schema-version UUID.
    assert entry["Data"][0] == 0x03
    assert entry["Data"][1] == 0x00
    assert entry["SystemMetadata"]["ContentType"] == "application/avro"
    assert entry["Metadata"]["eventType"] == "OrderPlaced"
    assert entry["Metadata"]["source"] == "com.example.orders"
    assert "Id" not in entry  # the updated model has no per-entry Id


def test_find_failures_treats_success_codes_as_success():
    response = {
        "FailedEntryCount": 0,
        "Entries": [
            {"SuccessCode": "PUBLISHED", "EventId": "e1"},
            {"SuccessCode": "DEDUPLICATED", "EventId": "e2"},
        ],
    }
    assert publish.find_failures(response) == []


def test_find_failures_reports_error_entries():
    response = {
        "FailedEntryCount": 1,
        "Entries": [
            {"SuccessCode": "PUBLISHED"},
            {"ErrorCode": "InvalidInput", "ErrorMessage": "bad"},
        ],
    }
    failures = publish.find_failures(response)
    assert len(failures) == 1
    assert failures[0]["index"] == 1


def test_publish_success_with_stubber():
    client = _client()
    record = publish.build_order("order-abc")
    entry = publish.build_entry(record, SCHEMA_VERSION_ID)

    stubber = Stubber(client)
    # Expected params are validated against the model: EventBusArn targets the
    # bus, each entry carries Data/SystemMetadata/Metadata (no Id), and the Glue
    # registry is named on the request.
    stubber.add_response(
        "put_raw_events",
        {"FailedEntryCount": 0, "Entries": [{"SuccessCode": "PUBLISHED", "EventId": "e1"}]},
        {
            "EventBusArn": BUS_ARN,
            "Entries": [entry],
            "SchemaRegistryConfiguration": {"RegistryUri": REGISTRY_ARN},
        },
    )
    with stubber:
        response = publish.publish(client, BUS_ARN, REGISTRY_ARN, record, SCHEMA_VERSION_ID)
    assert response["Entries"][0]["SuccessCode"] == "PUBLISHED"


def test_publish_raises_on_failed_entry():
    client = _client()
    record = publish.build_order("order-abc")
    entry = publish.build_entry(record, SCHEMA_VERSION_ID)

    stubber = Stubber(client)
    stubber.add_response(
        "put_raw_events",
        {
            "FailedEntryCount": 1,
            "Entries": [{"ErrorCode": "InvalidInput", "ErrorMessage": "bad frame"}],
        },
        {
            "EventBusArn": BUS_ARN,
            "Entries": [entry],
            "SchemaRegistryConfiguration": {"RegistryUri": REGISTRY_ARN},
        },
    )
    with stubber:
        with pytest.raises(RuntimeError, match="failed entries"):
            publish.publish(client, BUS_ARN, REGISTRY_ARN, record, SCHEMA_VERSION_ID)
