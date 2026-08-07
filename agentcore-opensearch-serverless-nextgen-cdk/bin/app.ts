#!/usr/bin/env node
import * as cdk from 'aws-cdk-lib';
import { AgentcoreOpensearchStack } from '../lib/agentcore-opensearch-stack';

if (!process.env.CDK_DEFAULT_ACCOUNT) {
  throw new Error('CDK_DEFAULT_ACCOUNT environment variable is required. Run: export CDK_DEFAULT_ACCOUNT=$(aws sts get-caller-identity --query Account --output text)');
}

const app = new cdk.App();
new AgentcoreOpensearchStack(app, 'AgentcoreOpensearchServerlessNextgenStack', {
  env: {
    account: process.env.CDK_DEFAULT_ACCOUNT,
    region: process.env.CDK_DEFAULT_REGION || 'us-east-1',
  },
});
