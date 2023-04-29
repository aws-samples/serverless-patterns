#!/usr/bin/env node

const cdk = require('aws-cdk-lib');

const {SampleStack} = require('../lib/sample-stack');
const {SamplePublicZoneStack} = require('../lib/sample-public-zone-stack');
const {SamplePrivateZoneStack} = require("../lib/sample-private-zone-stack");

const app = new cdk.App();
const env = {
    account: process.env.CDK_DEPLOY_ACCOUNT || process.env.CDK_DEFAULT_ACCOUNT,
    region: process.env.CDK_DEPLOY_REGION || process.env.CDK_DEFAULT_REGION
}

new SampleStack(app, 'SampleStack', {
   env: env
});


// Uncomment to deploy stack
/*
new SamplePublicZoneStack(app, 'PublicZoneStack', {
    env: env
});
*/


// Uncomment to deploy stack
/*
new SamplePrivateZoneStack(app, 'PrivateZoneStack', {
    env: env
});
*/
