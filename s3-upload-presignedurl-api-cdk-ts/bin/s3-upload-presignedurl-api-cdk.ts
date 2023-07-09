#!/usr/bin/env node
import 'source-map-support/register';
import * as cdk from 'aws-cdk-lib';
import { S3UploadPresignedURLAPIStack } from '../lib/s3-upload-presignedurl-api-cdk-stack';

const app = new cdk.App();
new S3UploadPresignedURLAPIStack(app, 'S3UploadPresignedURLAPIStack', {});
