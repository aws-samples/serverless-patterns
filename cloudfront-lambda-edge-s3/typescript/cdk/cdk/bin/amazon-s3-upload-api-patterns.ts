#!/usr/bin/env node
import "source-map-support/register";
import * as cdk from "aws-cdk-lib";
import { AmazonS3UploadApiPatternsStack } from "../lib/amazon-s3-upload-api-patterns-stack";

const app = new cdk.App();
new AmazonS3UploadApiPatternsStack(app, "AmazonS3UploadApiPatternsStack", {
  env: { account: process.env.CDK_DEFAULT_ACCOUNT, region: "us-east-1" },
});
