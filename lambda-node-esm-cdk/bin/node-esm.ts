#!/usr/bin/env node
import 'source-map-support/register';
import * as cdk from 'aws-cdk-lib';
import { NodeEsmStack } from '../lib/node-esm-stack';

const app = new cdk.App();
new NodeEsmStack(app, 'NodeEsmStack');