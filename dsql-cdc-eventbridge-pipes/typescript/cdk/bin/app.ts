#!/usr/bin/env node
// Copyright Amazon.com, Inc. or its affiliates. All Rights Reserved.
// SPDX-License-Identifier: MIT-0

import 'source-map-support/register';
import * as cdk from 'aws-cdk-lib';
import { DsqlCdcEventbridgePipesStack } from '../lib/dsql-cdc-eventbridge-pipes-stack';

const app = new cdk.App();
new DsqlCdcEventbridgePipesStack(app, 'DsqlCdcEventbridgePipesStack', {
  description: 'Amazon Aurora DSQL CDC to Amazon EventBridge with Amazon EventBridge Pipes (uksb-1tupboc57)',
});
