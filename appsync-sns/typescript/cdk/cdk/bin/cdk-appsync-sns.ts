#!/usr/bin/env node
import * as cdk from 'aws-cdk-lib';
import { CdkAppSyncSnSStack } from '../lib/main'

const app = new cdk.App()
new CdkAppSyncSnSStack(app, 'CdkAppSyncSnSStack')
