#!/usr/bin/env node
import * as cdk from 'aws-cdk-lib';
import { Construct } from "constructs";
import * as core from 'aws-cdk-lib';
import { aws_iam as iam } from 'aws-cdk-lib';
import { aws_kms as kms } from 'aws-cdk-lib';
import { aws_s3 as s3 } from 'aws-cdk-lib';
import { aws_logs as logs } from 'aws-cdk-lib';
import { Effect } from 'aws-cdk-lib/aws-iam';
import { aws_kinesis as kinesis } from 'aws-cdk-lib';
import * as flink from '@aws-cdk/aws-kinesisanalytics-flink-alpha'
import * as path from 'path';


export class CdkStack extends cdk.Stack {
  constructor(scope: Construct, id: string, props?: cdk.StackProps) {
    super(scope, id, props);

  const app = new core.App();
  const stack = new core.Stack(app, 'FlinkApp');

  const prefix = Math.random().toString(36).substring(2,8);
  const account_id = process.env.CDK_DEFAULT_ACCOUNT
  const region = process.env.CDK_DEFAULT_REGION

  const streamKey = new kms.Key(stack, "StreamKey");

  const outputBucket = new s3.Bucket(stack, 'Bucket', {
    bucketName: `ka-app-code-${prefix}`,
    blockPublicAccess: s3.BlockPublicAccess.BLOCK_ALL,
    encryption: s3.BucketEncryption.S3_MANAGED,
    removalPolicy: cdk.RemovalPolicy.DESTROY,
    enforceSSL: true,
    versioned: true,
  });

  const kinesisStream = new kinesis.Stream(stack, 'KinesisDataStream', {
    streamName: stack.node.tryGetContext('InputStream'),
    shardCount: 3,
    retentionPeriod: cdk.Duration.hours(48),
    encryption: kinesis.StreamEncryption.KMS,
    encryptionKey: streamKey,
  });

  const flinkRole = new iam.Role(stack, 'FlinkRole', {
    assumedBy: new iam.ServicePrincipal('kinesisanalytics.amazonaws.com'),
  });

  const loggroup = new logs.LogGroup(stack, 'FlinkAppLogGroup', {
    retention: logs.RetentionDays.ONE_DAY,
  });

  flinkRole.attachInlinePolicy(new iam.Policy(stack, 'FlinkRolePolicy', {
    statements: [
      new iam.PolicyStatement({
      actions: [
        "s3:Abort*",
        "s3:DeleteObject*",
        "s3:GetObject*",
        "s3:GetBucket*",
        "s3:List*",
        "s3:ListBucket",
        "s3:PutObject"
      ],
      effect: Effect.ALLOW,
      resources: [
        `arn:aws:s3:::${outputBucket.bucketName}`,
        `arn:aws:s3:::${outputBucket.bucketName}/*`
      ],
    }),
    new iam.PolicyStatement({
      actions: [
        "logs:DescribeLogGroups"
      ],
      effect: Effect.ALLOW,
      resources: [
        `arn:aws:logs:${region}:${account_id}:log-group:*`
      ],
    }),
    new iam.PolicyStatement({
      actions: [
        "logs:DescribeLogStreams"
      ],
      effect: Effect.ALLOW,
      resources: [
        `arn:aws:logs:${region}:${account_id}:log-group:${loggroup.logGroupName}:log-stream:*`
      ],
    }),
    new iam.PolicyStatement({
      actions: [
        "logs:PutLogEvents"
      ],
      effect: Effect.ALLOW,
      resources: [
        `arn:aws:logs:${region}:${account_id}:log-group:${loggroup.logGroupName}:log-stream:*`
      ],
    }),
    new iam.PolicyStatement({
      actions: [
        "kinesis:DescribeStream",
        "kinesis:GetShardIterator",
        "kinesis:GetRecords",
        "kinesis:ListShards"
      ],
      effect: Effect.ALLOW,
      resources: [
        `arn:aws:kinesis:${region}:${account_id}:stream/${kinesisStream.streamName}`
      ],
    })],
  }));

  streamKey.grantDecrypt(flinkRole);

  const flinkApp = new flink.Application(stack, 'App', {
    code: flink.ApplicationCode.fromAsset(path.join(__dirname, '../flinkapp/target/flink-kds-s3.jar')),
    runtime: flink.Runtime.FLINK_1_15,
    snapshotsEnabled: false,
    role: flinkRole,
    logGroup: loggroup,
    propertyGroups: {
      FlinkApplicationProperties: {
        'input.stream': kinesisStream.streamName,
        'stream.region': region!,
        's3.path': `s3://${outputBucket.bucketName}/flink/msf`
      },
    },
  });

  flinkApp.node.addDependency(kinesisStream);

    }
  }