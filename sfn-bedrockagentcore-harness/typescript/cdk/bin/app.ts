#!/usr/bin/env node
import 'source-map-support/register';
import * as cdk from 'aws-cdk-lib';
import { SfnBedrockagentcoreHarnessStack } from '../lib/sfn-bedrockagentcore-harness-stack';

const app = new cdk.App();
new SfnBedrockagentcoreHarnessStack(app, 'SfnBedrockagentcoreHarnessStack', {
  env: {
    account: process.env.CDK_DEFAULT_ACCOUNT,
    region: process.env.CDK_DEFAULT_REGION || 'us-east-1',
  },
});
