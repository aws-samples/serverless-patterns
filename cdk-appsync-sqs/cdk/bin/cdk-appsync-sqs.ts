#!/usr/bin/env node
import * as cdk from '@aws-cdk/core'
import { CdkAppSyncSqSStack } from '../lib/main'

const app = new cdk.App()
new CdkAppSyncSqSStack(app, 'CdkAppSyncSqSStack')
