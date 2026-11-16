#!/usr/bin/env node
import 'source-map-support/register';
import * as cdk from 'aws-cdk-lib';
import { DemoStack } from './lib/demo-stack';

const app = new cdk.App();
new DemoStack(app, 'DemoStack', {
    stackName: 'AppSync-Subscription-Enhanced-Filtering-Demo',
    description: 'Demo stack for the appsync-subscription-filter-cdk pattern (uksb-1tthgi812) (tag:appsync-subscription-filter-cdk)',
});
