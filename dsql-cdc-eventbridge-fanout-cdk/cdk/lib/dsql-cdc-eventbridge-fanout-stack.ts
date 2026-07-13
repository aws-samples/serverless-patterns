// Copyright Amazon.com, Inc. or its affiliates. All Rights Reserved.
// SPDX-License-Identifier: MIT-0 (2026)

import * as cdk from 'aws-cdk-lib';
import * as kinesis from 'aws-cdk-lib/aws-kinesis';
import * as lambda from 'aws-cdk-lib/aws-lambda';
import * as iam from 'aws-cdk-lib/aws-iam';
import * as events from 'aws-cdk-lib/aws-events';
import * as targets from 'aws-cdk-lib/aws-events-targets';
import * as sqs from 'aws-cdk-lib/aws-sqs';
import * as sns from 'aws-cdk-lib/aws-sns';
import * as sfn from 'aws-cdk-lib/aws-stepfunctions';
import * as sfnTasks from 'aws-cdk-lib/aws-stepfunctions-tasks';
import * as logs from 'aws-cdk-lib/aws-logs';
import * as cr from 'aws-cdk-lib/custom-resources';
import * as kinesisEvtSrc from 'aws-cdk-lib/aws-lambda-event-sources';
import { Construct } from 'constructs';
import * as path from 'path';

