#!/usr/bin/env node
// Copyright Amazon.com, Inc. or its affiliates. All Rights Reserved.
// SPDX-License-Identifier: MIT-0
import * as cdk from 'aws-cdk-lib';
import { AccessAnalyzerSfnStack } from '../lib/accessanalyzer-sfn-stack';

const app = new cdk.App();

// The account and Region come from the AWS CLI configuration or environment.
// IAM management events are delivered in us-east-1, so deploy the stack there
// (see the README). The stack adds a synth warning for any other Region.
new AccessAnalyzerSfnStack(app, 'AccessAnalyzerSfnStack', {
  env: {
    account: process.env.CDK_DEFAULT_ACCOUNT,
    region: process.env.CDK_DEFAULT_REGION,
  },
  description:
    'IAM inline policy check: Amazon EventBridge -> AWS Step Functions -> IAM Access Analyzer CheckAccessNotGranted -> Amazon SNS',
});
