// Copyright Amazon.com, Inc. or its affiliates. All Rights Reserved.
// SPDX-License-Identifier: MIT-0

/**
 * Consumer Lambda: log the OrderPlaced events delivered by the subscriber to
 * CloudWatch, proving the delivered event is the same domain event that was
 * originally published.
 *
 * Delivery shape (important, and verified against the live service):
 *   - A subscriber's Lambda target receives a BATCH: the event is a JSON array
 *     of delivered events, not a single object. The handler iterates it.
 *   - This subscriber uses a WITH_METADATA transformer, so each delivered event
 *     has the three-part envelope: `Data` (the payload), `Metadata` (the
 *     publisher's custom keys), and `SystemMetadata` (service-assigned fields).
 *   - The payload was published as Avro (ContentType application/avro) against a
 *     Glue Schema Registry. EventBridge decodes the Avro server-side and delivers
 *     `Data` as an already-decoded JSON object — the handler does NOT base64-decode
 *     or Avro-decode. `SystemMetadata` carries `aws:SchemaId` and
 *     `aws:RegistryType: Glue` recording the decode.
 *
 * Because the service does the Avro decode, this function needs no Avro library
 * and no bundled schema.
 */

interface DeliveredEvent {
  Data?: unknown;
  Metadata?: Record<string, unknown>;
  SystemMetadata?: Record<string, unknown>;
}

type HandlerEvent = DeliveredEvent | DeliveredEvent[];

/**
 * Return the delivered events as a list.
 *
 * The subscriber delivers a JSON array; tolerate a single object too so the
 * handler is easy to invoke by hand.
 */
function normalizeBatch(event: HandlerEvent): DeliveredEvent[] {
  if (Array.isArray(event)) {
    return event;
  }
  if (event && typeof event === "object") {
    return [event];
  }
  throw new Error(`unexpected event type: ${typeof event}`);
}

/**
 * Return the decoded domain record from one delivered event.
 *
 * `Data` arrives as a JSON object (the service already Avro-decoded it). If it
 * is delivered as a JSON string, parse it; anything else is unexpected.
 */
function extractRecord(item: DeliveredEvent): Record<string, unknown> {
  const data = item.Data;
  if (data && typeof data === "object") {
    return data as Record<string, unknown>;
  }
  if (typeof data === "string") {
    return JSON.parse(data);
  }
  throw new Error(`unexpected Data type: ${typeof data}`);
}

/** Lambda entry point. Logs each delivered OrderPlaced event. */
export async function handler(event: HandlerEvent): Promise<{ recordCount: number }> {
  const delivered = normalizeBatch(event);
  const records: Array<Record<string, unknown>> = [];

  delivered.forEach((item, index) => {
    const record = extractRecord(item);
    const metadata = item.Metadata ?? {};
    const systemMetadata = item.SystemMetadata ?? {};

    console.log(
      `OrderPlaced[${index}]: ${JSON.stringify(record)} | ` +
        `metadata=${JSON.stringify(metadata)} | ` +
        `schemaId=${systemMetadata["aws:SchemaId"]} registry=${systemMetadata["aws:RegistryType"]}`,
    );
    records.push(record);
  });

  return { recordCount: records.length };
}
