#!/usr/bin/env node
// Copyright Amazon.com, Inc. or its affiliates. All Rights Reserved.
// SPDX-License-Identifier: MIT-0 (2026)
import 'source-map-support/register';
import * as cdk from 'aws-cdk-lib';
import { EventbridgePipesBedrockEnrichmentStack } from '../lib/eventbridge-pipes-bedrock-enrichment-stack';

const app = new cdk.App();
new EventbridgePipesBedrockEnrichmentStack(app, 'EventbridgePipesBedrockEnrichmentStack', {
  description: 'Amazon EventBridge Pipes with Amazon Bedrock AI enrichment (uksb-1tupboc57)',
});
