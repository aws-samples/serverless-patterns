#!/usr/bin/env node
import { App } from 'aws-cdk-lib';
import { DemoStack } from '../lib/demo-stack';

const app = new App();

// Deploy demo stack showing custom resource with wait condition pattern
new DemoStack(app, 'CdkCustomResourceWithWaitConditionStack', {
  stackName: 'Custom-Resource-With-Wait-Condition-Demo',
  description: 'Demo of a custom resource with a wait condition',
  env: {
      region: process.env.CDK_DEFAULT_REGION,
      account: process.env.CDK_DEFAULT_ACCOUNT,
  },
});