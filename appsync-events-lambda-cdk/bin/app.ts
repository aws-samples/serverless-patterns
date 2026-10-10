#!/usr/bin/env node
import * as cdk from 'aws-cdk-lib';
import { AppsyncEventsLambdaStack } from '../lib/appsync-events-lambda-stack';
const app = new cdk.App();
new AppsyncEventsLambdaStack(app, 'AppsyncEventsLambdaStack');
