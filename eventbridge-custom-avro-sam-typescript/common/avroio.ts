// Copyright Amazon.com, Inc. or its affiliates. All Rights Reserved.
// SPDX-License-Identifier: MIT-0

/**
 * Shared Avro encode/decode helpers plus the AWS Glue Schema Registry wire
 * framing, used by the publisher (and the tests).
 *
 * Encoding uses Avro binary (the plain binary encoding, no object-container
 * framing), which is what EventBridge decodes against the Glue Schema Registry
 * when the payload is published with ContentType application/avro.
 *
 * The consumer does NOT use this module: EventBridge decodes the Avro
 * server-side and delivers Data as already-decoded JSON.
 */

import { readFileSync } from "node:fs";
import { dirname, join } from "node:path";
import { fileURLToPath } from "node:url";
import avro from "avsc";

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
  // placedAt is the Avro `long` with logicalType timestamp-millis. avsc's
  // default handling of a plain long is a JS number (epoch milliseconds), which
  // is what we encode.
  placedAt: number;
}

// Resolve the schema relative to this file so it works regardless of the
// caller's working directory.
const SCHEMA_PATH = join(dirname(fileURLToPath(import.meta.url)), "..", "schema", "order_placed.avsc");

/** Load and parse the OrderPlaced Avro schema into an avsc type. */
export function loadType(path: string = SCHEMA_PATH): avro.Type {
  const schemaJson = JSON.parse(readFileSync(path, "utf-8"));
  return avro.Type.forSchema(schemaJson);
}

const TYPE = loadType();

/**
 * Serialize a domain record to Avro binary bytes.
 *
 * Returns raw bytes. Do NOT base64-encode these before handing them to the SDK;
 * the SDK does the wire encoding itself.
 */
export function encode(record: Order, type: avro.Type = TYPE): Buffer {
  return type.toBuffer(record);
}

/** Deserialize Avro binary bytes back into a domain record. */
export function decode(data: Buffer, type: avro.Type = TYPE): Order {
  return type.fromBuffer(data) as Order;
}

// --- AWS Glue Schema Registry wire format ---------------------------------
//
// When a payload is published to EventBridge with ContentType application/avro
// and decoded against a Glue registry, the bytes must carry the Glue wire
// header, not bare Avro. The frame is:
//
//     byte 0      header version, always 0x03
//     byte 1      compression: 0x00 = none, 0x05 = zlib
//     bytes 2-17  16-byte schema-version UUID (big-endian)
//     bytes 18+   the Avro binary payload
//
// EventBridge reads the header to look up the schema version, so bare Avro is
// rejected with "Malformed Glue wire format".

export const GLUE_HEADER_VERSION = 0x03;
export const GLUE_COMPRESSION_NONE = 0x00;

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
 * Wrap Avro bytes in the Glue Schema Registry wire format.
 *
 * `schemaVersionId` is the Glue SchemaVersionId (a UUID string), obtained from
 * glue:GetSchemaVersion.
 */
export function glueFrame(avroBytes: Buffer, schemaVersionId: string): Buffer {
  const header = Buffer.from([GLUE_HEADER_VERSION, GLUE_COMPRESSION_NONE]);
  return Buffer.concat([header, uuidToBytes(schemaVersionId), avroBytes]);
}

/**
 * Split a Glue-framed payload into its schema-version id and Avro bytes.
 *
 * Validates the header version and compression byte; throws on a frame that is
 * not uncompressed Glue-format.
 */
export function glueUnframe(framed: Buffer): { schemaVersionId: string; avroBytes: Buffer } {
  if (framed.length < 18) {
    throw new Error("payload too short to be Glue-framed");
  }
  if (framed[0] !== GLUE_HEADER_VERSION) {
    throw new Error(`unexpected Glue header version: 0x${framed[0].toString(16)}`);
  }
  if (framed[1] !== GLUE_COMPRESSION_NONE) {
    throw new Error(`compressed Glue payloads are not supported here: 0x${framed[1].toString(16)}`);
  }
  return {
    schemaVersionId: bytesToUuid(framed.subarray(2, 18)),
    avroBytes: framed.subarray(18),
  };
}

/** Avro-encode a record and wrap it in the Glue wire format. */
export function encodeFramed(record: Order, schemaVersionId: string, type: avro.Type = TYPE): Buffer {
  return glueFrame(encode(record, type), schemaVersionId);
}

/** Strip the Glue wire header and Avro-decode the payload. */
export function decodeFramed(framed: Buffer, type: avro.Type = TYPE): Order {
  return decode(glueUnframe(framed).avroBytes, type);
}
