#!/usr/bin/env node
import * as cdk from 'aws-cdk-lib';
import { CentralApiStack } from '../lib/central-api-stack';
import { ServiceAStack } from '../lib/service-a-stack';
import { ServiceBStack } from '../lib/service-b-stack';
import config from '../config.json';
import { CentralApiResourcesStack } from '../lib/central-api-resources-stack';
import { Tags } from 'aws-cdk-lib';

const app = new cdk.App();
const centralApiAccount = config.stacks.centralAPI.account || process.env.CENTRAL_API_ACCOUNT_NUMBER;
const serviceAAccount = config.stacks.serviceA.account || process.env.SERVICE_A_ACCOUNT_NUMBER;
const serviceBAccount = config.stacks.serviceB.account || process.env.SERVICE_B_ACCOUNT_NUMBER;
const region = config.region || process.env.REGION;

// Stop execution if the account numbers are not defined
if (!centralApiAccount || !serviceAAccount || !serviceBAccount || !region) {
  throw new Error('Account numbers and/or region for stacks are not defined. Define them in the config file or as environment variables as mentioned in the README');
}

const centralApi = new CentralApiStack(app, 'CentralApiStack', {
  cidr: config.cidrs.centralAPI,
  accountsForIEPShare: [serviceAAccount, serviceBAccount],
  stage: config.stacks.centralAPI.stage,
  apiDescription: config.stacks.centralAPI.apiDescription,
  iepParam: config.params.interfaceEp.param,
  iepParamId: config.params.interfaceEp.paramId,
  env: {
    account: centralApiAccount,
    region: region,
  },
});
const centralApiResources = new CentralApiResourcesStack(app, 'CentralApiResourcesStack', {
  svcAUriParam: config.params.svcAUri.param,
  svcAUriParamId: config.params.svcAUri.paramId,
  svcBUriParam: config.params.svcBUri.param,
  svcBUriParamId: config.params.svcBUri.paramId,
  svcAAccount: serviceAAccount,
  svcBAccount: serviceBAccount,
  stage: config.stacks.centralAPI.stage,
  env: {
    account: centralApiAccount,
    region: region,
  },
});
const serviceA = new ServiceAStack(app, 'ServiceAStack', {
  cidr: config.cidrs.serviceA,
  iepParam: config.params.interfaceEp.param,
  iepParamId: config.params.interfaceEp.paramId,
  uriParam: config.params.svcAUri.param,
  uriParamId: config.params.svcAUri.paramId,
  centralApiAccount: centralApiAccount,
  stage: config.stacks.serviceA.stage,
  apiDescription: config.stacks.serviceA.apiDescription,
  env: {
    account: serviceAAccount,
    region: region,
  },
});
const serviceB = new ServiceBStack(app, 'ServiceBStack', {
  cidr: config.cidrs.serviceB,
  iepParam: config.params.interfaceEp.param,
  iepParamId: config.params.interfaceEp.paramId,
  uriParam: config.params.svcBUri.param,
  uriParamId: config.params.svcBUri.paramId,
  centralApiAccount: centralApiAccount,
  stage: config.stacks.serviceB.stage,
  apiDescription: config.stacks.serviceB.apiDescription,
  env: {
    account: serviceBAccount,
    region: region,
  },
});

// Setting tags for all the taggable resoruces in the stacks
const tags = config.tags;
tags.forEach((tag) => {
  Tags.of(centralApi).add(tag.key, tag.value);
  Tags.of(centralApiResources).add(tag.key, tag.value);
  Tags.of(serviceA).add(tag.key, tag.value);
  Tags.of(serviceB).add(tag.key, tag.value);
});


