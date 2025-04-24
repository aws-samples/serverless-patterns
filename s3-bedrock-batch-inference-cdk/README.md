# Amazon S3 to Amazon Bedrock Batch Inference using an Amazon EventBridge Rule

This pattern demonstrates how to trigger a Bedrock batch inference job when an object, that is the input to the batch inference job, is uploaded to S3. The pattern is implemented using AWS CDK.

Learn more about this pattern at [Serverless Land Patterns](https://serverlessland.com/patterns/s3-eventbridge-bedrock-batch-cdk)

Important: this application uses various AWS services and there are costs associated with these services after the Free Tier usage - please see the AWS Pricing page for details. You are responsible for any AWS costs incurred. No warranty is implied in this example.

## Requirements

- [Create an AWS account](https://portal.aws.amazon.com/gp/aws/developer/registration/index.html) if you do not already have one and log in. The IAM user that you use must have sufficient permissions to make necessary AWS service calls and manage AWS resources.
- [Access to the Bedrock foundation model](https://docs.aws.amazon.com/bedrock/latest/userguide/model-access-modify.html) that you want to use is granted 
- [AWS CLI](https://docs.aws.amazon.com/cli/latest/userguide/install-cliv2.html) installed and configured
- [Git Installed](https://git-scm.com/book/en/v2/Getting-Started-Installing-Git)
- [AWS CDK](https://docs.aws.amazon.com/cdk/latest/guide/cli.html) installed and configured
- [Python 3.13](https://www.python.org/downloads/) installed

## Deployment Instructions

1. Create a new directory, navigate to that directory in a terminal and clone the GitHub repository:
    ```shell
    git clone https://github.com/aws-samples/serverless-patterns
    ```
2. Change directory to the pattern directory:
    ```shell
    cd s3-bedrock-batch-inference-cdk
    ```
3. Deploy the stack:
   Replace the `ModelARN` with the arn of the model you want to use.
   ```shell
   cdk deploy --parameters ModelARN=arn:aws:bedrock:us-west-2::foundation-model/anthropic.claude-3-sonnet-20240229-v1:0
   ```

## How it works
![End to End Architecture](images/architecture.png)

This pattern creates an S3 bucket to store the input and output of the batch inference job. It also creates an EventBridge rule that is triggered when a batch inference input file is uploaded. EventBridge will create a new Bedrock batch inference job with the specified model. The output of the job is also stored in the same S3 bucket.

## Testing
 - Once the pattern is deployed successfully you should see the name of the S3 bucket in the output.
 - Upload the sample `input.jsonl` to this bucket by running this command
   
  ```shell
   aws s3 cp model_input/input.jsonl  s3://bedrockbatchinferencepatt-bedrockbatchinferencebuc-kbjlcequyqzo/input/
   ```

 - The upload will trigger the batch inference job. You can check the status of the jobs by running this command:
```shell
  aws bedrock list-model-invocation-jobs  | jq '.invocationJobSummaries[] | {jobArn, status, submitTime}'

```

 - You can monitor the job status in the AWS Console

## Cleanup

1. Delete the stack
   ```bash
   cdk destroy
   ```

---

Copyright 2025 Amazon.com, Inc. or its affiliates. All Rights Reserved.

SPDX-License-Identifier: MIT-0
