#!/usr/bin/env node
import * as cdk from 'aws-cdk-lib';
import { ApigwLambdaPowertoolsOpenapiStack } from '../lib/parent-stack';

const app = new cdk.App();

new ApigwLambdaPowertoolsOpenapiStack(app, 'ApigwLambdaStack', {
  stageName: 'dev',
  description: 'REST API Gateway with Lambda integration using openapi spec',
});