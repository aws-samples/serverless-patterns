#!/usr/bin/env node
import * as cdk from 'aws-cdk-lib';
import { DynamicEventBridgeSchedulesStack } from '../lib/src-stack';

const app = new cdk.App();
new DynamicEventBridgeSchedulesStack(app, 'DynamicEventBridgeSchedules');
