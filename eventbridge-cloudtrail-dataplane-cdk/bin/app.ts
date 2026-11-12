#!/usr/bin/env node
import 'source-map-support/register';
import * as cdk from 'aws-cdk-lib';
import { EventbridgeCloudtrailDataplaneStack } from '../lib/eventbridge-cloudtrail-dataplane-stack';

const app = new cdk.App();
new EventbridgeCloudtrailDataplaneStack(app, 'EventbridgeCloudtrailDataplaneStack');
