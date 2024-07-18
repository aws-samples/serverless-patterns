# Document embeddings for Amazon Bedrock using Amazon S3/AWS Lambda/Amazon OpenSearch Serverless

This pattern can be used to automatically create embeddings using Amazon Bedrock for documents uploaded to an Amazon S3 bucket and store the embeddings along with the document content in an Amazon OpenSearch Serverless index.

This pattern is useful for RAG-based applications that use Amazon S3 as source for the knowledge base for their LLM models. The pattern helps to seamlessly create and store the embeddings for new documents once they are upload to S3.

Learn more about this pattern at Serverless Land Patterns: https://serverlessland.com/patterns/s3-lambda-bedrock-aoss

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
    cd s3-lambda-bedrock-aoss
    ```
3. Build the layers and prepare the application for deployment
    ```
    sam build
    ```
4. Use AWS SAM to deploy the AWS resources for the pattern as specified in the template.yml file:
    ```
    sam deploy --guided
    ```
5. During the prompts:
    * Enter a stack name
    * Enter the desired AWS Region
    * For template parameters, accept the default values or provide your own values
    * Allow SAM CLI to create IAM roles with the required permissions.

    Once you have run `sam deploy --guided` mode once and saved arguments to a configuration file (samconfig.toml), you can use `sam deploy` in future to use these defaults.

1. Note the outputs from the SAM deployment process. These contain the resource names and/or ARNs which are used for testing.

## How it works
This pattern creates the follow resources an S3 Bucket, an EventBridge Rule, two Lambda functions and an OpenSearch collection with a vector index.

When a new document is uploaded to S3, EventBridge receives an S3 <code>Object Created</code> event. An Event rule is configured to match the S3 <code>Object Created</code> and trigger a Lambda function. The Lambda function downloads the document, extracts content of each page in the document. The Lambda function code then iterates through the pages, invokes Amazon Titan Embeddings model to create embeddings for each page. The  embeddings along with the page content are then stored in a vector index in a OpenSearch Serverless collection.

Only PDF documents are currently supported

## Testing

1. Upload a pdf document to S3. You can provide your own or use the example.pdf provided in  ```examples``` folder

    ```
    aws s3 cp examples/example.pdf s3://<SourceBucketName>
    ```

2. Tail the Amazon CloudWatch log group for the Lambda function to follow the log outputs from the Lambda

    ```
    aws logs tail /aws/lambda/<DocumentIngestionLambdaFunctionName>
    ```

### Sample Output
Processing document key example.pdf from  Bucket serverless-vectorization-sourcebucket-xmpxwbn1ar3i

    Downloaded file to local path /tmp/example.pdf
    Extracted 1 pages
    Created embeddings for page #1
    Indexed content for page #1
    Finished Processing document. 1 document page(s) indexed

## Cleanup

1. Delete the stack
    ``` 
    sam delete
    ```
2. Confirm the stack has been deleted
    ```
    aws cloudformation list-stacks --query "StackSummaries[?contains(StackName,'STACK_NAME')].StackStatus"
    ```

> [!NOTE]  
> Before deleting the template, make sure to empty the source bucket after backing up any neccessary documents


----
Copyright 2024 Amazon.com, Inc. or its affiliates. All Rights Reserved.

SPDX-License-Identifier: MIT-0