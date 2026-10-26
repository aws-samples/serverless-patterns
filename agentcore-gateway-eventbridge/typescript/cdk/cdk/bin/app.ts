#!/usr/bin/env node
import * as cdk from 'aws-cdk-lib';
import { AgentCoreGatewayEventBridgeStack } from '../lib/agentcore-gateway-eventbridge-stack';

const app = new cdk.App();

new AgentCoreGatewayEventBridgeStack(app, 'AgentCoreGatewayEventBridgeStack', {
  description:
    'ServerlessLand pattern: AgentCore Runtime agent emits events to EventBridge via AgentCore Gateway MCP tool',
  env: {
    account: process.env.CDK_DEFAULT_ACCOUNT,
    region: process.env.CDK_DEFAULT_REGION,
  },
});
