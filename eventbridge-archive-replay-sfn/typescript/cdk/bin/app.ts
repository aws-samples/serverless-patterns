#!/usr/bin/env node
import * as cdk from 'aws-cdk-lib';
import { EventbridgeArchiveReplaySfnStack } from '../lib/eventbridge-archive-replay-sfn-stack';

const app = new cdk.App();
new EventbridgeArchiveReplaySfnStack(app, 'EventbridgeArchiveReplaySfnStack', {
  env: { account: process.env.CDK_DEFAULT_ACCOUNT, region: process.env.CDK_DEFAULT_REGION },
});
