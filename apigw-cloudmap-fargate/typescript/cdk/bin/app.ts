#!/usr/bin/env node
import * as cdk from 'aws-cdk-lib';
import { ApigwCloudMapFargateStack } from '../lib/apigw-cloudmap-fargate-stack';

const app = new cdk.App();
new ApigwCloudMapFargateStack(app, 'ApigwCloudMapFargateStack', {
  env: { account: process.env.CDK_DEFAULT_ACCOUNT, region: process.env.CDK_DEFAULT_REGION },
});
