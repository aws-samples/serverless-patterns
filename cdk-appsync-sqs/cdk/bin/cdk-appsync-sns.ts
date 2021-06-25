#!/usr/bin/env node
import * as cdk from '@aws-cdk/core'
import { CdkAppSyncSnSStack } from '../lib/main'

const app = new cdk.App()
new CdkAppSyncSnSStack(app, 'CdkAppSyncSnSStack')
