# AWS Lambda to Amazon SNS Using the Serverless Framework

This Serverless Framework project deploys a Lambda function, an SNS topic and the IAM permissions required to run the application. The Lambda function publishes a message to the SNS topic when invoked.

Learn more about this pattern at Serverless Land Patterns: https://serverlessland.com/patterns/lambda-sns-sls/

Important: this application uses various AWS services and there are costs associated with these services after the Free Tier usage - please see the [AWS Pricing page](https://aws.amazon.com/pricing/) for details. You are responsible for any AWS costs incurred. No warranty is implied in this example.

## Requirements

- [Create an AWS account](https://portal.aws.amazon.com/gp/aws/developer/registration/index.html) if you do not already have one and log in. The IAM user that you use must have sufficient permissions to make necessary AWS service calls and manage AWS resources.
- [AWS CLI](https://docs.aws.amazon.com/cli/latest/userguide/install-cliv2.html) installed and configured
- [Git Installed](https://git-scm.com/book/en/v2/Getting-Started-Installing-Git)
- [Serverless Framework](https://www.serverless.com/) installed

## Deployment Instructions

1. Create a new directory, navigate to that directory in a terminal and clone the GitHub repository:
   ```
   git clone https://github.com/aws-samples/serverless-patterns
   ```
1. Change directory to the pattern directory:
   ```
   cd lambda-sns-sls
   ```
1. Using the editor of your choice, oopen up the serverless.yml file and change any of the configuration settings to match your environment.
1. From the command line, use the Serverless Framework to deploy the AWS resources for the pattern as specified in the template.yml file:
   ```
   serverless deploy
   ```
1. Note the outputs from the Serverless Framework deployment process. These contain the resource names and/or ARNs which are used for testing.

## Example payload from SNS

```
{
    "Messages": [
        {
            "MessageId": "12345678-876d-41f7-b32c-1234567890",
            "ReceiptHandle": "AQEBZfn1234567890O78Kn0C1234567890/z1+1234567890f2bQYOvD9RL1234567890Srr7+XQ/U1234567890j7nL+uaDVnJL1234567890mASoiwI/yQ1234567890gv/h17BW12345678908Pry0JM1234567890DfHE1g1234567890aMisj1234567890M+rC+ZF21234567890QdQpEwrX01234567890Fw6w2+Po0OA1234567890DkKgGuEmebp1234567890w7nNXujzSnzIXj1234567890CqfDOb2D1234567890kCk841+01234567890OaYzXV1234567890C+ruRXj1234567890AR5+vj8+U1234567890SJplJLjd1234567890YWV8o1234567890gJXb12345678901234567890",
            "MD5OfBody": "1234567890eb64e60d1234567890",
            "Body": "Message at Wed Feb 10 2021 13:47:31 GMT+0000 (Coordinated Universal Time)"
        }
    ]
}

```

### Testing

Use the [AWS CLI](https://aws.amazon.com/cli/) to invoke the Lambda function. The function name is in the outputs of the AWS SAM deployment (the key is `QueuePublisherFunction`):

1. Invoke the Lambda function to publish a message to the SNS queue:

```bash
serverless invoke --function ENTER_YOUR_FUNCTION_NAME
```

2. To retrieve the message from the SNS topic, refer to the AWS SNS documentation here:
   https://docs.aws.amazon.com/sns/latest/dg/sns-create-subscribe-endpoint-to-topic.html

## Cleanup

1. Delete the stack
   ```bash
   serverless remove
   ```
1. Confirm the stack has been deleted
   ```bash
   serverless info
   ```

---

Copyright 2021 Amazon.com, Inc. or its affiliates. All Rights Reserved.

SPDX-License-Identifier: MIT-0
