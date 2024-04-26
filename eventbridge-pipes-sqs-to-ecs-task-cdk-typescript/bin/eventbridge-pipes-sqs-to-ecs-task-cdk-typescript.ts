#!/usr/bin/env node
import 'source-map-support/register';
import * as cdk from 'aws-cdk-lib';
import { EventbridgePipesSqsToEcsTaskCdkTypescriptStack } from '../lib/app';

const app = new cdk.App();
new EventbridgePipesSqsToEcsTaskCdkTypescriptStack(app, 'EventbridgePipesSqsToEcsTaskCdkTypescriptStack', {
});