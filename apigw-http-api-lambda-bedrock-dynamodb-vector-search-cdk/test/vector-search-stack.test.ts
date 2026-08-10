import * as cdk from "aws-cdk-lib";
import { Match, Template } from "aws-cdk-lib/assertions";
import { VectorSearchStack } from "../lib/vector-search-stack";

describe("VectorSearchStack", () => {
  test("creates the semantic search API and DynamoDB vector index", () => {
    const app = new cdk.App();
    const stack = new VectorSearchStack(app, "TestStack");
    const template = Template.fromStack(stack);

    template.hasResourceProperties("AWS::DynamoDB::Table", {
      BillingMode: "PAY_PER_REQUEST",
      KeySchema: [
        { AttributeName: "tenantId", KeyType: "HASH" },
        { AttributeName: "documentId", KeyType: "RANGE" },
      ],
      PointInTimeRecoverySpecification: {
        PointInTimeRecoveryEnabled: true,
      },
    });
    template.hasResourceProperties("Custom::DynamoDBVectorIndex", {
      IndexName: "document-embedding-index",
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
        NonKeyAttributes: ["title", "content"],
      },
    });
    template.hasResourceProperties("AWS::Lambda::Function", {
      Runtime: "nodejs22.x",
      Architectures: ["arm64"],
      Environment: {
        Variables: Match.objectLike({
          VECTOR_INDEX_NAME: "document-embedding-index",
          EMBEDDING_MODEL_ID: "amazon.titan-embed-text-v2:0",
          VECTOR_DIMENSIONS: "1024",
        }),
      },
    });
    template.hasResourceProperties("AWS::ApiGatewayV2::Route", {
      RouteKey: "POST /documents",
    });
    template.hasResourceProperties("AWS::ApiGatewayV2::Route", {
      RouteKey: "POST /search",
    });
    template.resourceCountIs("AWS::StepFunctions::StateMachine", 0);
    template.resourceCountIs("AWS::Logs::LogGroup", 3);
    template.hasResourceProperties("AWS::IAM::Policy", {
      PolicyDocument: {
        Statement: Match.arrayWith([
          Match.objectLike({
            Action: "dynamodb:SearchVectors",
            Effect: "Allow",
          }),
          Match.objectLike({
            Action: "bedrock:InvokeModel",
            Effect: "Allow",
          }),
        ]),
      },
    });
  });
});
