// Copyright Amazon.com, Inc. or its affiliates. All Rights Reserved.
// SPDX-License-Identifier: MIT-0

/**
 * Tests for the ordered-processing consumer Lambda handler.
 *
 * The handler logs each delivered order in processing order. These tests assert
 * it processes a batch and logs the sequence numbers it received, in order.
 */

import { afterEach, describe, expect, it, vi } from "vitest";

import { handler } from "../consumer/handler.js";

interface Order {
  orderId: string;
  orderGroup: string;
  seq: number;
  customerId: string;
  amount: number;
  currency: string;
  placedAt: string;
  [key: string]: unknown;
}

function order(group: string, seq: number): Order {
  return {
    orderId: `${group}-${String(seq).padStart(3, "0")}`,
    orderGroup: group,
    seq,
    customerId: "cust-1",
    amount: 100.0 + seq,
    currency: "USD",
    placedAt: "2026-09-21T12:00:00Z",
  };
}

// RAW PutEvents delivery: the payload is the classic envelope with the order
// under `detail`.
function deliveredEvent(o: Order) {
  return { detail: o, "detail-type": "OrderPlaced", source: "com.example.orders" };
}

function captureLogs() {
  const lines: string[] = [];
  vi.spyOn(console, "log").mockImplementation((...args: unknown[]) => {
    lines.push(args.join(" "));
  });
  return lines;
}

afterEach(() => {
  vi.restoreAllMocks();
});

describe("handler", () => {
  it("processes a single event", async () => {
    captureLogs();
    const result = await handler([deliveredEvent(order("g1", 1))]);
    expect(result.processed).toBe(1);
  });

  it("processes a batch in received order", async () => {
    const lines = captureLogs();
    const group = "g-order";
    const batch = [1, 2, 3].map((seq) => deliveredEvent(order(group, seq)));
    const result = await handler(batch);
    expect(result.processed).toBe(3);

    const seqs = lines
      .filter((l) => l.includes("Processing order"))
      .map((l) => Number.parseInt(l.split("seq=")[1].split(" ")[0], 10));
    expect(seqs).toEqual([1, 2, 3]);
  });

  it("logs group, seq, and orderId", async () => {
    const lines = captureLogs();
    await handler([deliveredEvent(order("mygroup", 7))]);
    const logged = lines.join(" ");
    expect(logged).toContain("mygroup");
    expect(logged).toContain("seq=7");
    expect(logged).toContain("mygroup-007");
  });

  it("accepts a single object with top-level order fields", async () => {
    captureLogs();
    // Hand-invocation: order fields at the top level (no `detail` envelope).
    const result = await handler(order("g", 1));
    expect(result.processed).toBe(1);
  });
});
