import * as cdk from '@aws-cdk/core';
import { Table, BillingMode, AttributeType } from '@aws-cdk/aws-dynamodb';

export class CdkStack extends cdk.Stack {
  constructor(scope: cdk.Construct, id: string, props?: cdk.StackProps) {
    super(scope, id, props);

    // DynamoDB Table
    const dynamoTable = new Table(this, 'DynamoTable', {
      partitionKey: {name:'ID', type: AttributeType.STRING},
      billingMode: BillingMode.PAY_PER_REQUEST
    });
  }
}
