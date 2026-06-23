#!/usr/bin/env node
import * as cdk from 'aws-cdk-lib';
import { LambdaDsqlMultiRegionStack } from '../lib/lambda-dsql-multi-region-stack';

const app = new cdk.App();
new LambdaDsqlMultiRegionStack(app, 'LambdaDsqlMultiRegionStack', {
  env: { region: 'us-east-1' },
});
