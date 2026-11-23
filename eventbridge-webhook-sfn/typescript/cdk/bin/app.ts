#!/usr/bin/env node
import * as cdk from 'aws-cdk-lib';
import { EventbridgeWebhookSfnStack } from '../lib/eventbridge-webhook-sfn-stack';

const app = new cdk.App();
new EventbridgeWebhookSfnStack(app, 'EventbridgeWebhookSfnStack', {
  env: { account: process.env.CDK_DEFAULT_ACCOUNT, region: process.env.CDK_DEFAULT_REGION },
});
