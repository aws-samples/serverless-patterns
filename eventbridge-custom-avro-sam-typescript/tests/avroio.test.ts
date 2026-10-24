// Copyright Amazon.com, Inc. or its affiliates. All Rights Reserved.
// SPDX-License-Identifier: MIT-0

/** Round-trip and Glue-framing tests for the shared Avro helper. */

import { describe, expect, it } from "vitest";

import {
  decode,
  decodeFramed,
  encode,
  encodeFramed,
  glueUnframe,
  type Order,
} from "../common/avroio.js";

function sampleRecord(): Order {
  return {
    orderId: "order-123",
    customerId: "cust-987",
    amount: 129.95,
    currency: "USD",
    items: [
      { sku: "SKU-1", qty: 2 },
      { sku: "SKU-2", qty: 1 },
    ],
    placedAt: 1789601953851,
  };
}

describe("encode", () => {
  it("produces non-empty bytes", () => {
    const encoded = encode(sampleRecord());
    expect(Buffer.isBuffer(encoded)).toBe(true);
    expect(encoded.length).toBeGreaterThan(0);
  });
});

describe("Glue framing", () => {
  it("round-trips through the wire format", () => {
    const versionId = "e424651b-7a41-405d-bf05-2cae8cdf5aea";
    const framed = encodeFramed(sampleRecord(), versionId);
    // Header: 0x03, 0x00, then the 16-byte UUID.
    expect(framed[0]).toBe(0x03);
    expect(framed[1]).toBe(0x00);
    const { schemaVersionId } = glueUnframe(framed);
    expect(schemaVersionId).toBe(versionId);
    const decoded = decodeFramed(framed);
    expect(decoded.orderId).toBe(sampleRecord().orderId);
  });
});

describe("round trip", () => {
  it("is lossless", () => {
    const original = sampleRecord();
    const decoded = decode(encode(original));
    expect(decoded.orderId).toBe(original.orderId);
    expect(decoded.customerId).toBe(original.customerId);
    expect(decoded.amount).toBe(original.amount);
    expect(decoded.currency).toBe(original.currency);
    expect(decoded.items).toEqual(original.items);
    expect(decoded.placedAt).toBe(original.placedAt);
  });
});
