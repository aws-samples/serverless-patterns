#!/usr/bin/env node
// Copyright Amazon.com, Inc. or its affiliates. All Rights Reserved.
// SPDX-License-Identifier: MIT-0
// 2026

import * as cdk from 'aws-cdk-lib';
import { MacieSfnS3QuarantineStack } from '../lib/macie-sfn-s3-quarantine-stack';

const app = new cdk.App();
new MacieSfnS3QuarantineStack(app, 'MacieSfnS3QuarantineStack', {
  env: {
    account: process.env.CDK_DEFAULT_ACCOUNT,
    region: process.env.CDK_DEFAULT_REGION,
  },
});
