#!/usr/bin/env node
import 'source-map-support/register';
import * as cdk from 'aws-cdk-lib';
import { FirehoseLambdaStack } from '../lib/firehose-lambda-stack';

const app = new cdk.App();
new FirehoseLambdaStack(app, 'FirehoseLambdaStack', {

});