import * as path from "node:path";
import * as cdk from "aws-cdk-lib";
import * as dynamodb from "aws-cdk-lib/aws-dynamodb";
import * as lambda from "aws-cdk-lib/aws-lambda";
import * as lambdaNodejs from "aws-cdk-lib/aws-lambda-nodejs";
import * as logs from "aws-cdk-lib/aws-logs";
import * as customResources from "aws-cdk-lib/custom-resources";
import { Construct } from "constructs";

export enum VectorDistanceFunction {
  COSINE = "COSINE",
  DOT_PRODUCT = "DOT_PRODUCT",
  EUCLIDEAN = "EUCLIDEAN",
}

export enum VectorSearchSchemaElementType {
  HASH = "HASH",
  INLINE_FILTER = "INLINE_FILTER",
}

export enum VectorProjectionType {
  ALL = "ALL",
  INCLUDE = "INCLUDE",
  KEYS_ONLY = "KEYS_ONLY",
}

export interface VectorSearchSchemaElement {
  readonly attributeName: string;
  readonly elementType: VectorSearchSchemaElementType;
  readonly attributeType: dynamodb.AttributeType;
}

export interface VectorIndexProjection {
  readonly projectionType: VectorProjectionType;
  readonly nonKeyAttributes?: string[];
}

export interface DynamoDbVectorIndexProps {
  readonly table: dynamodb.ITable;
  readonly indexName: string;
  readonly vectorAttributeName: string;
  readonly dimensions: number;
  readonly distanceFunction: VectorDistanceFunction;
  readonly searchSchema?: VectorSearchSchemaElement[];
  readonly projection?: VectorIndexProjection;
}

/**
 * Adds a native vector index to a CDK-managed DynamoDB table.
 *
 * Vector index creation and backfill are asynchronous. The custom-resource
 * provider waits until the index is ACTIVE and Backfilling is false.
 */
export class DynamoDbVectorIndex extends Construct {
  public readonly indexArn: string;
  public readonly indexName: string;

  public constructor(scope: Construct, id: string, props: DynamoDbVectorIndexProps) {
    super(scope, id);

    validateProps(props);

    this.indexName = props.indexName;
    this.indexArn = `${props.table.tableArn}/index/${props.indexName}`;

    const provider = getOrCreateProvider(cdk.Stack.of(this));
    props.table.grant(provider.onEventHandler, "dynamodb:DescribeTable", "dynamodb:UpdateTable");

    const projection = props.projection ?? {
      projectionType: VectorProjectionType.KEYS_ONLY,
    };

    const resource = new cdk.CustomResource(this, "Resource", {
      serviceToken: provider.serviceToken,
      resourceType: "Custom::DynamoDBVectorIndex",
      properties: {
        TableName: props.table.tableName,
        IndexName: props.indexName,
        VectorAttributeName: props.vectorAttributeName,
        Dimensions: props.dimensions,
        DistanceFunction: props.distanceFunction,
        SearchSchema: (props.searchSchema ?? []).map((element) => ({
          AttributeName: element.attributeName,
          SearchSchemaElementType: element.elementType,
          AttributeType: toScalarAttributeType(element.attributeType),
        })),
        Projection: {
          ProjectionType: projection.projectionType,
          NonKeyAttributes: projection.nonKeyAttributes ?? [],
        },
      },
    });

    resource.node.addDependency(props.table);
  }
}

class VectorIndexProvider extends Construct {
  public readonly onEventHandler: lambdaNodejs.NodejsFunction;
  public readonly serviceToken: string;

  public constructor(scope: Construct, id: string) {
    super(scope, id);

    const entry = path.join(__dirname, "../src/vector-index-provider.ts");
    const commonFunctionProps: Omit<lambdaNodejs.NodejsFunctionProps, "handler"> = {
      entry,
      runtime: lambda.Runtime.NODEJS_22_X,
      timeout: cdk.Duration.minutes(14),
      memorySize: 256,
      bundling: {
        bundleAwsSDK: true,
        minify: true,
        sourceMap: true,
      },
    };

    this.onEventHandler = new lambdaNodejs.NodejsFunction(this, "OnEvent", {
      ...commonFunctionProps,
      handler: "onEvent",
      logGroup: new logs.LogGroup(this, "OnEventLogs", {
        retention: logs.RetentionDays.ONE_WEEK,
        removalPolicy: cdk.RemovalPolicy.DESTROY,
      }),
    });

    const provider = new customResources.Provider(this, "Framework", {
      onEventHandler: this.onEventHandler,
    });
    this.serviceToken = provider.serviceToken;
  }
}

function getOrCreateProvider(stack: cdk.Stack): VectorIndexProvider {
  const providerId = "DynamoDbVectorIndexProvider";
  const existing = stack.node.tryFindChild(providerId);
  if (existing) {
    return existing as VectorIndexProvider;
  }
  return new VectorIndexProvider(stack, providerId);
}

function toScalarAttributeType(attributeType: dynamodb.AttributeType): "S" | "N" | "B" {
  switch (attributeType) {
    case dynamodb.AttributeType.STRING:
      return "S";
    case dynamodb.AttributeType.NUMBER:
      return "N";
    case dynamodb.AttributeType.BINARY:
      return "B";
  }
}

function validateProps(props: DynamoDbVectorIndexProps): void {
  if (!/^[A-Za-z0-9_.-]{3,255}$/.test(props.indexName)) {
    throw new Error("indexName must be 3-255 characters and contain only letters, numbers, _, -, or .");
  }
  if (!props.vectorAttributeName) {
    throw new Error("vectorAttributeName must not be empty");
  }
  if (!Number.isInteger(props.dimensions) || props.dimensions < 1 || props.dimensions > 4096) {
    throw new Error("dimensions must be an integer between 1 and 4096");
  }

  const searchSchema = props.searchSchema ?? [];
  const hashElements = searchSchema.filter(
    (element) => element.elementType === VectorSearchSchemaElementType.HASH,
  );
  const inlineFilters = searchSchema.filter(
    (element) => element.elementType === VectorSearchSchemaElementType.INLINE_FILTER,
  );
  if (hashElements.length > 1) {
    throw new Error("A vector index can have at most one HASH search-schema element");
  }
  if (inlineFilters.length > 18) {
    throw new Error("A vector index can have at most 18 INLINE_FILTER search-schema elements");
  }
  const attributeNames = searchSchema.map((element) => element.attributeName);
  if (new Set(attributeNames).size !== attributeNames.length) {
    throw new Error("Search-schema attribute names must be unique");
  }

  const projection = props.projection;
  if (projection?.projectionType === VectorProjectionType.INCLUDE) {
    if (!projection.nonKeyAttributes?.length) {
      throw new Error("INCLUDE projection requires at least one nonKeyAttribute");
    }
  } else if (projection?.nonKeyAttributes?.length) {
    throw new Error("nonKeyAttributes can only be supplied with an INCLUDE projection");
  }
}
