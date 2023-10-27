#!/usr/bin/env node
import 'source-map-support/register';
import * as cdk from 'aws-cdk-lib';
import { ApiGwHttpLambdaDocumentDbStack } from '../lib/apigw-http-lambda-documentdb-stack';

const app = new cdk.App();

new ApiGwHttpLambdaDocumentDbStack(app, 'ApiGwHttpLambdaDocumentDbStack');