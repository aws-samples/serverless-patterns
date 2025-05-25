#!/usr/bin/env node
const cdk = require('aws-cdk-lib');
const { LambdaSqsBestPracticesCdkStack } = require('../lib/lambda-sqs-best-practices-cdk-stack');

const app = new cdk.App();
new LambdaSqsBestPracticesCdkStack(app, 'LambdaSqsBestPracticesCdkStack', {});