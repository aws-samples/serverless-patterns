#!/usr/bin/env node
import 'source-map-support/register';
import * as cdk from 'aws-cdk-lib';
import { LambdaSNSFiltersLambdaStack } from '../lib/lambda-sns-filters-lambda';

const app = new cdk.App();
new LambdaSNSFiltersLambdaStack(app, 'LambdaSNSFiltersLambdaStack', {});
