#!/usr/bin/env node
import 'source-map-support/register';
import * as cdk from 'aws-cdk-lib';
import { LambdaExtensionParameterStoreCdkStack } from '../lib/lambda-extension-parameter-store-cdk-stack';

const app = new cdk.App();
new LambdaExtensionParameterStoreCdkStack(app, 'LambdaExtensionParameterStoreCdkStack');