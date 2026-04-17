#!/usr/bin/env node
import "source-map-support/register";
import * as cdk from "aws-cdk-lib";
import { EventBridgeSqsFairQueueLambdaStack } from "../lib/eventbridge-sqs-fair-queue-lambda-stack";

const app = new cdk.App();
new EventBridgeSqsFairQueueLambdaStack(
  app,
  "EventBridgeSqsFairQueueLambdaStack"
);
