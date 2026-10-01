import * as cdk from "aws-cdk-lib";
import * as apigateway from "aws-cdk-lib/aws-apigateway";
import * as lambda from "aws-cdk-lib/aws-lambda-nodejs";
import { Runtime } from "aws-cdk-lib/aws-lambda";
import * as dynamodb from "aws-cdk-lib/aws-dynamodb";
import * as cognito from "aws-cdk-lib/aws-cognito";
import * as path from "path";
import { Construct } from "constructs";

export interface ApigwDynamodbApikeyStackProps extends cdk.StackProps {
  /**
   * Optional: An existing Usage Plan ID to associate with this API's stage.
   * If provided, the stack will import the usage plan and associate it with the API stage.
   * If not provided, the usage plan association is skipped.
   */
  usagePlanId?: string;
}

export class ApigwDynamodbApikeyStack extends cdk.Stack {
  constructor(scope: Construct, id: string, props?: ApigwDynamodbApikeyStackProps) {
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
      passwordPolicy: {
        minLength: 12,
        requireUppercase: true,
        requireLowercase: true,
        requireDigits: true,
        requireSymbols: true,
      },
      mfa: cognito.Mfa.OPTIONAL,
      mfaSecondFactor: {
        sms: true,
        otp: true,
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
        USER_POOL_ID: userPool.userPoolId,
        CLIENT_ID: userPoolClient.userPoolClientId,
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
      apiKeySourceType: apigateway.ApiKeySourceType.AUTHORIZER,
    });

    // Associate an existing usage plan with this API's deployment stage (if provided)
    const usagePlanId = props?.usagePlanId || this.node.tryGetContext("usagePlanId");
    if (usagePlanId) {
      new cdk.custom_resources.AwsCustomResource(this, "UsagePlanStageAssociation", {
        onCreate: {
          service: "APIGateway",
          action: "updateUsagePlan",
          parameters: {
            usagePlanId: usagePlanId,
            patchOperations: [
              {
                op: "add",
                path: "/apiStages",
                value: `${api.restApiId}:${api.deploymentStage.stageName}`,
              },
            ],
          },
          physicalResourceId: cdk.custom_resources.PhysicalResourceId.of(
            `${usagePlanId}-${api.restApiId}-stage`,
          ),
        },
        onDelete: {
          service: "APIGateway",
          action: "updateUsagePlan",
          parameters: {
            usagePlanId: usagePlanId,
            patchOperations: [
              {
                op: "remove",
                path: "/apiStages",
                value: `${api.restApiId}:${api.deploymentStage.stageName}`,
              },
            ],
          },
        },
        policy: cdk.custom_resources.AwsCustomResourcePolicy.fromStatements([
          new cdk.aws_iam.PolicyStatement({
            actions: ["apigateway:PATCH"],
            resources: [
              `arn:aws:apigateway:${this.region}::/usageplans/${usagePlanId}`,
            ],
          }),
        ]),
      });
    }

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
