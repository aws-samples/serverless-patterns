#!/usr/bin/env node
import { App } from 'aws-cdk-lib';
import { AppSyncEventBridgeStack } from '../lib/appsync-eventbridge-datasource-stack';

const app = new App();

new AppSyncEventBridgeStack(app, 'AppSyncEventBridgeStack', {});

