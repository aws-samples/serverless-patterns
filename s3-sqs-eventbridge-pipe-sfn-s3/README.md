# Copying a file between Amazon S3 buckets via Amazon Eventbridge Pipes & AWS Step Functions

This pattern shows how to use S3 Event Notifications, queue them on Amazon SQS, and then use Amazon EventBridge Pipes to launch an AWS StepFunctions state machine and copy the file from the source S3 bucket to a destination.  Modifying the state machine would allow manipulation of the file.

Important: this application uses various AWS services and there are costs associated with these services after the Free Tier usage - please see the [AWS Pricing page](https://aws.amazon.com/pricing/) for details. You are responsible for any AWS costs incurred. No warranty is implied in this example.

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
2. Change directory to the pattern directory:
    ```
    cd s3-sqs-eventbridge-pipe-sfn-s3
    ```
3. From the command line, use AWS SAM to deploy the AWS resources for the pattern as specified in the template.yml file:
    ```
    sam deploy --guided
    ```
4. During the prompts:
    * Enter a stack name
    * Enter the desired AWS Region
    * Allow SAM CLI to create IAM roles with the required permissions.

    Once you have run `sam deploy --guided` mode once and saved arguments to a configuration file (samconfig.toml),  you 
   can use `sam deploy` in future to use these defaults.

5. Note the outputs from the SAM deployment process. These contain the resource names and/or ARNs which are used for testing.

## How it works

When a file is created in the source S3 bucket, an 
[S3 Event Notification](https://docs.aws.amazon.com/AmazonS3/latest/userguide/EventNotifications.html) fires with
[this structure](https://docs.aws.amazon.com/AmazonS3/latest/userguide/notification-content-structure.html). 
This is enqueued onto a standard Amazon SQS Queue.

The EventBridge service polls the SQS Queue and invokes the EventBridge Pipe synchronously with an event that contains queue 
messages. EventBridge reads messages in batches and invokes the pipe once for each batch. When the pipe successfully 
processes a batch, EventBridge deletes its messages from the queue.
The structure of the batch is [described here](https://docs.aws.amazon.com/eventbridge/latest/userguide/eb-pipes-sqs.html)

The EventBridge Pipe then executes the 
[AWS Step Functions Express Workflow](https://docs.aws.amazon.com/step-functions/latest/dg/concepts-standard-vs-express.html) 
state machine 
[described in s3-sqs-eventbridge-pipe-sfn-s3.asl.json](./workflow/s3-sqs-eventbridge-pipe-sfn-s3.asl.json). 
This loops through each message in the batch dequeued from SQS using a Map state, loops through each record from the S3 
Event Notification using another Map state, and then copies the file from the source S3 Bucket to the destination S3 
Bucket. In a real world scenario the state machine would be modified to manipulate the file as desired.


## Testing

Provide steps to trigger the integration and show what should be observed if successful.

1. Stream logs from StepFunctions LogGroup 

```
sam logs --cw-log-group <LogGroup Name> --tail
```

2. Put a file into the source bucket

```
aws s3api put-object --bucket <source-bucket-name> --key <source-bucket-filename> --body <local-filename>
```

3. Observe the logs for the new execution.

## Cleanup
 
1. Delete the stack

 ```bash
 sam delete
 ```

----
Copyright 2024 Amazon.com, Inc. or its affiliates. All Rights Reserved.

SPDX-License-Identifier: MIT-0
