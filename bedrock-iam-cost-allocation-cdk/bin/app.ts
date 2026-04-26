#!/usr/bin/env node
import * as cdk from 'aws-cdk-lib';
import { BedrockIamCostAllocationStack } from '../lib/bedrock-iam-cost-allocation-stack';

const app = new cdk.App();
new BedrockIamCostAllocationStack(app, 'BedrockIamCostAllocationStack');
