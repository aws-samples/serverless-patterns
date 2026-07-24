#!/usr/bin/env node
import "source-map-support/register";
import * as cdk from "aws-cdk-lib";
import { SfnBedrockInvokemodelStack } from "../lib/sfn-bedrock-invokemodel-stack";

const app = new cdk.App();
new SfnBedrockInvokemodelStack(app, "SfnBedrockInvokemodelStack");
