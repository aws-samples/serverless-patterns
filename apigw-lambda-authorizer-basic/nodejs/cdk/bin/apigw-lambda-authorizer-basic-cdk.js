#!/usr/bin/env node

const cdk = require('aws-cdk-lib');
const { BasicAuthorizerStack } = require('../lib/basic-authorizer-stack');

const app = new cdk.App();

new BasicAuthorizerStack(app, 'BasicAuthorizerStack', {

});
