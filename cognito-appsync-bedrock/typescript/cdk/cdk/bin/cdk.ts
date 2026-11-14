#!/usr/bin/env node
import * as cdk from "aws-cdk-lib";
import { CdkStack } from "../lib/cdk-stack";

const app = new cdk.App();
new CdkStack(app, "AppsyncBedrockCognitoStack", {
  description:
    "AWS CDK Stack for AppSync with Bedrock integration using Cognito User Pool authenticator.",
});
