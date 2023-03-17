#!/usr/bin/env node
import * as cdk from 'aws-cdk-lib';
import { EbSqsEcsStack } from '../lib/eb-sqs-ecs-stack';
import { env } from 'process';

const app = new cdk.App();
new EbSqsEcsStack(app, 'EbSqsEcsStack', { 
  env: { 
    account: process.env.CDK_DEFAULT_ACCOUNT, 
    region: process.env.CDK_DEFAULT_REGION 
}});