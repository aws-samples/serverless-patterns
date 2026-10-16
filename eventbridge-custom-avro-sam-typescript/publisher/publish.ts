// Copyright Amazon.com, Inc. or its affiliates. All Rights Reserved.
// SPDX-License-Identifier: MIT-0

/**
 * Publish a rich OrderPlaced domain event to an EventBridge custom event bus
 * (the eventsv2 API) in Avro binary format, decoded against an AWS Glue Schema
 * Registry.
 *
 * Usage:
 *   tsx publisher/publish.ts \
 *       --bus-arn arn:aws:events:<region>:<account>:event-busv2/avro-orders-bus/<id> \
 *       --registry-arn arn:aws:glue:<region>:<account>:registry/avro-orders-registry \
 *       [--region <region>] [--order-id order-123]
 *
 * Both ARNs can also be supplied via the BUS_ARN and REGISTRY_ARN environment
 * variables, and the region via AWS_REGION.
 *
 * How Avro decoding is wired: the service decodes the payload against a schema
 * registry named ON THE PUBLISH REQUEST (SchemaRegistryConfiguration.RegistryUri),
 * not on the bus. EventBridge reads the registry with the CALLER's own
 * credentials, so the identity running this needs Glue read access on the
 * registry (glue:GetSchemaVersion, plus the reads the service uses to decode).
 * The IAM action for publishing is `events:PutRawEvents` (never `eventsv2:`).
 */

import {
  EventBridgeV2Client,
  PutRawEventsCommand,
  type PutRawEventsCommandOutput,
  type PutRawEventsRequestEntry,
} from "@aws-sdk/client-eventbridgev2";
import { GetSchemaVersionCommand, GlueClient } from "@aws-sdk/client-glue";

import { encodeFramed, type Order } from "../common/avroio.js";

const CONTENT_TYPE_AVRO = "application/avro";

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

/**
 * Build a single PutRawEvents entry from a domain record.
 *
 * `Data` is Avro bytes wrapped in the Glue Schema Registry wire format (a header
 * naming the schema-version UUID, then the Avro binary). Bare Avro is rejected by
 * the service as "Malformed Glue wire format". `Metadata` carries the "enhanced"
 * custom keys a METADATA-scoped subscriber filter can route on.
 */
export function buildEntry(record: Order, schemaVersionId: string): PutRawEventsRequestEntry {
  return {
    Data: new Uint8Array(encodeFramed(record, schemaVersionId)),
    SystemMetadata: { ContentType: CONTENT_TYPE_AVRO },
    Metadata: {
      eventType: "OrderPlaced",
      source: "com.example.orders",
      schemaVersion: "1",
    },
  };
}

/**
 * Look up the latest schema-version UUID for OrderPlaced.
 *
 * The registry ARN's name is used to address the schema; the version id is what
 * the Glue wire header must carry so EventBridge can decode the payload.
 */
export async function resolveSchemaVersionId(
  glue: GlueClient,
  registryArn: string,
): Promise<string> {
  const registryName = registryArn.split("/").pop() as string;
  const resp = await glue.send(
    new GetSchemaVersionCommand({
      SchemaId: { RegistryName: registryName, SchemaName: "OrderPlaced" },
      SchemaVersionNumber: { LatestVersion: true },
    }),
  );
  if (!resp.SchemaVersionId) {
    throw new Error("GetSchemaVersion did not return a SchemaVersionId");
  }
  return resp.SchemaVersionId;
}

export interface Failure {
  index: number;
  ErrorCode?: string;
  ErrorMessage?: string;
}

/** Return the failed per-entry results (an entry with an ErrorCode). */
export function findFailures(response: PutRawEventsCommandOutput): Failure[] {
  const failures: Failure[] = [];
  (response.Entries ?? []).forEach((entry, index) => {
    if (entry.ErrorCode) {
      failures.push({ index, ErrorCode: entry.ErrorCode, ErrorMessage: entry.ErrorMessage });
    }
  });
  return failures;
}

const sleep = (ms: number): Promise<void> => new Promise((r) => setTimeout(r, ms));

/**
 * Call PutRawEvents, retrying ThrottlingException with backoff + jitter.
 *
 * Targets the bus directly via `EventBusArn` and names the Glue registry on the
 * request so the service can decode the Avro payload.
 */
export async function putRawWithBackoff(
  client: EventBridgeV2Client,
  busArn: string,
  registryArn: string,
  entries: PutRawEventsRequestEntry[],
  attempts = 5,
): Promise<PutRawEventsCommandOutput> {
  let delayMs = 200;
  for (let attempt = 0; attempt < attempts; attempt++) {
    try {
      return await client.send(
        new PutRawEventsCommand({
          EventBusArn: busArn,
          Entries: entries,
          SchemaRegistryConfiguration: { RegistryUri: registryArn },
        }),
      );
    } catch (error) {
      const name = (error as { name?: string }).name;
      if (name !== "ThrottlingException" || attempt === attempts - 1) {
        throw error;
      }
      await sleep(delayMs + Math.random() * delayMs);
      delayMs *= 2;
    }
  }
  throw new Error("exhausted retry attempts without a response");
}

/** Encode one domain record and publish it to the bus; throw on any failure. */
export async function publish(
  client: EventBridgeV2Client,
  busArn: string,
  registryArn: string,
  record: Order,
  schemaVersionId: string,
): Promise<PutRawEventsCommandOutput> {
  const entries = [buildEntry(record, schemaVersionId)];
  const response = await putRawWithBackoff(client, busArn, registryArn, entries);
  if (findFailures(response).length > 0 || response.FailedEntryCount) {
    throw new Error(`publish had failed entries: ${JSON.stringify(findFailures(response))}`);
  }
  return response;
}

interface Args {
  busArn?: string;
  registryArn?: string;
  region?: string;
  orderId: string;
}

export function parseArgs(argv: string[]): Args {
  const args: Args = {
    busArn: process.env.BUS_ARN,
    registryArn: process.env.REGISTRY_ARN,
    region: process.env.AWS_REGION,
    orderId: `order-${Math.floor(Date.now() / 1000)}`,
  };
  for (let i = 0; i < argv.length; i++) {
    const next = (): string => argv[++i];
    switch (argv[i]) {
      case "--bus-arn":
        args.busArn = next();
        break;
      case "--registry-arn":
        args.registryArn = next();
        break;
      case "--region":
        args.region = next();
        break;
      case "--order-id":
        args.orderId = next();
        break;
    }
  }
  return args;
}

export async function main(argv: string[]): Promise<number> {
  const args = parseArgs(argv);
  if (!args.busArn || !args.registryArn) {
    console.error(
      "error: --bus-arn and --registry-arn are required (or set BUS_ARN and REGISTRY_ARN).",
    );
    return 2;
  }

  const clientConfig = args.region ? { region: args.region } : {};
  const client = new EventBridgeV2Client(clientConfig);
  const glue = new GlueClient(clientConfig);

  const schemaVersionId = await resolveSchemaVersionId(glue, args.registryArn);
  const record = buildOrder(args.orderId);
  const response = await publish(client, args.busArn, args.registryArn, record, schemaVersionId);

  const entry = response.Entries?.[0];
  console.log(
    `Published orderId=${record.orderId} ` +
      `-> SuccessCode=${entry?.SuccessCode} EventId=${entry?.EventId}`,
  );
  return 0;
}

// Run main() only when invoked directly (not when imported by tests).
const isMain = process.argv[1] && import.meta.url === `file://${process.argv[1]}`;
if (isMain) {
  main(process.argv.slice(2)).then((code) => {
    process.exitCode = code;
  });
}
