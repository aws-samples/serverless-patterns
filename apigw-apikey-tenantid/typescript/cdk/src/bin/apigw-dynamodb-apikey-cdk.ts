#!/usr/bin/env node
import * as cdk from "aws-cdk-lib";
import { ApigwUsagePlanApiKeyStack } from "../lib/apigw-usageplan-apikey-stack";
import { ApigwDynamodbApikeyStack } from "../lib/apigw-dynamodb-apikey-stack";

const app = new cdk.App();

// Stack 1: Creates the Usage Plan and API Key (optional, deploy independently)
new ApigwUsagePlanApiKeyStack(app, "ApigwUsagePlanApiKeyCdkStack", {
  env: {
    account: process.env.CDK_DEFAULT_ACCOUNT,
    region: process.env.CDK_DEFAULT_REGION,
  },
});

// Stack 2: Creates the API Gateway, Lambda Authorizer, DynamoDB, and Cognito (deploy independently)
// To associate with an existing usage plan, pass the usage plan ID via context:
//   cdk deploy ApigwDynamodbApikeyCdkStack -c usagePlanId=<USAGE_PLAN_ID>
new ApigwDynamodbApikeyStack(app, "ApigwDynamodbApikeyCdkStack", {
  env: {
    account: process.env.CDK_DEFAULT_ACCOUNT,
    region: process.env.CDK_DEFAULT_REGION,
  },
});
