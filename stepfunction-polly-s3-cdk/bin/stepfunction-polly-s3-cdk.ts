#!/usr/bin/env node
import 'source-map-support/register';
import * as cdk from 'aws-cdk-lib';
import { StepfunctionPollyS3CdkStack } from '../lib/stepfunction-polly-s3-cdk-stack';

const app = new cdk.App();
new StepfunctionPollyS3CdkStack(app, 'StepfunctionPollyS3CdkStack');