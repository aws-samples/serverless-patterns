import {
  AttributeDefinition,
  CreateVectorIndexAction,
  DescribeTableCommand,
  DynamoDBClient,
  Projection,
  ResourceNotFoundException,
  SearchSchemaElement,
  UpdateTableCommand,
  VectorIndexDescription,
} from "@aws-sdk/client-dynamodb";
import type { CloudFormationCustomResourceEvent } from "aws-lambda";

const dynamodb = new DynamoDBClient({});

interface VectorIndexProperties {
  readonly TableName: string;
  readonly IndexName: string;
  readonly VectorAttributeName: string;
  readonly Dimensions: number | string;
  readonly DistanceFunction: "COSINE" | "DOT_PRODUCT" | "EUCLIDEAN";
  readonly SearchSchema?: Array<{
    readonly AttributeName: string;
    readonly SearchSchemaElementType: "HASH" | "INLINE_FILTER";
    readonly AttributeType: "S" | "N" | "B";
  }>;
  readonly Projection: {
    readonly ProjectionType: "ALL" | "INCLUDE" | "KEYS_ONLY";
    readonly NonKeyAttributes?: string[];
  };
  readonly ServiceToken?: string;
}

interface OnEventResponse {
  readonly PhysicalResourceId: string;
}

export async function onEvent(event: CloudFormationCustomResourceEvent): Promise<OnEventResponse> {
  const properties = parseProperties(event.ResourceProperties);
  const physicalResourceId = physicalId(properties);

  if (event.RequestType === "Delete") {
    await deleteIndexIfPresent(properties);
    await waitForIndex(properties, false);
    return { PhysicalResourceId: event.PhysicalResourceId ?? physicalResourceId };
  }

  if (event.RequestType === "Update") {
    const oldProperties = parseProperties(event.OldResourceProperties);
    const sameResource =
      oldProperties.TableName === properties.TableName &&
      oldProperties.IndexName === properties.IndexName;
    if (sameResource && !sameConfiguration(oldProperties, properties)) {
      throw new Error(
        "DynamoDB vector-index dimensions, distance function, schema, vector attribute, and projection are immutable. " +
          "Change indexName to replace the index safely.",
      );
    }
  }

  await createIndexIfNeeded(properties);
  await waitForIndex(properties, true);
  return { PhysicalResourceId: physicalResourceId };
}

async function createIndexIfNeeded(properties: VectorIndexProperties): Promise<void> {
  const table = await describeTable(properties.TableName);
  const existing = table.VectorIndexes?.find((index) => index.IndexName === properties.IndexName);
  if (existing) {
    assertExistingIndexMatches(existing, properties);
    return;
  }

  const attributeDefinitions: AttributeDefinition[] = (properties.SearchSchema ?? [])
    .map((element) => ({
      AttributeName: element.AttributeName,
      AttributeType: element.AttributeType,
    }));

  const create: CreateVectorIndexAction = {
    IndexName: properties.IndexName,
    VectorAttribute: { AttributeName: properties.VectorAttributeName },
    Dimensions: Number(properties.Dimensions),
    DistanceFunction: properties.DistanceFunction,
    Projection: toProjection(properties),
    SearchSchema: toSearchSchema(properties),
  };

  await dynamodb.send(
    new UpdateTableCommand({
      TableName: properties.TableName,
      // DynamoDB requires every SearchSchema attribute in this UpdateTable
      // request, including attributes already used by the base table key.
      AttributeDefinitions: attributeDefinitions.length ? attributeDefinitions : undefined,
      VectorIndexUpdates: [{ Create: create }],
    }),
  );
}

async function waitForIndex(
  properties: VectorIndexProperties,
  shouldExist: boolean,
): Promise<void> {
  const deadline = Date.now() + 13 * 60 * 1000;
  while (Date.now() < deadline) {
    const index = await findIndex(properties.TableName, properties.IndexName);
    if (!shouldExist && !index) {
      return;
    }
    if (shouldExist && index?.IndexStatus === "ACTIVE" && index.Backfilling !== true) {
      return;
    }
    await delay(10_000);
  }
  throw new Error(
    `Timed out waiting for vector index ${properties.IndexName} on table ${properties.TableName}`,
  );
}

