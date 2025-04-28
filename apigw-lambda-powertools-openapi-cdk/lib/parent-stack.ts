import * as cdk from "aws-cdk-lib";
import { Construct } from "constructs";
import { DynamoDBStack } from "./dynamodb-stack";
import { LambdaStack } from "./lambda-stack";
import { ApiGatewayStack } from "./api-gateway-stack";
import { SecretsStack } from "./secrets-stack";
import { CognitoStack } from "./cognito-stack";

interface ParentStackProps extends cdk.StackProps {
  stageName: string;
}

export class ParentStack extends cdk.Stack {
  constructor(
    scope: Construct,
    id: string,
    props: ParentStackProps
  ) {
    super(scope, id, props);

    const secretsStack = new SecretsStack(this, "OrdersSecretsStack", {
      stageName: props.stageName,
    });

    const dynamoDbStack = new DynamoDBStack(this, "OrdersDynamoDBStack", {
      stageName: props.stageName,
    });
    const cognitoStack = new CognitoStack(this, "OrdersCognitoStack", {
      stageName: props.stageName,
    });

    const lambdaStack = new LambdaStack(this, "OrdersLambdaStack", {
      stageName: props.stageName,
      apiKey: secretsStack.apiKey,
      description: "Lambda functions for the API",
      table: dynamoDbStack.table,
    });

    const apiGatewayStack = new ApiGatewayStack(this, "OrdersApiStack", {
      stageName: props.stageName,
      handleLambda: lambdaStack.crudLambda,
      searchLambda: lambdaStack.searchLambda,
      description: "API Gateway with Lambda integration",
      userPool: cognitoStack.userPool,
    });

    new cdk.CfnOutput(this, "UserPoolId", {
      value: cognitoStack.userPool.userPoolId,
      description: "UserPoolId",
      exportName: "UserPoolId",
    });
    new cdk.CfnOutput(this, "UserPoolClientId", {
      value: cognitoStack.userPoolClient.userPoolClientId,
      description: "UserPoolClientId",
      exportName: "UserPoolClientId",
    });
    new cdk.CfnOutput(this, "ApiGatewayEndpoint", {
      value: apiGatewayStack.api.url,
      description: "ApiGatewayEndpoint",
      exportName: "ApiGatewayEndpoint",
    });
  }
}
