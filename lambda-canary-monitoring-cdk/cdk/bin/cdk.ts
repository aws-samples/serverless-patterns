#!/usr/bin/env node
import 'source-map-support/register';
import * as cdk from 'aws-cdk-lib';
import { LambdaCanaryMonitoringStack } from '../lib/lambda-canary-stack';
import { MonitoringStack } from '../lib/monitoring-stack';

const app = new cdk.App();

const monitoring = new MonitoringStack(app, 'MonitoringStack');

new LambdaCanaryMonitoringStack(app, 'LambdaCanaryStack', {
  VERSION_NUMBER: '1',
  monitoring,
});