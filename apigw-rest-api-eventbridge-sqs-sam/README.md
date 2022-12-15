# API Gateway REST API to EventBridge with event payload composition and SQS as target

The APIGW payload is sent to EventBridge as a custom event payload. In the integration request, a custom payload is created and passed to EventBridge to target an SQS.

Learn more about this pattern at Serverless Land Patterns: [https://serverlessland.com/patterns?services=apigw%2Ceventbridge](https://serverlessland.com/patterns?services=apigw%2Ceventbridge

Important: this application uses various AWS services and there are costs associated with these services after the Free Tier usage - please see the [AWS Pricing page](https://aws.amazon.com/pricing/) for details.

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
    cd apigw-eventbridge
    ```
1. From the command line, use AWS SAM to deploy the AWS resources for the pattern as specified in the template.yml file:
    ```
    sam deploy --guided --capabilities CAPABILITY_NAMED_IAM
    ```
1. During the prompts:
    * Enter a stack name
    * Enter the desired AWS Region
    * Allow SAM CLI to create IAM roles with the required permissions.

    Once you have run `sam deploy --guided` mode once and saved arguments to a configuration file (samconfig.toml), you can use `sam deploy` in future to use these defaults.

1. Note the outputs from the SAM deployment process. These contain the resource names and/or ARNs which are used for testing.

## Testing

Use your preferred terminal to send a http request.

```bash
curl --location --request POST 'https://[YOUT_API_URL]' \
--header 'Content-Type: application/json' \
--data-raw '{
    "Detail":{ 
      "IsHelloWorldExample": "Hello" 
    },
    "DetailType":"POSTED",
    "Source":"demo.event"
}'
```

The response would be like:

```bash
{
  "Entries":[
    {
      "EventId":"f0021bf7-e696-508a-823e-424aa2f48dfa"
    }
  ],
  "FailedEntryCount":0
} 
```

This means your event was published successfuly and you should see it in the SQS.

## Cleanup

1. Delete the stack
    ```bash
    sam delete
    ```
----

Copyright 2022 Amazon.com, Inc. or its affiliates. All Rights Reserved.

SPDX-License-Identifier: MIT-0
