#!/usr/bin/env node
import "source-map-support/register";
import * as cdk from "aws-cdk-lib";
import { EventBridgePipesIotCoreStack } from "../lib/cdk-stack";

const app = new cdk.App();

const IOT_EVENTS_TOPIC_NAME = "iot-test-topic";
const IOT_DATA_ENDPOINT = "{paste your endpoint here}"; // You must replace this with aws iot endpoint found in IotCore settings
const DYNAMODB_TABLE_NAME = "iot-events-table";
const REST_API_NAME = "iot-rest-api";
const REST_API_RESOURCE = "iot";
const PIPE_NAME = "iot-pipe";

new EventBridgePipesIotCoreStack(app, "EventBridgePipesIotCoreStack", {
  iotTopicName: IOT_EVENTS_TOPIC_NAME,
  iotDataEndpoint: IOT_DATA_ENDPOINT,
  dynamoDbTableName: DYNAMODB_TABLE_NAME,
  apiGateway: {
    restApiName: REST_API_NAME,
    iotResourcePath: REST_API_RESOURCE,
  },
  pipeName: PIPE_NAME,
});
