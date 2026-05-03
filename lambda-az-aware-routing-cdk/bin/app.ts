#!/usr/bin/env node
import "source-map-support/register";
import * as cdk from "aws-cdk-lib";
import { LambdaAzAwareRoutingStack } from "../lib/lambda-az-aware-routing-stack";

const app = new cdk.App();
new LambdaAzAwareRoutingStack(app, "LambdaAzAwareRoutingStack", {
  env: {
    account: process.env.CDK_DEFAULT_ACCOUNT,
    region: process.env.CDK_DEFAULT_REGION,
  },
});
