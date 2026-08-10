import {
  DescribeTableCommand,
  DynamoDBClient,
  UpdateTableCommand,
} from "@aws-sdk/client-dynamodb";
import type { CloudFormationCustomResourceEvent } from "aws-lambda";
import { mockClient } from "aws-sdk-client-mock";
import { onEvent } from "../src/vector-index-provider";

const dynamodbMock = mockClient(DynamoDBClient);

const resourceProperties = {
  ServiceToken: "service-token",
  TableName: "Documents",
  IndexName: "embedding-index",
  VectorAttributeName: "embedding",
  Dimensions: 1024,
  DistanceFunction: "COSINE",
  SearchSchema: [
    {
      AttributeName: "tenantId",
      SearchSchemaElementType: "HASH",
      AttributeType: "S",
    },
    {
      AttributeName: "category",
      SearchSchemaElementType: "INLINE_FILTER",
      AttributeType: "S",
    },
  ],
  Projection: {
    ProjectionType: "INCLUDE",
    NonKeyAttributes: ["title"],
  },
};

describe("vector index provider", () => {
  beforeEach(() => dynamodbMock.reset());

  test("includes every search-schema attribute definition when creating the index", async () => {
    dynamodbMock
      .on(DescribeTableCommand)
      .resolvesOnce({
        Table: {
          TableName: "Documents",
          AttributeDefinitions: [
            { AttributeName: "tenantId", AttributeType: "S" },
            { AttributeName: "documentId", AttributeType: "S" },
          ],
          VectorIndexes: [],
        },
      })
      .resolves({
        Table: {
          TableName: "Documents",
          VectorIndexes: [
            { IndexName: "embedding-index", IndexStatus: "ACTIVE", Backfilling: false },
          ],
        },
      });
    dynamodbMock.on(UpdateTableCommand).resolves({});

    const response = await onEvent(event("Create"));

    expect(response.PhysicalResourceId).toBe("Documents/index/embedding-index");
    const update = dynamodbMock.commandCalls(UpdateTableCommand)[0].args[0].input;
    expect(update).toEqual({
      TableName: "Documents",
      AttributeDefinitions: [
        { AttributeName: "tenantId", AttributeType: "S" },
        { AttributeName: "category", AttributeType: "S" },
      ],
      VectorIndexUpdates: [
        {
          Create: {
            IndexName: "embedding-index",
            VectorAttribute: { AttributeName: "embedding" },
            Dimensions: 1024,
            DistanceFunction: "COSINE",
            SearchSchema: [
              {
                AttributeName: "tenantId",
                SearchSchemaElementType: "HASH",
              },
              {
                AttributeName: "category",
                SearchSchemaElementType: "INLINE_FILTER",
              },
            ],
            Projection: {
              ProjectionType: "INCLUDE",
              NonKeyAttributes: ["title"],
            },
          },
        },
      ],
    });
  });

  test("rejects an in-place immutable configuration change", async () => {
    const updated = {
      ...resourceProperties,
      Dimensions: 1536,
    };

    await expect(
      onEvent(event("Update", updated, resourceProperties)),
    ).rejects.toThrow("Change indexName to replace the index safely");
    expect(dynamodbMock.calls()).toHaveLength(0);
  });

  test("treats an index already being deleted as an idempotent delete", async () => {
    dynamodbMock
      .on(DescribeTableCommand)
      .resolvesOnce({
        Table: {
          TableName: "Documents",
          VectorIndexes: [{ IndexName: "embedding-index", IndexStatus: "DELETING" }],
        },
      })
      .resolves({
        Table: { TableName: "Documents", VectorIndexes: [] },
      });

    await expect(onEvent(event("Delete"))).resolves.toEqual({
      PhysicalResourceId: "Documents/index/embedding-index",
    });
    expect(dynamodbMock.commandCalls(UpdateTableCommand)).toHaveLength(0);
  });
});

function event(
  requestType: "Create" | "Update" | "Delete",
  properties: Record<string, unknown> = resourceProperties,
  oldProperties?: Record<string, unknown>,
): CloudFormationCustomResourceEvent {
  return {
    RequestType: requestType,
    ServiceToken: "service-token",
    ResponseURL: "https://example.com/response",
    StackId: "stack-id",
    RequestId: "request-id",
    LogicalResourceId: "VectorIndex",
    PhysicalResourceId: "Documents/index/embedding-index",
    ResourceType: "Custom::DynamoDBVectorIndex",
    ResourceProperties: properties,
    OldResourceProperties: oldProperties,
  } as CloudFormationCustomResourceEvent;
}
