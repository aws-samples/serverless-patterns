#!/usr/bin/env node
import 'source-map-support/register';
import * as cdk from 'aws-cdk-lib';
import { LambdaRuby4BedrockStack } from '../lib/lambda-ruby4-bedrock-stack';

const app = new cdk.App();
new LambdaRuby4BedrockStack(app, 'LambdaRuby4BedrockStack');
