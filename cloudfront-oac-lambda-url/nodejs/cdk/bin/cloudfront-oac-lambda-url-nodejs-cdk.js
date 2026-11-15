#!/usr/bin/env node
const cdk = require('aws-cdk-lib');
const { CloudfrontOacLambdaUrlNodejsCdkStack } = require('../lib/cloudfront-oac-lambda-url-nodejs-cdk-stack');

const app = new cdk.App();
new CloudfrontOacLambdaUrlNodejsCdkStack(app, 'CloudfrontOacLambdaUrlNodejsCdkStack');
