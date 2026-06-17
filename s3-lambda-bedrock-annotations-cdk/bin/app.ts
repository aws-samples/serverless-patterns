#!/usr/bin/env node
import 'source-map-support/register';
import * as cdk from 'aws-cdk-lib';
import { S3LambdaBedrockAnnotationsStack } from '../lib/s3-lambda-bedrock-annotations-stack';

const app = new cdk.App();
new S3LambdaBedrockAnnotationsStack(app, 'S3LambdaBedrockAnnotationsStack');
