# Event generation, their distribution via Amazon EventBridge rules to rate controlled processing using Amazon SQS and AWS Lambda

This pattern contains a sample AWS Cloud Development Kit (AWS CDK) template for creating a Lambda function that posts AWS EventBridge events to the default domain bus. This CDK template defines EventBridge rules to distribute events based on rules to SQS queues also created in the CK template.  This CDK template also deploys a AWS Lambda functions linked to each queue for event-type specific processing.

Learn more about this pattern at Serverless Land Patterns:: https://serverlessland.com/patterns/s3-eventbridge-lambda

Important: This template uses various AWS services and there are costs associated with these services after the Free Tier usage - please see the [AWS Pricing page](https://aws.amazon.com/pricing/) for details. You are responsible for any AWS costs incurred. No warranty is implied in this example.

## Requirements

- [Create an AWS account](https://portal.aws.amazon.com/gp/aws/developer/registration/index.html) if you do not already have one and log in. The IAM user that you use must have sufficient permissions to make necessary AWS service calls and manage AWS resources.
- [AWS CLI](https://docs.aws.amazon.com/cli/latest/userguide/install-cliv2.html) installed and configured
- [Git Installed](https://git-scm.com/book/en/v2/Getting-Started-Installing-Git)
- [AWS CDK](https://docs.aws.amazon.com/cdk/latest/guide/cli.html) installed and configured

## Setup


## Deployment Instructions

1. Create a new directory, navigate to that directory in a terminal and clone the GitHub repository:
   ```bash
   git clone https://github.com/aws-samples/serverless-patterns
   ```

1. 
```
cd lambda-eventbridge-sqs-lambda-cdk-python
```

Install the required dependencies (aws-cdk-lib and constructs) into your Python environment 
```
pip install -r requirements.txt
```

1. From the command line, configure AWS CDK:
   ```bash
   cdk bootstrap ACCOUNT-NUMBER/REGION # e.g.
   cdk bootstrap 1111111111/us-east-1
   cdk bootstrap --profile test 1111111111/us-east-1
   ```
1. From the command line, use AWS CDK to deploy the AWS resources for the pattern as specified in the `stack/s3-eventbridge-lambda-stack.ts`
   ```bash
   cdk deploy
   ```


## How it works

- Go to the Lambda ARN printed as part of the CDK output. Do a Test invocation of the Lambda from the console.
- This will send three events to EventBridge and each will be routed to either the email/sftp/3papi SQS queue.
- Finally each of the processing Lambdas get triggered by the message on their respective queues.


## Testing

1. Go to the Lambda ARN printed as part of the CDK output. Do a Test invocation of the Lambda from the console.
1. This will send three events to EventBridge and each will be routed to either the email/sftp/3papi SQS queue and eventually to the processor Lambdas.



## Cleanup

1. Delete the stack
   ```bash
   cdk destroy
   ```


## Documentation and useful references
- [Reducing custom code by using advanced rules in Amazon EventBridge](https://aws.amazon.com/blogs/compute/reducing-custom-code-by-using-advanced-rules-in-amazon-eventbridge/)
- [Use Amazon EventBridge to Build Decoupled, Event-Driven Architectures](https://serverlessland.com/learn/eventbridge/)

----
Copyright 2024 Amazon.com, Inc. or its affiliates. All Rights Reserved.

SPDX-License-Identifier: MIT-0