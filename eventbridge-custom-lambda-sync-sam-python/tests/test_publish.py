# Copyright Amazon.com, Inc. or its affiliates. All Rights Reserved.
# SPDX-License-Identifier: MIT-0

"""Unit tests for the publisher's entry-building, grouping, and result-checking.

Uses botocore's Stubber, which validates request parameters against the real
eventsv2 service model — so a wrong field name or shape (e.g. the EventGroupId
nesting) fails without a live call.
"""

import json

import boto3
import pytest
from botocore.stub import Stubber

from publisher import publish

# Test-only placeholders. The region and account are arbitrary: these tests run
# fully offline against a botocore stubber and never call AWS.
TEST_REGION = "aws-region-1"
BUS_ARN = f"arn:aws:events:{TEST_REGION}:111122223333:event-busv2/sync-orders-bus/abc123def456ghi789jkl012m"


def _client():
    return boto3.client(
        "eventsv2",
        region_name=TEST_REGION,
        aws_access_key_id="test",
        aws_secret_access_key="test",
    )


def test_build_order_carries_group_and_seq():
    order = publish.build_order("grp", 3)
    assert order["orderGroup"] == "grp"
    assert order["seq"] == 3
    assert order["orderId"] == "grp-003"


def test_build_entry_sets_event_group_id():
    entry = publish.build_entry(publish.build_order("grp", 1), "grp")
    assert entry["Source"] == "com.example.orders"
    assert entry["DetailType"] == "OrderPlaced"
    assert entry["SystemMetadata"]["EventGroupId"] == "grp"
    assert json.loads(entry["Detail"])["seq"] == 1


def test_find_failures_empty_on_success():
    assert publish.find_failures({"FailedEntryCount": 0, "Entries": [{"EventId": "e1"}]}) == []


def test_find_failures_reports_errors():
    resp = {"FailedEntryCount": 1, "Entries": [{"ErrorCode": "ValidationError", "ErrorMessage": "bad"}]}
    failures = publish.find_failures(resp)
    assert len(failures) == 1 and failures[0]["index"] == 0


def test_publish_sequence_publishes_each_in_order():
    client = _client()
    group = "grp"
    count = 3

    stubber = Stubber(client)
    for seq in range(1, count + 1):
        entry = publish.build_entry(publish.build_order(group, seq), group)
        stubber.add_response(
            "put_events",
            {"FailedEntryCount": 0, "Entries": [{"EventId": f"e{seq}"}]},
            {"EventBusArn": BUS_ARN, "Entries": [entry]},
        )
    with stubber:
        event_ids = publish.publish_sequence(client, BUS_ARN, group, count)
    assert event_ids == ["e1", "e2", "e3"]


def test_publish_one_raises_on_failed_entry():
    client = _client()
    order = publish.build_order("grp", 1)
    entry = publish.build_entry(order, "grp")

    stubber = Stubber(client)
    stubber.add_response(
        "put_events",
        {"FailedEntryCount": 1, "Entries": [{"ErrorCode": "ValidationError", "ErrorMessage": "bad"}]},
        {"EventBusArn": BUS_ARN, "Entries": [entry]},
    )
    with stubber:
        with pytest.raises(RuntimeError, match="failed entries"):
            publish.publish_one(client, BUS_ARN, order, "grp")
