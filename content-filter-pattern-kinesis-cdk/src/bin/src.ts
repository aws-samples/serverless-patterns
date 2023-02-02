#!/usr/bin/env node
import 'source-map-support/register';
import * as cdk from 'aws-cdk-lib';
import { ContentFilterStack } from '../lib/content-filter-stack';

const app = new cdk.App();
new ContentFilterStack(app, 'ContentFilterStack');
