#!/usr/bin/env node
import 'source-map-support/register';
import * as cdk from 'aws-cdk-lib';
import { SfnAgentcoreBedrockStack } from '../lib/sfn-agentcore-bedrock-stack';

const app = new cdk.App();
new SfnAgentcoreBedrockStack(app, 'SfnAgentcoreBedrockStack');
