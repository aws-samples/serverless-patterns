#!/usr/bin/env node
import * as cdk from 'aws-cdk-lib';
import { CdkAppSyncSqSStack } from '../lib/main'

const app = new cdk.App()
new CdkAppSyncSqSStack(app, 'CdkAppSyncSqSStack')
