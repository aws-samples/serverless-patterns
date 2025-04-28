#!/usr/bin/env node
import * as cdk from "aws-cdk-lib";
import { ParentStack } from "../lib/parent-stack";

const app = new cdk.App();

new ParentStack(app, "ApigwLambdaPowertoolsOpenapiStack", {
  stageName: "dev",
  description: "REST API Gateway with Lambda integration using openapi spec",
});
