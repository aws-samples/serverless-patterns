#!/usr/bin/env node
import * as cdk from 'aws-cdk-lib';
import { LambdaElasticacheIntegrationpatternCdkStack } from '../lib/lambda-elasticache-integrationpattern-cdk-stack';

const app = new cdk.App();
new LambdaElasticacheIntegrationpatternCdkStack(app, 'LambdaElasticacheIntegrationpatternCdkStack', {
    /* If you don't specify 'env', this stack will be environment-agnostic.
   * Account/Region-dependent features and context lookups will not work,
   * but a single synthesized template can be deployed anywhere. */

    /* Currently we are using account and region from CLI configuration. Comment if
    you are using other options*/
    env: {
        account: process.env.CDK_DEFAULT_ACCOUNT, 
        region: process.env.CDK_DEFAULT_REGION
    }
    // Uncomment the next line if you know exactly what Account and Region you  want to deploy the stack to.
    // env: { account: '123456789012', region: 'us-east-1' }
    // For more information, see https://docs.aws.amazon.com/cdk/latest/guide/environments.html

});
