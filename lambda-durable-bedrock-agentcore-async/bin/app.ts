#!/usr/bin/env node
import 'source-map-support/register';
import * as cdk from 'aws-cdk-lib';
import { AgentCoreStrandsStack } from '../lib/agentcore-strands-stack';
import { DurableAgentStack } from '../lib/durable-agent-stack';

const app = new cdk.App();

const env = {
  account: process.env.CDK_DEFAULT_ACCOUNT,
  region: process.env.CDK_DEFAULT_REGION,
};

const agentCoreStack = new AgentCoreStrandsStack(app, 'AgentCoreStrandsStack', { env });

new DurableAgentStack(app, 'DurableAgentStack', {
  env,
  agentRuntimeArn: agentCoreStack.runtimeArn,
  agentRuntimeEndpointUrl: agentCoreStack.runtimeEndpointUrl,
});
