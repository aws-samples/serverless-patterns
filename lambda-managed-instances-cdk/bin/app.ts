#!/usr/bin/env node
import { App } from 'aws-cdk-lib/core';
import { DemoStack } from '../lib/demo-stack';

const app = new App();
new DemoStack(app, 'LambdaManagedInstancesDemo', {
  stackName: 'lambda-managed-instances',
  env: { 
    account: process.env.CDK_DEFAULT_ACCOUNT, 
    region: process.env.CDK_DEFAULT_REGION 
  },
  description: 'Simple Hello World Lambda function running on Lambda Managed Instances',
});