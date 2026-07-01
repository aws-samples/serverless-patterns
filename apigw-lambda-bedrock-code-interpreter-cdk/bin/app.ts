#!/usr/bin/env node
import * as cdk from 'aws-cdk-lib';
import { ApigwLambdaBedrockCodeInterpreterStack } from '../lib/apigw-lambda-bedrock-code-interpreter-stack';
const app = new cdk.App();
new ApigwLambdaBedrockCodeInterpreterStack(app, 'ApigwLambdaBedrockCodeInterpreterStack', { env: { region: 'us-east-1' } });
