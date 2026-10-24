#!/usr/bin/env node
import * as cdk from 'aws-cdk-lib';
import { LambdaWebCloudFrontOacStack } from '../lib/lambda-web-cloudfront-oac-stack';

const app = new cdk.App();

new LambdaWebCloudFrontOacStack(app, 'lambda-web-cloudfront-oac-cdk', {
  // The Web Function lives in this Region (its home Region). CloudFront is global.
  env: {
    account: process.env.CDK_DEFAULT_ACCOUNT,
    region: process.env.CDK_DEFAULT_REGION,
  },
  description:
    'Serverless patterns - Lambda Web Function behind CloudFront with Origin Access Control (CDK)',
});
