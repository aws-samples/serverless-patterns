#!/usr/bin/env node
import 'source-map-support/register';
import * as cdk from 'aws-cdk-lib';
import { LambdaElasticIpStack } from '../lib/cdk-stack';

const app = new cdk.App();

const patternStack = new LambdaElasticIpStack(app, 'LambdaElasticIpStack', {
  env: {
    region: process.env.CDK_DEFAULT_REGION,
    account: process.env.CDK_DEFAULT_ACCOUNT,
  },
});

app.synth();
