#!/usr/bin/env node
import 'source-map-support/register';
import * as cdk from 'aws-cdk-lib';
import { HttpApiLambdaStack } from '../lib/httpapi-lambda-stack';

const app = new cdk.App();
new HttpApiLambdaStack(app, 'HttpApiLambdaStack', { });