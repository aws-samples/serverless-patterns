# AWS EventBridge Pipes from DynamoDB Stream To IoT Core Topic via API Gateway AWS Integration

This project contains a sample AWS Cloud Development Kit (AWS CDK) template for deploying a DynamoDb Table with a Stream configured to an EventBridge Pipe. Items data tunneled through Pipe will target an API Gateway endpoint that uses AWS direct integration to publish the a message to a pre-configured IoT Core Topic with the item data.

![Architecture](assets/DDB%20-_%20EB%20Pipe%20-_%20API%20Gateway%20-_%20IoT%20Core%20Topic%20Pattern.svg)

Learn more about this pattern at Serverless Land Patterns: https://serverlessland.com/patterns/eventbridge-pipes-ddb-stream-apigateway-iot-core-cdk.

Important: this application uses various AWS services and there are costs associated with these services after the Free Tier usage - please see the [AWS Pricing page](https://aws.amazon.com/pricing/) for details. You are responsible for any AWS costs incurred. No warranty is implied in this example.

## Requirements

- [Create an AWS account](https://portal.aws.amazon.com/gp/aws/developer/registration/index.html) if you do not already have one and log in. The IAM user that you use must have sufficient permissions to make necessary AWS service calls and manage AWS resources.
- [AWS CLI](https://docs.aws.amazon.com/cli/latest/userguide/install-cliv2.html) installed and configured
- [Git Installed](https://git-scm.com/book/en/v2/Getting-Started-Installing-Git)
- [AWS CDK](https://docs.aws.amazon.com/cdk/latest/guide/cli.html) installed and configured

## Deployment Instructions

1. Create a new directory, navigate to that directory in a terminal and clone the GitHub repository:
   ```bash
   git clone https://github.com/aws-samples/serverless-patterns
   ```
2. Change directory to the pattern directory:
   ```bash
   cd serverless-patterns/eventbridge-pipes-ddb-stream-apigateway-iot-core-cdk/cdk
   ```
3. Install dependencies:
   ```bash
   npm install
   ```
4. Fill in the iot core Endpoint:

Follow the steps in the [inputs](#inputs) section to fetch your account iot core endpoint and fill it in the `cdk.ts` file

```typescript
#!/usr/bin/env node
const app = new cdk.App();

const IOT_EVENTS_TOPIC_NAME = "iot-test-topic";
const IOT_DATA_ENDPOINT = "{paste your endpoint here}"; // You must replace this with aws iot endpoint found in IotCore settings
.
.
.

new EventBridgePipesIotCoreStack(app, "EventBridgePipesIotCoreStack", {
  iotDataEndpoint: IOT_DATA_ENDPOINT,
  iotTopicName: IOT_EVENTS_TOPIC_NAME,
  .
  .
  .
});

```

4. From the command line, configure AWS CDK:
   ```bash
   cdk bootstrap ACCOUNT-NUMBER/REGION # e.g.
   cdk bootstrap 9999999999/us-east-1
   cdk bootstrap --profile test 9999999999/us-east-1
   ```
5. From the command line, use AWS CDK to deploy the AWS resources for the pattern as specified in the `lib/cdk-stack.ts` file:
   ```bash
   cdk deploy
   ```
6. Note: The AWS CDK deployment process will output the DynamoDB table name, the API endpoint and the IoT Core Topic name used for testing this project

## How it works

This pattern follows a _functionless_ approach to achieve a full-circle event propagation, and report the change back to the client.

The following resources will be provisioned:

- A DynamoDB Table that stores data and configured with a DDB Stream
- An EventBridge Pipe configured as a target for the DDB Stream
- A REST Api configured as a target for the EventBridge Pipe
- The REST Api configures a path `iot` with a POST request and an AWS Direct Service Integration to IoT Data
- An IoT Core Topic & IoT Core Endpoint to publish data to

IoT Core is an AWS service that covers a wide verity of use cases. One important feature that can be leveraged in serverless event driven architectures, is the scalable pub/sub topic based api.

NOTICE: the pattern doesn't use AWS Lambda at any stage to propagate the data change

**_Disclaimer:_** This pattern doesn't favor one architectural pattern over another. It is merely an example of using _functionless_ development with IoT Core

## Testing

To test this pattern you will need to use both the AWS Console and the AWS CLI.

### Inputs

Every AWS account has an IoT Core Endpoint associated with it. You can find your endpoint as follows:

1. Open the AWS IoT Console in a browser window.
2. Click on `Settings`
3. Under `Device data endpoint` copy the `Endpoint`
4. Navigate to the `bin/cdk.ts` file and paste that string for the value of the `IOT_DATA_ENDPOINT`

### AWS Console Part

1. Open the AWS IoT Console in the second browser window.
2. In the AWS IoT Core Console, in the `Test` section (left-side pane), select the `MQTT test client`.
3. Under the `Subscribe to a topic` subscribe to `iot-test-topic` topic.
4. Open a terminal window and run the following DynamoDB CLI put command to put an item in the DynamoDB table. Before running the command you must edit the {DynamoDBTableName} placeholder with the name of the deployed DynamoDB table. This is printed in the stack outputs on the console by `cdk deploy` command. Note that this requires AWS CLI v2.

```bash
aws dynamodb put-item \
--table-name "DYNAMODB_TABLE_NAME" \
--item {dynamodb item} \

# Example
aws dynamodb put-item \
    --table-name iot-events-table \
    --item pk={S="MESSAGE#1234"},sk={S="CHANNEL#1231"},messageId={S="1234"}
```

5. Switch back to the `MQTT test client` and check if you got the stream item you used in the CLI call. For the example above you should see the following output in the `MQTT test client` window, on the `iot-test-topic` topic:

```json
{
  "eventID": "5017fda64d0f565da62a8d92f462969a",
  "eventName": "INSERT",
  "eventVersion": "1.1",
  "eventSource": "aws:dynamodb",
  "awsRegion": "us-east-1",
  "dynamodb": {
    "ApproximateCreationDateTime": 1682398613,
    "Keys": {
      "sk": {
        "S": "CHANNEL#1231"
      },
      "pk": {
        "S": "MESSAGE#1234"
      }
    },
    "NewImage": {
      "sk": {
        "S": "CHANNEL#1231"
      },
      "messageId": {
        "S": "1234"
      },
      "pk": {
        "S": "MESSAGE#1234"
      }
    },
    "SequenceNumber": "100000000033474848853",
    "SizeBytes": 69,
    "StreamViewType": "NEW_AND_OLD_IMAGES"
  },
  "eventSourceARN": "arn:aws:dynamodb:us-east-1:{{account-number}}:table/iot-events-table/stream/2023-04-25T04:46:13.030"
}
```

## Cleanup

1. Delete the stack
   ```bash
   cdk destroy
   ```

## Resources

1. [AWS IoT HTTPS](https://docs.aws.amazon.com/iot/latest/developerguide/http.html)
2. [AWS Solutions Constructs for API Gateway integration to IoT Core](https://github.com/awslabs/aws-solutions-constructs/tree/58e726ff2050a4d6ff4734a6b556e1f81d97e9aa/source/patterns/%40aws-solutions-constructs/aws-apigateway-iot)

---

Copyright 2023 Amazon.com, Inc. or its affiliates. All Rights Reserved.

SPDX-License-Identifier: MIT-0
