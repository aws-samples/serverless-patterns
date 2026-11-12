#!/usr/bin/env node
// Copyright Amazon.com, Inc. or its affiliates. All Rights Reserved.
// SPDX-License-Identifier: MIT-0
import * as cdk from 'aws-cdk-lib';
import { BackupSfnStack } from '../lib/backup-sfn-stack';

const app = new cdk.App();
new BackupSfnStack(app, 'BackupSfnRestoreValidationStack', {
  description:
    'AWS Backup restore testing of an Amazon DynamoDB table, validated by AWS Step Functions through Amazon EventBridge',
});
