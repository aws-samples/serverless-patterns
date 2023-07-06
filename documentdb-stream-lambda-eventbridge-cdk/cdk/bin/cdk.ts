#!/usr/bin/env node
import 'source-map-support/register';
import * as cdk from 'aws-cdk-lib';
import { DocumentDbStreamLambdaEventBridgeStack } from '../lib/cdk-stack';

const app = new cdk.App();

const patternStack = new DocumentDbStreamLambdaEventBridgeStack(app, 'DocumentDbStreamLambdaEventBridgeStack', {
  env: {
    region: process.env.CDK_DEFAULT_REGION,
    account: process.env.CDK_DEFAULT_ACCOUNT,
  },
  databaseName: '', // insert DocumentDB database name
  collectionName: '', // insert DocumentDB collection name
  docDbClusterId: '', // insert DocumentDB cluster id
  secretName: '', // insert DocumentDB Secrete Manager secret name
  docDbClusterSecretArn: '', // insert DocumentDB Secrete Manager secret arn
  securityGroupId: '', // insert DocumentDB security group id
  vpcLambdaEndpointExist: false,
  vpcEventBridgeEndpointExist: false,
  vpcSecretManagerEndpointExist: false,
});

app.synth();
