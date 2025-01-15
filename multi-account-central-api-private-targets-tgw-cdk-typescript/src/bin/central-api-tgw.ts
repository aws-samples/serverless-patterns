#!/usr/bin/env node
import { App, Tags } from 'aws-cdk-lib';
import { CentralApiStack } from '../lib/central-api-stack';
import { ServiceAStack } from '../lib/service-a-stack';
import { ServiceBStack } from '../lib/service-b-stack';
import { TgwStack } from '../lib/tgw-stack';
import config from '../config.json';

const app = new App();
const centralApiAccount =
  config.stacks.centralAPI.account || process.env.CENTRAL_API_ACCOUNT_NUMBER;
const serviceAAccount =
  config.stacks.serviceA.account || process.env.SERVICE_A_ACCOUNT_NUMBER;
const serviceBAccount =
  config.stacks.serviceB.account || process.env.SERVICE_B_ACCOUNT_NUMBER;
const tgwAccount = config.stacks.tgw.account || process.env.TGW_ACCOUNT_NUMBER;
const region = config.region || process.env.REGION;

// Stop execution if the account numbers are not defined
if (!centralApiAccount || !serviceAAccount || !serviceBAccount || !tgwAccount || !region) {
  throw new Error(
    'Account numbers and/or region for stacks are not defined. Define them in the config file or as environment variables as mentioned in the README'
  );
}

const centralAPIStack = new CentralApiStack(app, 'CentralApiStack', {
  svcAAccount: serviceAAccount,
  svcAParamId: config.params.svcANLB.paramId,
  svcAParamName: config.params.svcANLB.param,
  svcBAccount: serviceBAccount,
  svcBParamId: config.params.svcBNLB.paramId,
  svcBParamName: config.params.svcBNLB.param,
  tgwParamId: config.params.tgw.paramId,
  tgwParamName: config.params.tgw.param,
  tgwAccount: tgwAccount,
  svcACidr: config.cidrs.serviceA,
  svcBCidr: config.cidrs.serviceB,
  centralApiCidr: config.cidrs.centralAPI,
  stage: config.stacks.centralAPI.stage,
  apiDescription: config.stacks.centralAPI.apiDescription,
  tags: convertTagArrayToJSONObj(config.tags),
  env: { account: centralApiAccount, region: region },
});
const serviceAStack = new ServiceAStack(app, 'ServiceAStack', {
  accountsForNLBShare: [centralApiAccount],
  svcACidr: config.cidrs.serviceA,
  svcBCidr: config.cidrs.serviceB,
  centralApiCidr: config.cidrs.centralAPI,
  tgwParamId: config.params.tgw.paramId,
  tgwParamName: config.params.tgw.param,
  tgwAccount: tgwAccount,
  svcANLBParamId: config.params.svcANLB.paramId,
  svcANLBParamName: config.params.svcANLB.param,
  env: { account: serviceAAccount, region: region },
});
const serviceBStack = new ServiceBStack(app, 'ServiceBStack', {
  accountsForNLBShare: [centralApiAccount],
  svcACidr: config.cidrs.serviceA,
  svcBCidr: config.cidrs.serviceB,
  centralApiCidr: config.cidrs.centralAPI,
  tgwParamId: config.params.tgw.paramId,
  tgwParamName: config.params.tgw.param,
  tgwAccount: tgwAccount,
  svcBNLBParamId: config.params.svcBNLB.paramId,
  svcBNLBParamName: config.params.svcBNLB.param,
  env: { account: serviceBAccount, region: region },
});
const tgwStack = new TgwStack(app, 'TgwStack', {
  accountsToShare: [
    serviceAAccount,
    serviceBAccount,
    centralApiAccount,
  ],
  tgwParamId: config.params.tgw.paramId,
  tgwParamName: config.params.tgw.param,
  env: { account: tgwAccount, region: region },
});

// Setting tags for all the taggable resoruces in the stacks
const tags = config.tags;
tags.forEach((tag) => {
  Tags.of(centralAPIStack).add(tag.key, tag.value);
  Tags.of(tgwStack).add(tag.key, tag.value);
  Tags.of(serviceAStack).add(tag.key, tag.value);
  Tags.of(serviceBStack).add(tag.key, tag.value);
});

// Function to convert tags area to tags JSON Object
function convertTagArrayToJSONObj(tags: {key: string, value: string}[]) {
  const tagsJSON: {[key: string]: string} = {};
  tags.forEach((tag) => {
    tagsJSON[tag.key] = tag.value;
  });
  return tagsJSON;
}