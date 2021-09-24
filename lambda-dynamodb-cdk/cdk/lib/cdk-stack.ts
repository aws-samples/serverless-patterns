import * as cdk from '@aws-cdk/core';
import { Table, BillingMode, AttributeType } from '@aws-cdk/aws-dynamodb';
import { NodejsFunction } from '@aws-cdk/aws-lambda-nodejs';
import * as lambda from '@aws-cdk/aws-lambda';
import * as path from 'path';

export class CdkStack extends cdk.Stack {
  constructor(scope: cdk.Construct, id: string, props?: cdk.StackProps) {
    super(scope, id, props);

    // DynamoDB Table
    const dynamoTable = new Table(this, 'DynamoTable', {
      partitionKey: {name:'ID', type: AttributeType.STRING},
      billingMode: BillingMode.PAY_PER_REQUEST
    });

    // Lambda function
    const lambdaPutDynamoDB = new NodejsFunction(
      this,
      'lambdaPutDynamoDBHandler',
      {
        runtime: lambda.Runtime.NODEJS_12_X,
        memorySize: 1024,
        timeout: cdk.Duration.seconds(3),
        entry: path.join(__dirname, '../src/app.ts'),
        handler: 'main',
      }
    );
  }
}
