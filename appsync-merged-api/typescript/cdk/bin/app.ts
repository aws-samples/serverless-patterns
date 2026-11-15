#!/usr/bin/env node
import * as cdk from 'aws-cdk-lib';
import { AppsyncMergedApiStack } from '../lib/appsync-merged-api-stack';

const app = new cdk.App();
new AppsyncMergedApiStack(app, 'AppsyncMergedApiStack', {
  env: { account: process.env.CDK_DEFAULT_ACCOUNT, region: process.env.CDK_DEFAULT_REGION },
});
