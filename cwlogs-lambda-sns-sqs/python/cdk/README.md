# Amazon CloudWatch Logs Subscription to AWS Lambda to Amazon SNS to Amazon SQS with CDK

This pattern demonstrates how to use CloudWatch Logs Subscription to stream CloudWatch Logs to SNS. The CloudWatch Log Group, Log Stream, Subscription filters, Lambda Function, SNS Topic, SQS Queue with SNS Subscription and required IAM Role & Permissions are all deployed using the CDK Stack. For the specified filter parameter, the subscriber a Lambda Function receives the log data from CloudWatch Logs, the Lambda function publishes it to SNS, and a SQS subscriber obtains the same.

Learn more about this pattern at Serverless Land Patterns: [serverlessland.com/patterns/cwlogs-lambda-sns-sqs-cdk](https://serverlessland.com/patterns/cwlogs-lambda-sns-sqs-cdk)

Important: this application uses various AWS services and there are costs associated with these services after the Free Tier usage - please see the [AWS Pricing page](https://aws.amazon.com/pricing/) for details. You are responsible for any AWS costs incurred. No warranty is implied in this example.

## Requirements

- [Create an AWS account](https://portal.aws.amazon.com/gp/aws/developer/registration/index.html) if you do not already have one and log in. The IAM user that you use must have sufficient permissions to make necessary AWS service calls and manage AWS resources.
- [AWS CLI](https://docs.aws.amazon.com/cli/latest/userguide/install-cliv2.html) installed and configured
- [Git Installed](https://git-scm.com/book/en/v2/Getting-Started-Installing-Git)
- [AWS Cloud Development Kit](https://docs.aws.amazon.com/cdk/v2/guide/getting_started.html) (AWS CDK) v2 Installed

## Deployment Instructions

1. Create a new directory, navigate to that directory in a terminal and clone the GitHub repository:
   ```
   git clone https://github.com/aws-samples/serverless-patterns
   ```
2. Change directory to the pattern directory:
   ```
   cd serverless-patterns/cwlogs-lambda-sns-sqs-cdk/
   ```
3. Create a virtual environment for python:
   ```
   python3 -m venv .venv
   ```
4. Activate the virtual environment:
   ```
   source .venv/bin/activate
   ```
   On a Windows platform, you would use this:
   ```
   .venv\Scripts\activate.bat
   ```
5. Install the required python modules:
   ```
   pip install -r requirements.txt
   ```
6. From the command line, use AWS CDK to synthesize an AWS CloudFormation:
   ```
   cdk synth
   ```
7. From the command line, use AWS CDK to deploy the AWS resources for the pattern:
   ```
   cdk deploy 
   ```
   
   Expected Result:
   
   ```
   Outputs:
      cwlogs-lambda-sns-sqs.LOGGROUPNAME = cwlogs-lambda-sns-sqs-myLogGroup11111XXX-XXXXXXX
      cwlogs-lambda-sns-sqs.LOGSTREAMNAME = cwlogs-lambda-sns-sqs-myLogStream11111YYYY-YYYYYYY
      cwlogs-lambda-sns-sqs.QUEUEURL = https://sqs.us-east-1.amazonaws.com/111122223333/cwlogs-lambda-sns-sqs-myQueue11111ZZZZ-b188560f
   Stack ARN:
      arn:aws:cloudformation:us-east-1:111122223333:stack/cwlogs-lambda-sns-sqs/a1b2c3d4-5678-90ab-cdef-EXAMPLEbbbbb
   ```

## Testing

Use the [AWS CLI](https://aws.amazon.com/cli/) to send logs to CloudWatch and retrieve the filtered logs from the SQS queue. The LOG_GROUP_NAME, LOG_STREAM_NAME and QUEUE_URL are in the stack outputs. Example logs are available in the `example_logs.json` file. As needed update the timestamp to most recent using [epochconverter](https://www.epochconverter.com/).

1. Send logs to CloudWatch:

   ```
   aws logs put-log-events --log-group-name LOG_GROUP_NAME --log-stream-name LOG_STREAM_NAME --log-events file://example_logs.json
   ```

2. Retrieve the filtered logs from the SQS queue:

   ```
   aws sqs receive-message --queue-url QUEUE_URL
   ```

## Cleanup

1. To delete the stack, run:
   ```
   cdk destroy
   ```
   
## Useful commands

 * `cdk ls`          list all stacks in the app
 * `cdk synth`       emits the synthesized CloudFormation template
 * `cdk deploy`      deploy this stack to your default AWS account/region
 * `cdk diff`        compare deployed stack with current state
 * `cdk docs`        open CDK documentation

---

Copyright 2023 Amazon.com, Inc. or its affiliates. All Rights Reserved.

SPDX-License-Identifier: MIT-0
