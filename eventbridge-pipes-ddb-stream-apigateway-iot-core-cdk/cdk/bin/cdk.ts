#!/usr/bin/env node
import 'source-map-support/register';
import * as cdk from 'aws-cdk-lib';
import { EventBridgePipesIotCoreStack } from '../lib/cdk-stack';

const app = new cdk.App();

const IOT_EVENTS_TOPIC_NAME = 'iot-test-topic';
const IOT_DATA_ENDPOINT = '{paste your endpoint here}'; // You must replace this with aws iot endpoint found in IotCore settings
const DYNAMODB_TABLE_NAME = 'iot-events-table';
const REST_API_NAME = 'iot-rest-api';
const REST_API_RESOURCE = 'iot';
const PIPE_NAME = 'iot-pipe';

new EventBridgePipesIotCoreStack(app, 'EventBridgePipesIotCoreStack', {
  iotTopicName: IOT_EVENTS_TOPIC_NAME,
  iotDataEndpoint: IOT_DATA_ENDPOINT,
  dynamoDbTableName: DYNAMODB_TABLE_NAME,
  apiGateway: {
    restApiName: REST_API_NAME,
    apiResource: REST_API_RESOURCE,
  },
  pipeName: PIPE_NAME,
  /* If you don't specify 'env', this stack will be environment-agnostic.
   * Account/Region-dependent features and context lookups will not work,
   * but a single synthesized template can be deployed anywhere. */
  /* Uncomment the next line to specialize this stack for the AWS Account
   * and Region that are implied by the current CLI configuration. */
  // env: { account: process.env.CDK_DEFAULT_ACCOUNT, region: process.env.CDK_DEFAULT_REGION },
  /* Uncomment the next line if you know exactly what Account and Region you
   * want to deploy the stack to. */
  // env: { account: '123456789012', region: 'us-east-1' },
  /* For more information, see https://docs.aws.amazon.com/cdk/latest/guide/environments.html */
});
