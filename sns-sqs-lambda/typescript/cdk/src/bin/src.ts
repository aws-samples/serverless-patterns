#!/usr/bin/env node
import 'source-map-support/register';
import * as cdk from 'aws-cdk-lib';
import { SNSSQSLambdaStack } from '../lib/sns-sqs-lambda-cdk';

const app = new cdk.App();
new SNSSQSLambdaStack(app, 'SNSSQSLambdaStack', {});
