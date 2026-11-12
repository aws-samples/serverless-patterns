#!/usr/bin/env node
import "source-map-support/register";
import * as cdk from "aws-cdk-lib";
import { LambdaManagedInstancesBedrockStack } from "../lib/lambda-managed-instances-bedrock-stack";

const app = new cdk.App();
new LambdaManagedInstancesBedrockStack(app, "LambdaManagedInstancesBedrockStack");
