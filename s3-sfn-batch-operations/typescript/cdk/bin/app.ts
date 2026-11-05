#!/usr/bin/env node
import * as cdk from 'aws-cdk-lib';
import { S3SfnBatchOperationsStack } from '../lib/s3-sfn-batch-operations-stack';

const app = new cdk.App();
new S3SfnBatchOperationsStack(app, 'S3SfnBatchOperationsStack', {
  env: { account: process.env.CDK_DEFAULT_ACCOUNT, region: process.env.CDK_DEFAULT_REGION },
});
