# API Gateway REST API to EventBridge with event payload composition and SQS as target

The APIGW payload is sent to Amazon EventBridge as a custom event payload. A custom payload is created in the integration request and passed to EventBridge with the "DetailType":"POSTED". A rule matches these events and sends the event to SQS. A Lambda function polls the SQS queue and writes the payload to CloudWatch Logs.

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
2. Change the directory to the pattern directory:
    ```
    cd apigw-rest-api-eventbridge-sqs-sam
    ```
3. From the command line, use AWS SAM to deploy the AWS resources for the pattern as specified in the template.yml file:
    ```
    sam build
    sam deploy --guided --capabilities CAPABILITY_NAMED_IAM
    ```
4. During the prompts:
    * Enter a stack name
    * Enter the desired AWS Region
    * Allow SAM CLI to create IAM roles with the required permissions.

    Once you have run `sam deploy --guided` mode once and saved arguments to a configuration file (samconfig.toml), you can use `sam deploy` in future to use these defaults.

5. Note the outputs from the SAM deployment process. These contain the resource names and/or ARNs which are used for testing.

## Testing

1. Use your preferred terminal to send an http request.

```bash
curl --location --request POST '[YOUT_API_URL]' \
--header 'Content-Type: application/json' \
--data-raw '{
    "Detail":{ 
      "IsHelloWorldExample": "Hello" 
    },
    "DetailType":"POSTED",
    "Source":"demo.event"
}'
```

2. The response would be like this:

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

3. This means your event was published successfully to EventBridge.

4. To view the message sent to SQS, either navigate to the Lambda console and check the logs, or use `sam logs` to retrieve the logs within your terminal. Replace (stack-name) with the name you gave your your AWS SAM stack.

```bash
sam logs --stack-name (stack-name)
```

Below are snippets from the logs
```
2022-12-17T08:05:42.754Z  5c0616f6-523d-54cb-8b83-4ae128b6822b  INFO  {
  data: { IsHelloWorldExample: 'Hello' },
  metadata: {
    requestId: 'bcb9dd02-b9a4-40b8-ae9d-37a4fdb9d8cc',
    requestTimeEpoch: '1671264101920'
  }
}

```

## Cleanup

1. Delete the stack
    ```bash
    sam delete
    ```
----

Copyright 2022 Amazon.com, Inc. or its affiliates. All Rights Reserved.

SPDX-License-Identifier: MIT-0
