#!/usr/bin/env node
import "source-map-support/register";
import * as cdk from "aws-cdk-lib";
import { LambdaStrandsAgentBedrockStack } from "../lib/lambda-strands-agent-bedrock-stack";

const app = new cdk.App();
new LambdaStrandsAgentBedrockStack(app, "LambdaStrandsAgentBedrockStack", {
  env: {
    account: process.env.CDK_DEFAULT_ACCOUNT,
    region: process.env.CDK_DEFAULT_REGION,
  },
});
