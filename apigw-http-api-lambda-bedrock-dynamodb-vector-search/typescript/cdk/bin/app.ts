#!/usr/bin/env node
import * as cdk from "aws-cdk-lib";
import { VectorSearchStack } from "../lib/vector-search-stack";

const app = new cdk.App();

new VectorSearchStack(app, "DynamoDbVectorSearchPatternStack", {
  description: "Serverless semantic search with API Gateway, Lambda, Bedrock, and DynamoDB",
});
