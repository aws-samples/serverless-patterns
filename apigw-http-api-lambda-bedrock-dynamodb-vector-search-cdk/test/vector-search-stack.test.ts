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
    template.hasResourceProperties("AWS::DynamoDB::Table", {
      SSESpecification: { SSEEnabled: true },
      AttributeDefinitions: [
        { AttributeName: "tenantId", AttributeType: "S" },
        { AttributeName: "documentId", AttributeType: "S" },
        { AttributeName: "category", AttributeType: "S" },
      ],
      VectorIndexes: [{
        IndexName: "document-embedding-index",
        VectorAttribute: { AttributeName: "embedding" },
        Dimensions: 1024,
        DistanceFunction: "COSINE",
        SearchSchema: [
          { AttributeName: "tenantId", SearchSchemaElementType: "HASH" },
          { AttributeName: "category", SearchSchemaElementType: "INLINE_FILTER" },
        ],
        Projection: {
          ProjectionType: "INCLUDE",
          NonKeyAttributes: ["title", "content"],
        },
      }],
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
    template.resourceCountIs("AWS::Logs::LogGroup", 1);
    template.resourceCountIs("AWS::Lambda::Function", 1);
    template.resourceCountIs("Custom::DynamoDBVectorIndex", 0);
    template.hasResourceProperties("AWS::IAM::Policy", {
      PolicyDocument: {
        Statement: Match.arrayWith([
          Match.objectLike({
            Action: "dynamodb:SearchVectors",
            Effect: "Allow",
            Resource: {
              "Fn::Join": ["", [
                { "Fn::GetAtt": [stack.getLogicalId(
                  stack.node.findChild("Documents").node.defaultChild as cdk.CfnResource,
                ), "Arn"] },
                "/index/document-embedding-index",
              ]],
            },
          }),
          Match.objectLike({
            Action: "bedrock:InvokeModel",
            Effect: "Allow",
          }),
        ]),
      },
    });
    const resources = Object.values(template.toJSON().Resources) as Array<{
      Type: string;
      Properties?: { PolicyDocument?: { Statement: Array<{ Action: string | string[] }> } };
    }>;
    const actions = resources
      .filter((resource) => resource.Type === "AWS::IAM::Policy")
      .flatMap((resource) => resource.Properties?.PolicyDocument?.Statement ?? [])
      .flatMap((statement) => statement.Action);
    expect(actions).not.toContain("dynamodb:UpdateTable");
    expect(actions).not.toContain("dynamodb:DescribeTable");
  });
});
