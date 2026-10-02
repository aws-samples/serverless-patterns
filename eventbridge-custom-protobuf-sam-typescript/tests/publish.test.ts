// Copyright Amazon.com, Inc. or its affiliates. All Rights Reserved.
// SPDX-License-Identifier: MIT-0

/**
 * Unit tests for the publisher's entry-building, schema-version lookup, and
 * result-checking. Uses aws-sdk-client-mock to intercept the EventBridgeV2 and
 * Glue clients, so the tests run fully offline and never call AWS.
 */

import { beforeEach, describe, expect, it, vi } from "vitest";
import { mockClient } from "aws-sdk-client-mock";
import {
  EventBridgeV2Client,
  PutRawEventsCommand,
} from "@aws-sdk/client-eventbridgev2";
import { GetSchemaVersionCommand, GlueClient } from "@aws-sdk/client-glue";

import {
  buildEntry,
  findFailures,
  publish,
  resolveSchemaVersionId,
} from "../publisher/publish.js";
import { buildOrder, glueUnframe } from "../common/protoio.js";

const TEST_REGION = "aws-region-1";
const BUS_ARN = `arn:aws:events:${TEST_REGION}:111122223333:event-busv2/proto-orders-bus/abc123`;
const REGISTRY_ARN = `arn:aws:glue:${TEST_REGION}:111122223333:registry/proto-orders-registry`;
const SCHEMA_VERSION_ID = "e424651b-7a41-405d-bf05-2cae8cdf5aea";

const ebMock = mockClient(EventBridgeV2Client);
const glueMock = mockClient(GlueClient);

beforeEach(() => {
  ebMock.reset();
  glueMock.reset();
  vi.spyOn(console, "log").mockImplementation(() => {});
});

describe("buildEntry", () => {
  it("frames the Data as Glue-wire Protobuf (with message index) and sets metadata", async () => {
    const entry = await buildEntry(buildOrder("order-abc"), SCHEMA_VERSION_ID);
    const data = entry.Data as Uint8Array;
    // Data is raw bytes, Glue-framed: 0x03, 0x00, UUID, then message-index 0x01.
    expect(data[0]).toBe(0x03);
    expect(data[1]).toBe(0x00);
    expect(data[18]).toBe(0x01);
    expect(entry.SystemMetadata?.ContentType).toBe("application/protobuf");
    expect(entry.Metadata?.eventType).toBe("OrderPlaced");
    // The framed UUID matches the schema version we asked for.
    const { schemaVersionId } = glueUnframe(Buffer.from(data));
    expect(schemaVersionId).toBe(SCHEMA_VERSION_ID);
  });
});

describe("resolveSchemaVersionId", () => {
  it("reads the latest version id from Glue by registry + schema name", async () => {
    glueMock.on(GetSchemaVersionCommand).resolves({ SchemaVersionId: SCHEMA_VERSION_ID });
    const glue = new GlueClient({ region: TEST_REGION });
    const id = await resolveSchemaVersionId(glue, REGISTRY_ARN);
    expect(id).toBe(SCHEMA_VERSION_ID);
    const call = glueMock.commandCalls(GetSchemaVersionCommand)[0];
    expect(call.args[0].input.SchemaId).toEqual({
      RegistryName: "proto-orders-registry",
      SchemaName: "OrderPlaced",
    });
  });
});

describe("findFailures", () => {
  it("is empty on success", () => {
    expect(findFailures({ FailedEntryCount: 0, Entries: [{ EventId: "e1" }] } as never)).toEqual([]);
  });

  it("reports errors", () => {
    const resp = { FailedEntryCount: 1, Entries: [{ ErrorCode: "ValidationError" }] };
    const failures = findFailures(resp as never);
    expect(failures).toHaveLength(1);
    expect(failures[0].index).toBe(0);
  });
});

describe("publish", () => {
  it("sends PutRawEvents naming the registry and returns on success", async () => {
    ebMock.on(PutRawEventsCommand).resolves({
      FailedEntryCount: 0,
      Entries: [{ SuccessCode: "PUBLISHED", EventId: "e1" }],
    });
    const client = new EventBridgeV2Client({ region: TEST_REGION });
    const response = await publish(
      client,
      BUS_ARN,
      REGISTRY_ARN,
      buildOrder("order-abc"),
      SCHEMA_VERSION_ID,
    );
    expect(response.Entries?.[0].SuccessCode).toBe("PUBLISHED");

    const call = ebMock.commandCalls(PutRawEventsCommand)[0];
    expect(call.args[0].input.EventBusArn).toBe(BUS_ARN);
    expect(call.args[0].input.SchemaRegistryConfiguration?.RegistryUri).toBe(REGISTRY_ARN);
  });

  it("throws when an entry fails", async () => {
    ebMock.on(PutRawEventsCommand).resolves({
      FailedEntryCount: 1,
      Entries: [{ ErrorCode: "ValidationError", ErrorMessage: "bad" }],
    });
    const client = new EventBridgeV2Client({ region: TEST_REGION });
    await expect(
      publish(client, BUS_ARN, REGISTRY_ARN, buildOrder("order-abc"), SCHEMA_VERSION_ID),
    ).rejects.toThrow(/failed entries/);
  });
});
