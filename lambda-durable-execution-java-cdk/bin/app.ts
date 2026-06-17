#!/usr/bin/env node
import "source-map-support/register";
import * as cdk from "aws-cdk-lib";
import { LambdaDurableExecutionJavaStack } from "../lib/lambda-durable-execution-java-stack";

const app = new cdk.App();
new LambdaDurableExecutionJavaStack(app, "LambdaDurableExecutionJavaStack");
