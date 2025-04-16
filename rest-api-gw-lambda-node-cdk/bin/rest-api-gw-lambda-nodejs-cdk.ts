#!/usr/bin/env node
import * as cdk from 'aws-cdk-lib';
import { RestApiGwLambdaStack } from '../lib/rest-api-gateway-lambda-stack';

const app = new cdk.App();

new RestApiGwLambdaStack(app, 'RestApiGwLambdaStack', {
  stageName: 'v1',
  description: 'REST API Gateway with Lambda integration using openapi spec',
});