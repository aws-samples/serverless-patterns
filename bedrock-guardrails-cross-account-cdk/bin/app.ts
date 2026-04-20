#!/usr/bin/env node
import 'source-map-support/register';
import * as cdk from 'aws-cdk-lib';
import { BedrockGuardrailsCrossAccountStack } from '../lib/bedrock-guardrails-cross-account-stack';

const app = new cdk.App();
new BedrockGuardrailsCrossAccountStack(app, 'BedrockGuardrailsCrossAccountStack');
