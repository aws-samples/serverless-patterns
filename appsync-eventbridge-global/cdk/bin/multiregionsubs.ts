#!/usr/bin/env node
import 'source-map-support/register';
import * as cdk from '@aws-cdk/core';
import { GlobalSubsRegion1 } from '../lib/globalSubs-region1-stack';
import { GlobalSubsRegion2 } from '../lib/globalSubs-region2-stack';
import { GlobalSubsXRegionEBRulesRegion1 } from '../lib/globalSubs-ebXRegionRulesRegion1-stack';
import { GlobalSubsXRegionEBRulesRegion2 } from '../lib/globalSubs-ebXRegionRulesRegion2-stack';

const app = new cdk.App();
const Stack1 = new GlobalSubsRegion1(app, 'GlobalSubsRegion1', {
  /* If you don't specify 'env', this stack will be environment-agnostic.
   * Account/Region-dependent features and context lookups will not work,
   * but a single synthesized template can be deployed anywhere. */

  /* Uncomment the next line to specialize this stack for the AWS Account
   * and Region that are implied by the current CLI configuration. */
  // env: { account: process.env.CDK_DEFAULT_ACCOUNT, region: process.env.CDK_DEFAULT_REGION },

  /* Uncomment the next line if you know exactly what Account and Region you
   * want to deploy the stack to. */
  env: { region: 'us-west-2' }

  /* For more information, see https://docs.aws.amazon.com/cdk/latest/guide/environments.html */
});
const Stack2 = new GlobalSubsRegion2(app, 'GlobalSubsRegion2', {
  /* If you don't specify 'env', this stack will be environment-agnostic.
   * Account/Region-dependent features and context lookups will not work,
   * but a single synthesized template can be deployed anywhere. */

  /* Uncomment the next line to specialize this stack for the AWS Account
   * and Region that are implied by the current CLI configuration. */
  // env: { account: process.env.CDK_DEFAULT_ACCOUNT, region: process.env.CDK_DEFAULT_REGION },

  /* Uncomment the next line if you know exactly what Account and Region you
   * want to deploy the stack to. */
  env: { region: 'ap-southeast-2' }

  /* For more information, see https://docs.aws.amazon.com/cdk/latest/guide/environments.html */
});

new GlobalSubsXRegionEBRulesRegion1(app, 'GlobalSubsXRegionEBRulesRegion1', {
  eventBus: Stack2.eventBus,
  env: { region: 'us-west-2' }
});

new GlobalSubsXRegionEBRulesRegion2(app, 'GlobalSubsXRegionEBRulesRegion2', {
  eventBus: Stack1.eventBus,
  env: { region: 'ap-southeast-2' }
});