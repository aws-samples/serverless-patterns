#!/usr/bin/env node
// Copyright Amazon.com, Inc. or its affiliates. All Rights Reserved.
// SPDX-License-Identifier: MIT-0 (2026)

import 'source-map-support/register';
import * as cdk from 'aws-cdk-lib';
import { GuarddutyFileModificationSfnResponseStack } from '../lib/guardduty-file-modification-sfn-response-stack';

const app = new cdk.App();
new GuarddutyFileModificationSfnResponseStack(app, 'GuarddutyFileModificationSfnResponseStack', {
  description: 'Amazon GuardDuty sensitive file modification with AWS Step Functions incident response (uksb-1tupboc57)',
});
