# AWS EventBridge to AWS AppSync Events

This pattern demonstrates how you can send events from EventBridge to an AppSync Events API. This will allow you to consume events in real-time over WebSockets. This stack will deploy the following resources: 

Important: this application uses various AWS services and there are costs associated with these services after the Free Tier usage - please see the [AWS Pricing page](https://aws.amazon.com/pricing/) for details. You are responsible for any AWS costs incurred. No warranty is implied in this example.

## Requirements

* [Create an AWS account](https://portal.aws.amazon.com/gp/aws/developer/registration/index.html) if you do not already have one and log in. The IAM user that you use must have sufficient permissions to make necessary AWS service calls and manage AWS resources.
* [AWS CLI](https://docs.aws.amazon.com/cli/latest/userguide/install-cliv2.html) installed and configured
* [Git Installed](https://git-scm.com/book/en/v2/Getting-Started-Installing-Git)
* [AWS Serverless Application Model](https://docs.aws.amazon.com/serverless-application-model/latest/developerguide/serverless-sam-cli-install.html) (AWS SAM) installed
* [Create an AppSync Events API](https://docs.aws.amazon.com/appsync/latest/eventapi/create-event-api-tutorial.html) and note the HTTP endpoint and API Key created. You will need this later. 

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
    sam deploy --guided
    ```
1. During the prompts:
    * Enter a stack name
    * Enter the desired AWS Region
    * Allow SAM CLI to create IAM roles with the required permissions.

    Once you have run `sam deploy --guided` mode once and saved arguments to a configuration file (samconfig.toml), you can use `sam deploy` in future to use these defaults.

1. Note the `EventBusName` output from the SAM deployment process. You will use this in the testing process in the Console. 

## How it works

A new EventBus is created with a rule to catch events in your account which match a specified detail-type. These events are then sent to an API Destination which is an AppSync Events API. If there are errors delivering these events to your Events API, they will be delivered to a DLQ where you can inspect what went wrong. 

### How to change what is sent to your Events API

* [This link ](https://docs.aws.amazon.com/eventbridge/latest/userguide/eb-transform-target-input.html) describes how you can change the mapping templates in the EventBridge rules. You will see these in the CloudFormation Template under `InputTemplate` and  `InputTransformer`.

## Testing

### Set up your Events API to listen to events
- Go to your pre-created Events API in the console.
- Click the pub/sub editor tab.
- Scroll down to the subscriptions section and click on "connect".
- For channel, leave the `default` parameter as it is. Replace `/*` with `/serverless-patterns`.
- Click on Subscribe.

### Publish test events to EventBridge

- Open a new tab and go to the EventBridge Console.
- Click "Event buses" on the left menu.
- On the top right, click "send events".
- Select the newly created event bus. For "event source" put anything and for "detail type" enter `serverless-patterns`.
- Enter the following payload: `{"message":"hello from test"}`.
- Send the event.
- Swap back to your Events API tab, you should see a new message arrived in the following format: 
```
{
  "detailType": "serverless-patterns",
  "region": "{{your-region}}",
  "message": "hello from test"
}
```

### Troubleshooting
If events are not arriving in your Events API Console you should go to the SQS console, find the SQS queue created by this stack as your DLQ and poll for messages. Any errors should be shown in the attributes of the messages. 

If there are no messages in the DLQ, double check that you have correctly entered the channel parameters in the Events API Console. 

## Cleanup
 
1. Delete the stack
    ```bash
    sam delete --stack-name {{YOUR_STACK_NAME}}
    ```

----
Copyright 2024 Amazon.com, Inc. or its affiliates. All Rights Reserved.

SPDX-License-Identifier: MIT-0
