#!/usr/bin/env node
import 'source-map-support/register';
import * as cdk from 'aws-cdk-lib';
import { S3TriggerFargateTaskStack } from './s3-trigger-fargate-task-stack';
const description = "S3-Fargate Pattern (uksb-1tthgi812) (tag:s3-eventbridge-fargate-cdk)";
const app = new cdk.App();
new S3TriggerFargateTaskStack(app, 'S3TriggerFargateTaskStack', {description:description
});
