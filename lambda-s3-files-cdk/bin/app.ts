#!/usr/bin/env node
import "source-map-support/register";
import * as cdk from "aws-cdk-lib";
import { LambdaS3FilesStack } from "../lib/lambda-s3-files-stack";

const app = new cdk.App();
new LambdaS3FilesStack(app, "LambdaS3FilesStack");
