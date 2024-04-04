# Amazon Kinesis Data Firehose Data Transformation with AWS Lambda

This pattern demonstrates how to transform streaming data received by Amazon Kinesis Data Firehose using AWS Lambda before delivering the transformed data to Amazon S3.

The pattern uses the AWS Cloud Development Kit (AWS CDK) to deploy a Kinesis Data Firehose delivery stream, a Lambda function to transform source data, and an Amazon S3 bucket to receive the transformed data. 

Learn more about this pattern at Serverless Land Patterns: https://serverlessland.com/patterns/firehose-transformation-cdk-typescript

Important: this application uses various AWS services and there are costs associated with these services after the Free Tier usage - please see the [AWS Pricing page](https://aws.amazon.com/pricing/) for details. You are responsible for any AWS costs incurred. No warranty is implied in this example.

## Requirements

* [Create an AWS account](https://portal.aws.amazon.com/gp/aws/developer/registration/index.html) if you do not already have one and log in. The IAM user that you use must have sufficient permissions to make necessary AWS service calls and manage AWS resources.
* [AWS CLI](https://docs.aws.amazon.com/cli/latest/userguide/install-cliv2.html) installed and configured
* [Git Installed](https://git-scm.com/book/en/v2/Getting-Started-Installing-Git)
* [AWS CDK](https://docs.aws.amazon.com/cdk/latest/guide/cli.html) installed and configured

## Deployment Instructions

1. Create a new directory, navigate to that directory in a terminal and clone the GitHub repository:
    ```
    git clone https://github.com/aws-samples/serverless-patterns
    ```
1. Change directory to the pattern directory:
    ```
    cd serverless-patterns/firehose-transformation-cdk-typescript/src
    ```
1. Install dependencies:
   ```
   npm install
   ```
1. Bootstrap environment (if you have not done so already)
    ```
    cdk bootstrap
    ```
1. Deploy the stack to your default AWS account and region.
    ```
    cdk deploy
    ```

## How it works

Kinesis Data Firehose can invoke a Lambda function to transform incoming source data and deliver the transformed data to destinations. In this architecture, Kinesis Data Firehose invokes the specified Lambda function asynchronously with each buffered batch using the AWS Lambda synchronous invocation mode. The transformed data is sent from Lambda to Kinesis Data Firehose. Kinesis Data Firehose then sends it to the destination S3 bucket when the specified destination buffering size or buffering interval is reached, whichever happens first.

## Testing

1. Open the Kinesis Data Firehose console at https://console.aws.amazon.com/firehose/

2. Choose the {stack-name}-firehosestream-{stream-id} delivery stream

3. Under **Test with demo data**, choose **Start sending demo data** to generate sample stock ticker data.

4. After a few seconds, choose **Stop sending demo data**

5. Verify that test events are being sent to the destination S3 bucket. Note that it might take a few minutes for new objects to appear in the bucket, based on the buffering configuration.

    ```
    aws s3 ls s3://{destination_bucket_name} --recursive --human-readable --summarize
    ```

    Or nagivate to the S3 console and manually verify that the demo data has been sent to S3

## Cleanup
 
Run the following command to delete the resources

```bash
cdk destroy
```

----
Copyright 2023 Amazon.com, Inc. or its affiliates. All Rights Reserved.

SPDX-License-Identifier: MIT-0