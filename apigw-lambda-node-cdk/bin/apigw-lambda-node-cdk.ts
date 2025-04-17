#!/usr/bin/env node
import * as cdk from 'aws-cdk-lib';
import { ApigwLambdaNodeStack } from '../lib/apigw-lambda-node-cdk-stack';

const app = new cdk.App();

new ApigwLambdaNodeStack(app, 'ApigwLambdaStack', {
  stageName: 'v1',
  description: 'REST API Gateway with Lambda integration using openapi spec',
});