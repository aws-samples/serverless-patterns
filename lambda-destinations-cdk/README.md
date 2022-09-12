# Lambda Destinations to Lambda and SQS

This sample proyect shows how to create a Lambda function that on success sends message to another function and on failure to SQS using Lambda destinations.

Learn more about this pattern at Serverless Land Patterns: << Add the live URL here >>

Important: this application uses various AWS services and there are costs associated with these services after the Free Tier usage - please see the [AWS Pricing page](https://aws.amazon.com/pricing/) for details. You are responsible for any AWS costs incurred. No warranty is implied in this example.

## Requirements

- [Create an AWS account](https://portal.aws.amazon.com/gp/aws/developer/registration/index.html) if you do not already have one and log in. The IAM user that you use must have sufficient permissions to make necessary AWS service calls and manage AWS resources.
- [AWS CLI](https://docs.aws.amazon.com/cli/latest/userguide/install-cliv2.html) installed and configured
- [Git installed](https://git-scm.com/book/en/v2/Getting-Started-Installing-Git)
- [AWS CDK installed](https://docs.aws.amazon.com/cdk/v2/guide/getting_started.html)

## Deployment Instructions

1. Create a new directory, navigate to that directory in a terminal and clone the GitHub repository:
   ```
   git clone https://github.com/aws-samples/serverless-patterns
   ```
1. Change directory to the pattern directory:
   ```
   cd lambda-destinations-cdk
   ```
1. From the command line, use AWS CDK to deploy the AWS resources for the pattern as specified in the template.yml file:
   ```
   cdk deploy
   ```
1. Note the outputs from the CDK deployment process. These contain the resource names and/or ARNs which are used for testing.

## How it works

The sender Lambda function has configured Lambda destinations. If the sender function succeeds it execution it will send a message to the onSuccess destination configured, in this case the reciever function. If the sender function fails it sends a message to the onFailure destination configured, in this case a AWS SQS queue.

## Testing

Provide steps to trigger the integration and show what should be observed if successful.

To test, you need to invoke the sender function in the async mode.

To send the message to the successfull destination:

```
aws lambda invoke --function-name NAME --invocation-type Event response.json
```

To send the message to the failure destination:

```
aws lambda invoke --function-name NAME --cli-binary-format raw-in-base64-out --payload '{ "test": "fail" }' response.json
```

Then verify the reciever function logs or amount of messages in the SQS queue, depending on the function results.

## Cleanup

1. Delete the stack
   ```bash
   cdk destroy
   ```

---

Copyright 2022 Amazon.com, Inc. or its affiliates. All Rights Reserved.

SPDX-License-Identifier: MIT-0
