# Amazon S3 to AWS CloudTrail to Amazon EventBridge



Learn more about this pattern at the Serverless Land Patterns Collection: https://serverlessland.com/patterns/s3-cloudtrail-eventbridge

Note: From December 2021, S3 allows publishing events directly to EventBridge [LINK](https://serverlessland.com/patterns/s3-eventbridge). The approach in current pattern can be useful in cases where event auditing/monitoring/logging is additionally required. 

Important: this application uses various AWS services and there are costs associated with these services after the Free Tier usage - please see the [AWS Pricing page](https://aws.amazon.com/pricing/) for details.

You are responsible for any AWS costs incurred. No warranty is implied in this example.

## Requirements

* [Create an AWS account](https://portal.aws.amazon.com/gp/aws/developer/registration/index.html) if you do not already have one and log in. The IAM user that you use must have sufficient permissions to make necessary AWS service calls and manage AWS resources.
* [AWS CLI](https://docs.aws.amazon.com/cli/latest/userguide/install-cliv2.html) installed and configured
* [Git Installed](https://git-scm.com/book/en/v2/Getting-Started-Installing-Git)
* [AWS Serverless Application Model](https://docs.aws.amazon.com/serverless-application-model/latest/developerguide/serverless-sam-cli-install.html) (AWS SAM) installed

## Deployment Instructions

1. Create a new directory, navigate to that directory in a terminal and clone the GitHub repository

```
git clone https://github.com/aws-samples/serverless-patterns
```

2. Change directory to the pattern directory:

```
cd serverless-patterns/s3-eventbridge
```

3. From the command line, use AWS SAM to deploy the AWS resources for the pattern as specified in the template.yml file:

```
sam deploy —guided
```

4. During the prompts:
   * Enter a stack name
   * Enter the desired AWS Region
   * Enter unique bucket names
   * Allow SAM CLI to create IAM roles with the required permissions.

```
Once you have run `sam deploy -guided` mode once and saved arguments to a configuration file (samconfig.toml), you can use `sam deploy` in future to use these defaults.
```

5. Note the outputs from the SAM deployment process. The URL for SQS is present and will be used for testing.

## How it works

This pattern sends Amazon S3 events to Amazon EventBridge using AWS CloudTrail. EventBridge event is sent to SQS for monitoring.

Data events are not logged by default. To record CloudTrail data events, supported resources or resource types have to be explicitly added. (See Resources section for additional context)

The SAM template deploys:
* An S3 Bucket - where source images are pushed
* CloudTrail - that captures Data events on above S3 bucket
* Another S3 bucket - where cloud trail writes its logs
* A BucketPolicy - that allows cloud trail to write to logs  bucket
* An EventBridge rule that identifies s3 data events and sends them to an SQS
* An SQS Queue - where event notifications are sent
* A QueuePolicy - that allows for Event to be sent to the SQS queue


## Testing

Use the [AWS CLI](https://aws.amazon.com/cli/) to push an image into an S3 bucket. 


1. Push an image into the S3 bucket:

```bash
aws s3 cp /path/to/image/helloworld1.png s3://<s3-bucket-name>
```

2. Check message in SQS queue to validate that the S3 event was published correctly
```bash
aws sqs receive-message --queue-url <queue-url-from-output-after-sam-deploy> 
```

3. You should see an event that was delivered to the event bus:. Note the message contains some relevant info like
```
below are snippets from the sqs message:

\"eventName\":\"PutObject\"
\"Host\":\"<s3-bucket-name>.s3.us-west-2.amazonaws.com\"
\"key\":\"helloworld1.png\"
```

## Cleanup

1. Navigate to the S3 buckets in AWS console and delete all artifacts so that buckets become empty. 

2. Delete the stack
   
    ```bash
    aws cloudformation delete-stack --stack-name STACK_NAME
    ```
   
3. Confirm the stack has been deleted
   
    ```bash
    aws cloudformation list-stacks --query "StackSummaries[?contains(StackName,'STACK_NAME')].StackStatus"
    ```
   

----
Copyright 2021 Amazon.com, Inc. or its affiliates. All Rights Reserved.

SPDX-License-Identifier: MIT-0
