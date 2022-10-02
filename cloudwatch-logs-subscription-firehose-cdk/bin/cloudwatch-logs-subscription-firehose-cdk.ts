#!/usr/bin/env node
import 'source-map-support/register';
import * as cdk from 'aws-cdk-lib';
import { CloudwatchLogsSubscriptionFirehoseCdkStack } from '../lib/cloudwatch-logs-subscription-firehose-cdk-stack';

const app = new cdk.App();
new CloudwatchLogsSubscriptionFirehoseCdkStack(app, 'CloudwatchLogsSubscriptionFirehoseCdkStack');