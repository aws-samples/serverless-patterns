import { Stack, StackProps, CfnOutput } from 'aws-cdk-lib';
import { Construct } from 'constructs';
import { Table, BillingMode, AttributeType, StreamViewType } from 'aws-cdk-lib/aws-dynamodb';
import { NodejsFunction } from 'aws-cdk-lib/aws-lambda-nodejs';
import { aws_lambda as lambda }from 'aws-cdk-lib';
import * as path from 'path';
import { DynamoEventSource } from 'aws-cdk-lib/aws-lambda-event-sources';

export class DynamoToLambdaCdkStack extends Stack {
  constructor(scope: Construct, id: string, props?: StackProps) {
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
    new CfnOutput(this, 'DynamoDbTableName', { value: dynamoTable.tableName });
    new CfnOutput(this, 'LambdaFunctionArn', { value: lambdaReadStream.functionArn });
  }
}
