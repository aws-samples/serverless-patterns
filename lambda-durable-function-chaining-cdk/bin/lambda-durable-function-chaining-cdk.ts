#!/usr/bin/env node
import * as cdk from "aws-cdk-lib/core";
import { LambdaDurableFunctionChainingCdkStack } from "../lib/lambda-durable-function-chaining-cdk-stack";

const app = new cdk.App();
new LambdaDurableFunctionChainingCdkStack(app, "LambdaDurableFunctionChainingCdkStack", {
  env: {
    account: process.env.CDK_DEFAULT_ACCOUNT,
    region: process.env.CDK_DEFAULT_REGION,
  },
});
