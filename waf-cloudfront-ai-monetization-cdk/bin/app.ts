#!/usr/bin/env node
import 'source-map-support/register';
import * as cdk from 'aws-cdk-lib';
import { WafCloudfrontAiMonetizationStack } from '../lib/waf-cloudfront-ai-monetization-stack';

const app = new cdk.App();
new WafCloudfrontAiMonetizationStack(app, 'WafCloudfrontAiMonetizationStack', {
  env: {
    account: process.env.CDK_DEFAULT_ACCOUNT,
    region: 'us-east-1', // Required: WAF for CloudFront must be in us-east-1
  },
});
