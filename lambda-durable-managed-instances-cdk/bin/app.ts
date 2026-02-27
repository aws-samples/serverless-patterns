#!/usr/bin/env node
import { App } from 'aws-cdk-lib/core';
import { DemoStack } from '../lib/demo-stack';

const app = new App();
new DemoStack(app, 'LambdaDurableFunctionsManagedInstancesDemo', {
  stackName: 'lambda-durable-functions-managed-instances',
  env: { 
    account: process.env.CDK_DEFAULT_ACCOUNT, 
    region: 'us-east-2' 
  },
  description: 'POC stack demonstrating Lambda durable functions running on Lambda Managed Instances',
});
