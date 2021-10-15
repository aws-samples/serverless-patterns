import * as cdk from '@aws-cdk/core';
import { Table, BillingMode, AttributeType, StreamViewType } from '@aws-cdk/aws-dynamodb';
import { NodejsFunction } from '@aws-cdk/aws-lambda-nodejs';
import * as lambda from '@aws-cdk/aws-lambda';
import * as path from 'path';
import { DynamoEventSource } from '@aws-cdk/aws-lambda-event-sources';

export class DynamoToLambdaCdkStack extends cdk.Stack {
  constructor(scope: cdk.Construct, id: string, props?: cdk.StackProps) {
    super(scope, id, props);
    // DynamoDB table
    const dynamoTable = new Table(this, 'DynamoTable', {
      partitionKey: {name:'pk', type: AttributeType.STRING},
      billingMode: BillingMode.PAY_PER_REQUEST,
      stream: StreamViewType.NEW_IMAGE
    });
    // Lambda Function to read from Stream
    const lambdaReadStream = new NodejsFunction(this, 'readStream', {
      entry: 'lambda-fns/readStream/handler.js',
      handler: 'handler'
    });

    // Write permissions for Lambda
    dynamoTable.grantReadWriteData(lambdaReadStream);

    // Event Source Mapping DynamoDB -> Lambda
    lambdaReadStream.addEventSource(new DynamoEventSource(dynamoTable, {
      startingPosition: lambda.StartingPosition.TRIM_HORIZON,
      batchSize: 10,
      retryAttempts: 0
    }))

    // Outputs
    new cdk.CfnOutput(this, 'DynamoDbTableName', { value: dynamoTable.tableName });
    new cdk.CfnOutput(this, 'LambdaFunctionArn', { value: lambdaReadStream.functionArn });
  }
}
