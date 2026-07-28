#!/usr/bin/env node
// Copyright Amazon.com, Inc. or its affiliates. All Rights Reserved.
// SPDX-License-Identifier: MIT-0 (2026)

import 'source-map-support/register';
import * as cdk from 'aws-cdk-lib';
import { WafAgentcoreGatewayBedrockStack } from '../lib/waf-agentcore-gateway-bedrock-stack';

const app = new cdk.App();
new WafAgentcoreGatewayBedrockStack(app, 'WafAgentcoreGatewayBedrockStack', {
  env: {
    account: process.env.CDK_DEFAULT_ACCOUNT,
    region: process.env.CDK_DEFAULT_REGION,
  },
});
