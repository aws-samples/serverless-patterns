#!/usr/bin/env node
import * as cdk from 'aws-cdk-lib';
import { S3ToLambdaCdkStack } from '../lib/s3-to-lambda-cdk-stack';

const app = new cdk.App();
new S3ToLambdaCdkStack(app, 'S3ToLambdaCdkStack');
