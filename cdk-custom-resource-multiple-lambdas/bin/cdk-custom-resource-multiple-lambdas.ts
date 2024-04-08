#!/usr/bin/env node
import 'source-map-support/register';
import * as cdk from 'aws-cdk-lib';
import { CdkCustomResourceMultipleLambdasStack } from '../lib/cdk-custom-resource-multiple-lambdas-stack';

const app = new cdk.App();

new CdkCustomResourceMultipleLambdasStack(app, 'CdkCustomResourceMultipleLambdasStack', {
    stackName: 'Custom-Resource-With-Multiple-Lambdas-Demo',
    description: 'Demo of custom resource with multiple lambda functions',
    env: {
        region: process.env.CDK_DEFAULT_REGION,
        account: process.env.CDK_DEFAULT_ACCOUNT,
    },
});