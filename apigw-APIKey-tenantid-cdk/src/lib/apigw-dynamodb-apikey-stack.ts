import * as cdk from "aws-cdk-lib";
import * as apigateway from "aws-cdk-lib/aws-apigateway";
import * as lambda from "aws-cdk-lib/aws-lambda-nodejs";
import { Runtime } from "aws-cdk-lib/aws-lambda";
import * as dynamodb from "aws-cdk-lib/aws-dynamodb";
import * as cognito from "aws-cdk-lib/aws-cognito";
import * as path from "path";
import { Construct } from "constructs";

export class ApigwDynamodbApikeyStack extends cdk.Stack {
  constructor(scope: Construct, id: string, props?: cdk.StackProps) {
    super(scope, id, props);

    // DynamoDB table mapping tenantId -> apiKey
    const table = new dynamodb.Table(this, "TenantApiKeyTable", {
      partitionKey: { name: "tenantId", type: dynamodb.AttributeType.STRING },
      billingMode: dynamodb.BillingMode.PAY_PER_REQUEST,
      removalPolicy: cdk.RemovalPolicy.DESTROY,
    });

    // Cognito User Pool with custom tenantId attribute
    const userPool = new cognito.UserPool(this, "TenantUserPool", {
      selfSignUpEnabled: false,
      signInAliases: { email: true },
      customAttributes: {
        tenantId: new cognito.StringAttribute({ mutable: false }),
      },
      removalPolicy: cdk.RemovalPolicy.DESTROY,
    });

    const userPoolClient = userPool.addClient("TenantUserPoolClient", {
      authFlows: { userPassword: true },
    });

    // Lambda authorizer log group
    const authorizerLogGroup = new cdk.aws_logs.LogGroup(this, "AuthorizerLogGroup", {
      retention: cdk.aws_logs.RetentionDays.ONE_WEEK,
      removalPolicy: cdk.RemovalPolicy.DESTROY,
    });

    // Lambda authorizer
    const authorizerFn = new lambda.NodejsFunction(this, "DynamoDbApiKeyAuthorizer", {
      runtime: Runtime.NODEJS_22_X,
      entry: path.join(__dirname, "lambda/dynamodb-authorizer.js"),
      timeout: cdk.Duration.seconds(10),
      environment: {
        TABLE_NAME: table.tableName,
      },
      bundling: {
        externalModules: ["@aws-sdk/*"],
      },
      logGroup: authorizerLogGroup,
    });

    table.grantReadData(authorizerFn);

    // API Gateway
    const api = new apigateway.RestApi(this, "ApiGateway", {
      restApiName: "DynamoDB API Key Protected Service",
      description: "API protected with DynamoDB-based API key authorization",
    });

    // Token authorizer using Authorization header (Cognito JWT)
    const lambdaAuthorizer = new apigateway.TokenAuthorizer(this, "TokenAuthorizer", {
      handler: authorizerFn,
      identitySource: "method.request.header.Authorization",
    });

    // Protected endpoint with mock integration
    const protectedResource = api.root.addResource("protected");

    protectedResource.addMethod(
      "GET",
      new apigateway.MockIntegration({
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
      }),
      {
        authorizer: lambdaAuthorizer,
        methodResponses: [{ statusCode: "200" }],
      },
    );

    new cdk.CfnOutput(this, "ApiUrl", {
      value: api.url,
      description: "URL of the API Gateway",
    });

    new cdk.CfnOutput(this, "TableName", {
      value: table.tableName,
      description: "DynamoDB table name for tenant-apikey mappings",
    });

    new cdk.CfnOutput(this, "UserPoolId", {
      value: userPool.userPoolId,
      description: "Cognito User Pool ID",
    });

    new cdk.CfnOutput(this, "UserPoolClientId", {
      value: userPoolClient.userPoolClientId,
      description: "Cognito User Pool Client ID",
    });
  }
}
