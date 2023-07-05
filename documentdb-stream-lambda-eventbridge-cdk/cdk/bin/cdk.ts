#!/usr/bin/env node
import 'source-map-support/register';
import * as cdk from 'aws-cdk-lib';
import { DocumentDbStreamLambdaEventBridgeStack } from '../lib/cdk-stack';
import { DocumentDbStack } from '../lib/db-stack';

const app = new cdk.App();

// const docDbStack = new DocumentDbStack(app, 'DocumentDbStack', {
//   secretName: 'DocumentDBSecret',
//   env: {
//     region: process.env.CDK_DEFAULT_REGION,
//     account: process.env.CDK_DEFAULT_ACCOUNT,
//   },
// });

const patternStack = new DocumentDbStreamLambdaEventBridgeStack(app, 'DocumentDbStreamLambdaEventBridgeStack', {
  env: {
    region: process.env.CDK_DEFAULT_REGION,
    account: process.env.CDK_DEFAULT_ACCOUNT,
  },
  databaseName: 'docdb',
  collectionName: 'products',
  docDbClusterId: 'docdbcluster',
  secretName: 'DocumentDBSecret',
  docDbClusterSecretArn: 'arn:aws:secretsmanager:us-east-2:640999649296:secret:DocumentDBSecret-HMIA1G',
  securityGroupId: 'sg-06a7bec23b05bb040',
  vpcLambdaEndpointExist: false,
  vpcEventBridgeEndpointExist: false,
  vpcSecretManagerEndpointExist: false,
  /* If you don't specify 'env', this stack will be environment-agnostic.
   * Account/Region-dependent features and context lookups will not work,
   * but a single synthesized template can be deployed anywhere. */
  /* Uncomment the next line to specialize this stack for the AWS Account
   * and Region that are implied by the current CLI configuration. */
  // env: { account: process.env.CDK_DEFAULT_ACCOUNT, region: process.env.CDK_DEFAULT_REGION },
  /* Uncomment the next line if you know exactly what Account and Region you
   * want to deploy the stack to. */
  // env: { account: '123456789012', region: 'us-east-1' },
  /* For more information, see https://docs.aws.amazon.com/cdk/latest/guide/environments.html */
});

// patternStack.addDependency(docDbStack);
app.synth();
