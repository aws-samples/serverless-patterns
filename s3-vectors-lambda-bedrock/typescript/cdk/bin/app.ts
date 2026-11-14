#!/usr/bin/env node
import "source-map-support/register";
import * as cdk from "aws-cdk-lib";
import { S3VectorsLambdaBedrockStack } from "../lib/s3-vectors-lambda-bedrock-stack";

const app = new cdk.App();
new S3VectorsLambdaBedrockStack(app, "S3VectorsLambdaBedrockStack");
