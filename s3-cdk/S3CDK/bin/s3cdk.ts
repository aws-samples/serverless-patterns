import 'source-map-support/register';
import * as cdk from '@aws-cdk/core';
import { S3CdkStack } from '../lib/s3cdk-stack';

const app = new cdk.App();
new S3CdkStack(app, 'S3CdkStack',{});