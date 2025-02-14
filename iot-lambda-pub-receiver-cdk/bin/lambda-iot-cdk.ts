#!/usr/bin/env node
import 'source-map-support/register';
import * as cdk from 'aws-cdk-lib';
import { LambdaIotCdkStack } from '../lib/lambda-iot-cdk-stack';

const app = new cdk.App();
new LambdaIotCdkStack(app, 'LambdaIotCdkStack', { });