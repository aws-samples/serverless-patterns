#!/usr/bin/env node
// Copyright Amazon.com, Inc. or its affiliates. All Rights Reserved.
// SPDX-License-Identifier: MIT-0 (2026)

import 'source-map-support/register';
import * as cdk from 'aws-cdk-lib';
import { CloudwatchLogAlarmLambdaRemediationStack } from '../lib/cloudwatch-log-alarm-lambda-remediation-stack';

const app = new cdk.App();
new CloudwatchLogAlarmLambdaRemediationStack(app, 'CloudwatchLogAlarmLambdaRemediationStack', {
  description: 'Amazon CloudWatch Log Alarm with AWS Lambda auto-remediation (uksb-1tupboc57)',
});
