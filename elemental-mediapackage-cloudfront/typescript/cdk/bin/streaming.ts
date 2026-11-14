#!/usr/bin/env node
import 'source-map-support/register';
import * as cdk from 'aws-cdk-lib';
import { StreamingStack } from '../lib/streaming_stack';

const app = new cdk.App();
new StreamingStack(app, 'StreamingStack');