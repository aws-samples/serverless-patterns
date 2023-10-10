# AWS Lambda to AWS SNS with filters to AWS Lambda

This pattern demonstrates how to create a Lambda function that sends a message to an SNS topic using AWS SDK. The topic has filters and depending on the message content it triggers a specific function or not. One function gets trigger always no matter what is the content of the message. The other one only when there is a message that matches the filter.

Learn more about this pattern at Serverless Land Patterns: https://serverlessland.com/patterns/lambda-sns-filters-lambda

Important: this application uses various AWS services and there are costs associated with these services after the Free Tier usage - please see the [AWS Pricing page](https://aws.amazon.com/pricing/) for details. You are responsible for any AWS costs incurred. No warranty is implied in this example.

## Requirements

- [Create an AWS account](https://portal.aws.amazon.com/gp/aws/developer/registration/index.html) if you do not already have one and log in. The IAM user that you use must have sufficient permissions to make necessary AWS service calls and manage AWS resources.
- [AWS CLI](https://docs.aws.amazon.com/cli/latest/userguide/install-cliv2.html) installed and configured
- [Git Installed](https://git-scm.com/book/en/v2/Getting-Started-Installing-Git)
- [AWS CDK installed](https://docs.aws.amazon.com/cdk/v2/guide/getting_started.html)

## Deployment Instructions

1. Create a new directory, navigate to that directory in a terminal and clone the GitHub repository:
   ```
   git clone https://github.com/aws-samples/serverless-patterns
   ```
1. Change directory to the pattern directory:
   ```
   cd lambda-sns-filteres-lambda
   ```
1. From the command line, use AWS SAM to deploy the AWS resources for the pattern as specified in the template.yml file:

   ```
   cdk deploy
   ```

1. Note the outputs from the SAM deployment process. These contain the resource names and/or ARNs which are used for testing.

## How it works

The sender Lambda function sends a message to an SNS topic using AWS SDK.
The SNS topic has 2 functions subscribed. One of the function is subscribed to all the messages in the topic. The other one only to the messages that contain the attribute color red.

## Testing

To test the filtering, invoke the sender function, then this function will send a message to the SNS topic and only the function that is subscribed to all the messages will get triggered.

```
aws lambda invoke --function-name NAME --payload '{ "color": "green" }' response.json
```

Then verify the reciever function logs and you will see that it got triggered with the same message that the sender put.

You can now send a payload with the color red and that will trigger both functions.

```
aws lambda invoke --function-name NAME --payload '{ "color": "red" }' response.json
```

## Cleanup

1. Delete the stack
   ```bash
   cdk destroy
   ```

---

Copyright 2022 Amazon.com, Inc. or its affiliates. All Rights Reserved.

SPDX-License-Identifier: MIT-0
