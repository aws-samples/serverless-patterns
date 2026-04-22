import * as cdk from "aws-cdk-lib";
import * as apigateway from "aws-cdk-lib/aws-apigateway";
import * as lambda from "aws-cdk-lib/aws-lambda-nodejs";
import * as cognito from "aws-cdk-lib/aws-cognito";
import * as iam from "aws-cdk-lib/aws-iam";
import { Runtime } from "aws-cdk-lib/aws-lambda";
import * as path from "path";
import { Construct } from "constructs";

export class ApigwArbitraryKeysStack extends cdk.Stack {
  constructor(scope: Construct, id: string, props?: cdk.StackProps) {
    super(scope, id, props);

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

    const authorizerLogGroup = new cdk.aws_logs.LogGroup(this, "AuthorizerLogGroup", {
      retention: cdk.aws_logs.RetentionDays.ONE_WEEK,
      removalPolicy: cdk.RemovalPolicy.DESTROY,
    });

    const authorizerFn = new lambda.NodejsFunction(this, "ArbitraryKeyAuthorizer", {
      runtime: Runtime.NODEJS_24_X,
      entry: path.join(__dirname, "lambda/arbitrary-key-authorizer.js"),
      timeout: cdk.Duration.seconds(10),
      bundling: { externalModules: ["@aws-sdk/*"] },
      logGroup: authorizerLogGroup,
    });

    // Allow lambda to read usage plans
    authorizerFn.addToRolePolicy(
      new iam.PolicyStatement({
        actions: ["apigateway:GET"],
        resources: [`arn:aws:apigateway:${this.region}::/usageplans`],
      }),
    );

    // API Gateway with key source from AUTHORIZER
    const api = new apigateway.RestApi(this, "ApiGateway", {
      restApiName: "Arbitrary Usage Identifier Key Service",
      apiKeySourceType: apigateway.ApiKeySourceType.AUTHORIZER,
      deploy: false,
    });

    // Token authorizer using Authorization header (Cognito JWT)
    const lambdaAuthorizer = new apigateway.TokenAuthorizer(this, "TokenAuthorizer", {
      handler: authorizerFn,
      identitySource: "method.request.header.Authorization",
    });

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
        requestTemplates: { "application/json": '{ "statusCode": 200 }' },
      }),
      {
        authorizer: lambdaAuthorizer,
        apiKeyRequired: true,
        methodResponses: [{ statusCode: "200" }],
      },
    );

    // Prod stage
    const prodDeployment = new apigateway.Deployment(this, "ProdDeployment", { api });
    const prodStage = new apigateway.Stage(this, "ProdStage", {
      deployment: prodDeployment,
      stageName: "prod",
    });
    api.deploymentStage = prodStage;

    // Dev stage
    const devDeployment = new apigateway.Deployment(this, "DevDeployment", { api });
    const devStage = new apigateway.Stage(this, "DevStage", {
      deployment: devDeployment,
      stageName: "dev",
    });

    // Usage plans per stage
    const prodUsagePlan = new apigateway.UsagePlan(this, "ProdUsagePlan", {
      name: "ProdUsagePlan",
      throttle: { rateLimit: 100, burstLimit: 50 },
      quota: { limit: 10000, period: apigateway.Period.MONTH },
      apiStages: [{ api, stage: prodStage }],
    });

    const devUsagePlan = new apigateway.UsagePlan(this, "DevUsagePlan", {
      name: "DevUsagePlan",
      throttle: { rateLimit: 10, burstLimit: 5 },
      quota: { limit: 1000, period: apigateway.Period.MONTH },
      apiStages: [{ api, stage: devStage }],
    });

    new cdk.CfnOutput(this, "ProdApiUrl", { value: prodStage.urlForPath("/") });
    new cdk.CfnOutput(this, "DevApiUrl", { value: devStage.urlForPath("/") });
    new cdk.CfnOutput(this, "ProdUsagePlanId", { value: prodUsagePlan.usagePlanId });
    new cdk.CfnOutput(this, "DevUsagePlanId", { value: devUsagePlan.usagePlanId });
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
