import * as path from 'path';
import * as cdk from 'aws-cdk-lib';
import * as dynamodb from 'aws-cdk-lib/aws-dynamodb';
import * as events from 'aws-cdk-lib/aws-events';
import * as targets from 'aws-cdk-lib/aws-events-targets';
import * as iam from 'aws-cdk-lib/aws-iam';
import * as lambda from 'aws-cdk-lib/aws-lambda';
import * as destinations from 'aws-cdk-lib/aws-lambda-destinations';
import * as logs from 'aws-cdk-lib/aws-logs';
import * as sqs from 'aws-cdk-lib/aws-sqs';
import { Construct } from 'constructs';

// The eight Identity Store events this pattern records. Listing the detail-types is required: AWS CloudTrail also
// sends Identity Store API calls to Amazon EventBridge with source "aws.identitystore", and a rule on the source
// alone would deliver those to the function as well.
const DETAIL_TYPES = [
  'User Created', 'User Updated', 'User Deleted',
  'Group Created', 'Group Updated', 'Group Deleted',
  'GroupMembership Created', 'GroupMembership Deleted',
];

export class IdentitystoreEventbridgeLambdaStack extends cdk.Stack {
  constructor(scope: Construct, id: string, props?: cdk.StackProps) {
    super(scope, id, props);

    const identityStoreId = String(this.node.tryGetContext('identityStoreId') ?? '');
    if (!/^(d-[0-9a-f]{10}|[0-9a-f]{8}(-[0-9a-f]{4}){3}-[0-9a-f]{12})$/.test(identityStoreId)) {
      throw new Error('Pass your identity store ID: cdk deploy -c identityStoreId=d-xxxxxxxxxx');
    }

    // Change ledger: the EventBridge event id is the key, so a duplicate delivery cannot add a second row.
    const table = new dynamodb.Table(this, 'ChangeLedger', {
      partitionKey: { name: 'eventId', type: dynamodb.AttributeType.STRING },
      billingMode: dynamodb.BillingMode.PAY_PER_REQUEST,
      removalPolicy: cdk.RemovalPolicy.DESTROY, // demo data is deleted with the stack
      deletionProtection: false,
    });
    table.addGlobalSecondaryIndex({
      indexName: 'resource-index',
      partitionKey: { name: 'resourceId', type: dynamodb.AttributeType.STRING },
      sortKey: { name: 'eventTime', type: dynamodb.AttributeType.STRING },
    });

    // Receives events that EventBridge cannot deliver to the function, and invocations that fail after all retries.
    const deadLetterQueue = new sqs.Queue(this, 'DeadLetterQueue', {
      encryption: sqs.QueueEncryption.SQS_MANAGED,
      enforceSSL: true,
      retentionPeriod: cdk.Duration.days(14),
      removalPolicy: cdk.RemovalPolicy.DESTROY,
    });

    const logGroup = new logs.LogGroup(this, 'FunctionLogGroup', {
      retention: logs.RetentionDays.ONE_WEEK,
      removalPolicy: cdk.RemovalPolicy.DESTROY,
    });

    const fn = new lambda.Function(this, 'LedgerFunction', {
      runtime: lambda.Runtime.NODEJS_24_X,
      handler: 'index.handler',
      code: lambda.Code.fromAsset(path.join(__dirname, '..', 'src')),
      timeout: cdk.Duration.seconds(30), // two Describe calls and one write, each client call allows up to 3 attempts of 3 seconds
      environment: { TABLE_NAME: table.tableName },
      logGroup,
      retryAttempts: 2,
      maxEventAge: cdk.Duration.hours(1),
      onFailure: new destinations.SqsDestination(deadLetterQueue),
    });

    // Describe actions need the identity store and the user or group. User and group ARNs contain no identity store
    // ID, so they can only be matched with a wildcard; the identity store ARN pins the calls to this store.
    fn.addToRolePolicy(new iam.PolicyStatement({
      actions: ['identitystore:DescribeUser', 'identitystore:DescribeGroup'],
      resources: [
        `arn:${this.partition}:identitystore::${this.account}:identitystore/${identityStoreId}`,
        `arn:${this.partition}:identitystore:::user/*`,
        `arn:${this.partition}:identitystore:::group/*`,
      ],
    }));
    fn.addToRolePolicy(new iam.PolicyStatement({ actions: ['dynamodb:PutItem'], resources: [table.tableArn] }));

    // Rule on the default event bus of the account and Region where Identity Center is enabled.
    new events.Rule(this, 'IdentityStoreChangeRule', {
      description: 'AWS IAM Identity Center Identity Store change events for one identity store',
      eventPattern: {
        source: ['aws.identitystore'],
        detailType: DETAIL_TYPES,
        detail: { 'identity-store': { id: [identityStoreId] } },
      },
      targets: [new targets.LambdaFunction(fn, {
        deadLetterQueue,
        retryAttempts: 3,
        maxEventAge: cdk.Duration.hours(1),
      })],
    });

    new cdk.CfnOutput(this, 'FunctionName', { value: fn.functionName });
    new cdk.CfnOutput(this, 'TableName', { value: table.tableName });
    new cdk.CfnOutput(this, 'DeadLetterQueueUrl', { value: deadLetterQueue.queueUrl });
    new cdk.CfnOutput(this, 'LogGroupName', { value: logGroup.logGroupName });
  }
}
