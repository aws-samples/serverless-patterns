# S3 to Lambda to Bedrock Embeddings

This pattern explains how to deploy a SAM application with Amazon S3, AWS Lambda and Amazon Bedrock.

This pattern is useful for LLM RAG Usecases in getting vector embeddings of the documents uploaded to S3 via S3 event notification. Once the files are placed in S3, AWS Lambda picks up the files via event notification and post the content to Amazon Bedrock embedding model and gets the vector embedding of the content as response. 

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
1. Change directory to the pattern directory:
    ```
    cd s3-lambda-bedrock
    ```
1. From the command line, use AWS SAM to deploy the AWS resources for the pattern as specified in the template.yml file:
    ```
    sam build
    sam deploy --guided
    ```
1. During the prompts:
    * Enter a stack name
    * Enter the desired AWS Region
    * Enter the ContentBucketName - Provide a n ame for a new S3 bucket which will be created
    * Allow SAM CLI to create IAM roles with the required permissions.

    Once you have run `sam deploy --guided` mode once and saved arguments to a configuration file (samconfig.toml), you can use `sam deploy` in future to use these defaults.

1. Note the outputs from the SAM deployment process. These contain the resource names and/or ARNs which are used for testing.

## How it works

The Amazon S3 event notification listens for a putobject api operation and when a new object is uploaded to the bucket,  Amazon S3 invokes your function asynchronously with an event that contains details about the object. With the object details in the event Lambda reads the content of the object and call Amazon Bedrock Titan Embedding service to get the vector embeddings of the object content.


## Testing

Create a text document with some content and upload it to the S3 bucket (bucket details in sam deploy output). You will be able to validate the lambda response in Cloudwatch Logs LogGroup.

1. Tail to the Lambda function log to get the logs
```
aws logs tail "/aws/lambda/BedrockEmb" --follow --format json 
```
2. Upload the sample file to S3 using below command. Please note the file needs to uploaded to a directory named "content". Refer below for example
```
aws s3 cp sampletext.txt s3://<bucketName>/content/
```

### Sample Output:
You should be able to get the output in the log tails windows in the embedding format similar to below. This is the vector embedding of the content of the file we uploaded to S3. 
```
{'embedding': [-0.26367188, 0.12011719, 0.34375, 0.23144531, 0.042236328, 0.24316406, -0.34570312, 3.9815903e-05, 0.04711914, -0.3828125, 0.19921875, 0.12011719, 0.20019531, 0.2109375, -0.375, 0.076660156, -0.067871094, 0.5078125, 0.0009765625, -0.076660156, -0.26953125, 0.09277344, -0.23632812, -0.07421875, 0.42578125, -0.11279297, -0.3671875, 0.22265625, 0.055664062, 0.2578125, -0.75390625, -0.7421875, 0.48242188, 0.064941406, -0.095214844, -0.047607422, 0.032226562, 0.20019531, 0.16796875, 0.16015625, 0.56640625, -0.859375, -0.053955078, -0.55078125, 0.08496094, 0.1953125, 0.16796875, 0.515625, 0.43945312, -0.15625, -0.08154297, -0.072265625, -0.36328125, -0.029785156, 0.42578125, 0.2109375, -0.40429688, 0.055908203, -0.3984375, 0.19628906, 0.2890625, 0.31445312, -0.21777344, -0.26367188, -0.25195312, -0.13183594, 0.24902344, -0.46484375, 0.12597656, 0.18261719, -0.43359375, 0.05908203, 0.390625, -0.25976562, 0.53515625, 0.5234375, -0.43554688, 0.06738281, 0.25585938, -0.29492188, -0.072753906, 0.10253906, 0.23535156, 0.375, 0.30273438, 0.58203125, -0.30664062, 0.22363281, 0.00012302399, -0.52734375, -0.3359375, 0.04272461, 0.296875, 0.42382812]}
```

## Cleanup
 
1. Delete the stack
```
    sam delete
```
----
Copyright 2023 Amazon.com, Inc. or its affiliates. All Rights Reserved.

SPDX-License-Identifier: MIT-0
