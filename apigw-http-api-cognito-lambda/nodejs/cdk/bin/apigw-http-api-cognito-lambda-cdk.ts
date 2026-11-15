#!/usr/bin/env node
import 'source-map-support/register';
import * as cdk from 'aws-cdk-lib';
import { HttpApiCognitoLambdaStack } from '../lib/http-api-cognito-lambda-stack';

const app = new cdk.App();
new HttpApiCognitoLambdaStack(app, 'HttpApiCognitoLambdaStack', { });