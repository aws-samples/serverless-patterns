#!/usr/bin/env node
import 'source-map-support/register';
import * as cdk from 'aws-cdk-lib';
import { CdkStack } from '../cdk/cdk-stack';

const app = new cdk.App();

new CdkStack(app, 'LambdaExtensionSsmSecretsCdkPhpStack', {
  // This is required by bref
  env: { region: 'us-east-1' },

  /* For more information, see https://docs.aws.amazon.com/cdk/latest/guide/environments.html */
  stackName: 'LambdaExtensionSsmSecretsCdkPhpStack',
});
