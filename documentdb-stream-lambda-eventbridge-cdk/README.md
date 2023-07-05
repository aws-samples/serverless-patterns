# Amazon DocumentDB Stream To EventBridge via AWS Lambda Integration

This project contains a sample AWS Cloud Development Kit (AWS CDK) template for configuring and deploying a CDC Stream (Similar to DynamoDB Stream) for Amazon DocumentDB using AWS Lambda and EventBridge. The stream will processes changes and send them to an EventBridge Bus for further processing.

Learn more about this pattern at Serverless Land Patterns: https://serverlessland.com/patterns/documentdb-stream-lambda-eventbridge-cdk.

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
   cd serverless-patterns/documentdb-stream-lambda-eventbridge-cdk/cdk
   ```
3. Install dependencies:
   ```bash
   npm install
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
6. Note: The AWS CDK deployment process will output the Amazon DocumentDB name, the Lambda ARN used as a CDC Stream, the EventBridge Bus used for receiving the changes from the stream

## How it works

This pattern will use an already existing Amazon DocumentDB Database and attach a lambda function that will stream any change detected to the items in the aforementioned database.

The following resources will be provisioned:

- A Lambda Function that process the changes from an already existing Amazon DocumentDB Database and sends them to an EventBridge Bus
- An AWS CDK Custom Resource Lambda Function that enables the CDC of Amazon DocumentDB onto the stream Lambda Function
- A VPC Endpoint for the AWS Lambda Service (This is crucial to enabling the Lambda Event Source Mapping off of the Amazon DocumentDB Database)
- A VPC Endpoint for the AWS Secret Manager Service (This is crucial to allow the Lambda Event Source Mapping off of the Amazon DocumentDB Database)
- An EventBridge Bus that will receive changes from the Lambda and publish them to an EventBridge Rule
- An EventBridge Rule that receive the changes for bus and publish them to given targets for further processing
- A Lambda Function that acts as a target for the EventBridge Rule and further process the changes

## Testing

To test this pattern you will need to use both the AWS Console and the AWS CLI.

### Inputs

This pattern attaches a CDC Lambda Stream to an already existing Amazon DocumentDB Stream. So, it requires the following:

1. Amazon DocumentDB Cluster ARN
2. AWS Secret Manager ARN for the Database
3. AWS VPC ID where the Amazon DocumentDB Cluster is provisioned (if not provided will use default VPC)
4. AWS Security Group ID for the Amazon DocumentDB Cluster
5. Amazon DocumentDB Database Name
6. Amazon DocumentDB Collection Name

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

1. [Get Started with Amazon DocumentDB](https://docs.aws.amazon.com/documentdb/latest/developerguide/get-started-guide.html)
2. [Enabling Amazon DocumentDB Change Streams](https://docs.aws.amazon.com/documentdb/latest/developerguide/change_streams.html#change_streams-enabling)
3. [Tutorial: Using AWS Lambda with Amazon DocumentDB Streams](https://docs.aws.amazon.com/lambda/latest/dg/with-documentdb-tutorial.html)

---

Copyright 2023 Amazon.com, Inc. or its affiliates. All Rights Reserved.

SPDX-License-Identifier: MIT-0
