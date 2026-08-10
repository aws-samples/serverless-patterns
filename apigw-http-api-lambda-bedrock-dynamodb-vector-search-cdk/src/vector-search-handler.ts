import {
  BedrockRuntimeClient,
  InvokeModelCommand,
} from "@aws-sdk/client-bedrock-runtime";
import {
  DynamoDBClient,
  PutItemCommand,
  SearchVectorsCommand,
} from "@aws-sdk/client-dynamodb";
import { marshall, unmarshall } from "@aws-sdk/util-dynamodb";
import type {
  APIGatewayProxyEventV2,
  APIGatewayProxyStructuredResultV2,
} from "aws-lambda";

const bedrock = new BedrockRuntimeClient({});
const dynamodb = new DynamoDBClient({});

interface DocumentRequest {
  readonly documentId: string;
  readonly title: string;
  readonly content: string;
  readonly tenantId: string;
  readonly category: string;
}

interface SearchRequest {
  readonly query: string;
  readonly tenantId: string;
  readonly category?: string;
  readonly topK?: number;
}

export async function handler(
  event: APIGatewayProxyEventV2,
): Promise<APIGatewayProxyStructuredResultV2> {
  try {
    if (event.routeKey === "POST /documents") {
      return await ingestDocument(parseJsonBody(event));
    }
    if (event.routeKey === "POST /search") {
      return await searchDocuments(parseJsonBody(event));
    }
    return jsonResponse(404, { message: "Route not found" });
  } catch (error) {
    if (error instanceof RequestValidationError) {
      return jsonResponse(400, { message: error.message });
    }
    console.error("Request failed", error);
    return jsonResponse(500, { message: "Internal server error" });
  }
}

async function ingestDocument(body: unknown): Promise<APIGatewayProxyStructuredResultV2> {
  const document = validateDocument(body);
  const embedding = await generateEmbedding(document.content);
  const tableName = requiredEnvironmentVariable("TABLE_NAME");

  await dynamodb.send(
    new PutItemCommand({
      TableName: tableName,
      Item: marshall(
        {
          ...document,
          embedding,
          createdAt: new Date().toISOString(),
        },
        { removeUndefinedValues: true },
      ),
    }),
  );

  return jsonResponse(201, {
    documentId: document.documentId,
    message: "Document embedded and stored",
  });
}

async function searchDocuments(body: unknown): Promise<APIGatewayProxyStructuredResultV2> {
  const request = validateSearch(body);
  const embedding = await generateEmbedding(request.query);

  const expressionAttributeNames: Record<string, string> = {
    "#tenantId": "tenantId",
  };
  const expressionAttributeValues = {
    ":tenantId": { S: request.tenantId },
    ...(request.category ? { ":category": { S: request.category } } : {}),
  };
  const conditions = ["#tenantId = :tenantId"];
  if (request.category) {
    expressionAttributeNames["#category"] = "category";
    conditions.push("#category = :category");
  }

  const response = await dynamodb.send(
    new SearchVectorsCommand({
      TableName: requiredEnvironmentVariable("TABLE_NAME"),
      IndexName: requiredEnvironmentVariable("VECTOR_INDEX_NAME"),
      SearchVector: embedding.map((value) => ({ N: String(value) })),
      TopK: request.topK ?? 5,
      SearchConditionExpression: conditions.join(" AND "),
      ExpressionAttributeNames: expressionAttributeNames,
      ExpressionAttributeValues: expressionAttributeValues,
      ProjectionExpression: "documentId, title, content, category",
    }),
  );

  return jsonResponse(200, {
    query: request.query,
    results: (response.SearchResults ?? []).map((result) => ({
      score: result.Score,
      ...(result.Item ? unmarshall(result.Item) : {}),
    })),
  });
}

async function generateEmbedding(text: string): Promise<number[]> {
  const dimensions = Number(requiredEnvironmentVariable("VECTOR_DIMENSIONS"));
  const response = await bedrock.send(
    new InvokeModelCommand({
      modelId: requiredEnvironmentVariable("EMBEDDING_MODEL_ID"),
      contentType: "application/json",
      accept: "application/json",
      body: JSON.stringify({
        inputText: text,
        dimensions,
        normalize: true,
      }),
    }),
  );

  const payload = JSON.parse(new TextDecoder().decode(response.body)) as {
    embedding?: number[];
  };
  if (!payload.embedding || payload.embedding.length !== dimensions) {
    throw new Error("The embedding model returned an unexpected vector size");
  }
  return payload.embedding;
}

function parseJsonBody(event: APIGatewayProxyEventV2): unknown {
  if (!event.body) {
    throw new RequestValidationError("Request body is required");
  }
  try {
    const body = event.isBase64Encoded
      ? Buffer.from(event.body, "base64").toString("utf8")
      : event.body;
    return JSON.parse(body) as unknown;
  } catch {
    throw new RequestValidationError("Request body must be valid JSON");
  }
}

function validateDocument(value: unknown): DocumentRequest {
  const body = requireObject(value);
  return {
    documentId: requireString(body, "documentId"),
    title: requireString(body, "title"),
    content: requireString(body, "content"),
    tenantId: requireString(body, "tenantId"),
    category: requireString(body, "category"),
  };
}

function validateSearch(value: unknown): SearchRequest {
  const body = requireObject(value);
  const topK = body.topK;
  if (topK !== undefined && (!Number.isInteger(topK) || Number(topK) < 1 || Number(topK) > 100)) {
    throw new RequestValidationError("topK must be an integer between 1 and 100");
  }
  return {
    query: requireString(body, "query"),
    tenantId: requireString(body, "tenantId"),
    category: optionalString(body, "category"),
    topK: topK === undefined ? undefined : Number(topK),
  };
}

function requireObject(value: unknown): Record<string, unknown> {
  if (!value || typeof value !== "object" || Array.isArray(value)) {
    throw new RequestValidationError("Request body must be a JSON object");
  }
  return value as Record<string, unknown>;
}

function requireString(value: Record<string, unknown>, key: string): string {
  const result = value[key];
  if (typeof result !== "string" || !result.trim()) {
    throw new RequestValidationError(`${key} must be a non-empty string`);
  }
  return result.trim();
}

function optionalString(value: Record<string, unknown>, key: string): string | undefined {
  if (value[key] === undefined) {
    return undefined;
  }
  return requireString(value, key);
}

function requiredEnvironmentVariable(name: string): string {
  const value = process.env[name];
  if (!value) {
    throw new Error(`Missing environment variable ${name}`);
  }
  return value;
}

function jsonResponse(statusCode: number, body: unknown): APIGatewayProxyStructuredResultV2 {
  return {
    statusCode,
    headers: { "content-type": "application/json" },
    body: JSON.stringify(body),
  };
}

class RequestValidationError extends Error {}
