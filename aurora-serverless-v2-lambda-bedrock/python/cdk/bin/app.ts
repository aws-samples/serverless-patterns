#!/usr/bin/env node
import "source-map-support/register";
import * as cdk from "aws-cdk-lib";
import { AuroraServerlessV2LambdaBedrockStack } from "../lib/aurora-serverless-v2-lambda-bedrock-stack";

const app = new cdk.App();
new AuroraServerlessV2LambdaBedrockStack(
  app,
  "AuroraServerlessV2LambdaBedrockStack",
  {
    env: {
      account: process.env.CDK_DEFAULT_ACCOUNT,
      region: process.env.CDK_DEFAULT_REGION,
    },
  }
);
