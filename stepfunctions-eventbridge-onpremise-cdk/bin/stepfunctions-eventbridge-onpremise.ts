#!/usr/bin/env node
import * as cdk from 'aws-cdk-lib';
import { StateMachineStack } from "../lib/state-machine-stack";

const app = new cdk.App();

// Reading config from cdk.json, update config with your own
const config = app.node.tryGetContext('configuration');

new StateMachineStack(app, 'StateMachineToOnPremStack', {
  env: {
    account: process.env.CDK_DEFAULT_ACCOUNT,
    region: process.env.CDK_DEFAULT_REGION
  },
  vpcId: config.vpcId,
  onPremiseCidr: config.onPremiseCidr,
  apiDomainName: config.apiDomainName,
  apiKeySecretArn: config.apiKeySecretArn
});