function delay(milliseconds: number): Promise<void> {
  return new Promise((resolve) => setTimeout(resolve, milliseconds));
}

async function deleteIndexIfPresent(properties: VectorIndexProperties): Promise<void> {
  const index = await findIndex(properties.TableName, properties.IndexName);
  if (!index) {
    return;
  }
  if (index.IndexStatus === "DELETING") {
    return;
  }
  await dynamodb.send(
    new UpdateTableCommand({
      TableName: properties.TableName,
      VectorIndexUpdates: [{ Delete: { IndexName: properties.IndexName } }],
    }),
  );
}

async function findIndex(
  tableName: string,
  indexName: string,
): Promise<VectorIndexDescription | undefined> {
  try {
    const table = await describeTable(tableName);
    return table.VectorIndexes?.find((index) => index.IndexName === indexName);
  } catch (error) {
    if (error instanceof ResourceNotFoundException) {
      return undefined;
    }
    throw error;
  }
}

async function describeTable(tableName: string) {
  const response = await dynamodb.send(new DescribeTableCommand({ TableName: tableName }));
  if (!response.Table) {
    throw new Error(`DynamoDB did not return a description for table ${tableName}`);
  }
  return response.Table;
}

function assertExistingIndexMatches(
  existing: VectorIndexDescription,
  properties: VectorIndexProperties,
): void {
  const matches =
    existing.VectorAttribute?.AttributeName === properties.VectorAttributeName &&
    existing.Dimensions === Number(properties.Dimensions) &&
    existing.DistanceFunction === properties.DistanceFunction &&
    normalizedSchema(existing.SearchSchema) === normalizedSchema(toSearchSchema(properties)) &&
    normalizedProjection(existing.Projection) === normalizedProjection(toProjection(properties));

  if (!matches) {
    throw new Error(
      `Vector index ${properties.IndexName} already exists on ${properties.TableName} with a different configuration`,
    );
  }
}

function sameConfiguration(
  oldProperties: VectorIndexProperties,
  newProperties: VectorIndexProperties,
): boolean {
  return (
    oldProperties.VectorAttributeName === newProperties.VectorAttributeName &&
    Number(oldProperties.Dimensions) === Number(newProperties.Dimensions) &&
    oldProperties.DistanceFunction === newProperties.DistanceFunction &&
    normalizedSchema(toSearchSchema(oldProperties)) === normalizedSchema(toSearchSchema(newProperties)) &&
    normalizedProjection(toProjection(oldProperties)) ===
      normalizedProjection(toProjection(newProperties))
  );
}

function toSearchSchema(properties: VectorIndexProperties): SearchSchemaElement[] | undefined {
  if (!properties.SearchSchema?.length) {
    return undefined;
  }
  return properties.SearchSchema.map((element) => ({
    AttributeName: element.AttributeName,
    SearchSchemaElementType: element.SearchSchemaElementType,
  }));
}

function toProjection(properties: VectorIndexProperties): Projection {
  return {
    ProjectionType: properties.Projection.ProjectionType,
    NonKeyAttributes:
      properties.Projection.ProjectionType === "INCLUDE"
        ? properties.Projection.NonKeyAttributes
        : undefined,
  };
}

function normalizedSchema(schema: SearchSchemaElement[] | undefined): string {
  return JSON.stringify(
    [...(schema ?? [])].sort((left, right) =>
      (left.AttributeName ?? "").localeCompare(right.AttributeName ?? ""),
    ),
  );
}

function normalizedProjection(projection: Projection | undefined): string {
  return JSON.stringify({
    ProjectionType: projection?.ProjectionType,
    NonKeyAttributes: [...(projection?.NonKeyAttributes ?? [])].sort(),
  });
}

function physicalId(properties: VectorIndexProperties): string {
  return `${properties.TableName}/index/${properties.IndexName}`;
}

function parseProperties(properties: Record<string, unknown>): VectorIndexProperties {
  const parsed = properties as unknown as VectorIndexProperties;
  if (
    !parsed.TableName ||
    !parsed.IndexName ||
    !parsed.VectorAttributeName ||
    !parsed.Dimensions ||
    !parsed.DistanceFunction ||
    !parsed.Projection
  ) {
    throw new Error("The DynamoDB vector-index custom resource is missing required properties");
  }
  return parsed;
}
