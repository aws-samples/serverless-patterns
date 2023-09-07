#!/usr/bin/env node
import * as cdk from 'aws-cdk-lib';
import { PPEIoTViolations } from '../lib/s3-lambda-rekognition-iot-stack';

const app = new cdk.App();
new PPEIoTViolations(app, 'PPEIoTViolationsStack');