export class DsqlCdcEventbridgeFanoutStack extends cdk.Stack {
  constructor(scope: Construct, id: string, props?: cdk.StackProps) {
    super(scope, id, props);

    const region = cdk.Stack.of(this).region;
    const account = cdk.Stack.of(this).account;

    // --- Context parameters ---
    const dsqlClusterId = new cdk.CfnParameter(this, 'DsqlClusterId', {
      type: 'String',
      description: 'Amazon Aurora DSQL cluster identifier',
    });

    // =========================================================
    // 1. Amazon Kinesis Data Stream (CDC target)
    // =========================================================
    const cdcStream = new kinesis.Stream(this, 'CdcStream', {
      streamName: `dsql-cdc-${cdk.Names.uniqueId(this).slice(-8).toLowerCase()}`,
      shardCount: 1,
      retentionPeriod: cdk.Duration.hours(24),
      encryption: kinesis.StreamEncryption.MANAGED,
    });

    // =========================================================
    // 2. IAM Role for DSQL to write to Kinesis
    // =========================================================
    const dsqlCdcRole = new iam.Role(this, 'DsqlCdcRole', {
      assumedBy: new iam.ServicePrincipal('dsql.amazonaws.com'),
      description: 'Allows Amazon Aurora DSQL CDC to write to Amazon Kinesis',
      inlinePolicies: {
        KinesisWrite: new iam.PolicyDocument({
          statements: [
            new iam.PolicyStatement({
              effect: iam.Effect.ALLOW,
              actions: [
                'kinesis:PutRecord',
                'kinesis:PutRecords',
                'kinesis:DescribeStream',
              ],
              resources: [cdcStream.streamArn],
            }),
          ],
        }),
      },
    });

    // =========================================================
    // 3. Custom Resource: Create/Delete DSQL CDC Stream
    //    (No CFN resource type for DSQL streams yet — use SDK)
    // =========================================================
    const streamManagerFn = new lambda.Function(this, 'CdcStreamManagerFn', {
      runtime: lambda.Runtime.PYTHON_3_12,
      handler: 'handler.on_event',
      code: lambda.Code.fromAsset(path.join(__dirname, '../../lambdas/cdc-stream-manager'), {
        bundling: {
          image: lambda.Runtime.PYTHON_3_12.bundlingImage,
          command: [
            'bash', '-c',
            'pip install -r requirements.txt -t /asset-output && cp handler.py /asset-output/',
          ],
        },
      }),
      timeout: cdk.Duration.minutes(5),
      memorySize: 256,
      description: 'Custom Resource: manages Amazon Aurora DSQL CDC stream lifecycle',
      environment: {
        CLUSTER_ID: dsqlClusterId.valueAsString,
        KINESIS_STREAM_ARN: cdcStream.streamArn,
        CDC_ROLE_ARN: dsqlCdcRole.roleArn,
      },
    });

    streamManagerFn.addToRolePolicy(new iam.PolicyStatement({
      effect: iam.Effect.ALLOW,
      actions: [
        'dsql:CreateStream',
        'dsql:DeleteStream',
        'dsql:GetStream',
        'dsql:ListStreams',
      ],
      resources: [
        `arn:aws:dsql:${region}:${account}:cluster/${dsqlClusterId.valueAsString}`,
        `arn:aws:dsql:${region}:${account}:cluster/${dsqlClusterId.valueAsString}/stream/*`,
      ],
    }));

    streamManagerFn.addToRolePolicy(new iam.PolicyStatement({
      effect: iam.Effect.ALLOW,
      actions: ['iam:PassRole'],
      resources: [dsqlCdcRole.roleArn],
      conditions: {
        StringEquals: { 'iam:PassedToService': 'dsql.amazonaws.com' },
      },
    }));

    const cdcStreamCr = new cr.Provider(this, 'CdcStreamProvider', {
      onEventHandler: streamManagerFn,
    });

    const cdcStreamResource = new cdk.CustomResource(this, 'DsqlCdcStream', {
      serviceToken: cdcStreamCr.serviceToken,
      properties: {
        ClusterId: dsqlClusterId.valueAsString,
        KinesisStreamArn: cdcStream.streamArn,
        RoleArn: dsqlCdcRole.roleArn,
      },
    });

    // =========================================================
    // 4. Amazon EventBridge Custom Event Bus
    // =========================================================
    const cdcEventBus = new events.EventBus(this, 'CdcEventBus', {
      eventBusName: 'dsql-cdc-events',
    });

    // =========================================================
    // 5. AWS Lambda: CDC Processor (Kinesis → EventBridge)
    // =========================================================
    const cdcProcessorFn = new lambda.Function(this, 'CdcProcessorFn', {
      runtime: lambda.Runtime.PYTHON_3_12,
      handler: 'handler.lambda_handler',
      code: lambda.Code.fromAsset(path.join(__dirname, '../../lambdas/cdc-processor')),
      timeout: cdk.Duration.seconds(60),
      memorySize: 256,
      description: 'Processes Amazon Aurora DSQL CDC events and fans out to Amazon EventBridge',
      environment: {
        EVENT_BUS_NAME: cdcEventBus.eventBusName,
      },
    });

    cdcProcessorFn.addToRolePolicy(new iam.PolicyStatement({
      effect: iam.Effect.ALLOW,
      actions: ['events:PutEvents'],
      resources: [cdcEventBus.eventBusArn],
    }));

    cdcProcessorFn.addEventSource(new kinesisEvtSrc.KinesisEventSource(cdcStream, {
      startingPosition: lambda.StartingPosition.TRIM_HORIZON,
      batchSize: 100,
      maxBatchingWindow: cdk.Duration.seconds(5),
      retryAttempts: 3,
      bisectBatchOnError: true,
    }));

    // =========================================================
    // 6. Fan-out Target A: Amazon SQS (Audit Queue)
    // =========================================================
    const auditDlq = new sqs.Queue(this, 'AuditDlq', {
      queueName: 'dsql-cdc-audit-dlq',
      retentionPeriod: cdk.Duration.days(14),
      encryption: sqs.QueueEncryption.SQS_MANAGED,
    });

    const auditQueue = new sqs.Queue(this, 'AuditQueue', {
      queueName: 'dsql-cdc-audit',
      visibilityTimeout: cdk.Duration.seconds(30),
      encryption: sqs.QueueEncryption.SQS_MANAGED,
      deadLetterQueue: { queue: auditDlq, maxReceiveCount: 3 },
    });

    new events.Rule(this, 'AuditRule', {
      eventBus: cdcEventBus,
      ruleName: 'route-all-changes-to-audit',
      description: 'Route ALL CDC events to Amazon SQS audit queue',
      eventPattern: {
        source: ['dsql.cdc'],
      },
      targets: [new targets.SqsQueue(auditQueue)],
    });

    // =========================================================
    // 7. Fan-out Target B: AWS Step Functions (Data Validation)
    // =========================================================
    const validatePass = new sfn.Pass(this, 'ValidationPassed', {
      result: sfn.Result.fromObject({ validated: true }),
    });

    const validateFail = new sfn.Pass(this, 'ValidationFailed', {
      result: sfn.Result.fromObject({ validated: false }),
    });

    const validationChoice = new sfn.Choice(this, 'HasRequiredFields')
      .when(
        sfn.Condition.isPresent('$.detail.newImage'),
        validatePass,
      )
      .otherwise(validateFail);

    const validationStateMachine = new sfn.StateMachine(this, 'ValidationWorkflow', {
      definitionBody: sfn.DefinitionBody.fromChainable(validationChoice),
      timeout: cdk.Duration.minutes(5),
      tracingEnabled: true,
      logs: {
        destination: new logs.LogGroup(this, 'ValidationLogGroup', {
          logGroupName: '/aws/stepfunctions/dsql-cdc-validation',
          retention: logs.RetentionDays.ONE_WEEK,
          removalPolicy: cdk.RemovalPolicy.DESTROY,
        }),
        level: sfn.LogLevel.ERROR,
      },
    });

    new events.Rule(this, 'ValidationRule', {
      eventBus: cdcEventBus,
      ruleName: 'route-inserts-to-validation',
      description: 'Route INSERT events to AWS Step Functions for validation',
      eventPattern: {
        source: ['dsql.cdc'],
        detailType: ['INSERT'],
      },
      targets: [new targets.SfnStateMachine(validationStateMachine)],
    });

    // =========================================================
    // 8. Fan-out Target C: Amazon SNS (Real-time Alerts)
    // =========================================================
    const alertTopic = new sns.Topic(this, 'AlertTopic', {
      topicName: 'dsql-cdc-delete-alerts',
      displayName: 'Amazon Aurora DSQL CDC - DELETE Alerts',
    });

    new events.Rule(this, 'DeleteAlertRule', {
      eventBus: cdcEventBus,
      ruleName: 'route-deletes-to-alert',
      description: 'Route DELETE events to Amazon SNS for alerting',
      eventPattern: {
        source: ['dsql.cdc'],
        detailType: ['DELETE'],
      },
      targets: [new targets.SnsTopic(alertTopic)],
    });

    // =========================================================
    // Outputs
    // =========================================================
    new cdk.CfnOutput(this, 'KinesisStreamArn', {
      value: cdcStream.streamArn,
      description: 'Amazon Kinesis Data Stream ARN (CDC target)',
    });

    new cdk.CfnOutput(this, 'EventBusArn', {
      value: cdcEventBus.eventBusArn,
      description: 'Amazon EventBridge custom event bus ARN',
    });

    new cdk.CfnOutput(this, 'AuditQueueUrl', {
      value: auditQueue.queueUrl,
      description: 'Amazon SQS audit queue URL',
    });

    new cdk.CfnOutput(this, 'ValidationStateMachineArn', {
      value: validationStateMachine.stateMachineArn,
      description: 'AWS Step Functions validation workflow ARN',
    });

    new cdk.CfnOutput(this, 'AlertTopicArn', {
      value: alertTopic.topicArn,
      description: 'Amazon SNS alert topic ARN',
    });

    new cdk.CfnOutput(this, 'CdcStreamId', {
      value: cdcStreamResource.getAttString('StreamId'),
      description: 'Amazon Aurora DSQL CDC stream identifier',
    });
  }
}
