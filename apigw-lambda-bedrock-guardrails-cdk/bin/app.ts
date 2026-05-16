#!/usr/bin/env node
import 'source-map-support/register';
import * as cdk from 'aws-cdk-lib';
import { ApigwLambdaBedrockGuardrailsStack } from '../lib/apigw-lambda-bedrock-guardrails-stack';

const app = new cdk.App();
new ApigwLambdaBedrockGuardrailsStack(app, 'ApigwLambdaBedrockGuardrailsStack');
