# Enrich EventBridge Pipes source data with API destinations

This pattern shows how to use EventBridge Pipes to enrich messages data coming from SQS Queue using API destinations

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
    cd eventbridge-pipes-sqs-enrich-api-destination
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

1. Note the outputs from the SAM deployment process. These contain the resource names and/or ARNs which are used for testing.

## How it works

EventBridge Pipes polls for messages from the SQS queue, EventBridge pipe enriches message data using an API destination. For our use case, the body of the SQS message has a US zip code, and EventBridge Pipe extracts the zip code from the message and sends it as a path parameter to the API destination. API returns additional details about the zip code as a response. EventBridge Pipe receives a response from the API destination and sends it to a target of Cloudwatch Logs.

## Testing

Provide steps to trigger the integration and show what should be observed if successful.

1. Stream logs from StepFunctions LogGroup 

```
sam logs --cw-log-group <LogGroup Name> --tail
```

2. Put a message into the queue

```
aws sqs send-message --queue-url ENTER_YOUR_SQS_QUEUE_URL --message-body file://event.json
```

3. Observe the logs for the new execution.

## Cleanup
 
1. Delete the stack
    ```bash
    sam delete
    ```

----
Copyright 2022 Amazon.com, Inc. or its affiliates. All Rights Reserved.

SPDX-License-Identifier: MIT-0
