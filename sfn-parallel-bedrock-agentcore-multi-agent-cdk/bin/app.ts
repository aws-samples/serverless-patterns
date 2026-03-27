#!/usr/bin/env node
import 'source-map-support/register';
import * as cdk from 'aws-cdk-lib';
import { AgentCoreStack } from '../lib/agentcore-stack';
import { OrchestratorStack } from '../lib/orchestrator-stack';

const app = new cdk.App();

const env = {
  account: process.env.CDK_DEFAULT_ACCOUNT,
  region: process.env.CDK_DEFAULT_REGION,
};

const agentCoreStack = new AgentCoreStack(app, 'MultiAgentCoreStack', { env });

new OrchestratorStack(app, 'MultiAgentOrchestratorStack', {
  env,
  researchRuntimeArn: agentCoreStack.researchRuntimeArn,
  researchEndpointUrl: agentCoreStack.researchEndpointUrl,
  synthesisRuntimeArn: agentCoreStack.synthesisRuntimeArn,
  synthesisEndpointUrl: agentCoreStack.synthesisEndpointUrl,
});
