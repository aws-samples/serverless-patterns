import {
  BedrockRuntimeClient,
  InvokeModelCommand,
  InvokeModelCommandOutput,
} from "@aws-sdk/client-bedrock-runtime";
import {
  DynamoDBClient,
  PutItemCommand,
  SearchVectorsCommand,
} from "@aws-sdk/client-dynamodb";
import { marshall, unmarshall } from "@aws-sdk/util-dynamodb";
import type { APIGatewayProxyEventV2 } from "aws-lambda";
import { mockClient } from "aws-sdk-client-mock";
import { handler } from "../src/vector-search-handler";

const bedrockMock = mockClient(BedrockRuntimeClient);
const dynamodbMock = mockClient(DynamoDBClient);

describe("vector search handler", () => {
  beforeEach(() => {
    bedrockMock.reset();
    dynamodbMock.reset();
    process.env.TABLE_NAME = "Documents";
    process.env.VECTOR_INDEX_NAME = "embedding-index";
    process.env.EMBEDDING_MODEL_ID = "amazon.titan-embed-text-v2:0";
    process.env.VECTOR_DIMENSIONS = "2";
    bedrockMock.on(InvokeModelCommand).resolves({
      body: Uint8Array.from(
        Buffer.from(JSON.stringify({ embedding: [0.1, 0.2] })),
      ) as unknown as InvokeModelCommandOutput["body"],
    });
  });

  test("embeds and stores a document", async () => {
    dynamodbMock.on(PutItemCommand).resolves({});

    const response = await handler(
      apiEvent("POST /documents", {
        documentId: "doc-1",
        title: "DynamoDB vector search",
        content: "DynamoDB can search vectors alongside operational data.",
        tenantId: "tenant-1",
        category: "aws",
      }),
    );

    expect(response.statusCode).toBe(201);
    const put = dynamodbMock.commandCalls(PutItemCommand)[0].args[0].input;
    expect(put.TableName).toBe("Documents");
    expect(unmarshall(put.Item ?? {})).toMatchObject({
      documentId: "doc-1",
      tenantId: "tenant-1",
      category: "aws",
      embedding: [0.1, 0.2],
    });
  });

  test("embeds a query and returns vector search results", async () => {
    dynamodbMock.on(SearchVectorsCommand).resolves({
      SearchResults: [
        {
          Score: 0.02,
          Item: marshall({
            documentId: "doc-1",
            title: "DynamoDB vector search",
            content: "DynamoDB can search vectors alongside operational data.",
            tenantId: "tenant-1",
            category: "aws",
          }),
        },
      ],
    });

    const response = await handler(
      apiEvent("POST /search", {
        query: "How do I search embeddings?",
        tenantId: "tenant-1",
        category: "aws",
        topK: 3,
      }),
    );

    expect(response.statusCode).toBe(200);
    expect(JSON.parse(response.body ?? "{}")).toMatchObject({
      results: [{ documentId: "doc-1", score: 0.02 }],
    });
    const search = dynamodbMock.commandCalls(SearchVectorsCommand)[0].args[0].input;
    expect(search).toMatchObject({
      TableName: "Documents",
      IndexName: "embedding-index",
      TopK: 3,
      SearchConditionExpression: "#tenantId = :tenantId AND #category = :category",
      SearchVector: [{ N: "0.1" }, { N: "0.2" }],
      ProjectionExpression: "documentId, title, content, category",
    });
  });

  test("returns a validation response for an invalid topK", async () => {
    const response = await handler(
      apiEvent("POST /search", {
        query: "query",
        tenantId: "tenant-1",
        topK: 101,
      }),
    );

    expect(response.statusCode).toBe(400);
    expect(dynamodbMock.calls()).toHaveLength(0);
    expect(bedrockMock.calls()).toHaveLength(0);
  });

  test("rejects text that exceeds the embedding model character limit", async () => {
    const response = await handler(
      apiEvent("POST /documents", {
        documentId: "doc-1",
        title: "Oversized document",
        content: "a".repeat(50_001),
        tenantId: "tenant-1",
        category: "aws",
      }),
    );

    expect(response.statusCode).toBe(400);
    expect(JSON.parse(response.body ?? "{}")).toEqual({
      message: "content must not exceed 50000 characters",
    });
    expect(dynamodbMock.calls()).toHaveLength(0);
    expect(bedrockMock.calls()).toHaveLength(0);
  });

  test("validates DynamoDB key sizes using UTF-8 bytes", async () => {
    const response = await handler(
      apiEvent("POST /search", {
        query: "query",
        tenantId: "é".repeat(1_025),
      }),
    );

    expect(response.statusCode).toBe(400);
    expect(JSON.parse(response.body ?? "{}")).toEqual({
      message: "tenantId must not exceed 2048 UTF-8 bytes",
    });
    expect(dynamodbMock.calls()).toHaveLength(0);
    expect(bedrockMock.calls()).toHaveLength(0);
  });
});

function apiEvent(routeKey: string, body: unknown): APIGatewayProxyEventV2 {
  return {
    version: "2.0",
    routeKey,
    rawPath: routeKey.split(" ")[1],
    rawQueryString: "",
    headers: { "content-type": "application/json" },
    requestContext: {
      accountId: "test-account",
      apiId: "api-id",
      domainName: "example.execute-api.us-east-1.amazonaws.com",
      domainPrefix: "example",
      http: {
        method: "POST",
        path: routeKey.split(" ")[1],
        protocol: "HTTP/1.1",
        sourceIp: "127.0.0.1",
        userAgent: "jest",
      },
      requestId: "request-id",
      routeKey,
      stage: "$default",
      time: "10/Aug/2026:00:00:00 +0000",
      timeEpoch: 0,
    },
    body: JSON.stringify(body),
    isBase64Encoded: false,
  };
}
