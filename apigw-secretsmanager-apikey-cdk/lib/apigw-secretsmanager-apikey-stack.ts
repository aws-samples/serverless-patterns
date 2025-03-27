import * as cdk from "aws-cdk-lib";
import * as apigateway from "aws-cdk-lib/aws-apigateway";
import * as lambda from "aws-cdk-lib/aws-lambda-nodejs";
import { Runtime } from "aws-cdk-lib/aws-lambda";
import * as iam from "aws-cdk-lib/aws-iam";
import * as path from "path";
import { Construct } from "constructs";

export class ApigwSecretsmanagerApikeyStack extends cdk.Stack {
  constructor(scope: Construct, id: string, props?: cdk.StackProps) {
    super(scope, id, props);

    // Create IAM role for the authorizer Lambda
    const authorizerRole = new iam.Role(this, "AuthorizerRole", {
      assumedBy: new iam.ServicePrincipal("lambda.amazonaws.com"),
      managedPolicies: [iam.ManagedPolicy.fromAwsManagedPolicyName("service-role/AWSLambdaBasicExecutionRole")],
    });

    // Add more specific permission to access only relevant Secrets Manager secrets
    authorizerRole.addToPolicy(
      new iam.PolicyStatement({
        actions: ["secretsmanager:GetSecretValue", "secretsmanager:DescribeSecret"],
        resources: [`arn:aws:secretsmanager:${this.region}:${this.account}:secret:api-key-*`],
      }),
    );

    // Create a dedicated logGroup for ApiKeyAuthorizer
    const authorizerLogGroup = new cdk.aws_logs.LogGroup(this, "AuthorizerLogGroup", {
      retention: cdk.aws_logs.RetentionDays.ONE_WEEK,
      removalPolicy: cdk.RemovalPolicy.DESTROY,
    });

    // Create Lambda authorizer
    const authorizer = new lambda.NodejsFunction(this, "ApiKeyAuthorizer", {
      runtime: Runtime.NODEJS_22_X,
      entry: path.join(__dirname, "lambda/authorizer.js"),
      role: authorizerRole,
      timeout: cdk.Duration.seconds(10),
      environment: {
        SECRET_PREFIX: "api-key-",
      },
      bundling: {
        externalModules: [
          "@aws-sdk/*", // AWS SDK v3 modules
        ],
      },
      logGroup: authorizerLogGroup,
    });

    // Create API Gateway
    const api = new apigateway.RestApi(this, "ApiGateway", {
      restApiName: "API Key Protected Service",
      description: "API protected with API key authorization",
    });

    // Create Lambda authorizer
    const lambdaAuthorizer = new apigateway.TokenAuthorizer(this, "TokenAuthorizer", {
      handler: authorizer,
      identitySource: "method.request.header.x-api-key",
    });

    // Sample protected endpoint
    const protectedResource = api.root.addResource("protected");

    // Mock integration for demo purposes
    const integration = new apigateway.MockIntegration({
      integrationResponses: [
        {
          statusCode: "200",
          responseTemplates: {
            "application/json": '{ "message": "Access granted" }',
          },
        },
      ],
      passthroughBehavior: apigateway.PassthroughBehavior.NEVER,
      requestTemplates: {
        "application/json": '{ "statusCode": 200 }',
      },
    });

    // Add method with authorizer
    protectedResource.addMethod("GET", integration, {
      authorizer: lambdaAuthorizer,
      methodResponses: [{ statusCode: "200" }],
    });

    // Output the API URL
    new cdk.CfnOutput(this, "ApiUrl", {
      value: api.url,
      description: "URL of the API Gateway",
    });
  }
}
