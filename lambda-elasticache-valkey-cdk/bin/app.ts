#!/usr/bin/env node
import 'source-map-support/register';
import * as cdk from 'aws-cdk-lib';
import { LambdaElasticacheValkeyStack } from '../lib/lambda-elasticache-valkey-stack';
const app = new cdk.App();
new LambdaElasticacheValkeyStack(app, 'LambdaElasticacheValkeyStack', { env: { account: process.env.CDK_DEFAULT_ACCOUNT, region: process.env.CDK_DEFAULT_REGION } });
