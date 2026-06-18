#!/usr/bin/env node
import * as cdk from 'aws-cdk-lib';
import { AgentcoreWebSearchStack } from '../lib/agentcore-web-search-stack';

const app = new cdk.App();
new AgentcoreWebSearchStack(app, 'AgentcoreWebSearchStack', {
  env: { region: 'us-east-1' },
});
