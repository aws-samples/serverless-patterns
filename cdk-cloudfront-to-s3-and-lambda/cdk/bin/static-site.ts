#!/usr/bin/env node
import 'source-map-support/register';
import * as cdk from 'aws-cdk-lib';
import { StaticSiteStack } from '../lib/static-site-stack';

const app = new cdk.App();
new StaticSiteStack(app, 'StaticSiteStack', {
  //TODO: To be able to deploy Lamda@Edge requires explicitly setting the region.
  env: { region: 'eu-west-2' },

  /* For more information, see https://docs.aws.amazon.com/cdk/latest/guide/environments.html */
});
