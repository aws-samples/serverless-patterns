#!/usr/bin/env node
import 'source-map-support/register';
import * as cdk from 'aws-cdk-lib';
import { BedrockGuardrailsEnforcementStack } from '../lib/bedrock-guardrails-enforcement-stack';

const app = new cdk.App();
new BedrockGuardrailsEnforcementStack(app, 'BedrockGuardrailsEnforcementStack');
