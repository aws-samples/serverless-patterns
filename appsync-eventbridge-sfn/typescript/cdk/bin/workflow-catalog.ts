#!/usr/bin/env node
import * as cdk from "aws-cdk-lib";
import { WorkflowCatalogStack } from "../lib/workflow-catalog-stack";

const app = new cdk.App();

const stack = new WorkflowCatalogStack(app, "WorkflowCatalogStack", {
  description:
    "Self-service workflow catalog: a GraphQL front door for Step Functions workflows, built with AppSync, EventBridge, Lambda, and DynamoDB",
  env: {
    account: process.env.CDK_DEFAULT_ACCOUNT,
    region: process.env.CDK_DEFAULT_REGION,
  },
});

cdk.Tags.of(stack).add("Pattern", "SelfServiceWorkflowCatalog");
