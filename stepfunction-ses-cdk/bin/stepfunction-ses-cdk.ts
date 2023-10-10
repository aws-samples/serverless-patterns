#!/usr/bin/env node
import 'source-map-support/register';
import * as cdk from 'aws-cdk-lib';
import { StepfunctionSesCdkStack } from '../lib/stepfunction-ses-cdk-stack';

const app = new cdk.App();
new StepfunctionSesCdkStack(app, 'StepfunctionSesCdkStack');