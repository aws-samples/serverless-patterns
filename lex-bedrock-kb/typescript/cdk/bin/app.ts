#!/usr/bin/env node
// Copyright Amazon.com, Inc. or its affiliates. All Rights Reserved.
// SPDX-License-Identifier: MIT-0
import * as cdk from 'aws-cdk-lib';
import { LexBedrockKbStack } from '../lib/lex-bedrock-kb-stack';

// The stack is Region-agnostic: it deploys to the Region of your AWS CLI profile or AWS_REGION.
const app = new cdk.App();
new LexBedrockKbStack(app, 'LexBedrockKbStack');
