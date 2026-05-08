#!/usr/bin/env node
import 'source-map-support/register';
import * as cdk from 'aws-cdk-lib';
import { CloudfrontKvsLambdaStack } from '../lib/cloudfront-kvs-lambda-stack';
const app = new cdk.App();
new CloudfrontKvsLambdaStack(app, 'CloudfrontKvsLambdaStack', { env: { account: process.env.CDK_DEFAULT_ACCOUNT, region: 'us-east-1' } });
