#!/usr/bin/env node
import * as cdk from "aws-cdk-lib";
import { ApigwDynamodbApikeyStack } from "../lib/apigw-dynamodb-apikey-stack";

const app = new cdk.App();
new ApigwDynamodbApikeyStack(app, "ApigwDynamodbApikeyCdkStack", {
  env: {
    account: process.env.CDK_DEFAULT_ACCOUNT,
    region: process.env.CDK_DEFAULT_REGION,
  },
});
