// Copyright Amazon.com, Inc. or its affiliates. All Rights Reserved.
// SPDX-License-Identifier: MIT-0

import * as cdk from 'aws-cdk-lib';
import * as kinesis from 'aws-cdk-lib/aws-kinesis';
import * as lambda from 'aws-cdk-lib/aws-lambda';
import * as iam from 'aws-cdk-lib/aws-iam';
import * as events from 'aws-cdk-lib/aws-events';
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
    const partition = cdk.Stack.of(this).partition;

    // Explicit log groups with one-week retention that cdk destroy removes with the stack
    const logGroup = (id: string) => new logs.LogGroup(this, id, {
      retention: logs.RetentionDays.ONE_WEEK,
      removalPolicy: cdk.RemovalPolicy.DESTROY,
    });

    // --- Context parameters ---
    const dsqlClusterId = new cdk.CfnParameter(this, 'DsqlClusterId', {
      type: 'String',
      description: 'Amazon Aurora DSQL cluster identifier',
      // The value goes into IAM trust and resource ARNs, so only a real identifier (26 lowercase letters and digits) is accepted
      allowedPattern: '^[a-z0-9]{26}$',
      constraintDescription: 'Must be a 26 character Amazon Aurora DSQL cluster identifier',
    });

    // =========================================================
    // 1. Amazon Kinesis Data Streams (CDC target)
    // =========================================================
    // Aurora DSQL CDC guidance: on-demand mode and a 10 MiB maximum record size.
    // A CDC record larger than the stream's maximum record size leaves the CDC stream impaired.
    const cdcStream = new kinesis.Stream(this, 'CdcStream', {
      streamName: `dsql-cdc-${cdk.Names.uniqueId(this).slice(-8).toLowerCase()}`,
      streamMode: kinesis.StreamMode.ON_DEMAND,
      retentionPeriod: cdk.Duration.hours(24),
      encryption: kinesis.StreamEncryption.MANAGED,
      removalPolicy: cdk.RemovalPolicy.DESTROY, // the construct default is RETAIN, which leaves a billing stream behind
    });
    (cdcStream.node.defaultChild as kinesis.CfnStream).maxRecordSizeInKiB = 10240;

    // =========================================================
    // 2. IAM Role for Amazon Aurora DSQL to write to Amazon Kinesis Data Streams
    // =========================================================
    const dsqlCdcRole = new iam.Role(this, 'DsqlCdcRole', {
      // Confused deputy protection, as documented for Aurora DSQL CDC service roles
      assumedBy: new iam.ServicePrincipal('dsql.amazonaws.com', {
        conditions: {
          StringEquals: { 'aws:SourceAccount': account },
          ArnLike: {
            'aws:SourceArn': `arn:${partition}:dsql:${region}:${account}:cluster/${dsqlClusterId.valueAsString}/stream/*`,
          },
        },
      }),
      description: 'Allows Amazon Aurora DSQL CDC to write to Amazon Kinesis Data Streams',
      inlinePolicies: {
        KinesisWrite: new iam.PolicyDocument({
          statements: [
            new iam.PolicyStatement({
              effect: iam.Effect.ALLOW,
              actions: [
                'kinesis:PutRecord',
                'kinesis:PutRecords',
              ],
              resources: [cdcStream.streamArn],
            }),
          ],
        }),
      },
    });

    // =========================================================
    // 3. Custom Resource: Create/Delete DSQL CDC Stream
    //    (No CFN resource type for DSQL streams yet - use SDK)
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
      logGroup: logGroup('CdcStreamManagerLogs'),
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
        `arn:${partition}:dsql:${region}:${account}:cluster/${dsqlClusterId.valueAsString}`,
        `arn:${partition}:dsql:${region}:${account}:cluster/${dsqlClusterId.valueAsString}/stream/*`,
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
      logGroup: logGroup('CdcStreamProviderLogs'),
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
    // 5. AWS Lambda: CDC Processor (Amazon Kinesis Data Streams → Amazon EventBridge)
    // =========================================================
    const processorLogs = logGroup('CdcProcessorLogs');
    const cdcProcessorFn = new lambda.Function(this, 'CdcProcessorFn', {
      runtime: lambda.Runtime.PYTHON_3_12,
      handler: 'handler.lambda_handler',
      code: lambda.Code.fromAsset(path.join(__dirname, '../../lambdas/cdc-processor')),
      timeout: cdk.Duration.seconds(60),
      memorySize: 256,
      description: 'Processes Amazon Aurora DSQL CDC events and publishes to Amazon EventBridge',
      logGroup: processorLogs,
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
    // Outputs
    // =========================================================
    new cdk.CfnOutput(this, 'KinesisStreamArn', {
      value: cdcStream.streamArn,
      description: 'ARN of the stream in Amazon Kinesis Data Streams (CDC target)',
    });

    new cdk.CfnOutput(this, 'EventBusArn', {
      value: cdcEventBus.eventBusArn,
      description: 'Amazon EventBridge custom event bus ARN - add rules and targets to consume CDC events',
    });

    new cdk.CfnOutput(this, 'CdcProcessorFunctionName', {
      value: cdcProcessorFn.functionName,
      description: 'AWS Lambda CDC processor function name',
    });

    new cdk.CfnOutput(this, 'CdcProcessorLogGroup', {
      value: processorLogs.logGroupName,
      description: 'Amazon CloudWatch Logs log group of the CDC processor',
    });

    new cdk.CfnOutput(this, 'CdcStreamId', {
      value: cdcStreamResource.getAttString('StreamId'),
      description: 'Amazon Aurora DSQL CDC stream identifier',
    });
  }
}
