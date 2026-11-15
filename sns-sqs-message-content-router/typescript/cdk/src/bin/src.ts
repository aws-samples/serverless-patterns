#!/usr/bin/env node
import 'source-map-support/register';
import * as cdk from 'aws-cdk-lib';
import { SrcStack } from '../lib/src-stack';

const app = new cdk.App();
new SrcStack(app, 'cdk-stack-message-router', {

});