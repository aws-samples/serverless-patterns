// Copyright Amazon.com, Inc. or its affiliates. All Rights Reserved.
// SPDX-License-Identifier: MIT-0

/**
 * Shared Protobuf encode/decode helpers plus the AWS Glue Schema Registry
 * Protobuf wire framing, used by the publisher (and the tests).
 *
 * The .proto is loaded at RUNTIME with protobufjs (protobuf.load) — there is no
 * codegen step and no generated bindings to commit. The consumer does NOT use
 * this module: EventBridge decodes the Protobuf server-side and delivers Data as
 * already-decoded JSON.
 *
 *   Inner encoding : OrderPlaced encoded with protobufjs
 *   Wire framing   : the AWS Glue Schema Registry Protobuf frame (see below)
 */

import { dirname, join } from "node:path";
import { fileURLToPath } from "node:url";
import protobuf from "protobufjs";

export interface OrderItem {
  sku: string;
  qty: number;
}

export interface Order {
  orderId: string;
  customerId: string;
  amount: number;
  currency: string;
  items: OrderItem[];
  // int64 in the .proto; a JS number is fine for millisecond timestamps (well
  // within Number.MAX_SAFE_INTEGER). protobufjs is told to emit longs as numbers.
  placedAt: number;
}

const PROTO_PATH = join(dirname(fileURLToPath(import.meta.url)), "..", "proto", "order_placed.proto");

// protobufjs uses the JSON (camelCase) names for fields — `orderId`, `placedAt`,
// etc. — not the .proto snake_case. Our Order interface already uses those
// camelCase names, so we hand protobufjs the Order object directly (no mapping).
// Note: this is protobufjs's local convention. EventBridge's server-side Glue
// decode delivers the field names from the .proto to the consumer; the consumer
// treats the delivered Data as opaque JSON, so the two paths are independent.

let cachedRoot: protobuf.Root | undefined;

/** Load and cache the protobuf Root from the .proto file. */
export async function loadRoot(path: string = PROTO_PATH): Promise<protobuf.Root> {
  if (!cachedRoot) {
    cachedRoot = await protobuf.load(path);
  }
  return cachedRoot;
}

/** Serialize a domain record to raw Protobuf wire bytes. */
export async function encode(order: Order): Promise<Buffer> {
  const root = await loadRoot();
  const OrderPlaced = root.lookupType("com.example.orders.OrderPlaced");
  // fromObject maps the camelCase JSON field names onto the message.
  const message = OrderPlaced.fromObject(order);
  return Buffer.from(OrderPlaced.encode(message).finish());
}

/** Deserialize raw Protobuf wire bytes into a domain record. */
export async function decode(data: Buffer): Promise<Order> {
  const root = await loadRoot();
  const OrderPlaced = root.lookupType("com.example.orders.OrderPlaced");
  // longs (int64) as numbers, enums as values — keeps placedAt a plain number.
  return OrderPlaced.toObject(OrderPlaced.decode(data), { longs: Number }) as Order;
}

// --- AWS Glue Schema Registry wire format (Protobuf) ----------------------
//
// Frame layout (uncompressed):
//   byte 0        header version, always 0x03
//   byte 1        compression: 0x00 = none, 0x05 = zlib
//   bytes 2-17    16-byte schema-version UUID (big-endian)
//   bytes 18..    message-index (unsigned varint), then the Protobuf payload
//
// The message-index identifies WHICH message type in the .proto the payload is.
// Glue assigns indices by breadth-first traversal of all message types in the
// file, sorted lexicographically by full name, position in that list, written
// as a plain unsigned varint (NOT zig-zag). For order_placed.proto that is
// OrderItem = 0, OrderPlaced = 1, so the byte is 0x01.
//
// Getting this wrong does NOT fail the publish — the service decodes the bytes
// against the WRONG message type and delivers a garbled record. So we compute
// the index the same way Glue does rather than hardcode it.

export const GLUE_HEADER_VERSION = 0x03;
export const GLUE_COMPRESSION_NONE = 0x00;

const MESSAGE_FULL_NAMES = ["com.example.orders.OrderItem", "com.example.orders.OrderPlaced"];
const ORDER_PLACED_FULL_NAME = "com.example.orders.OrderPlaced";

