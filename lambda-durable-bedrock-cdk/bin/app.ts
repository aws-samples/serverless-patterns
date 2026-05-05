#!/usr/bin/env node
import "source-map-support/register";
import * as cdk from "aws-cdk-lib";
import { LambdaDurableBedrockStack } from "../lib/lambda-durable-bedrock-stack";

const app = new cdk.App();
new LambdaDurableBedrockStack(app, "LambdaDurableBedrockStack");
