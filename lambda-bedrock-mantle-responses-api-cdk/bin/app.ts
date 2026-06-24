#!/usr/bin/env node
import 'source-map-support/register';
import * as cdk from 'aws-cdk-lib';
import { LambdaBedrockMantleStack } from '../lib/stack';

if (!process.env.CDK_DEFAULT_ACCOUNT) {
  throw new Error('CDK_DEFAULT_ACCOUNT environment variable is required. Run: aws sts get-caller-identity');
}

const app = new cdk.App();
new LambdaBedrockMantleStack(app, 'LambdaBedrockMantleResponsesApiStack', {
  env: {
    account: process.env.CDK_DEFAULT_ACCOUNT,
    region: process.env.CDK_DEFAULT_REGION || 'us-east-1',
  },
});
