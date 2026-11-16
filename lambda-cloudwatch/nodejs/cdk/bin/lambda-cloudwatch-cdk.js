#!/usr/bin/env node

const { App } = require('aws-cdk-lib');       
const { LambdaCloudWatchCdkStack } = require('../lib/lambda-cloudwatch-cdk-stack');

const app = new App();
new LambdaCloudWatchCdkStack(app, 'LambdaCloudWatchCdkStack', {
  /* If you don't specify 'env', this stack will be environment-agnostic.
   * Account/Region-dependent features and context lookups will not work,
   * but a single synthesized template can be deployed anywhere. */

  /* Uncomment the next line to specialize this stack for the AWS Account
   * and Region that are implied by the current CLI configuration. */
  // env: { account: process.env.CDK_DEFAULT_ACCOUNT, region: process.env.CDK_DEFAULT_REGION },

  /* Uncomment the next line if you know exactly what Account and Region you
   * want to deploy the stack to. */

  /* For more information, see https://docs.aws.amazon.com/cdk/latest/guide/environments.html */
});