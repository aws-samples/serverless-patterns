# Transforming EventBridge Events to CloudEvents

If your EventBridge target e.g., a Lambda function, expects a JSON-encoded [CloudEvent](https://cloudevents.io/) an
EventBridge [Input Transformer](https://docs.aws.amazon.com/eventbridge/latest/userguide/eb-transform-target-input.html)
can be used to perform a lossless conversion from the EventBridge event format to CloudEvents.

This pattern demonstrates using an input transformation in an EventBridge rule on a custom event bus to convert an
EventBridge event to a *structured JSON-encoded* CloudEvent.

Learn more about this pattern at Serverless Land Patterns:
https://serverlessland.com/patterns/eventbridge-cloudevents-transformer-cdk-typescript

Important: this application uses various AWS services and there are costs associated with these services after the Free
Tier usage - please see the [AWS Pricing page](https://aws.amazon.com/pricing/) for details. You are responsible for any
AWS costs incurred. No warranty is implied in this example.

## Requirements

* [Create an AWS account](https://portal.aws.amazon.com/gp/aws/developer/registration/index.html) if you do not already
  have one and log in. The IAM user that you use must have sufficient permissions to make necessary AWS service calls
  and manage AWS resources.
* [AWS CLI](https://docs.aws.amazon.com/cli/latest/userguide/install-cliv2.html) installed and configured
* [Git](https://git-scm.com/book/en/v2/Getting-Started-Installing-Git) installed
* [Node and NPM](https://nodejs.org/en/download/) installed
* [AWS Cloud Development Kit](https://docs.aws.amazon.com/cdk/latest/guide/cli.html) (AWS CDK) installed

## Deployment Instructions

1. Create a new directory, navigate to that directory in a terminal and clone the GitHub repository:

    ``` 
    git clone https://github.com/aws-samples/serverless-patterns
    ```
    
1. Change directory to the pattern directory:

    ```
    cd serverless-patterns/eventbridge-cloudevents-transformer-cdk-typescript/src
    ```
    
1. Install dependencies:

    ```
    npm install
    ```
    
1. From the command line, configure AWS CDK (unless already done):

   ```
   # cdk bootstrap <ACCOUNT-NUMBER/REGION>
   cdk bootstrap 1111111111/us-east-1
   ```

1. From the command line, use AWS CDK to deploy the AWS resources for the pattern:
   
    ```
    cdk deploy 
    ```

## How it works

This pattern demonstrates using an input transformation in an EventBridge rule on a custom event bus to convert an
EventBridge event to a *structured JSON-encoded* CloudEvent. A Lambda function, using the [CloudEvents SDK for
TypeScript](https://github.com/cloudevents/sdk-javascript), is configured as a target on the rule, using the SDK in the
handler to consume the incoming CloudEvent without performing manual deserialization from the EventBridge format.

The example input transformer in this pattern uses the following EventBridge to CloudEvents field mappings
(customizable). For demo purposes, `account` and `region` are mapped to CloudEvent extension attributes.

| EventBridge   | CloudEvents |
|---------------|-------------|
| `id`          | `id`        |
| `source`      | `source`    |
| `detail-type` | `type`      |
| `time`        | `time`      |
| `detail`      | `data`      |
| `account`     | `account`   |
| `region`      | `region`    |

> **Note**  
> If there is a stable, i.e., always present, JSON field in the EventBridge `detail` payload for a particular object,
> e.g., an order id, it can be easily mapped to the CloudEvents `subject` field, e.g. `subject:
> EventField.fromPath('$.detail.order_id')` (not shown in this example).

### Example

Given the following EventBridge event:

```json
{
    "version": "0",
    "id": "58c17c28-ce07-3b3d-a8c2-92830a2910de",
    "account": "1234567890",
    "time": "2023-07-03T13:18:31Z",
    "region": "us-east-1",
    "detail-type": "test.event",
    "source": "test.source",
    "resources": [],
    "detail": {
        "hello": "world"
    }
}
```

The transformed event as received by the Lambda function is:

```json
{
    "specversion": "1.0",
    "id": "58c17c28-ce07-3b3d-a8c2-92830a2910de",
    "time": "2023-07-03T13:18:31.000Z",
    "type": "test.event",
    "source": "test.source",
    "data": {
        "hello": "world"
    },
    "region": "us-east-1",
    "account": "1234567890"
}
```

## Testing

Step-by-step instructions to understand the implementation for the pattern:

1. Deploy the `EbLambdaCloudeventsStack` as described [above](#deployment-instructions)
2. Verify the custom event bus, rule, input transformer and Lambda function were created
3. In the AWS console, open the custom event bus and click on `Send Events` in the upper right (the rule used in this example will match any event from the same account)
4. Make sure the right event bus is selected
5. For `Event source` enter `test.source`
6. For `Detail type` enter `test.event`
7. For `Event detail` enter `{"hello":"world"}`
8. Check the CloudWatch logs for the function to see the resulting (converted) CloudEvent logged by the Lambda function
9. If you don't see an event, try sending it again or inspect the dead-letter queue

## Cleanup

Delete the stack:

```
cdk destroy
```

----
Copyright 2023 Amazon.com, Inc. or its affiliates. All Rights Reserved.

SPDX-License-Identifier: MIT-0
