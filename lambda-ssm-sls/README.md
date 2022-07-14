# AWS Lambda GET and PUT to Amazon SSM Parameter Store Using the Serverless Framework

This Serverless Framework project deploys a Lambda function, an SSM Parameter Store entry and the IAM permissions required to run the application. The Lambda function publishes a message to the SQS queue when invoked.

Learn more about this pattern at Serverless Land Patterns: https://serverlessland.com/patterns/lambda-ssm-sls/

Important: this application uses various AWS services and there are costs associated with these services after the Free Tier usage - please see the [AWS Pricing page](https://aws.amazon.com/pricing/) for details. You are responsible for any AWS costs incurred. No warranty is implied in this example.

## Requirements

- [Create an AWS account](https://portal.aws.amazon.com/gp/aws/developer/registration/index.html) if you do not already have one and log in. The IAM user that you use must have sufficient permissions to make necessary AWS service calls and manage AWS resources.
- [AWS CLI](https://docs.aws.amazon.com/cli/latest/userguide/install-cliv2.html) installed and configured
- [Git Installed](https://git-scm.com/book/en/v2/Getting-Started-Installing-Git)
- [Curl Installed](https://curl.se/download.html)
- [Serverless Framework](https://www.serverless.com/) installed
- [Serverless Framework Plugin Python Requirements](https://www.serverless.com/plugins/serverless-python-requirements) installed

## Deployment Instructions

1. Create a new directory, navigate to that directory in a terminal and clone the GitHub repository:
   ```
   git clone https://github.com/aws-samples/serverless-patterns
   ```
1. Change directory to the pattern directory:
   ```
   cd lambda-ssm-sls
   ```
1. Using the editor of your choice, oopen up the serverless.yml file and change any of the configuration settings to match your environment.
1. From the command line, use the Serverless Framework to deploy the AWS resources for the pattern as specified in the template.yml file:
   ```
   serverless deploy
   ```
1. Note the outputs from the Serverless Framework deployment process. These contain the HTTP GET and PUT endpoints.

### Testing

Use the [AWS CLI](https://aws.amazon.com/cli/) to invoke the Lambda function. The function name is in the outputs of the AWS SAM deployment (the key is `QueuePublisherFunction`):

1. Invoke the Lambda function to get the current value from the SSM Parameter Store:

```bash
curl http://YOUR_LAMBDA_GET_ENDPOINT
```

2. Update the value in the SSM Parameter Store

```bash
curl -X PUT http://YOUR_LAMBDA_PUT_ENDPOINT -d "YOUR_NEW_VALUE"
```

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
