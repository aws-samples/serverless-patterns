#!/usr/bin/env node
import 'source-map-support/register';
import * as cdk from 'aws-cdk-lib';
import { S3EventBridgeStack } from '../lib/s3-eventbridge-sfn-stack';

const app = new cdk.App();
new S3EventBridgeStack(app, 'S3EventBridgeSfnStackStack', {
});