import {
  aws_dynamodb as ddb,
  CfnOutput,
  custom_resources,
  RemovalPolicy,
  Stack,
  StackProps
} from 'aws-cdk-lib';
import { Construct } from 'constructs';

export class DynamodbSeedDataOnCreateCdkStack extends Stack {
  constructor(scope: Construct, id: string, props?: StackProps) {
    super(scope, id, props);

    const table = new ddb.Table(this, 'MyDynamoDBTable', {
      partitionKey: { name: 'pk', type: ddb.AttributeType.STRING },
      sortKey: { name: 'type', type: ddb.AttributeType.STRING },
      billingMode: ddb.BillingMode.PAY_PER_REQUEST,
      removalPolicy: RemovalPolicy.DESTROY,
    });

    new custom_resources.AwsCustomResource(this, 'ddbInitData', {
      onCreate: {
        service: 'DynamoDB',
        action: 'putItem',
        parameters: {
          TableName: table.tableName,
          Item: {
            pk: { S: 'DiscountCode_ABC' },
            type: { S: 'DiscountCode' },
            code: { S: 'ABCD' },
          }
        },
        physicalResourceId: custom_resources.PhysicalResourceId.of(Date.now().toString()),
      },
      policy: custom_resources.AwsCustomResourcePolicy.fromSdkCalls({
        resources: [table.tableArn],
      }),
    });

    // Outputs
    new CfnOutput(this, 'DynamoDBTable', {
      value: table.tableName,
      description: 'DyanmoDB Table',
      exportName: 'DyanmoDBTableName',
    });
  }
}