/**
 * Replicate Glue's message-index assignment: lexicographically sorted full
 * names, index = position. (Level-order traversal is irrelevant here because
 * there are no nested message types.)
 */
export function messageIndex(fullName: string = ORDER_PLACED_FULL_NAME): number {
  return [...MESSAGE_FULL_NAMES].sort().indexOf(fullName);
}

/** Encode a non-negative integer as an unsigned LEB128 varint. */
export function encodeVarint(value: number): Buffer {
  const out: number[] = [];
  let v = value;
  for (;;) {
    const byte = v & 0x7f;
    v >>>= 7;
    if (v) {
      out.push(byte | 0x80);
    } else {
      out.push(byte);
      return Buffer.from(out);
    }
  }
}

/** Decode an unsigned varint at `offset`; return [value, newOffset]. */
export function decodeVarint(buf: Buffer, offset: number): [number, number] {
  let result = 0;
  let shift = 0;
  let pos = offset;
  for (;;) {
    const byte = buf[pos];
    result |= (byte & 0x7f) << shift;
    pos += 1;
    if (!(byte & 0x80)) {
      return [result >>> 0, pos];
    }
    shift += 7;
  }
}

/** Convert a UUID string to its 16 big-endian bytes. */
export function uuidToBytes(uuid: string): Buffer {
  const hex = uuid.replace(/-/g, "");
  if (hex.length !== 32) {
    throw new Error(`invalid UUID: ${uuid}`);
  }
  return Buffer.from(hex, "hex");
}

/** Convert 16 big-endian bytes to a UUID string. */
export function bytesToUuid(bytes: Buffer): string {
  const hex = bytes.toString("hex");
  return [
    hex.slice(0, 8),
    hex.slice(8, 12),
    hex.slice(12, 16),
    hex.slice(16, 20),
    hex.slice(20, 32),
  ].join("-");
}

/**
 * Wrap raw Protobuf bytes in the Glue Schema Registry Protobuf wire format.
 *
 * `schemaVersionId` is the Glue SchemaVersionId (a UUID string) from
 * glue:GetSchemaVersion. The message index for OrderPlaced is computed the way
 * Glue assigns it.
 */
export function glueFrame(protoBytes: Buffer, schemaVersionId: string): Buffer {
  const header = Buffer.from([GLUE_HEADER_VERSION, GLUE_COMPRESSION_NONE]);
  const indexBytes = encodeVarint(messageIndex());
  return Buffer.concat([header, uuidToBytes(schemaVersionId), indexBytes, protoBytes]);
}

/** Split a Glue-framed Protobuf payload into its schema-version id and Protobuf bytes. */
export function glueUnframe(framed: Buffer): { schemaVersionId: string; protoBytes: Buffer } {
  if (framed.length < 19) {
    throw new Error("payload too short to be a Glue Protobuf frame");
  }
  if (framed[0] !== GLUE_HEADER_VERSION) {
    throw new Error(`unexpected Glue header version: 0x${framed[0].toString(16)}`);
  }
  if (framed[1] !== GLUE_COMPRESSION_NONE) {
    throw new Error(`compressed Glue payloads are not supported here: 0x${framed[1].toString(16)}`);
  }
  const schemaVersionId = bytesToUuid(framed.subarray(2, 18));
  const [, payloadOffset] = decodeVarint(framed, 18);
  return { schemaVersionId, protoBytes: framed.subarray(payloadOffset) };
}

/** Protobuf-encode a record and wrap it in the Glue Protobuf wire format. */
export async function encodeFramed(order: Order, schemaVersionId: string): Promise<Buffer> {
  return glueFrame(await encode(order), schemaVersionId);
}

/** Strip the Glue wire header/index and Protobuf-decode the payload. */
export async function decodeFramed(framed: Buffer): Promise<Order> {
  return decode(glueUnframe(framed).protoBytes);
}

/** Construct a sample OrderPlaced domain record. */
export function buildOrder(orderId: string): Order {
  return {
    orderId,
    customerId: "cust-987",
    amount: 129.95,
    currency: "USD",
    items: [
      { sku: "SKU-1", qty: 2 },
      { sku: "SKU-2", qty: 1 },
    ],
    placedAt: Date.now(),
  };
}
