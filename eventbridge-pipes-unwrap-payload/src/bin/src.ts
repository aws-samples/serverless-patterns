#!/usr/bin/env node
import 'source-map-support/register';
import * as cdk from 'aws-cdk-lib';
import { UnwrapStack } from '../lib/unwrap-payload-with-pipes';

const app = new cdk.App();
new UnwrapStack(app, 'UnwrapStack');
