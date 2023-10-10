#!/usr/bin/env node
import 'source-map-support/register';
import * as cdk from 'aws-cdk-lib';
import { LambdaAdapterCdkStack } from '../stack/lambda-web-adapter-stack';

const app = new cdk.App();
new LambdaAdapterCdkStack(app, 'LambdaAdapterCdkStack', {});
