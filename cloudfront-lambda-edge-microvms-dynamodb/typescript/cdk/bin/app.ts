#!/usr/bin/env node
import * as cdk from "aws-cdk-lib";
import { MicrovmEdgeSessionsStack } from "../lib/microvm-edge-sessions-stack.js";

const app = new cdk.App();

// Lambda@Edge functions can only be created in us-east-1, so the whole stack lives there.
new MicrovmEdgeSessionsStack(app, "MicrovmEdgeSessionsStack", {
  env: { region: "us-east-1" },
  description: "Session routing to per-session AWS Lambda MicroVMs via CloudFront, Lambda@Edge and DynamoDB.",
});
