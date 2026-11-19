#!/usr/bin/env node
import * as cdk from 'aws-cdk-lib';
import { IdentitystoreEventbridgeLambdaStack } from '../lib/identitystore-eventbridge-lambda-stack';

const app = new cdk.App();
new IdentitystoreEventbridgeLambdaStack(app, 'IdentitystoreEventbridgeLambdaStack', {
  // Deploy in the account and Region of your AWS IAM Identity Center instance.
  env: { account: process.env.CDK_DEFAULT_ACCOUNT, region: process.env.CDK_DEFAULT_REGION },
});
