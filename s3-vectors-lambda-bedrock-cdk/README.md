# S3 Vectors with Lambda and Amazon Bedrock RAG

This pattern deploys a serverless RAG (Retrieval-Augmented Generation) pipeline using Amazon S3 Vectors for vector storage, Lambda for orchestration, and Amazon Bedrock for embeddings and text generation.

Learn more about this pattern at Serverless Land Patterns: https://serverlessland.com/patterns/s3-vectors-lambda-bedrock-cdk

Important: this application uses various AWS services and there are costs associated with these services after the Free Tier usage - please see the [AWS Pricing page](https://aws.amazon.com/pricing/) for details. You are responsible for any AWS costs incurred. No warranty is implied in this example.

## Requirements

* [Create an AWS account](https://portal.aws.amazon.com/gp/aws/developer/registration/index.html) if you do not already have one and log in.
* [AWS CLI](https://docs.aws.amazon.com/cli/latest/userguide/install-cliv2.html) installed and configured
* [Git Installed](https://git-scm.com/book/en/v2/Getting-Started-Installing-Git)
* [Node.js 18+](https://nodejs.org/en/download/) installed
* [AWS CDK v2](https://docs.aws.amazon.com/cdk/v2/guide/getting-started.html) installed
* [Amazon Bedrock model access](https://docs.aws.amazon.com/bedrock/latest/userguide/model-access.html) enabled for Amazon Titan Text Embeddings V2 and Anthropic Claude Sonnet

## Architecture

```
                    ┌──────────────────────────────────────────────────────┐
                    │                  S3 Vector Bucket                     │
                    │  ┌──────────────────────────────────┐                │
                    │  │  Vector Index (1024-dim, cosine)  │                │
                    │  └──────────────────────────────────┘                │
                    └──────────────┬───────────────┬───────────────────────┘
                                   │               │
                    ┌──────────────┴──┐   ┌───────┴──────────────┐
                    │  Ingest Lambda   │   │  Query Lambda         │
                    │  (embed + store) │   │  (search + generate)  │
                    └────────┬─────────┘   └────────┬──────────────┘
                             │                      │
                    ┌────────┴──────────────────────┴──────────┐
                    │           Amazon Bedrock                  │
                    │  Titan Embeddings V2  │  Claude Sonnet    │
                    └──────────────────────────────────────────┘
```

## How it works

**Ingest flow:**
1. Invoke the Ingest Lambda with an array of text documents.
2. Lambda calls Bedrock Titan Embeddings V2 to generate 1024-dimensional vectors.
3. Vectors are stored in an S3 vector index with metadata (source text, timestamp).

**Query flow:**
1. Invoke the Query Lambda with a natural language question.
2. Lambda embeds the question using the same Titan model.
3. Lambda queries S3 Vectors for the top-K most similar documents.
4. Retrieved context is sent to Bedrock Claude to generate a grounded answer.

## Deployment Instructions

1. Clone the repository:
    ```bash
    git clone https://github.com/aws-samples/serverless-patterns
    cd serverless-patterns/s3-vectors-lambda-bedrock-cdk
    ```

2. Install dependencies:
    ```bash
    npm install
    ```

3. Deploy the stack:
    ```bash
    cdk deploy
    ```

4. Note the function names from the stack outputs.

## Testing

1. Ingest sample documents:
    ```bash
    aws lambda invoke \
      --function-name <IngestFunctionName> \
      --payload '{
        "documents": [
          {"key": "serverless", "text": "Serverless computing lets you run code without managing servers. AWS Lambda automatically scales your application."},
          {"key": "containers", "text": "Containers package applications with their dependencies. Amazon ECS and EKS manage container orchestration."},
          {"key": "s3-vectors", "text": "Amazon S3 Vectors provides purpose-built vector storage for AI applications with sub-second query latency."}
        ]
      }' \
      --cli-binary-format raw-in-base64-out \
      ingest-output.json
    ```

2. Query with a question:
    ```bash
    aws lambda invoke \
      --function-name <QueryFunctionName> \
      --payload '{"question": "How do I store vectors for AI applications?"}' \
      --cli-binary-format raw-in-base64-out \
      query-output.json

    cat query-output.json | jq .
    ```

## Cleanup

1. Delete vectors and the vector index manually (S3 Vectors resources are not managed by CloudFormation):
    ```bash
    aws s3vectors delete-vector-index \
      --vector-bucket-name <VectorBucketName> \
      --index-name knowledge-base

    aws s3vectors delete-vector-bucket \
      --vector-bucket-name <VectorBucketName>
    ```

2. Delete the CDK stack:
    ```bash
    cdk destroy
    ```

----
Copyright 2026 Amazon.com, Inc. or its affiliates. All Rights Reserved.

SPDX-License-Identifier: MIT-0
