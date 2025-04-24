#!/usr/bin/env node
import * as cdk from "aws-cdk-lib";
import { ApigwSecretsmanagerApikeyStack } from "../lib/apigw-secretsmanager-apikey-stack";

const app = new cdk.App();
// amazonq-ignore-next-line
new ApigwSecretsmanagerApikeyStack(app, "ApigwSecretsmanagerApikeyCdkStack", {
  env: {
    account: process.env.CDK_DEFAULT_ACCOUNT,
    region: process.env.CDK_DEFAULT_REGION,
  },
});
