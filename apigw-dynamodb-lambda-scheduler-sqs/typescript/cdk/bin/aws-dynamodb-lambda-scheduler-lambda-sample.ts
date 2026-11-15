#!/usr/bin/env node
import * as cdk from 'aws-cdk-lib';
import 'source-map-support/register';
import { AwsDynamodbLambdaSchedulerLambdaSampleStack } from '../lib/aws-dynamodb-lambda-scheduler-lambda-sample-stack';

const app = new cdk.App();
new AwsDynamodbLambdaSchedulerLambdaSampleStack(app, 'AwsDynamodbLambdaSchedulerLambdaSampleStack', {
  });