#!/usr/bin/env node
import 'source-map-support/register';
import * as cdk from 'aws-cdk-lib';
import { DynamodbCrossAccountReplicationStack } from '../lib/dynamodb-cross-account-replication-stack';

const app = new cdk.App();

const account = process.env.CDK_DEFAULT_ACCOUNT;
const region = process.env.CDK_DEFAULT_REGION || 'us-east-1';

if (!account) {
  throw new Error('CDK_DEFAULT_ACCOUNT is required. Run: export CDK_DEFAULT_ACCOUNT=$(aws sts get-caller-identity --query Account --output text)');
}

new DynamodbCrossAccountReplicationStack(app, 'DynamodbCrossAccountReplicationStack', {
  env: { account, region },
});
