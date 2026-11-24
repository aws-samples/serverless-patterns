// Copyright Amazon.com, Inc. or its affiliates. All Rights Reserved.
// SPDX-License-Identifier: MIT-0

import * as cdk from 'aws-cdk-lib';
import * as kinesis from 'aws-cdk-lib/aws-kinesis';
import * as sqs from 'aws-cdk-lib/aws-sqs';
import * as events from 'aws-cdk-lib/aws-events';
import * as targets from 'aws-cdk-lib/aws-events-targets';
import * as pipes from 'aws-cdk-lib/aws-pipes';
import * as iam from 'aws-cdk-lib/aws-iam';
import * as logs from 'aws-cdk-lib/aws-logs';
import * as cr from 'aws-cdk-lib/custom-resources';
import { Construct } from 'constructs';

const SOURCE = 'dsql.cdc';
// One failure policy for both hops (pipe and rule targets): the service defaults are unlimited retries for a pipe
// and 185 attempts over 24 hours for a rule target, so a record that cannot be delivered would stay for a long time.
const MAX_RETRIES = 3;
const MAX_AGE = cdk.Duration.hours(1); // below the 24 hour retention of the stream, as pipes with a dead-letter queue need

export class DsqlCdcEventbridgePipesStack extends cdk.Stack {
  constructor(scope: Construct, id: string, props?: cdk.StackProps) {
    super(scope, id, props);

    const { region, account, partition } = this;
    const logGroup = (id: string) => new logs.LogGroup(this, id, {
      retention: logs.RetentionDays.ONE_WEEK,
      removalPolicy: cdk.RemovalPolicy.DESTROY,
    });
    const queue = (id: string, retention?: cdk.Duration) => new sqs.Queue(this, id, {
      encryption: sqs.QueueEncryption.SQS_MANAGED,
      retentionPeriod: retention,
      removalPolicy: cdk.RemovalPolicy.DESTROY,
    });

    const dsqlClusterId = new cdk.CfnParameter(this, 'DsqlClusterId', {
      type: 'String',
      description: 'Amazon Aurora DSQL cluster identifier',
      // The value goes into IAM trust and resource ARNs, so only a real identifier (26 lowercase letters and digits) is accepted
      allowedPattern: '^[a-z0-9]{26}$',
      constraintDescription: 'Must be a 26 character Amazon Aurora DSQL cluster identifier',
    });

    // Amazon Kinesis Data Streams: Aurora DSQL CDC guidance is on-demand mode and a 10 MiB maximum record size
    const cdcStream = new kinesis.Stream(this, 'CdcStream', {
      streamMode: kinesis.StreamMode.ON_DEMAND,
      encryption: kinesis.StreamEncryption.MANAGED,
      removalPolicy: cdk.RemovalPolicy.DESTROY, // the construct default is RETAIN, which leaves a billing stream behind
    });
    // The L2 construct has no property for the record size
    (cdcStream.node.defaultChild as kinesis.CfnStream).maxRecordSizeInKiB = 10240;

    // Amazon SQS: three consumers and two dead-letter queues (pipe, and rule targets)
    const auditQueue = queue('AuditQueue');
    const validationQueue = queue('ValidationQueue');
    const alertsQueue = queue('AlertsQueue');
    // The pipe dead-letter message points at a stream record that expires after 24 hours, so the SQS default (4 days) is enough;
    // the rule-target dead-letter queue holds the event itself, so it keeps messages for the SQS maximum
    const pipeDlq = queue('PipeDlq');
    const ruleDlq = queue('RuleTargetDlq', cdk.Duration.days(14));

    // Amazon EventBridge: custom event bus (Classic: a pipe cannot target the newer Custom Event Bus)
    const bus = new events.EventBus(this, 'CdcEventBus');

    // Amazon EventBridge Pipes: Amazon Kinesis Data Streams to the custom event bus
    const pipeLogs = logGroup('CdcPipeLogs');
    const pipeName = `${this.stackName}-cdc`; // fixed so the role trust can name the pipe ARN (no circular reference)
    const pipeRole = new iam.Role(this, 'CdcPipeRole', {
      assumedBy: new iam.ServicePrincipal('pipes.amazonaws.com', {
        conditions: {
          StringEquals: { 'aws:SourceAccount': account },
          ArnLike: { 'aws:SourceArn': `arn:${partition}:pipes:${region}:${account}:pipe/${pipeName}` },
        },
      }),
      inlinePolicies: {
        CdcPipe: new iam.PolicyDocument({
          statements: [
            new iam.PolicyStatement({
              actions: ['kinesis:DescribeStream', 'kinesis:DescribeStreamSummary', 'kinesis:GetRecords',
                'kinesis:GetShardIterator', 'kinesis:ListShards'],
              resources: [cdcStream.streamArn],
            }),
            new iam.PolicyStatement({ actions: ['events:PutEvents'], resources: [bus.eventBusArn] }),
            new iam.PolicyStatement({ actions: ['sqs:SendMessage'], resources: [pipeDlq.queueArn] }),
            // Lets the pipe write its error logs to its own log group
            new iam.PolicyStatement({
              actions: ['logs:CreateLogStream', 'logs:PutLogEvents'],
              resources: [pipeLogs.logGroupArn],
            }),
          ],
        }),
      },
    });

    new pipes.CfnPipe(this, 'CdcPipe', {
      name: pipeName,
      roleArn: pipeRole.roleArn,
      source: cdcStream.streamArn,
      sourceParameters: {
        kinesisStreamParameters: {
          startingPosition: 'TRIM_HORIZON',
          batchSize: 10, // an event bus accepts at most 10 events per request
          maximumRetryAttempts: MAX_RETRIES,
          maximumRecordAgeInSeconds: MAX_AGE.toSeconds(),
          onPartialBatchItemFailure: 'AUTOMATIC_BISECT', // halve a failing batch until the one bad record is left
          deadLetterConfig: { arn: pipeDlq.queueArn },
        },
        // Keep complete records only: chunked and fragment records (records whose JSON is larger than 9 MiB) are dropped
        filterCriteria: { filters: [{ pattern: JSON.stringify({ data: { type: ['full'] } }) }] },
      },
      target: bus.eventBusArn,
      targetParameters: {
        // The event type is the record's operation code: c, u or d
        eventBridgeEventBusParameters: { source: SOURCE, detailType: '$.data.op' },
        inputTemplate: `{
  "tableName": <$.data.source.table>,
  "operation": <$.data.op>,
  "newImage": <$.data.after>,
  "oldImage": <$.data.before>,
  "txId": <$.data.source.txId>,
  "recordId": <$.data.transaction.record_id>,
  "timestamp": <$.data.source.ts_ms>,
  "commitTimestampNs": "<$.data.source.ts_ns>"
}`,
      },
      logConfiguration: { level: 'ERROR', cloudwatchLogsLogDestination: { logGroupArn: pipeLogs.logGroupArn } },
    });

    // Amazon EventBridge rules: one per consumer. Updates (u) reach the audit queue only.
    const route = (id: string, consumer: sqs.Queue, description: string, detailType?: string) =>
      new events.Rule(this, id, {
        eventBus: bus,
        description,
        eventPattern: { source: [SOURCE], ...(detailType ? { detailType: [detailType] } : {}) },
        targets: [new targets.SqsQueue(consumer, {
          deadLetterQueue: ruleDlq,
          retryAttempts: MAX_RETRIES,
          maxEventAge: MAX_AGE,
        })],
      });
    route('AuditRule', auditQueue, 'Every change goes to the audit queue');
    route('InsertsRule', validationQueue, 'Inserts (c) go to the validation queue', 'c');
    route('DeletesRule', alertsQueue, 'Deletes (d) go to the alerts queue', 'd');

    // Amazon Aurora DSQL CDC stream. AWS CloudFormation has no resource type for it, so one SDK call creates it.
    const dsqlCdcRole = new iam.Role(this, 'DsqlCdcRole', {
      assumedBy: new iam.ServicePrincipal('dsql.amazonaws.com', {
        conditions: {
          StringEquals: { 'aws:SourceAccount': account },
          ArnLike: { 'aws:SourceArn': `arn:${partition}:dsql:${region}:${account}:cluster/${dsqlClusterId.valueAsString}/stream/*` },
        },
      }),
      description: 'Allows Amazon Aurora DSQL CDC to write to Amazon Kinesis Data Streams',
      inlinePolicies: {
        KinesisWrite: new iam.PolicyDocument({
          statements: [new iam.PolicyStatement({
            actions: ['kinesis:PutRecord', 'kinesis:PutRecords'],
            resources: [cdcStream.streamArn],
          })],
        }),
      },
    });
    const clusterArn = `arn:${partition}:dsql:${region}:${account}:cluster/${dsqlClusterId.valueAsString}`;
    const cdcStreamCr = new cr.AwsCustomResource(this, 'DsqlCdcStream', {
      installLatestAwsSdk: false,
      onCreate: {
        service: 'dsql',
        action: 'createStream',
        parameters: {
          clusterIdentifier: dsqlClusterId.valueAsString,
          targetDefinition: { kinesis: { streamArn: cdcStream.streamArn, roleArn: dsqlCdcRole.roleArn } },
          ordering: 'UNORDERED',
          format: 'JSON',
        },
        physicalResourceId: cr.PhysicalResourceId.fromResponse('streamIdentifier'),
      },
      onDelete: {
        service: 'dsql',
        action: 'deleteStream',
        parameters: { clusterIdentifier: dsqlClusterId.valueAsString, streamIdentifier: new cr.PhysicalResourceIdReference() },
        ignoreErrorCodesMatching: 'ResourceNotFoundException',
      },
      policy: cr.AwsCustomResourcePolicy.fromStatements([
        new iam.PolicyStatement({
          actions: ['dsql:CreateStream', 'dsql:DeleteStream'],
          resources: [clusterArn, `${clusterArn}/stream/*`],
        }),
        new iam.PolicyStatement({
          actions: ['iam:PassRole'],
          resources: [dsqlCdcRole.roleArn],
          conditions: { StringEquals: { 'iam:PassedToService': 'dsql.amazonaws.com' } },
        }),
      ]),
      logGroup: logGroup('CdcStreamCrLogs'),
    });
    cdcStreamCr.node.addDependency(dsqlCdcRole, cdcStream);

    const output = (id: string, value: string, description: string) => new cdk.CfnOutput(this, id, { value, description });
    output('PipeName', pipeName, 'Amazon EventBridge pipe name');
    output('KinesisStreamName', cdcStream.streamName, 'Amazon Kinesis Data Streams stream that receives the CDC records');
    output('CdcStreamId', cdcStreamCr.getResponseField('streamIdentifier'), 'Amazon Aurora DSQL CDC stream identifier');
    output('EventBusName', bus.eventBusName, 'Amazon EventBridge custom event bus; add rules and targets here');
    output('AuditQueueUrl', auditQueue.queueUrl, 'Receives every change');
    output('ValidationQueueUrl', validationQueue.queueUrl, 'Receives inserts');
    output('AlertsQueueUrl', alertsQueue.queueUrl, 'Receives deletes');
    output('PipeDlqUrl', pipeDlq.queueUrl, 'Dead-letter queue of the pipe');
    output('RuleTargetDlqUrl', ruleDlq.queueUrl, 'Dead-letter queue of the rule targets');
    output('PipeLogGroup', pipeLogs.logGroupName, 'Amazon CloudWatch Logs log group of the pipe');
  }
}
