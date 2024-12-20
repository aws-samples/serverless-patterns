#!/usr/bin/env node
import 'source-map-support/register';
import * as cdk from 'aws-cdk-lib';
import { DemoStack } from '../lib/demo-stack';

const app = new cdk.App();

new DemoStack(app, 'DemoStack', {
    stackName: 'Custom-Resource-With-Multiple-Lambdas-Demo',
    description: 'Demo of custom resource with multiple lambda functions',
    env: {
        region: process.env.CDK_DEFAULT_REGION,
        account: process.env.CDK_DEFAULT_ACCOUNT,
    },
});