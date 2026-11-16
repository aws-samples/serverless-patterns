#!/usr/bin/env node
import * as cdk from 'aws-cdk-lib';
import { ApigwDynamodbBulkPutStack } from '../lib/apigw-dynamodb-bulk-put-stack';

const app = new cdk.App();
new ApigwDynamodbBulkPutStack(app, 'ApigwDynamodbBulkPutStack', {
  env: { account: process.env.CDK_DEFAULT_ACCOUNT, region: process.env.CDK_DEFAULT_REGION },
});
