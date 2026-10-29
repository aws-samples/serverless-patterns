import * as path from 'path';
import * as cdk from 'aws-cdk-lib';
import { Construct } from 'constructs';
import * as agentcore from 'aws-cdk-lib/aws-bedrockagentcore';
import * as dynamodb from 'aws-cdk-lib/aws-dynamodb';
import * as iam from 'aws-cdk-lib/aws-iam';
import * as kinesis from 'aws-cdk-lib/aws-kinesis';
import * as kms from 'aws-cdk-lib/aws-kms';
import * as lambda from 'aws-cdk-lib/aws-lambda';
import * as eventsources from 'aws-cdk-lib/aws-lambda-event-sources';
import * as logs from 'aws-cdk-lib/aws-logs';

export class AgentcoreMemoryKinesisStack extends cdk.Stack {
  constructor(scope: Construct, id: string, props?: cdk.StackProps) {
    super(scope, id, props);

    // Customer managed key: FULL_CONTENT events carry the extracted memory text, so the stream is encrypted at rest.
    const streamKey = new kms.Key(this, 'StreamKey', {
      enableKeyRotation: true,
      pendingWindow: cdk.Duration.days(7), // shortest window; cdk destroy schedules the key for deletion
      removalPolicy: cdk.RemovalPolicy.DESTROY,
    });

    // One provisioned shard is enough for a few memory record events (about 0.015 USD per hour at the us-east-1 list price).
    const stream = new kinesis.Stream(this, 'MemoryRecordStream', {
      streamMode: kinesis.StreamMode.PROVISIONED,
      shardCount: 1,
      encryption: kinesis.StreamEncryption.KMS,
      encryptionKey: streamKey,
      removalPolicy: cdk.RemovalPolicy.DESTROY, // Kinesis streams default to RETAIN
    });

    // Built-in strategies need no Amazon Bedrock model permissions. The L2 creates the memory execution role
    // (trusted by bedrock-agentcore.amazonaws.com with aws:SourceAccount and aws:SourceArn), grants it
    // kinesis:ListShards, PutRecord, PutRecords and DescribeStream on the stream plus kms:Encrypt, ReEncrypt* and
    // GenerateDataKey* on the key, and makes the memory depend on that policy.
    const memory = new agentcore.Memory(this, 'Memory', {
      expirationDuration: cdk.Duration.days(7), // short-term event retention
      memoryStrategies: [
        agentcore.MemoryStrategy.usingBuiltInSemantic(),
        agentcore.MemoryStrategy.usingBuiltInUserPreference(),
      ],
      streamDeliveryResources: [
        agentcore.StreamDeliveryResource.kinesis(stream, {
          contentConfigurations: [{
            type: agentcore.StreamDeliveryContentType.MEMORY_RECORDS,
            level: agentcore.StreamDeliveryContentLevel.FULL_CONTENT,
          }],
        }),
      ],
    });

    // Keyed by memoryRecordId because MemoryRecordDeleted events carry no actor or namespace.
    const table = new dynamodb.Table(this, 'ProfileTable', {
      partitionKey: { name: 'memoryRecordId', type: dynamodb.AttributeType.STRING },
      billingMode: dynamodb.BillingMode.PAY_PER_REQUEST,
      removalPolicy: cdk.RemovalPolicy.DESTROY,
    });
    table.addGlobalSecondaryIndex({
      indexName: 'actor-index',
      partitionKey: { name: 'actorId', type: dynamodb.AttributeType.STRING },
    });

    const logGroup = new logs.LogGroup(this, 'ProjectorLogGroup', {
      retention: logs.RetentionDays.ONE_WEEK,
      removalPolicy: cdk.RemovalPolicy.DESTROY,
    });

    const projector = new lambda.Function(this, 'ProfileProjector', {
      runtime: lambda.Runtime.NODEJS_24_X,
      handler: 'index.handler',
      code: lambda.Code.fromAsset(path.join(__dirname, '..', 'lambda')),
      timeout: cdk.Duration.seconds(30),
      logGroup,
      loggingFormat: lambda.LoggingFormat.JSON,
      environment: { TABLE_NAME: table.tableName },
    });
    projector.addToRolePolicy(new iam.PolicyStatement({
      actions: ['dynamodb:PutItem', 'dynamodb:DeleteItem'],
      resources: [table.tableArn],
    }));

    // The payload is nested under memoryStreamEvent, so a top-level eventType filter would drop everything.
    // The StreamingEnabled validation event has no memoryRecordId and is filtered out here.
    projector.addEventSource(new eventsources.KinesisEventSource(stream, {
      startingPosition: lambda.StartingPosition.TRIM_HORIZON,
      batchSize: 10,
      retryAttempts: 3,
      reportBatchItemFailures: true,
      filters: [lambda.FilterCriteria.filter({
        data: {
          memoryStreamEvent: {
            eventType: lambda.FilterRule.or('MemoryRecordCreated', 'MemoryRecordUpdated', 'MemoryRecordDeleted'),
          },
        },
      })],
    }));

    new cdk.CfnOutput(this, 'MemoryId', { value: memory.memoryId });
    new cdk.CfnOutput(this, 'MemoryArn', { value: memory.memoryArn });
    new cdk.CfnOutput(this, 'StreamName', { value: stream.streamName });
    new cdk.CfnOutput(this, 'TableName', { value: table.tableName });
    new cdk.CfnOutput(this, 'FunctionName', { value: projector.functionName });
    new cdk.CfnOutput(this, 'ProjectorLogGroupName', { value: logGroup.logGroupName });
  }
}
