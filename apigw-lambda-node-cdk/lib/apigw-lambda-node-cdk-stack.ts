// lib/rest-api-gateway-lambda-stack.ts
import * as cdk from 'aws-cdk-lib';
import { Construct } from 'constructs';
import { DynamoDBStack } from './dynamodb-stack';
import { LambdaStack } from './lambda-stack';
import { ApiGatewayStack } from './api-gateway-stack';
import { SecretsStack } from './secrets-stack';
import { CognitoStack } from './cognito-stack';

interface ApigwLambdaNodeStackProps extends cdk.StackProps {
  stageName: string;
}

export class ApigwLambdaNodeStack extends cdk.Stack {
  constructor(scope: Construct, id: string, props: ApigwLambdaNodeStackProps) {
    super(scope, id, props);

    // Create Secrets Stack
    const secretsStack = new SecretsStack(this, 'OrdersSecretsStack', {
        crossRegionReferences: true
    });

    const dynamoDbStack = new DynamoDBStack(this, 'OrdersDynamoDBStack')

    const cognitoStack = new CognitoStack(this, 'OrdersCognitoStack');

    // Create Lambda nested stack
    const lambdaStack = new LambdaStack(this, 'OrdersLambdaStack', {
      stageName: props.stageName,
      apiKey: secretsStack.apiKey,
      description: 'Lambda functions for the API',
      table: dynamoDbStack.table
    });

    // Create API Gateway nested stack
    const apiGatewayStack = new ApiGatewayStack(this, 'OrdersApiStack', {
      stageName: props.stageName,
      handleLambda: lambdaStack.handleLambda,
      searchLambda: lambdaStack.searchLambda,
      description: 'API Gateway with Lambda integration',
      userPool: cognitoStack.userPool
    });
    apiGatewayStack.node.addDependency(cognitoStack);
  }
}
