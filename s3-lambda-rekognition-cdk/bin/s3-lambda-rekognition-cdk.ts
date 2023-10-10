#!/usr/bin/env node
import 'source-map-support/register';
import * as cdk from 'aws-cdk-lib';
import { S3LambdaRekognitionCdkStack } from '../lib/s3-lambda-rekognition-cdk-stack';

const app = new cdk.App();
new S3LambdaRekognitionCdkStack(app, 'S3LambdaRekognitionCdkStack');