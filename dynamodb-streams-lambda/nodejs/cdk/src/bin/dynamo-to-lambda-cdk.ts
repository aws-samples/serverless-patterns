#!/usr/bin/env node
import * as cdk from 'aws-cdk-lib';
import { DynamoToLambdaCdkStack } from '../lib/dynamo-to-lambda-cdk-stack';

const app = new cdk.App();
new DynamoToLambdaCdkStack(app, 'DynamoToLambdaCdkStack');
