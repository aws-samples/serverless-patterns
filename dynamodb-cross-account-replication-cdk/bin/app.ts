#!/usr/bin/env node
import 'source-map-support/register';
import * as cdk from 'aws-cdk-lib';
import { DynamodbCrossAccountReplicationStack } from '../lib/dynamodb-cross-account-replication-stack';

const app = new cdk.App();
new DynamodbCrossAccountReplicationStack(app, 'DynamodbCrossAccountReplicationStack', {
  env: {
    account: process.env.CDK_DEFAULT_ACCOUNT || '123456789012',
    region: process.env.CDK_DEFAULT_REGION || 'us-east-1',
  },
});
