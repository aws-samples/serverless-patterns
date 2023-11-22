# Amazon Kinesis Data Firehose Data Transformation with AWS Lambda

This pattern deploys a Kinesis Data Firehose Delivery Stream that invokes a Lambda function to transform incoming source data and delivers the transformed data to a destination Amazon S3 bucket. 

Learn more about this pattern at Serverless Land Patterns: [https://serverlessland.com/patterns/firehose-transformation-sam-python](https://serverlessland.com/patterns/firehose-transformation-sam-python)

Important: this application uses various AWS services and there are costs associated with these services after the Free Tier usage - please see the [AWS Pricing page](https://aws.amazon.com/pricing/) for details. You are responsible for any AWS costs incurred. No warranty is implied in this example.

## Requirements

* [Create an AWS account](https://portal.aws.amazon.com/gp/aws/developer/registration/index.html) if you do not already have one and log in. The IAM user that you use must have sufficient permissions to make necessary AWS service calls and manage AWS resources.
* [AWS CLI](https://docs.aws.amazon.com/cli/latest/userguide/install-cliv2.html) installed and configured
* [Git Installed](https://git-scm.com/book/en/v2/Getting-Started-Installing-Git)
* [AWS Serverless Application Model Command Line Interface](https://docs.aws.amazon.com/serverless-application-model/latest/developerguide/serverless-sam-cli-install.html) (AWS SAM CLI) installed

## Deployment Instructions

1. Create a new directory, navigate to that directory in a terminal and clone the GitHub repository:
    ``` 
    git clone https://github.com/aws-samples/serverless-patterns
    ```
1. Change directory to the pattern directory:
    ```
    cd serverless-patterns/firehose-transformation-sam-python
    ```
1. From the command line, use AWS SAM to build and deploy the AWS resources for the pattern as specified in the template.yml file:
    ```
    sam build
    sam deploy --guided
    ```
1. During the prompts:
    * Enter a stack name
    * Enter the desired AWS Region
    * Enter a bucket name
    * Allow SAM CLI to create IAM roles with the required permissions.

    Once you have run `sam deploy --guided` mode once and saved arguments to a configuration file (samconfig.toml), you can use `sam deploy` in future to use these defaults.

1. Note the outputs from the SAM deployment process. These contain the resource names and/or ARNs which are used for testing.

## How it works

Kinesis Data Firehose can invoke a Lambda function to transform incoming source data and deliver the transformed data to destinations. In this architecture, Kinesis Data Firehose invokes the specified Lambda function asynchronously with each buffered batch using the AWS Lambda synchronous invocation mode. The transformed data is sent from Lambda to Kinesis Data Firehose. Kinesis Data Firehose then sends it to the destination S3 bucket when the specified destination buffering size or buffering interval is reached, whichever happens first.

## Testing

1. Open the Kinesis Data Firehose console at https://console.aws.amazon.com/firehose/

2. Choose the {stack-name}-DeliveryStream-{stream-id} delivery stream

3. Under **Test with demo data**, choose **Start sending demo data** to generate sample stock ticker data.

4. After a few seconds, choose **Stop sending demo data**

5. Verify that test events are being sent to the destination S3 bucket. Note that it might take a few minutes for new objects to appear in the bucket, based on the buffering configuration.

```
aws s3 ls s3://{destination_bucket_name} --recursive --human-readable --summarize
```

Or nagivate to the S3 console and manually verify that the demo data has been sent to S3

## Cleanup
 
From the command line, use AWS SAM CLI to delete the AWS CloudFormation stack

```
sam delete
```

----
Copyright 2023 Amazon.com, Inc. or its affiliates. All Rights Reserved.

SPDX-License-Identifier: MIT-0