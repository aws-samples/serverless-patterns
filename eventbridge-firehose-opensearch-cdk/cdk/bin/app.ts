#!/usr/bin/env node
import * as cdk from 'aws-cdk-lib';
import { EventBridgeOpenSearchStack } from '../lib/eventbridge-opensearch-stack';

const app = new cdk.App();

new EventBridgeOpenSearchStack(app, 'EventMonitorStack', {
  description:
    'ServerlessLand pattern: stream all EventBridge events to OpenSearch via Amazon Data Firehose for near real-time monitoring',
  env: {
    account: process.env.CDK_DEFAULT_ACCOUNT,
    region: process.env.CDK_DEFAULT_REGION,
  },
});
