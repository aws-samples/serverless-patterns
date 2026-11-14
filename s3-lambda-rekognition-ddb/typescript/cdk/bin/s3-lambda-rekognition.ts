#!/usr/bin/env node
import * as cdk from 'aws-cdk-lib';
import { S3LambdaRekognitionStack } from '../lib/s3-lambda-rekognition-stack';

const app = new cdk.App();
new S3LambdaRekognitionStack(app, 'S3LambdaRekognitionStack');
