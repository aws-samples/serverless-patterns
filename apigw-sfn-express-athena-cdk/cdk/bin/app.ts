#!/usr/bin/env node
// Copyright 2026 Amazon.com, Inc. or its affiliates. All Rights Reserved.
// SPDX-License-Identifier: MIT-0

import 'source-map-support/register';
import * as cdk from 'aws-cdk-lib';
import { ApigwSfnExpressAthenaStack } from '../lib/apigw-sfn-express-athena-stack';

const app = new cdk.App();

new ApigwSfnExpressAthenaStack(app, 'ApigwSfnExpressAthenaStack', {
  // Uses the account/region from the ambient CDK environment
  // (CDK_DEFAULT_ACCOUNT / CDK_DEFAULT_REGION). No hardcoded values.
  env: {
    account: process.env.CDK_DEFAULT_ACCOUNT,
    region: process.env.CDK_DEFAULT_REGION,
  },
  description:
    'Amazon API Gateway -> AWS Step Functions Express -> Amazon Athena synchronous query, zero AWS Lambda (uksb-sfn-athena)',
});

app.synth();
