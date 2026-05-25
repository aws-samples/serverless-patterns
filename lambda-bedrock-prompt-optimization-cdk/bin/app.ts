#!/usr/bin/env node
import 'source-map-support/register';
import * as cdk from 'aws-cdk-lib';
import { LambdaBedrockPromptOptimizationStack } from '../lib/lambda-bedrock-prompt-optimization-stack';

const app = new cdk.App();
new LambdaBedrockPromptOptimizationStack(app, 'LambdaBedrockPromptOptimizationStack', {
  env: {
    account: process.env.CDK_DEFAULT_ACCOUNT,
    region: process.env.CDK_DEFAULT_REGION,
  },
});
