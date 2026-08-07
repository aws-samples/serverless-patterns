#!/usr/bin/env node
// Copyright Amazon.com, Inc. or its affiliates. All Rights Reserved.
// SPDX-License-Identifier: MIT-0 (2026)
import 'source-map-support/register';
import * as cdk from 'aws-cdk-lib';
import { SecurityhubFindingSfnRemediationStack } from '../lib/securityhub-finding-sfn-remediation-stack';

const app = new cdk.App();
new SecurityhubFindingSfnRemediationStack(app, 'SecurityhubFindingSfnRemediationStack', {
  description: 'AWS Security Hub auto-remediation with AWS Step Functions (uksb-1tupboc57)',
});
