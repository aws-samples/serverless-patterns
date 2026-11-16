#!/usr/bin/env node

const cdk = require('aws-cdk-lib');
const { AmplifyWebAppStack } = require('../lib/amplify-webapp-stack');

const app = new cdk.App();

new AmplifyWebAppStack(app, 'AmplifyWebAppStack', {

});