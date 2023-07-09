#!/usr/bin/env node
import 'source-map-support/register';
import * as cdk from 'aws-cdk-lib';
import { LambdaSNSLambdaStack } from '../lib/lambda-sns-lambda';

const app = new cdk.App();
new LambdaSNSLambdaStack(app, 'LambdaSNSLambdaStack', {});
