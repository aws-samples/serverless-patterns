#!/usr/bin/env node
import * as cdk from 'aws-cdk-lib';
import { ApigwLambdaBedrockCodeInterpreterStack } from '../lib/apigw-lambda-bedrock-code-interpreter-stack';
const app = new cdk.App();
new ApigwLambdaBedrockCodeInterpreterStack(app, 'ApigwLambdaBedrockCodeInterpreterStack', {
  env: { account: process.env.CDK_DEFAULT_ACCOUNT, region: process.env.CDK_DEFAULT_REGION },
});
