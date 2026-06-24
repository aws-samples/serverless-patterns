#!/usr/bin/env node
import * as cdk from 'aws-cdk-lib';
import { AgentcoreBrowserStack } from '../lib/agentcore-browser-stack';

const app = new cdk.App();
new AgentcoreBrowserStack(app, 'AgentcoreBrowserStack', {
  env: { region: 'us-east-1' },
});
