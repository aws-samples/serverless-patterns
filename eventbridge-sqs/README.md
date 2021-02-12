# Amazon EventBridge to Amazon SQS

This pattern creates an EventBridge rule and an SQS queue. The SNS topic is invoked by the EventBridge rule. 

Learn more about this pattern at Serverless Land Patterns: TBD

Important: this application uses various AWS services and there are costs associated with these services after the Free Tier usage - please see the [AWS Pricing page](https://aws.amazon.com/pricing/) for details. You are responsible for any AWS costs incurred. No warranty is implied in this example.

## Requirements

* AWS CLI already configured with Administrator permission
* [NodeJS 12.x installed](https://nodejs.org/en/download/)

## Installation Instructions

1. [Create an AWS account](https://portal.aws.amazon.com/gp/aws/developer/registration/index.html) if you do not already have one and login.

1. [Install Git](https://git-scm.com/book/en/v2/Getting-Started-Installing-Git) and [install the AWS Serverless Application Model CLI](https://docs.aws.amazon.com/serverless-application-model/latest/developerguide/serverless-sam-cli-install.html) on your local machine.

1. Create a new directory, navigate to that directory in a terminal and enter ```git clone this-repo-name```.

1. Change directory to this pattern.

1. From the command line, run:
```
sam deploy --guided
```
Choose a stack name, select the desired AWS Region, and allow SAM to create roles with the required permissions. Once you have run guided mode once, you can use `sam deploy` in future to use these defaults.

1. Note the outputs from the SAM deployment process. These contain the resource names and ARNs.

## Example event payload from EventBridge to SQS
```
{                                                                                                              
    "Messages": [
        {
            "MessageId": "12345678-68cf-4b7c-8513-123456789012",
            "ReceiptHandle": "AQEBxt123456789012WtqHJEI3UstldOHB0123456789012o699ZQb34s+WS9b72u123456789012m/nDByiV8kIdM0hXs1m+53z123456789012aucGe0UoFOH/A8ty7FrZdmlH6123456789012RsFsWWUCxMJ68qOTHNrmfP123456789012q0fNpAJaejha5co1wtA1s8k+fmJr43YtCWX123456789012682oG9V6LuVS123456789012G99uuePgIW1y123456789012KD0+123456789012r/RFf9F1pAEtqMPF+LkxWMMOQv123456789012UD3luTtDmEm+tE1234567890125nNWJ/123456789012/123456789012=",
            "MD5OfBody": "12345678901265371af6123456789012",
            "Body": "{\"version\":\"0\",\"id\":\"1234567806dd-6089-df65-2c51-123456789012\",\"detail-type\":\"transaction\",\"source\":\"demo.sqs\",\"account\":\"123456789012\",\"time\":\"2021-02-10T16:41:20Z\",\"region\":\"us-east-1\",\"resources\":[],\"detail\":{\"msg\":\"test\"}}"
        }
    ]
}
```

## How it works

The AWS SAM template deploys the resources and the IAM permissions required to run the application.

The EventBridge rule specified in `template.yaml` filters the events based upon the criteria in the `EventPattern` section. When matching events are sent to EventBridge that trigger the rule, they are delivered as a JSON event payload (see above) to the SQS queue.

## Testing

Use the [AWS CLI](https://aws.amazon.com/cli/) to send a test event to EventBridge:

1. Send an event to EventBridge:

```bash
aws events put-events --entries file://event.json
```

2. Retrieve the message from the SQS queue, using the queue URL from the AWS SAM deployment outputs:
```bash
aws sqs receive-message --queue-url ENTER_YOUR_QUEUE_URL
```


----
Copyright 2021 Amazon.com, Inc. or its affiliates. All Rights Reserved.

SPDX-License-Identifier: MIT-0
