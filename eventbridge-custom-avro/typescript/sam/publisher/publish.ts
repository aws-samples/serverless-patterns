// Copyright Amazon.com, Inc. or its affiliates. All Rights Reserved.
// SPDX-License-Identifier: MIT-0
/**
 * Publish an OrderPlaced domain event to an EventBridge custom event bus (the
 * eventsv2 API) in Avro binary format, decoded against an AWS Glue Schema
 * Registry.
 *
 * Usage:
 *   tsx publisher/publish.ts --bus-arn <bus-arn> --registry-arn <registry-arn> \
 *       [--region <region>] [--order-id order-123]
 *
 * Both ARNs can also be supplied via the BUS_ARN and REGISTRY_ARN environment
 * variables, and the region via AWS_REGION.
 *
 * How Avro decoding is wired: the service decodes the payload against a schema
 * registry named ON THE PUBLISH REQUEST (SchemaRegistryConfiguration.RegistryUri),
 * not on the bus. EventBridge reads the registry with the CALLER's own
 * credentials, so the identity running this needs Glue read access on the
 * registry. The IAM action for publishing is `events:PutRawEvents` (never
 * `eventsv2:`).
 */
import { parseArgs } from "node:util";
import {
  EventBridgeV2Client,
  PutRawEventsCommand,
  type PutRawEventsCommandOutput,
  type PutRawEventsRequestEntry,
} from "@aws-sdk/client-eventbridgev2";
import { GetSchemaVersionCommand, GlueClient } from "@aws-sdk/client-glue";
import { encodeFramed, type Order } from "../common/avroio.js";

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
 * `Data` is Avro bytes wrapped in the Glue Schema Registry wire format (bare Avro
 * is rejected as "Malformed Glue wire format"). Pass raw bytes; the SDK does the
 * wire encoding. `Metadata` carries the custom keys a METADATA-scoped subscriber
 * filter routes on.
 */
export function buildEntry(record: Order, schemaVersionId: string): PutRawEventsRequestEntry {
  return {
    Data: new Uint8Array(encodeFramed(record, schemaVersionId)),
    SystemMetadata: { ContentType: "application/avro" },
    Metadata: {
      eventType: "OrderPlaced",
      source: "com.example.orders",
      schemaVersion: "1",
    },
  };
}

/** Look up the latest OrderPlaced schema-version UUID for the Glue wire header. */
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
  return (response.Entries ?? [])
    .map((entry, index) => ({ index, ErrorCode: entry.ErrorCode, ErrorMessage: entry.ErrorMessage }))
    .filter((entry) => entry.ErrorCode);
}

/**
 * Encode one domain record and publish it to the bus; throw on any failure.
 *
 * Names the Glue registry on the request so the service can decode the Avro.
 * Throttling is retried by the SDK's default retry strategy.
 */
export async function publish(
  client: EventBridgeV2Client,
  busArn: string,
  registryArn: string,
  record: Order,
  schemaVersionId: string,
): Promise<PutRawEventsCommandOutput> {
  const response = await client.send(
    new PutRawEventsCommand({
      EventBusArn: busArn,
      Entries: [buildEntry(record, schemaVersionId)],
      SchemaRegistryConfiguration: { RegistryUri: registryArn },
    }),
  );
  const failures = findFailures(response);
  if (failures.length > 0 || response.FailedEntryCount) {
    throw new Error(`publish had failed entries: ${JSON.stringify(failures)}`);
  }
  return response;
}

export async function main(argv: string[]): Promise<number> {
  const { values } = parseArgs({
    args: argv,
    options: {
      "bus-arn": { type: "string", default: process.env.BUS_ARN },
      "registry-arn": { type: "string", default: process.env.REGISTRY_ARN },
      region: { type: "string", default: process.env.AWS_REGION },
      "order-id": { type: "string", default: `order-${Math.floor(Date.now() / 1000)}` },
    },
  });
  const busArn = values["bus-arn"];
  const registryArn = values["registry-arn"];
  if (!busArn || !registryArn) {
    console.error(
      "error: --bus-arn and --registry-arn are required (or set BUS_ARN and REGISTRY_ARN).",
    );
    return 2;
  }
  const clientConfig = values.region ? { region: values.region } : {};
  const client = new EventBridgeV2Client(clientConfig);
  const glue = new GlueClient(clientConfig);

  const schemaVersionId = await resolveSchemaVersionId(glue, registryArn);
  const record = buildOrder(values["order-id"] as string);
  const response = await publish(client, busArn, registryArn, record, schemaVersionId);
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
