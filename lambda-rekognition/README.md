# AWS Lambda to Amazon Rekognition

This pattern demonstrates how an event can be used to trigger a Lambda function and run Image analysis using Amazon Rekognition.

Learn more about this pattern at the Serverless Land Patterns Collection: https://serverlessland.com/patterns/lambda-rekognition

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
cd lambda-rekognition
```

3. From the command line, use AWS SAM to deploy the AWS resources for the pattern as specified in the template.yml file:

```
sam deploy --guided --capabilities CAPABILITY_IAM CAPABILITY_NAMED_IAM
```

4. During the prompts:
   * Enter a stack name
   * Enter the desired AWS Region
   * Enter some bucket name that exists and can be used for testing
   * Allow SAM CLI to create IAM roles with the required permissions.

```
Once you have run `sam deploy -guided` mode once and saved arguments to a configuration file (samconfig.toml), you can use `sam deploy` in future to use these defaults.
```


## How it works

This pattern uses an EventBridge event rule to trigger a Lambda Function. The Lambda runs an image analysis on the image specified in the incoming event.

Lambda uses Amazon Rekognition to run an analysis on that image. The image analysis used for demo is text recognition.

The SAM template accepts:
* Bucket name of any existing S3 bucket. This bucket will be the source of the image being processed.
  
The SAM template deploys:
* An EventBridge rule that identifies data events on source s3 bucket and the rule triggers a Lambda function for the matched event.
* Permissions for EventBridge to invoke a Lambda function
* An IAM role - that allows Lambda 
  - to use CloudWatch logs, 
  - to use detect_text Rekognition api, 
  - to pull an image from source S3 bucket
* A Lambda function that uses Amazon Rekognition



## Testing

Use the [AWS CLI](https://aws.amazon.com/cli/) to push an image into an S3 bucket.

For testing purposes, we put an event into EventBridge that is similar to S3 put image data event.


1. Push an image into the S3 bucket:

```bash
aws s3 cp /path/to/image/helloworld1.png s3://<s3-source-bucket-name>
```

2. Push a simulated event into EventBridge

```bash
aws events put-events --entries 'file:///path/to/event/put-image-event.json'
```

3. Open the most recent log file in CloudWatch logs for the log group "/aws/lambda/TextRecognitionLambdaFunction"
   

4. Lambda will print the "text" discovered in the image from image processing in the logs.

Input image
![](<image/helloworld1.png>)

```
below are snippets from the logs
	2021-12-02T17:39:59.513-06:00	2021-12-02T23:39:59.513Z 3e08409b-2151-4bfe-b3ea-8b5b9b3e91e7 INFO ========== Detected Text for: helloworld1.png ==========
	2021-12-02T17:39:59.513-06:00	2021-12-02T23:39:59.513Z 3e08409b-2151-4bfe-b3ea-8b5b9b3e91e7 INFO Detected Text: Hello World!
	2021-12-02T17:39:59.513-06:00	2021-12-02T23:39:59.513Z 3e08409b-2151-4bfe-b3ea-8b5b9b3e91e7 INFO Detected Text: 02-Dec-2021
	2021-12-02T17:39:59.513-06:00	2021-12-02T23:39:59.513Z 3e08409b-2151-4bfe-b3ea-8b5b9b3e91e7 INFO Detected Text: 2021, Amazon Web Services, Inc. or its Affiliates. 

```

## Cleanup

1. Delete the stack

    ```bash
    aws cloudformation delete-stack --stack-name STACK_NAME
    ```

1. Confirm the stack has been deleted

    ```bash
    aws cloudformation list-stacks --query "StackSummaries[?contains(StackName,'STACK_NAME')].StackStatus"
    ```


----
Copyright 2021 Amazon.com, Inc. or its affiliates. All Rights Reserved.

SPDX-License-Identifier: MIT-0
