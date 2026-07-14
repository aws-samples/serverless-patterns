// Copyright Amazon.com, Inc. or its affiliates. All Rights Reserved.
// SPDX-License-Identifier: MIT-0 (2026)

import * as cdk from 'aws-cdk-lib';
import * as sqs from 'aws-cdk-lib/aws-sqs';
import * as dynamodb from 'aws-cdk-lib/aws-dynamodb';
import * as lambda from 'aws-cdk-lib/aws-lambda';
import * as iam from 'aws-cdk-lib/aws-iam';
import * as pipes from 'aws-cdk-lib/aws-pipes';
import * as logs from 'aws-cdk-lib/aws-logs';
import { Construct } from 'constructs';
import * as path from 'path';

export class EventbridgePipesBedrockEnrichmentStack extends cdk.Stack {
  constructor(scope: Construct, id: string, props?: cdk.StackProps) {
    super(scope, id, props);

    const region = cdk.Stack.of(this).region;
    const account = cdk.Stack.of(this).account;

    // =========================================================
    // 1. Amazon SQS Queue (Pipe source)
    // =========================================================
    const sourceQueue = new sqs.Queue(this, 'SourceQueue', {
      queueName: 'pipes-bedrock-source',
      visibilityTimeout: cdk.Duration.seconds(120),
      encryption: sqs.QueueEncryption.SQS_MANAGED,
    });

    // =========================================================
    // 2. Amazon DynamoDB Table (Pipe target — enriched messages)
    // =========================================================
    const enrichedTable = new dynamodb.Table(this, 'EnrichedTable', {
      partitionKey: { name: 'messageId', type: dynamodb.AttributeType.STRING },
      billingMode: dynamodb.BillingMode.PAY_PER_REQUEST,
      removalPolicy: cdk.RemovalPolicy.DESTROY,
      timeToLiveAttribute: 'ttl',
    });

    // =========================================================
    // 3. AWS Lambda: Bedrock Enrichment Function
    //    Calls Amazon Bedrock to classify/summarize messages in-flight
    // =========================================================
    const enrichFn = new lambda.Function(this, 'EnrichFunction', {
      runtime: lambda.Runtime.PYTHON_3_12,
      handler: 'handler.lambda_handler',
      code: lambda.Code.fromAsset(path.join(__dirname, '../../lambdas/enrich')),
      timeout: cdk.Duration.seconds(60),
      memorySize: 256,
      description: 'Enriches messages via Amazon Bedrock (classify sentiment + extract entities)',
      environment: {
        MODEL_ID: 'us.anthropic.claude-sonnet-4-6',
      },
    });

    // Bedrock InvokeModel permission (scoped to inference profiles + foundation models)
    enrichFn.addToRolePolicy(new iam.PolicyStatement({
      effect: iam.Effect.ALLOW,
      actions: ['bedrock:InvokeModel'],
      resources: [
        `arn:aws:bedrock:*::foundation-model/*`,
        `arn:aws:bedrock:*:${account}:inference-profile/*`,
      ],
    }));

    // =========================================================
    // 4. IAM Role for Amazon EventBridge Pipes
    // =========================================================
    const pipeRole = new iam.Role(this, 'PipeRole', {
      assumedBy: new iam.ServicePrincipal('pipes.amazonaws.com'),
      description: 'Allows Amazon EventBridge Pipes to read SQS, invoke Lambda, write DynamoDB',
      inlinePolicies: {
        SourcePolicy: new iam.PolicyDocument({
          statements: [new iam.PolicyStatement({
            actions: [
              'sqs:ReceiveMessage',
              'sqs:DeleteMessage',
              'sqs:GetQueueAttributes',
            ],
            resources: [sourceQueue.queueArn],
          })],
        }),
        EnrichmentPolicy: new iam.PolicyDocument({
          statements: [new iam.PolicyStatement({
            actions: ['lambda:InvokeFunction'],
            resources: [enrichFn.functionArn],
          })],
        }),
        TargetPolicy: new iam.PolicyDocument({
          statements: [new iam.PolicyStatement({
            actions: ['dynamodb:PutItem'],
            resources: [enrichedTable.tableArn],
          })],
        }),
      },
    });

    // =========================================================
    // 5. Amazon EventBridge Pipe
    //    Source: SQS → Enrichment: Lambda (Bedrock) → Target: CloudWatch Logs
    //    (Enriched data also stored in DynamoDB by enrichment Lambda)
    // =========================================================

    // Target: CloudWatch Logs (lightweight, always-available target for enriched output)
    const targetLogGroup = new logs.LogGroup(this, 'EnrichedLogGroup', {
      logGroupName: '/pipes/bedrock-enriched-output',
      retention: logs.RetentionDays.ONE_WEEK,
      removalPolicy: cdk.RemovalPolicy.DESTROY,
    });

    // Update enrichment Lambda to also write to DynamoDB directly
    enrichedTable.grantWriteData(enrichFn);
    enrichFn.addEnvironment('ENRICHED_TABLE', enrichedTable.tableName);

    // Pipe role needs CloudWatch Logs PutLogEvents for the target
    pipeRole.addToPolicy(new iam.PolicyStatement({
      actions: ['logs:CreateLogStream', 'logs:PutLogEvents'],
      resources: [targetLogGroup.logGroupArn, `${targetLogGroup.logGroupArn}:*`],
    }));

    const pipe = new pipes.CfnPipe(this, 'BedrockEnrichmentPipe', {
      name: 'sqs-bedrock-enrich-dynamodb',
      description: 'Enriches Amazon SQS messages with Amazon Bedrock AI classification before writing to Amazon DynamoDB',
      roleArn: pipeRole.roleArn,
      source: sourceQueue.queueArn,
      sourceParameters: {
        sqsQueueParameters: {
          batchSize: 1,
          maximumBatchingWindowInSeconds: 5,
        },
      },
      enrichment: enrichFn.functionArn,
      target: targetLogGroup.logGroupArn,
      targetParameters: {
        cloudWatchLogsParameters: {
          logStreamName: 'enriched-events',
        },
      },
      logConfiguration: {
        cloudwatchLogsLogDestination: {
          logGroupArn: new logs.LogGroup(this, 'PipeLogGroup', {
            logGroupName: '/aws/pipes/bedrock-enrichment',
            retention: logs.RetentionDays.ONE_WEEK,
            removalPolicy: cdk.RemovalPolicy.DESTROY,
          }).logGroupArn,
        },
        level: 'ERROR',
      },
    });

    // =========================================================
    // Outputs
    // =========================================================
    new cdk.CfnOutput(this, 'SourceQueueUrl', {
      value: sourceQueue.queueUrl,
      description: 'Amazon SQS source queue URL — send messages here',
    });

    new cdk.CfnOutput(this, 'EnrichedTableName', {
      value: enrichedTable.tableName,
      description: 'Amazon DynamoDB table with enriched messages',
    });

    new cdk.CfnOutput(this, 'PipeName', {
      value: 'sqs-bedrock-enrich-dynamodb',
      description: 'Amazon EventBridge Pipe name',
    });

    new cdk.CfnOutput(this, 'EnrichFunctionName', {
      value: enrichFn.functionName,
      description: 'AWS Lambda enrichment function name',
    });
  }
}
