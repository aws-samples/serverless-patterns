#!/usr/bin/env node
import 'source-map-support/register';
import * as cdk from 'aws-cdk-lib';
import { RagRefreshStack } from '../lib/rag-refresh-stack';

const app = new cdk.App();

new RagRefreshStack(app, 'RagRefreshStack', {
  env: {
    account: process.env.CDK_DEFAULT_ACCOUNT,
    region: process.env.CDK_DEFAULT_REGION,
  },
});
