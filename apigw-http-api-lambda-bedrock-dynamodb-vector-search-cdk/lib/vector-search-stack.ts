import * as path from "node:path";
import * as cdk from "aws-cdk-lib";
import * as apigatewayv2 from "aws-cdk-lib/aws-apigatewayv2";
import * as integrations from "aws-cdk-lib/aws-apigatewayv2-integrations";
import * as dynamodb from "aws-cdk-lib/aws-dynamodb";
import * as iam from "aws-cdk-lib/aws-iam";
import * as lambda from "aws-cdk-lib/aws-lambda";
import * as lambdaNodejs from "aws-cdk-lib/aws-lambda-nodejs";
import * as logs from "aws-cdk-lib/aws-logs";
import { Construct } from "constructs";
import {
  DynamoDbVectorIndex,
  VectorDistanceFunction,
  VectorProjectionType,
  VectorSearchSchemaElementType,
} from "./dynamodb-vector-index";

const EMBEDDING_MODEL_ID = "amazon.titan-embed-text-v2:0";
const VECTOR_DIMENSIONS = 1024;
const VECTOR_INDEX_NAME = "document-embedding-index";

export class VectorSearchStack extends cdk.Stack {
  public constructor(scope: Construct, id: string, props?: cdk.StackProps) {
    super(scope, id, props);

    const table = new dynamodb.Table(this, "Documents", {
      partitionKey: {
        name: "documentId",
        type: dynamodb.AttributeType.STRING,
      },
      billingMode: dynamodb.BillingMode.PAY_PER_REQUEST,
      pointInTimeRecoverySpecification: {
        pointInTimeRecoveryEnabled: true,
      },
      removalPolicy: cdk.RemovalPolicy.DESTROY,
    });

    const vectorIndex = new DynamoDbVectorIndex(this, "DocumentEmbeddingIndex", {
      table,
      indexName: VECTOR_INDEX_NAME,
      vectorAttributeName: "embedding",
      dimensions: VECTOR_DIMENSIONS,
      distanceFunction: VectorDistanceFunction.COSINE,
      searchSchema: [
        {
          attributeName: "tenantId",
          elementType: VectorSearchSchemaElementType.HASH,
          attributeType: dynamodb.AttributeType.STRING,
        },
        {
          attributeName: "category",
          elementType: VectorSearchSchemaElementType.INLINE_FILTER,
          attributeType: dynamodb.AttributeType.STRING,
        },
      ],
      projection: {
        projectionType: VectorProjectionType.INCLUDE,
        nonKeyAttributes: ["title", "content"],
      },
    });

    const apiFunction = new lambdaNodejs.NodejsFunction(this, "VectorSearchFunction", {
      entry: path.join(__dirname, "../src/vector-search-handler.ts"),
      handler: "handler",
      runtime: lambda.Runtime.NODEJS_22_X,
      architecture: lambda.Architecture.ARM_64,
      memorySize: 512,
      timeout: cdk.Duration.seconds(30),
      environment: {
        TABLE_NAME: table.tableName,
        VECTOR_INDEX_NAME,
        EMBEDDING_MODEL_ID,
        VECTOR_DIMENSIONS: String(VECTOR_DIMENSIONS),
      },
      logGroup: new logs.LogGroup(this, "VectorSearchFunctionLogs", {
        retention: logs.RetentionDays.ONE_WEEK,
        removalPolicy: cdk.RemovalPolicy.DESTROY,
      }),
      bundling: {
        bundleAwsSDK: true,
        minify: true,
        sourceMap: true,
      },
    });

    table.grant(apiFunction, "dynamodb:PutItem");
    apiFunction.addToRolePolicy(
      new iam.PolicyStatement({
        actions: ["dynamodb:SearchVectors"],
        resources: [vectorIndex.indexArn],
      }),
    );
    apiFunction.addToRolePolicy(
      new iam.PolicyStatement({
        actions: ["bedrock:InvokeModel"],
        resources: [
          this.formatArn({
            service: "bedrock",
            region: this.region,
            account: "",
            resource: "foundation-model",
            resourceName: EMBEDDING_MODEL_ID,
          }),
        ],
      }),
    );

    const httpApi = new apigatewayv2.HttpApi(this, "VectorSearchApi", {
      description: "Ingest documents and run semantic search with DynamoDB vector indexes",
      corsPreflight: {
        allowHeaders: ["content-type"],
        allowMethods: [apigatewayv2.CorsHttpMethod.POST],
        allowOrigins: ["*"],
      },
    });
    const integration = new integrations.HttpLambdaIntegration(
      "VectorSearchIntegration",
      apiFunction,
    );

    httpApi.addRoutes({
      path: "/documents",
      methods: [apigatewayv2.HttpMethod.POST],
      integration,
    });
    httpApi.addRoutes({
      path: "/search",
      methods: [apigatewayv2.HttpMethod.POST],
      integration,
    });

    new cdk.CfnOutput(this, "ApiEndpoint", {
      description: "HTTP API base URL",
      value: httpApi.apiEndpoint,
    });
    new cdk.CfnOutput(this, "TableName", {
      description: "DynamoDB table containing documents and embeddings",
      value: table.tableName,
    });
    new cdk.CfnOutput(this, "VectorIndexName", {
      description: "DynamoDB vector index used by SearchVectors",
      value: vectorIndex.indexName,
    });
    new cdk.CfnOutput(this, "VectorSearchFunctionName", {
      description: "Lambda function backing both HTTP API routes",
      value: apiFunction.functionName,
    });
  }
}
