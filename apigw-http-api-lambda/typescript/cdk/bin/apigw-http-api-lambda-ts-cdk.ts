#!/usr/bin/env node
import 'source-map-support/register';
import * as cdk from 'aws-cdk-lib';
import { HttpApiLambdaStack } from '../lib/httpapi-lambda-stack';

const app = new cdk.App();
const description = "Serverlessland Pattern (uksb-1tthgi812) (tag:apigw-http-api-lambda-ts-cdk)"
new HttpApiLambdaStack(app, 'HttpApiLambdaStack', {description });
