# AWS Lambda send event to Amazon EventBridge using the Serverless Framework

This Serverless Framework project deploys a Lambda function and the IAM permissions required to run the application. The Lambda function publishes a message to the default EventBridge when invoked.

Learn more about this pattern at Serverless Land Patterns: https://serverlessland.com/patterns/lambda-eventbridge-sls/

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
   cd lambda-eventbridge-sls
   ```
1. Using the editor of your choice, open up the serverless.yml file and change any of the configuration settings to match your environment.
1. From the command line, use the Serverless Framework to deploy the AWS resources for the pattern as specified in the template.yml file:
   ```
   serverless deploy
   ```
1. Note the outputs from the Serverless Framework deployment process. This will contain the POST endpoint.

### Testing

Use the curl command to invoke the AWS Lambda:

1. Invoke the Lambda function to send an event to the default Event:

```bash
curl -X POST http://YOUR_LAMBDA_GET_ENDPOINT -H 'Content-Type: application/json' -d '{"entry1": "data1", "entry2": "data2"}'
```

## Cleanup

1. Delete the stack
   ```bash
   serverless remove --verbose
   ```
1. Confirm the stack has been deleted

   ```sh
   aws cloudformation list-stacks --query "StackSummaries[?contains(StackName,'lambda-eventbridge-sls')].StackStatus"
   ```

   Expected output

   ```json
   ["DELETE_COMPLETE"]
   ```

---

Copyright 2021 Amazon.com, Inc. or its affiliates. All Rights Reserved.

SPDX-License-Identifier: MIT-0
