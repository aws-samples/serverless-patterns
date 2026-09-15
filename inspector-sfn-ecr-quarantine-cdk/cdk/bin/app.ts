#!/usr/bin/env node
// Copyright Amazon.com, Inc. or its affiliates. All Rights Reserved.
// SPDX-License-Identifier: MIT-0
import 'source-map-support/register';
import * as cdk from 'aws-cdk-lib';
import { InspectorSfnEcrQuarantineStack } from '../lib/inspector-sfn-ecr-quarantine-stack';

const app = new cdk.App();

new InspectorSfnEcrQuarantineStack(app, 'InspectorSfnEcrQuarantineStack', {
  // The stack is environment-agnostic. It reads no hardcoded account/region;
  // resource ARNs are built from Aws.ACCOUNT_ID / Aws.REGION at synth time.
  description:
    'Auto-quarantine vulnerable Amazon ECR images: Amazon Inspector finding -> Amazon EventBridge -> AWS Step Functions -> Amazon ECR re-tag + Amazon SNS notify',
});

app.synth();
