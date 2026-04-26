#!/usr/bin/env node
import * as cdk from 'aws-cdk-lib';
import { LambdaMcpServerBedrockStack } from '../lib/lambda-mcp-server-bedrock-stack';

const app = new cdk.App();
new LambdaMcpServerBedrockStack(app, 'LambdaMcpServerBedrockStack');
