#!/usr/bin/env node
import 'source-map-support/register';
import * as cdk from 'aws-cdk-lib';
import { CloudwatchLogsSubscriptionLambdaCdkStack } from '../lib/cloudwatch-logs-subscription-lambda-cdk-stack';

const app = new cdk.App();
new CloudwatchLogsSubscriptionLambdaCdkStack(app, 'CloudwatchLogsSubscriptionLambdaCdkStack');