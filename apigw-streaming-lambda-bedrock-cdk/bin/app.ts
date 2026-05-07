#!/usr/bin/env node
import "source-map-support/register";
import * as cdk from "aws-cdk-lib";
import { ApigwStreamingLambdaBedrockStack } from "../lib/apigw-streaming-lambda-bedrock-stack";

const app = new cdk.App();
new ApigwStreamingLambdaBedrockStack(app, "ApigwStreamingLambdaBedrockStack");
