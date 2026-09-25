#!/usr/bin/env node
// Copyright Amazon.com, Inc. or its affiliates. All Rights Reserved.
// SPDX-License-Identifier: MIT-0 (2026)

import 'source-map-support/register';
import * as cdk from 'aws-cdk-lib';
import { DsqlCdcEventbridgeFanoutStack } from '../lib/dsql-cdc-eventbridge-fanout-stack';

const app = new cdk.App();
new DsqlCdcEventbridgeFanoutStack(app, 'DsqlCdcEventbridgeFanoutStack', {
  description: 'Amazon Aurora DSQL CDC to Amazon EventBridge fan-out pattern (uksb-1tupboc57)',
});
