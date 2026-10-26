#!/usr/bin/env node
// Copyright Amazon.com, Inc. or its affiliates. All Rights Reserved.
// SPDX-License-Identifier: MIT-0
import * as cdk from 'aws-cdk-lib';
import { LambdaRecursionSfnStack } from '../lib/lambda-recursion-sfn-stack';

const app = new cdk.App();
new LambdaRecursionSfnStack(app, 'LambdaRecursionSfnStack', {
  description:
    'AWS Lambda recursive loop detection metric, Amazon CloudWatch alarm, Amazon EventBridge rule and AWS Step Functions workflow that contains an AWS Lambda function that invokes itself',
});
