#!/usr/bin/env node
import 'source-map-support/register';
import * as cdk from 'aws-cdk-lib';
import { LambdaElasticIpStack } from '../lib/cdk-stack';

const app = new cdk.App();

const patternStack = new LambdaElasticIpStack(app, 'LambdaElasticIpStack', {
  env: {
    region: 'us-east-1' || process.env.CDK_DEFAULT_REGION,
    account: '199150394284' || process.env.CDK_DEFAULT_ACCOUNT,
  },
});

app.synth();
