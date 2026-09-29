// Copyright Amazon.com, Inc. or its affiliates. All Rights Reserved.
// SPDX-License-Identifier: MIT-0

/**
 * Tests for the consumer Lambda handler.
 *
 * Builds a synthetic delivery batch the way the live subscriber does: a
 * WITH_METADATA envelope whose `Data` is the already-decoded JSON record (the
 * service Avro-decodes against Glue before delivery), with `SystemMetadata`
 * carrying the Glue schema id.
 */

import { afterEach, describe, expect, it, vi } from "vitest";

import { handler } from "../consumer/handler.js";

function sampleRecord() {
  return {
    orderId: "order-xyz",
    customerId: "cust-1",
    amount: 42.5,
    currency: "USD",
    items: [{ sku: "A", qty: 3 }],
    placedAt: 1789601953851,
  };
}

function deliveredEvent(record: unknown, metadata: Record<string, unknown>) {
  return {
    Data: record,
    Metadata: metadata,
    SystemMetadata: {
      ContentType: "application/avro",
      "aws:SchemaId": "e424651b-7a41-405d-bf05-2cae8cdf5aea",
      "aws:RegistryType": "Glue",
      "aws:DeliveryType": "LIVE",
    },
  };
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
  it("processes a batch", async () => {
    captureLogs();
    const metadata = { eventType: "OrderPlaced", source: "com.example.orders" };
    const result = await handler([deliveredEvent(sampleRecord(), metadata)]);
    expect(result.recordCount).toBe(1);
  });

  it("logs the record, metadata, and Glue schema id", async () => {
    const lines = captureLogs();
    const metadata = { eventType: "OrderPlaced", source: "com.example.orders" };
    await handler([deliveredEvent(sampleRecord(), metadata)]);
    const logged = lines.join(" ");
    expect(logged).toContain("order-xyz"); // the originating orderId
    expect(logged).toContain("OrderPlaced"); // the custom metadata
    expect(logged).toContain("e424651b"); // the Glue schema id from SystemMetadata
  });

  it("accepts Data delivered as a JSON string", async () => {
    captureLogs();
    const ev = deliveredEvent(JSON.stringify(sampleRecord()), {});
    const result = await handler(ev);
    expect(result.recordCount).toBe(1);
  });

  it("accepts a single object", async () => {
    captureLogs();
    const result = await handler(deliveredEvent(sampleRecord(), {}));
    expect(result.recordCount).toBe(1);
  });
});
