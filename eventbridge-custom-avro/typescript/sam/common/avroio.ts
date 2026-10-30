// Copyright Amazon.com, Inc. or its affiliates. All Rights Reserved.
// SPDX-License-Identifier: MIT-0
/**
 * Avro encoding plus the AWS Glue Schema Registry wire framing, used by the
 * publisher.
 *
 * Encoding uses Avro binary (no object-container framing), which is what
 * EventBridge decodes against the Glue Schema Registry when the payload is
 * published with ContentType application/avro.
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
  // Avro `long` with logicalType timestamp-millis; avsc maps it to a JS number
  // (epoch milliseconds).
  placedAt: number;
}

// Resolve the schema relative to this file so it works from any working directory.
const SCHEMA_PATH = join(dirname(fileURLToPath(import.meta.url)), "..", "schema", "order_placed.avsc");

/** Load and parse the OrderPlaced Avro schema into an avsc type. */
export function loadType(path: string = SCHEMA_PATH): avro.Type {
  return avro.Type.forSchema(JSON.parse(readFileSync(path, "utf-8")));
}

export const ORDER_TYPE = loadType();

/** Serialize a domain record to Avro binary bytes (raw, not base64). */
export function encode(record: Order, type: avro.Type = ORDER_TYPE): Buffer {
  return type.toBuffer(record);
}

// --- AWS Glue Schema Registry wire format ---------------------------------
//
// The bytes published to EventBridge must carry the Glue wire header, not bare
// Avro (bare Avro is rejected with "Malformed Glue wire format"):
//
//     byte 0      header version, always 0x03
//     byte 1      compression: 0x00 = none
//     bytes 2-17  16-byte schema-version UUID (big-endian)
//     bytes 18+   the Avro binary payload
export const GLUE_HEADER_VERSION = 0x03;
export const GLUE_COMPRESSION_NONE = 0x00;

/** Avro-encode a record and wrap it in the Glue wire format. */
export function encodeFramed(
  record: Order,
  schemaVersionId: string,
  type: avro.Type = ORDER_TYPE,
): Buffer {
  const uuid = schemaVersionId.replace(/-/g, "");
  if (uuid.length !== 32) {
    throw new Error(`invalid schema version id: ${schemaVersionId}`);
  }
  const header = Buffer.from([GLUE_HEADER_VERSION, GLUE_COMPRESSION_NONE]);
  return Buffer.concat([header, Buffer.from(uuid, "hex"), encode(record, type)]);
}
