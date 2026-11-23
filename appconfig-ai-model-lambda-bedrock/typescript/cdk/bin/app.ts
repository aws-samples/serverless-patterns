#!/usr/bin/env node
import * as cdk from 'aws-cdk-lib';
import { AppconfigAiModelLambdaBedrockStack } from '../lib/appconfig-ai-model-lambda-bedrock-stack';

const app = new cdk.App();
new AppconfigAiModelLambdaBedrockStack(app, 'AppconfigAiModelLambdaBedrockStack', {
  env: { account: process.env.CDK_DEFAULT_ACCOUNT, region: process.env.CDK_DEFAULT_REGION },
});
