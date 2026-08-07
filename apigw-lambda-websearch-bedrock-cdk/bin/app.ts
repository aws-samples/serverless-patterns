#!/usr/bin/env node
import * as cdk from 'aws-cdk-lib';
import { ApigwLambdaWebsearchBedrockStack } from '../lib/apigw-lambda-websearch-bedrock-stack';

const app = new cdk.App();
new ApigwLambdaWebsearchBedrockStack(app, 'ApigwLambdaWebsearchBedrockStack', {
  env: { region: 'us-east-1' },
});
