#!/usr/bin/env node
import 'source-map-support/register';
import * as cdk from 'aws-cdk-lib';
import { LambdaInvoicingBedrockStack } from '../lib/lambda-invoicing-bedrock-stack';

const app = new cdk.App();
new LambdaInvoicingBedrockStack(app, 'LambdaInvoicingBedrockStack', {
  env: {
    account: process.env.CDK_DEFAULT_ACCOUNT,
    region: process.env.CDK_DEFAULT_REGION,
  },
});
