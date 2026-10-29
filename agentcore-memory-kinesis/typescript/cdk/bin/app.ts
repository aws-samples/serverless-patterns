#!/usr/bin/env node
import * as cdk from 'aws-cdk-lib';
import { AgentcoreMemoryKinesisStack } from '../lib/agentcore-memory-kinesis-stack';

const app = new cdk.App();
new AgentcoreMemoryKinesisStack(app, 'AgentcoreMemoryKinesisStack', {
  env: { account: process.env.CDK_DEFAULT_ACCOUNT, region: process.env.CDK_DEFAULT_REGION },
});
