#!/usr/bin/env node
// Copyright 2026 Amazon.com, Inc. or its affiliates. All Rights Reserved.
// SPDX-License-Identifier: MIT-0
import * as cdk from 'aws-cdk-lib';
import { AppSyncAuroraServerlessStack } from '../lib/appsync-aurora-serverless-v2-rds-data-api-stack';

const app = new cdk.App();
new AppSyncAuroraServerlessStack(app, 'AppSyncAuroraServerlessStack', {
  description:
    'AWS AppSync GraphQL API backed by Amazon Aurora Serverless v2 via the RDS Data API, with zero AWS Lambda functions (uses-appsync-aurora-serverless-v2-rds-data-api-cdk)',
});
