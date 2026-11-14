#!/usr/bin/env node
import { App } from 'aws-cdk-lib/core';
import { DemoStack } from '../lib/demo-stack';

const app = new App();
new DemoStack(app, 'LambdaDurableFunctionsManagedInstancesDemo', {
  stackName: 'lambda-durable-functions-managed-instances',
  env: { 
    account: process.env.CDK_DEFAULT_ACCOUNT, 
    region: process.env.CDK_DEFAULT_REGION ?? 'us-east-2',
  },
  description: 'POC stack demonstrating AWS Lambda durable functions running on AWS Lambda Managed Instances',
});
