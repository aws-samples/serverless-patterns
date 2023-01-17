# Enrich EventBridge Pipes source data with Salesforce via API destinations

This pattern shows how to use EventBridge Pipes to enrich messages data coming from SQS Queue using Salesforce with API destinations.

Learn more about this pattern at Serverless Land Patterns: << Add the live URL here >>

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
    cd eventbridge-pipes-sqs-enrich-with-sfdc
    ```
1. From the command line, use AWS SAM to deploy the AWS resources for the pattern as specified in the template.yml file:
    ```
    sam deploy --guided
    ```
1. During the prompts:
    * Enter a stack name
    * Enter the desired AWS Region
    * View Salesforce documentation for Salesforce connection parameters.
    * [SalesforceOAuthUrl](https://developer.salesforce.com/docs/atlas.en-us.214.0.api_rest.meta/api_rest/intro_understanding_oauth_endpoints.htm) for token requests
    * [SFEndpointUrl](https://developer.salesforce.com/docs/atlas.en-us.214.0.api_rest.meta/api_rest/dome_get_field_values.htm)
    * [SalesforceOauthClientId, SalesforceOauthClientSecret, SalesforceUsername, SalesforcePassword](https://developer.salesforce.com/docs/atlas.en-us.214.0.api_rest.meta/api_rest/intro_understanding_username_password_oauth_flow.htm)
    * Allow SAM CLI to create IAM roles with the required permissions.

    Once you have run `sam deploy --guided` mode once and saved arguments to a configuration file (samconfig.toml), you can use `sam deploy` in future to use these defaults.

2. Note the outputs from the SAM deployment process. These contain the resource names and/or ARNs which are used for testing.

## How it works

EventBridge Pipes polls for messages from the SQS queue, EventBridge pipe enriches message data using an API destination. For our use case, the body of the SQS message has an account ID, and EventBridge Pipe extracts the account ID from the message and sends it as a path parameter to the API destination Salesforce endpoint. API returns additional details about the account as a response. EventBridge Pipe receives a response from the API destination and sends it to a target of Cloudwatch Logs.

## Testing
1. Replace the content of the event.json file with an account ID in your Salesforce environment.

2. Put a message in the queue using the AWS CLI or the AWS Console.
aws sqs send-message --queue-url ENTER_YOUR_SQS_QUEUE_URL --message-body file://event.json

1. Navigate to the log group configured as the Pipe Target to see the account details coming from the API Destinations response or use `sam logs` to retrieve the logs within your terminal. Replace (stack-name) with the name you gave your your AWS SAM stack.

```bash
sam logs --stack-name (stack-name)
```

## Cleanup
 
1. Delete the stack
    ```bash
    sam delete
    ```
----
Copyright 2021 Amazon.com, Inc. or its affiliates. All Rights Reserved.

SPDX-License-Identifier: MIT-0