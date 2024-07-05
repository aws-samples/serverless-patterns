#!/usr/bin/env node

const cdk = require('aws-cdk-lib');
const { CdkApigwLambdaDynamodbStack } = require('../lib/cdk-apigw-lambda-dynamodb-stack');

const app = new cdk.App();
new CdkApigwLambdaDynamodbStack(app, 'CdkApigwLambdaDynamodbStack', {
});
