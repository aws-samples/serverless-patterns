#!/usr/bin/env node
import * as cdk from 'aws-cdk-lib';
import { AgentcoreGatewaySfnStack } from '../lib/agentcore-gateway-sfn-stack';

const app = new cdk.App();
new AgentcoreGatewaySfnStack(app, 'AgentcoreGatewaySfnStack', {
  env: { account: process.env.CDK_DEFAULT_ACCOUNT, region: process.env.CDK_DEFAULT_REGION },
});
