#!/usr/bin/env node
import * as cdk from "aws-cdk-lib";
import { PatternStack } from "../lib/pattern-stack";

const app = new cdk.App();
// amazonq-ignore-next-line
new PatternStack(app, "PatternStack", {
  env: {
    account: process.env.CDK_DEFAULT_ACCOUNT,
    region: process.env.CDK_DEFAULT_REGION,
  },
});
