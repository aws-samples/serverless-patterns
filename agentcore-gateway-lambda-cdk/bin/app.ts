#!/usr/bin/env node
import "source-map-support/register";
import * as cdk from "aws-cdk-lib";
import { AgentcoreGatewayLambdaStack } from "../lib/agentcore-gateway-lambda-stack";

const app = new cdk.App();
new AgentcoreGatewayLambdaStack(app, "AgentcoreGatewayLambdaStack", {
  env: {
    account: process.env.CDK_DEFAULT_ACCOUNT,
    region: process.env.CDK_DEFAULT_REGION,
  },
});
