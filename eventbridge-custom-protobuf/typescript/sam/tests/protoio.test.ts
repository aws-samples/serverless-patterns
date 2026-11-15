// Copyright Amazon.com, Inc. or its affiliates. All Rights Reserved.
// SPDX-License-Identifier: MIT-0

/** Round-trip, Glue-framing, and message-index tests for the Protobuf helper. */

import { describe, expect, it } from "vitest";

import {
  buildOrder,
  decode,
  decodeFramed,
  encode,
  encodeFramed,
  glueUnframe,
  messageIndex,
} from "../common/protoio.js";

const VERSION_ID = "e424651b-7a41-405d-bf05-2cae8cdf5aea";

describe("encode", () => {
  it("produces non-empty bytes", async () => {
    const encoded = await encode(buildOrder("order-123"));
    expect(Buffer.isBuffer(encoded)).toBe(true);
    expect(encoded.length).toBeGreaterThan(0);
  });
});

describe("messageIndex", () => {
  it("matches Glue's lexicographic rule (OrderItem=0, OrderPlaced=1)", () => {
    expect(messageIndex("com.example.orders.OrderItem")).toBe(0);
    expect(messageIndex("com.example.orders.OrderPlaced")).toBe(1);
    // Default is OrderPlaced.
    expect(messageIndex()).toBe(1);
  });
});

describe("Glue framing", () => {
  it("round-trips through the wire format with the message-index byte", async () => {
    const framed = await encodeFramed(buildOrder("order-123"), VERSION_ID);
    // Header: 0x03, 0x00, then the 16-byte UUID, then the message-index varint.
    expect(framed[0]).toBe(0x03);
    expect(framed[1]).toBe(0x00);
    // byte 18 is the message index varint: OrderPlaced = 1.
    expect(framed[18]).toBe(0x01);
    const { schemaVersionId } = glueUnframe(framed);
    expect(schemaVersionId).toBe(VERSION_ID);
    const decoded = await decodeFramed(framed);
    expect(decoded.orderId).toBe("order-123");
  });
});

describe("round trip", () => {
  it("is lossless", async () => {
    const original = buildOrder("order-xyz");
    const decoded = await decode(await encode(original));
    expect(decoded.orderId).toBe(original.orderId);
    expect(decoded.customerId).toBe(original.customerId);
    expect(decoded.amount).toBeCloseTo(original.amount);
    expect(decoded.currency).toBe(original.currency);
    expect(decoded.items).toEqual(original.items);
    expect(decoded.placedAt).toBe(original.placedAt);
  });
});
