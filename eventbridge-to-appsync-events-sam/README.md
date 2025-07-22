# Sending events from Amazon EventBridge to AWS AppSync Events

This pattern demonstrates how you can send events from EventBridge to an AppSync Event API. This will allow you to consume events in real-time over WebSockets. This stack will deploy the following resources: 
- **Amazon AppSync Events API**: Used as the destination which EventBridge will send events to. 
- **API Key**: To allow interactions with the above API.
- **EventBridge Event bus**: Use this event bus to send messages to for testing.
- **EventBridge Rule**: Catches messages matching a pattern specified in the template.
- **EventBridge API Destination**: HTTP invocation endpoint configured as a target for events. In this case, it's our pre-existing AppSync Event API HTTP endpoint passed in as a parameter.
- **EventBridge Connection**: Defines the authorization type and credentials to use for authorization with an API destination. In this case, we use the pre-existing API key passed in as a parameter. 
- **SQS Queue**: Stores messages that couldn't be delivered to the API destination successfully)
- **SQS Queue Policy**: The resource policy of the SQS queue, allowing EventBridge to put messages into the DLQ.
- **IAM Role**: IAM role which eventbridge assumes, the policy below is attached to it.
- **IAM Policy**: Defines permissions to allow EventBridge to invoke the API destination. 

Important: this application uses various AWS services and there are costs associated with these services after the Free Tier usage - please see the [AWS Pricing page](https://aws.amazon.com/pricing/) for details. You are responsible for any AWS costs incurred. No warranty is implied in this example.

## Requirements

* [Create an AWS account](https://portal.aws.amazon.com/gp/aws/developer/registration/index.html) if you do not already have one and log in. The IAM user that you use must have sufficient permissions to make necessary AWS service calls and manage AWS resources.
* [AWS CLI](https://docs.aws.amazon.com/cli/latest/userguide/install-cliv2.html) installed and configured
* [Git Installed](https://git-scm.com/book/en/v2/Getting-Started-Installing-Git)
* [AWS Serverless Application Model](https://docs.aws.amazon.com/serverless-application-model/latest/developerguide/serverless-sam-cli-install.html) (AWS SAM) installed

## Deployment Instructions

1. Create a new directory, navigate to that directory in a terminal and clone the GitHub repository:
    ``` 
    git clone https://github.com/aws-samples/serverless-patterns
    ```
1. Change directory to the pattern directory:
    ```
    cd eventbridge-to-appsync-events
    ```
1. From the command line, use AWS SAM to deploy the AWS resources for the pattern as specified in the template.yml file:
    ```
    sam deploy --guided --capabilities CAPABILITY_NAMED_IAM
    ```
1. During the prompts:
    * Enter a stack name
    * Allow SAM CLI to create IAM roles with the required permissions.
    * Keep default values to the rest of the parameters.

    Once you have run `sam deploy --guided` once and saved arguments to a configuration file (samconfig.toml), you can use `sam deploy` in future to use these defaults.

1. Note the `EventBusName` and `EventApiName` values from the SAM deployment process. You will use this in the testing process in the Console. 

## How it works

A new EventBridge event bus is created with a rule to catch events in your account which match a specified detail-type. These events are then sent to an API Destination which is an AppSync Event API. If there are errors delivering these events to your Events API, they will be delivered to a dead-letter queue (DLQ) where you can inspect what went wrong. 

### How to change what is sent to your Events API

* [This link ](https://docs.aws.amazon.com/eventbridge/latest/userguide/eb-transform-target-input.html) describes how you can change the mapping templates in the EventBridge rules. You will see these in the CloudFormation Template under `InputTemplate` and  `InputTransformer`.

## Testing

### Set up your Event API to listen to events
- Navigate to the AppSync Console and find the Event API created by the stack. You can find the name in the outputs with the key `EventApiName`. Click on it. 
- Click the Pub/Sub Editor editor tab.
- Scroll down to the Subscribe section and click on "connect".
- For channel, leave the `default` parameter as it is. Replace `/*` with `/serverless-patterns`.
- Click on Subscribe. You should see a `subscribe_success` message.

### Publish test events to EventBridge

- Open the Amazon EventBridge Console in a new tab.
- Click "Event buses" on the left menu.
- On the top right, click "send events".
- For the event bus dropdown, select the newly created event bus. You can find the name in the outputs with the key `EventBusName`. For "event source" enter anything (e.g `example.serverlesspatterns`) and for "detail type" enter `serverless-patterns`.
- Enter the following payload: `{"message":"hello from test"}`.
- Click "Send".
- Navigate back to your Events API tab, you should see a new message arrived in the subscription area as follows: 
```
{
  "detailType": "serverless-patterns",
  "region": "{{your-region}}",
  "message": "hello from test"
}
```

### Troubleshooting

**Check the Event Bus Name**: Ensure you are sending test messages to the correct event bus (name is in the outputs of the stack) with "detail type" of `serverless-patterns`. This example won't work on the default event bus.

**Events not arriving to Event API Console**: Go to the SQS console, find the SQS queue created by this stack (which is your DLQ) and poll for messages. Any errors should be shown in the attributes tab of the messages. 

**No messages in DLQ**: Double check that you have subscribed to the correct namespace/channel `default/serverless-patterns` in the Event API Console. Triple check you are sending messages to the correct event bus.

## Cleanup
 
1. Delete the stack
    ```bash
    sam delete
    ```

----
Copyright 2025 Amazon.com, Inc. or its affiliates. All Rights Reserved.

SPDX-License-Identifier: MIT-0
