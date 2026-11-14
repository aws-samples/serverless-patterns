#!/usr/bin/env node
import * as cdk from "aws-cdk-lib";
import { PatternStack } from "../lib/pattern-stack";

const app = new cdk.App();
new PatternStack(app, "S3LambdaTextractBedrockDurableStack", {
  env: {
    account: process.env.CDK_DEFAULT_ACCOUNT,
    region: process.env.CDK_DEFAULT_REGION,
  },
});
