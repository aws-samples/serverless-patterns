#!/usr/bin/env node
import * as cdk from 'aws-cdk-lib';
import { CdkCognitoApigatewayLambdaStack } from '../lib/cdk-cognito-apigateway-lambda-stack';

const app = new cdk.App();
new CdkCognitoApigatewayLambdaStack(app, 'CdkCognitoApigatewayLambdaStack', {
    env: {
        region: process.env.AWS_DEFAULT_REGION ?? 'us-east-2'
    }
});
