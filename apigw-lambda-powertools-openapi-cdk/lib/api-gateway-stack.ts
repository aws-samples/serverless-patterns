// lib/api-gateway-stack.ts
import * as cdk from "aws-cdk-lib";
import * as apigateway from "aws-cdk-lib/aws-apigateway";
import * as cognito from "aws-cdk-lib/aws-cognito";
import * as lambda from "aws-cdk-lib/aws-lambda";
import { Construct } from "constructs";
import * as path from "path";
import * as fs from "fs";

interface ApiGatewayStackProps extends cdk.NestedStackProps {
  handleLambda: lambda.Function;
  searchLambda: lambda.Function;
  stageName: string;
  userPool: cognito.UserPool;
}

export class ApiGatewayStack extends cdk.NestedStack {
  public readonly api: apigateway.SpecRestApi;

  constructor(scope: Construct, id: string, props: ApiGatewayStackProps) {
    super(scope, id, props);

    const openApiSpecContent = fs.readFileSync(
      path.join(__dirname, "openapi/openapi.json"),
      "utf8"
    );

    const openApiSpec = JSON.parse(
      openApiSpecContent
        .replaceAll("${lambdaArn}", props.handleLambda.functionArn)
        .replaceAll("${region}", cdk.Stack.of(this).region)
        .replaceAll("${searchLambdaArn}", props.searchLambda.functionArn)
        .replaceAll("${accountId}", cdk.Stack.of(this).account)
        .replaceAll("${userPoolId}", props.userPool.userPoolId)
    );

    this.api = new apigateway.SpecRestApi(this, "SampleApiGatewayLambda2Api", {
      restApiName: "OrdersAPI",
      description: "API Gateway with Lambda integration",
      apiDefinition: apigateway.ApiDefinition.fromInline(openApiSpec),
      deployOptions: {
        tracingEnabled: true,
        dataTraceEnabled: true,
        stageName: props.stageName,
      },
      cloudWatchRole: false,
    });

    new lambda.CfnPermission(this, "LambdaHandlerPermission", {
      action: "lambda:InvokeFunction",
      functionName: props.handleLambda.functionName,
      principal: "apigateway.amazonaws.com",
      sourceArn: `arn:aws:execute-api:${this.region}:${this.account}:${this.api.restApiId}/*/*/order*`,
    });

    new lambda.CfnPermission(this, "LambdaSearchPermission", {
      action: "lambda:InvokeFunction",
      functionName: props.searchLambda.functionName,
      principal: "apigateway.amazonaws.com",
      sourceArn: `arn:aws:execute-api:${this.region}:${this.account}:${this.api.restApiId}/*/*/orders/search*`,
    });
  }
}
