# Amazon API Gateway REST API to Amazon SES

This pattern creates an Amazon API Gateway REST API that integrates with Amazon SES.

Learn more about this pattern at Serverless Land Patterns: https://serverlessland.com/patterns/apigw-ses

Important: this application uses various AWS services and there are costs associated with these services after the Free Tier usage - please see the [AWS Pricing page](https://aws.amazon.com/pricing/) for details. You are responsible for any AWS costs incurred. No warranty is implied in this example.

## Requirements

* [Create an AWS account](https://portal.aws.amazon.com/gp/aws/developer/registration/index.html) if you do not already have one and log in. The IAM user that you use must have sufficient permissions to make necessary AWS service calls and manage AWS resources.
* [AWS CLI](https://docs.aws.amazon.com/cli/latest/userguide/install-cliv2.html) installed and configured
* [Git Installed](https://git-scm.com/book/en/v2/Getting-Started-Installing-Git)
* [AWS Serverless Application Model](https://docs.aws.amazon.com/serverless-application-model/latest/developerguide/serverless-sam-cli-install.html) (AWS SAM) installed
* [Verified identity in Amazon SES](https://docs.aws.amazon.com/ses/latest/dg/verify-addresses-and-domains.html) for each identity that you're going to use as a "From", "Source", "Sender", or "Return-Path" address. 

## Deployment Instructions

1. Create a new directory, navigate to that directory in a terminal and clone the GitHub repository:
    ``` 
    git clone https://github.com/aws-samples/serverless-patterns
    ```
1. Change directory to the pattern directory:
    ```
    cd apigw-ses-transformation
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

This pattern creates an Amazon API Gateway REST API that integrates with an Amazon SES. The API includes an API key and usage plan. The API integrates directly with the SES API and supports [SendEmail](https://docs.aws.amazon.com/ses/latest/APIReference/API_SendEmail.html) action.

## Testing

### API key value

Retrieve API Gateway API key value, so that you can provide the appropriate security context for the test messages:

``` sh
aws apigateway get-api-keys --region <region> --include-values --query "items[?name=='email-apikey'].value" --output text
```

### Sending a new test message to API Gateway endpoint

To test the endpoint first send data using the following command. Be sure to update the endpoint with endpoint of your stack.

``` sh
curl --location --request POST '<ApiRootUrl>/<stage>' \
--header 'Content-Type: application/json' \
--header 'x-api-key: <api key from the previous step>' \
--data-raw '{
    "to": ["to@email.com"],
    "from": "from@email.com",
    "subject": "This is a test email subject",
    "text": "This is a test email content",
    "html": "<p>This is a test email content</p>"
    }'
}'
```

Expected output:

```json
{ "SendEmailResponse": { "ResponseMetadata": { "RequestId":"<RequestId>" }, "SendEmailResult": { "MessageId":"<MessageId>" } } }
```

NOTE: If your account is still in the Amazon SES sandbox, you also need to verify any email addresses which you plan on sending email to, unless you're sending to test inboxes provided by the Amazon SES mailbox simulator.

## Cleanup
 
1. Delete the stack
    ```bash
    sam delete --stack-name STACK_NAME
    ```
1. Confirm the stack has been deleted
    ```bash
    aws cloudformation list-stacks --query "StackSummaries[?contains(StackName,'STACK_NAME')].StackStatus"
    ```
----
Copyright 2023 Amazon.com, Inc. or its affiliates. All Rights Reserved.

SPDX-License-Identifier: MIT-0