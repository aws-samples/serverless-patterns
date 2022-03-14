import { CfnOutput, Duration, RemovalPolicy, Stack, StackProps} from 'aws-cdk-lib';
import { Construct } from 'constructs';
import { Table, BillingMode, AttributeType } from 'aws-cdk-lib/aws-dynamodb';
import { NodejsFunction } from 'aws-cdk-lib/aws-lambda-nodejs';
import { Runtime } from 'aws-cdk-lib/aws-lambda';
import path = require('path');

export class CdkStack extends Stack {
  constructor(scope: Construct, id: string, props?: StackProps) {
    super(scope, id, props);

    // DynamoDB Table
    const dynamoTable = new Table(this, 'DynamoTable', {
      partitionKey: {name:'ID', type: AttributeType.STRING},
      billingMode: BillingMode.PAY_PER_REQUEST,
      removalPolicy: RemovalPolicy.DESTROY
    });

    // Lambda function
    const lambdaPutDynamoDB = new NodejsFunction(this, 'lambdaPutDynamoDBHandler', {
      runtime: Runtime.NODEJS_12_X,
      memorySize: 1024,
      timeout: Duration.seconds(3),
      entry: path.join(__dirname, '../src/app.ts'),
      handler: 'main',
      environment: {
        DatabaseTable: dynamoTable.tableName
      }
    });

    // Write permissions for Lambda
    dynamoTable.grantWriteData(lambdaPutDynamoDB);

    // Outputs
    new CfnOutput(this, 'DynamoDbTableName', { value: dynamoTable.tableName });
    new CfnOutput(this, 'LambdFunctionArn', { value: lambdaPutDynamoDB.functionArn });
  }
}
