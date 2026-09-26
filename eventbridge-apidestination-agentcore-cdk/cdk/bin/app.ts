#!/usr/bin/env node
import * as cdk from 'aws-cdk-lib';
import { EventBridgeAgentCoreStack } from '../lib/eventbridge-agentcore-stack';

const app = new cdk.App();

new EventBridgeAgentCoreStack(app, 'EventBridgeAgentCoreStack', {
  description:
    'ServerlessLand pattern: EventBridge API Destination -> AgentCore Runtime (Lambda-less event-driven agent invocation)',
  env: {
    account: process.env.CDK_DEFAULT_ACCOUNT,
    region: process.env.CDK_DEFAULT_REGION,
  },
});
