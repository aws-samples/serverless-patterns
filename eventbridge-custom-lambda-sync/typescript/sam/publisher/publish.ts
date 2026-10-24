// Copyright Amazon.com, Inc. or its affiliates. All Rights Reserved.
// SPDX-License-Identifier: MIT-0

/**
 * Publish an ordered sequence of OrderPlaced events to an EventBridge custom
 * event bus (the eventsv2 API) with PutEvents. Every event in a run shares one
 * SystemMetadata.EventGroupId, so the FIFO subscriber orders them relative to
 * one another and — invoking the consumer synchronously — processes them one at
 * a time, in sequence.
 *
 * Usage:
 *   tsx publisher/publish.ts \
 *       --bus-arn arn:aws:events:<region>:<account>:event-busv2/sync-orders-bus/<id> \
 *       [--region <region>] [--count 5] [--group order-group-<ts>]
 *
 * The bus ARN can also come from the BUS_ARN environment variable, and the
 * region from AWS_REGION. The IAM action needed is `events:PutEvents` on the bus
 * (the action namespace is `events:`, never `eventsv2:`).
 */

import {
  EventBridgeV2Client,
  PutEventsCommand,
  type PutEventsCommandOutput,
  type PutEventsRequestEntry,
} from "@aws-sdk/client-eventbridgev2";

const SOURCE = "com.example.orders";
const DETAIL_TYPE = "OrderPlaced";

export interface Order {
  orderId: string;
  orderGroup: string;
  seq: number;
  customerId: string;
  amount: number;
  currency: string;
  placedAt: string;
}

/** Construct one OrderPlaced record in a group with a sequence number. */
export function buildOrder(group: string, seq: number): Order {
  return {
    orderId: `${group}-${String(seq).padStart(3, "0")}`,
    orderGroup: group,
    seq,
    customerId: "cust-987",
    amount: 100.0 + seq,
    currency: "USD",
    placedAt: "2026-09-21T12:00:00Z",
  };
}

/**
 * Build a PutEvents entry, grouping the event for FIFO ordering.
 *
 * SystemMetadata.EventGroupId is what the FIFO subscriber orders within.
 */
export function buildEntry(order: Order, group: string): PutEventsRequestEntry {
  return {
    Source: SOURCE,
    DetailType: DETAIL_TYPE,
    Detail: JSON.stringify(order),
    SystemMetadata: { EventGroupId: group },
  };
}

export interface Failure {
  index: number;
  ErrorCode?: string;
  ErrorMessage?: string;
}

/** Return the failed per-entry results (an entry with an ErrorCode). */
export function findFailures(response: PutEventsCommandOutput): Failure[] {
  const failures: Failure[] = [];
  (response.Entries ?? []).forEach((entry, index) => {
    if (entry.ErrorCode) {
      failures.push({ index, ErrorCode: entry.ErrorCode, ErrorMessage: entry.ErrorMessage });
    }
  });
  return failures;
}

const sleep = (ms: number): Promise<void> => new Promise((r) => setTimeout(r, ms));

/** Call PutEvents, retrying ThrottlingException with backoff + jitter. */
export async function putEventsWithBackoff(
  client: EventBridgeV2Client,
  busArn: string,
  entries: PutEventsRequestEntry[],
  attempts = 5,
): Promise<PutEventsCommandOutput> {
  let delayMs = 200;
  for (let attempt = 0; attempt < attempts; attempt++) {
    try {
      return await client.send(new PutEventsCommand({ EventBusArn: busArn, Entries: entries }));
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

/** Publish a single grouped order; throw on a per-entry failure. */
export async function publishOne(
  client: EventBridgeV2Client,
  busArn: string,
  order: Order,
  group: string,
): Promise<PutEventsCommandOutput> {
  const response = await putEventsWithBackoff(client, busArn, [buildEntry(order, group)]);
  const failures = findFailures(response);
  if (failures.length > 0 || response.FailedEntryCount) {
    throw new Error(`publish had failed entries: ${JSON.stringify(failures)}`);
  }
  return response;
}

/** Publish `count` ordered events sharing `group`. Returns the event ids. */
export async function publishSequence(
  client: EventBridgeV2Client,
  busArn: string,
  group: string,
  count: number,
): Promise<Array<string | undefined>> {
  const eventIds: Array<string | undefined> = [];
  for (let seq = 1; seq <= count; seq++) {
    const order = buildOrder(group, seq);
    const response = await publishOne(client, busArn, order, group);
    const entry = response.Entries?.[0];
    eventIds.push(entry?.EventId);
    console.log(
      `Published seq=${seq} orderId=${order.orderId} ` +
        `-> SuccessCode=${entry?.SuccessCode} EventId=${entry?.EventId}`,
    );
  }
  return eventIds;
}

interface Args {
  busArn?: string;
  region?: string;
  count: number;
  group?: string;
}

export function parseArgs(argv: string[]): Args {
  const args: Args = {
    busArn: process.env.BUS_ARN,
    region: process.env.AWS_REGION,
    count: 5,
    group: undefined,
  };
  for (let i = 0; i < argv.length; i++) {
    const arg = argv[i];
    const next = (): string => argv[++i];
    switch (arg) {
      case "--bus-arn":
        args.busArn = next();
        break;
      case "--region":
        args.region = next();
        break;
      case "--count":
        args.count = Number.parseInt(next(), 10);
        break;
      case "--group":
        args.group = next();
        break;
    }
  }
  return args;
}

export async function main(argv: string[]): Promise<number> {
  const args = parseArgs(argv);
  if (!args.busArn) {
    console.error("error: --bus-arn is required (or set BUS_ARN).");
    return 2;
  }
  if (!Number.isInteger(args.count) || args.count < 1) {
    console.error("error: --count must be >= 1.");
    return 2;
  }

  const group = args.group ?? `order-group-${Math.floor(Date.now() / 1000)}`;
  const client = new EventBridgeV2Client(args.region ? { region: args.region } : {});

  console.log(`Publishing ${args.count} ordered events in group '${group}'...`);
  await publishSequence(client, args.busArn, group, args.count);
  console.log(
    `\nThe FIFO subscriber invokes the consumer synchronously and processes ` +
      `group '${group}' in order. Check the consumer log to see seq=1..${args.count} ` +
      `processed in sequence.`,
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
