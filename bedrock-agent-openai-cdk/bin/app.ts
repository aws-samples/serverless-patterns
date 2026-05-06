#!/usr/bin/env node
import "source-map-support/register";
import * as cdk from "aws-cdk-lib";
import { BedrockAgentOpenaiStack } from "../lib/bedrock-agent-openai-stack";

const app = new cdk.App();
new BedrockAgentOpenaiStack(app, "BedrockAgentOpenaiStack");
