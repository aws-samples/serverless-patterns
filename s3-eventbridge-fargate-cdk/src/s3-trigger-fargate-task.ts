#!/usr/bin/env node
import 'source-map-support/register';
import * as cdk from 'aws-cdk-lib';
import { S3TriggerFargateTaskStack } from './s3-trigger-fargate-task-stack';

const app = new cdk.App();
new S3TriggerFargateTaskStack(app, 'S3TriggerFargateTaskStack', {
});