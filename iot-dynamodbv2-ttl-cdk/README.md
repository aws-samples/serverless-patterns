# AWS IoT Core to Amazon DynamoDB

This pattern contains a sample AWS CDK stack to create an IoT Rule with a DynamoDB V2 action. 

![iot-dynambodbv2](./iot-dynamodbv2.png)

This pattern uses the [DynamoDBv2](https://docs.aws.amazon.com/iot/latest/developerguide/dynamodb-v2-rule-action.html) action to write all or parts of an MQTT message to an Amazon DynamoDB table. Each attribute in the payload is written to a separate column in the DynamoDB table. The SQL statement calculates a [Time to live (TTL)](https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/TTL.html) and puts into the payload when writing to the table.

Learn more about this pattern at Serverless Land Patterns: https://serverlessland.com/patterns/iot-dynamodbv2-ttl-cdk

Important: this application uses various AWS services and there are costs associated with these services after the Free Tier usage - please see the [AWS Pricing page](https://aws.amazon.com/pricing/) for details. You are responsible for any AWS costs incurred. No warranty is implied in this example.

## Requirements

* [Create an AWS account](https://portal.aws.amazon.com/gp/aws/developer/registration/index.html) if you do not already have one and log in. The IAM user that you use must have sufficient permissions to make necessary AWS service calls and manage AWS resources.
* [AWS CLI](https://docs.aws.amazon.com/cli/latest/userguide/install-cliv2.html) installed and configured
* [Git Installed](https://git-scm.com/book/en/v2/Getting-Started-Installing-Git)
* [Node and NPM](https://nodejs.org/en/download/) installed
* [AWS Cloud Development Kit](https://docs.aws.amazon.com/cdk/latest/guide/cli.html) (AWS CDK) installed

## Deployment Instructions

1. Clone the project to your local working directory

   ```sh
   git clone https://github.com/aws-samples/serverless-patterns/ 
   ```

2. Change the working directory to this pattern's directory

   ```sh
   cd serverless-patterns/iot-dynamodbv2-ttl-cdk
   ```
3. Set up the stack in your AWS account and region. 
- Change the working directory to the stack 

   ```sh
   cd iot-ddbv2
   ```
- Deploy the stack to your default AWS account and region. 

   ```sh
   cdk deploy
   ```
## How it works

The CDK app deploys the resources and the IAM permissions required to run the application. 
Review the [README](./iot-ddbv2/README.md) (the `Notes` section specially) in the `iot-ddbv2` folder for additional information.

## Testing

You can test the pattern using AWS Console.

### Using AWS Console

1. To simplify the testing process - use two browser windows side-by-side.
2. Log into the AWS Console, browse to Amazon DynamoDB in of the browser windows
3. Navigate to the `Explore items` in DynamoDB console, and select the table created by the CDK stack. The name used for the table is specified in `config.json` file, and the default name is `iotDynamoDBTable`.
4. Open the AWS IoT Console in the second browser window.
7. In the AWS IoT Core Console, in the `Test` section (left-side pane), select the `MQTT test client`. 
8. First under the `Subscribe to a topic` subscribe to `#` topic.
9. Then under `Publish to a topic`, in the Topic filter field enter this: `dt/` (do not miss the slash after the dt), type the following custom message:

   ```sh
   {
      "macId" : "AABBCCDDEEFF",
      "timestamp": 1660581788000,
      "temperature" : 63.25,
      "humidity" : 95.11
   }
   ```
Use a site such as [Epoch Converter](https://www.epochconverter.com/) to UTC timestamp in milliseconds and update the value to reflect the time when you are testing.
Then click the `Publish` button.
`macId` and `timestamp` fields in the message are mandatory since the CDK stack has configured DynamoDB table to use the `macId` field as the Partition Key and `timestamp` field as the Sort key.
You can generate a new/different value for `timestamp` and change the values of then click publish button. You should test by publishing the message a few more times - each time you should change the `timestamp` field, and optionally vary the `temperature` and `humidity` fields (use 2 digits after the decimal point).

10. Switch to the DynamoDB explore items window, and refresh to scan the table. You should be able to see data an entry with 5 columns. For the test message above you will observe:
```sh
macId          timestamp         humidity    temperature    ttl(TTL)
AABBCCDDEEFF   1660581788000     95.11       63.25          1660582121901

```
The `ttl` is computed using the `timestamp()` function in the SQL timestamp, and adding the value specified in `config.json` file (default is `30000`).

## Cleanup
 
Run the given command to delete the resources that were created. It might take some time for the CloudFormation stack to get deleted. See the Notes section in [README](./README.md)

```sh
cdk destroy
```

## Roadmap

1. Include a simulated IoT device sending MQTT messages to AWS IoT Core using [AWS IoT Device SDK v2 for Python](https://github.com/aws/aws-iot-device-sdk-python-v2)

## Resources
1. [AWS IoT Rule Actions](https://docs.aws.amazon.com/iot/latest/developerguide/iot-rule-actions.html)
2. [DynamoDBv2 Action](https://docs.aws.amazon.com/iot/latest/developerguide/dynamodb-v2-rule-action.html)

----
Copyright Amazon.com, Inc. or its affiliates. All Rights Reserved. 

SPDX-License-Identifier: MIT-0
