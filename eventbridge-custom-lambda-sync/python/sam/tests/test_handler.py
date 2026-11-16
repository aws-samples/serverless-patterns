# Copyright Amazon.com, Inc. or its affiliates. All Rights Reserved.
# SPDX-License-Identifier: MIT-0

"""Tests for the ordered-processing consumer Lambda handler.

The handler logs each delivered order in processing order. These tests assert it
processes a batch and logs the sequence numbers it received.
"""

from consumer import handler


def _delivered_event(order):
    # RAW PutEvents delivery: the payload is the classic envelope with the order
    # under `detail`.
    return {"detail": order, "detail-type": "OrderPlaced", "source": "com.example.orders"}


def _order(group, seq):
    return {
        "orderId": f"{group}-{seq:03d}",
        "orderGroup": group,
        "seq": seq,
        "customerId": "cust-1",
        "amount": 100.0 + seq,
        "currency": "USD",
        "placedAt": "2026-09-21T12:00:00Z",
    }


def test_processes_single_event():
    result = handler.handler([_delivered_event(_order("g1", 1))])
    assert result["processed"] == 1


def test_processes_batch_in_received_order(caplog):
    group = "g-order"
    batch = [_delivered_event(_order(group, seq)) for seq in (1, 2, 3)]
    with caplog.at_level("INFO"):
        result = handler.handler(batch)
    assert result["processed"] == 3

    # The per-event log lines carry seq= in the order they were processed.
    seqs = [
        int(r.getMessage().split("seq=")[1].split(" ")[0])
        for r in caplog.records
        if "Processing order" in r.getMessage()
    ]
    assert seqs == [1, 2, 3]


def test_logs_group_and_order_id(caplog):
    with caplog.at_level("INFO"):
        handler.handler([_delivered_event(_order("mygroup", 7))])
    logged = " ".join(r.getMessage() for r in caplog.records)
    assert "mygroup" in logged
    assert "seq=7" in logged
    assert "mygroup-007" in logged


def test_accepts_single_object_and_top_level_order():
    # Hand-invocation: order fields at the top level (no `detail` envelope).
    result = handler.handler(_order("g", 1))
    assert result["processed"] == 1
