#!/usr/bin/env node
import * as cdk from '@aws-cdk/core';
import { MSKToLambdaCdkStack } from '../lib/msk-to-lambda-cdk-stack';

const app = new cdk.App();
new MSKToLambdaCdkStack(app, 'MSKToLambdaCdkStack');
