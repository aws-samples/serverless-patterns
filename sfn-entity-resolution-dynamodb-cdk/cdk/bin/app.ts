#!/usr/bin/env node
// Copyright Amazon.com, Inc. or its affiliates. All Rights Reserved.
// SPDX-License-Identifier: MIT-0
// 2026

import * as cdk from 'aws-cdk-lib';
import { SfnEntityResolutionDynamodbStack } from '../lib/sfn-entity-resolution-dynamodb-stack';

const app = new cdk.App();
new SfnEntityResolutionDynamodbStack(app, 'SfnEntityResolutionDynamodbStack', {
  env: {
    account: process.env.CDK_DEFAULT_ACCOUNT,
    region: process.env.CDK_DEFAULT_REGION,
  },
});
