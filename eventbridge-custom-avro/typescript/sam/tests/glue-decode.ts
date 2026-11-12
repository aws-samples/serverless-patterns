// Copyright Amazon.com, Inc. or its affiliates. All Rights Reserved.
// SPDX-License-Identifier: MIT-0
/**
 * Test-only helpers that reverse the publisher's Glue framing and Avro encoding,
 * so the tests can prove the published bytes round-trip. The deployed pattern
 * never decodes Avro itself: EventBridge does that server-side.
 */
import type avro from "avsc";
import {
  GLUE_COMPRESSION_NONE,
  GLUE_HEADER_VERSION,
  ORDER_TYPE,
  type Order,
} from "../common/avroio.js";

/** Deserialize Avro binary bytes back into a domain record. */
export function decode(data: Buffer, type: avro.Type = ORDER_TYPE): Order {
  return type.fromBuffer(data) as Order;
}

/** Split a Glue-framed payload into its schema-version id and Avro bytes. */
export function glueUnframe(framed: Buffer): { schemaVersionId: string; avroBytes: Buffer } {
  if (framed.length < 18) {
    throw new Error("payload too short to be Glue-framed");
  }
  if (framed[0] !== GLUE_HEADER_VERSION || framed[1] !== GLUE_COMPRESSION_NONE) {
    throw new Error("not an uncompressed Glue-framed payload");
  }
  const hex = framed.subarray(2, 18).toString("hex");
  const schemaVersionId = [
    hex.slice(0, 8),
    hex.slice(8, 12),
    hex.slice(12, 16),
    hex.slice(16, 20),
    hex.slice(20, 32),
  ].join("-");
  return { schemaVersionId, avroBytes: framed.subarray(18) };
}

/** Strip the Glue wire header and Avro-decode the payload. */
export function decodeFramed(framed: Buffer): Order {
  return decode(glueUnframe(framed).avroBytes);
}
