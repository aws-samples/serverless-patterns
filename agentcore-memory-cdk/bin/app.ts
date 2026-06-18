#!/usr/bin/env node
import * as cdk from 'aws-cdk-lib';
import { AgentcoreMemoryStack } from '../lib/agentcore-memory-stack';

const app = new cdk.App();
new AgentcoreMemoryStack(app, 'AgentcoreMemoryStack', {
  env: { region: 'us-east-1' },
});
