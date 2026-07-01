#!/usr/bin/env node
// Copyright 2026 Amazon.com, Inc. or its affiliates. All Rights Reserved.
// SPDX-License-Identifier: MIT-0

import 'source-map-support/register';
import * as cdk from 'aws-cdk-lib';
import { SfnInvoicingBedrockChargebackStack } from '../lib/sfn-invoicing-bedrock-chargeback-stack';

const app = new cdk.App();
new SfnInvoicingBedrockChargebackStack(app, 'SfnInvoicingBedrockChargebackStack', {
  env: {
    account: process.env.CDK_DEFAULT_ACCOUNT,
    region: process.env.CDK_DEFAULT_REGION || 'us-east-1',
  },
});
