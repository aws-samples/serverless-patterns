// Copyright Amazon.com, Inc. or its affiliates. All Rights Reserved.
// SPDX-License-Identifier: MIT-0

/**
 * Unit tests for the publisher's entry-building, grouping, and result-checking.
 *
 * Uses aws-sdk-client-mock to intercept the EventBridgeV2 client, so the tests
 * run fully offline and never call AWS. The mock also lets us assert the exact
 * PutEvents request shape (including the SystemMetadata.EventGroupId nesting).
 */

import { beforeEach, describe, expect, it, vi } from "vitest";
import { mockClient } from "aws-sdk-client-mock";
import {
  EventBridgeV2Client,
  PutEventsCommand,
} from "@aws-sdk/client-eventbridgev2";

import {
  buildEntry,
  buildOrder,
  findFailures,
  publishOne,
  publishSequence,
} from "../publisher/publish.js";

const TEST_REGION = "aws-region-1";
const BUS_ARN = `arn:aws:events:${TEST_REGION}:111122223333:event-busv2/sync-orders-bus/abc123def456ghi789jkl012m`;

const ebMock = mockClient(EventBridgeV2Client);

beforeEach(() => {
  ebMock.reset();
  vi.spyOn(console, "log").mockImplementation(() => {});
});

describe("build helpers", () => {
  it("build_order carries group and seq", () => {
    const order = buildOrder("grp", 3);
    expect(order.orderGroup).toBe("grp");
    expect(order.seq).toBe(3);
    expect(order.orderId).toBe("grp-003");
  });

  it("build_entry sets the EventGroupId", () => {
    const entry = buildEntry(buildOrder("grp", 1), "grp");
    expect(entry.Source).toBe("com.example.orders");
    expect(entry.DetailType).toBe("OrderPlaced");
    expect(entry.SystemMetadata?.EventGroupId).toBe("grp");
    expect(JSON.parse(entry.Detail as string).seq).toBe(1);
  });
});

describe("findFailures", () => {
  it("is empty on success", () => {
    expect(findFailures({ FailedEntryCount: 0, Entries: [{ EventId: "e1" }] } as never)).toEqual([]);
  });

  it("reports errors", () => {
    const resp = {
      FailedEntryCount: 1,
      Entries: [{ ErrorCode: "ValidationError", ErrorMessage: "bad" }],
    };
    const failures = findFailures(resp as never);
    expect(failures).toHaveLength(1);
    expect(failures[0].index).toBe(0);
  });
});

describe("publishSequence", () => {
  it("publishes each in order and returns the event ids", async () => {
    const group = "grp";
    const count = 3;
    let call = 0;
    ebMock.on(PutEventsCommand).callsFake(() => {
      call += 1;
      return { FailedEntryCount: 0, Entries: [{ EventId: `e${call}` }] };
    });

    const client = new EventBridgeV2Client({ region: TEST_REGION });
    const eventIds = await publishSequence(client, BUS_ARN, group, count);
    expect(eventIds).toEqual(["e1", "e2", "e3"]);

    // Each call sent one entry carrying the shared EventGroupId, in order.
    const calls = ebMock.commandCalls(PutEventsCommand);
    expect(calls).toHaveLength(3);
    calls.forEach((c, i) => {
      const input = c.args[0].input;
      expect(input.EventBusArn).toBe(BUS_ARN);
      expect(input.Entries?.[0].SystemMetadata?.EventGroupId).toBe(group);
      expect(JSON.parse(input.Entries?.[0].Detail as string).seq).toBe(i + 1);
    });
  });
});

describe("publishOne", () => {
  it("throws on a failed entry", async () => {
    ebMock.on(PutEventsCommand).resolves({
      FailedEntryCount: 1,
      Entries: [{ ErrorCode: "ValidationError", ErrorMessage: "bad" }],
    });
    const client = new EventBridgeV2Client({ region: TEST_REGION });
    await expect(publishOne(client, BUS_ARN, buildOrder("grp", 1), "grp")).rejects.toThrow(
      /failed entries/,
    );
  });
});
