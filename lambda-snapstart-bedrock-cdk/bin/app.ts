#!/usr/bin/env node
import "source-map-support/register";
import * as cdk from "aws-cdk-lib";
import { LambdaSnapstartBedrockStack } from "../lib/lambda-snapstart-bedrock-stack";

const app = new cdk.App();
new LambdaSnapstartBedrockStack(app, "LambdaSnapstartBedrockStack");
