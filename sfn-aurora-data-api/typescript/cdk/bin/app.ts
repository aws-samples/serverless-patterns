#!/usr/bin/env node
import * as cdk from 'aws-cdk-lib';
import { SfnAuroraDataApiStack } from '../lib/sfn-aurora-data-api-stack';

const app = new cdk.App();
new SfnAuroraDataApiStack(app, 'SfnAuroraDataApiStack', {
  env: { account: process.env.CDK_DEFAULT_ACCOUNT, region: process.env.CDK_DEFAULT_REGION },
});
