#!/usr/bin/env node
/*! Copyright Amazon.com, Inc. or its affiliates. All Rights Reserved.
 *  SPDX-License-Identifier: MIT-0
 */

import * as cdk from 'aws-cdk-lib';

import { MskLambdaCdkStack } from '../lib/msk-lambda-cdk-stack';

const app = new cdk.App();
new MskLambdaCdkStack(app, 'MskLambdaCdkStack');
