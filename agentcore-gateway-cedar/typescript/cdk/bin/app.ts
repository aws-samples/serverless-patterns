#!/usr/bin/env node
// Copyright Amazon.com, Inc. or its affiliates. All Rights Reserved.
// SPDX-License-Identifier: MIT-0
import * as cdk from 'aws-cdk-lib';
import { AgentcoreGatewayCedarStack } from '../lib/agentcore-gateway-cedar-stack';

const app = new cdk.App();
new AgentcoreGatewayCedarStack(app, 'AgentcoreGatewayCedarStack', {
  description:
    'Amazon Bedrock AgentCore Gateway with a policy engine from Policy in Amazon Bedrock AgentCore (Cedar, ENFORCE), an AWS Lambda tool target and Amazon Cognito',
});
