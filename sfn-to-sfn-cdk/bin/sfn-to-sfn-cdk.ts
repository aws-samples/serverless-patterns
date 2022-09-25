#!/usr/bin/env node
import 'source-map-support/register';
import * as cdk from 'aws-cdk-lib';
import { SfnToSfnCdkStack } from '../lib/sfn-to-sfn-cdk-stack';

const app = new cdk.App();
new SfnToSfnCdkStack(app, 'SfnToSfnCdkStack');