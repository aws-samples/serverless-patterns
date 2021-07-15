#!/usr/bin/env node
import * as cdk from '@aws-cdk/core'
import { MainStack } from '../lib/main'

const app = new cdk.App()
new MainStack(app, 'CdkEventBridgeCallAppSyncStack')
