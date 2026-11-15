#!/usr/bin/env node

/*!  Copyright 2021 Amazon.com, Inc. or its affiliates. All Rights Reserved.
  *  SPDX-License-Identifier: MIT-0
 */

import 'source-map-support/register';
import * as cdk from 'aws-cdk-lib';
import { CdkApigwSnsSqsLambdaStack } from '../lib/cdk-apigw-sns-sqs-lambda-stack';

const app = new cdk.App();
new CdkApigwSnsSqsLambdaStack(app, 'CdkApigwSnsSqsLambdaStack', {
  /* If you don't specify 'env', this stack will be environment-agnostic.
   * Account/Region-dependent features and context lookups will not work,
   * but a single synthesized template can be deployed anywhere. */

  /* Uncomment the next line to specialize this stack for the AWS Account
   * and Region that are implied by the current CLI configuration. */
  // env: { account: process.env.CDK_DEFAULT_ACCOUNT, region: process.env.CDK_DEFAULT_REGION },

  /* Uncomment the next line if you know exactly what Account and Region you
   * want to deploy the stack to. */
  // env: { account: '123xxxyyyzzz', region: 'us-east-1' },

  /* For more information, see https://docs.aws.amazon.com/cdk/latest/guide/environments.html */
});
