# Automated AI Document Annotation with Amazon S3 Annotations and Amazon Bedrock

This pattern deploys an automated document enrichment pipeline that uses Amazon Bedrock to generate AI-powered metadata and stores it as queryable Amazon S3 annotations.

Learn more about this pattern at Serverless Land Patterns: https://serverlessland.com/patterns/s3-lambda-bedrock-annotations-cdk

Important: this application uses various AWS services and there are costs associated with these services after the Free Tier usage - please see the [AWS Pricing page](https://aws.amazon.com/pricing/) for details. You are responsible for any AWS costs incurred. No warranty is implied in this example.

## Requirements

- [Create an AWS account](https://portal.aws.amazon.com/gp/aws/developer/registration/index.html) if you do not already have one and log in. The IAM user that you use must have sufficient permissions to make necessary AWS service calls and manage AWS resources.
- [AWS CLI](https://docs.aws.amazon.com/cli/latest/userguide/install-cliv2.html) installed and configured
- [Git Installed](https://git-scm.com/book/en/v2/Getting-Started-Installing-Git)
- [Node.js 20+](https://nodejs.org/en/download/) installed
- [AWS CDK v2](https://docs.aws.amazon.com/cdk/v2/guide/getting_started.html) installed (`npm install -g aws-cdk`)
- [Python 3.12](https://www.python.org/downloads/) installed (for building the boto3 layer)
- [Amazon Bedrock model access](https://docs.aws.amazon.com/bedrock/latest/userguide/model-access.html) enabled for Anthropic Claude Sonnet in your account

## Architecture

![Architecture](architecture.png)

1. A file is uploaded to the Amazon S3 bucket.
2. Amazon S3 sends an Object Created event to Amazon EventBridge.
3. An Amazon EventBridge rule triggers the AWS Lambda function.
4. The Lambda function reads the object, invokes Amazon Bedrock (Claude Sonnet) to generate a structured summary, keywords, and content classification.
5. The AI-generated metadata is written back as an S3 annotation using the `PutObjectAnnotation` API.

## Deployment

1. Clone the repository and navigate to the pattern directory:

```bash
git clone https://github.com/aws-samples/serverless-patterns
cd serverless-patterns/s3-lambda-bedrock-annotations-cdk
```

2. Build the boto3 layer (required for S3 Annotations API support):

```bash
cd src/boto3-layer
pip install -r requirements.txt -t python
cd ../..
```

3. Install CDK dependencies and deploy:

```bash
npm install
cdk bootstrap  # if not already done
cdk deploy
```

## Testing

1. Upload a text file to the bucket:

```bash
BUCKET_NAME=$(aws cloudformation describe-stacks --stack-name S3LambdaBedrockAnnotationsStack --query 'Stacks[0].Outputs[?OutputKey==`BucketName`].OutputValue' --output text)

echo "Amazon S3 Annotations is a new feature that allows you to attach rich, queryable metadata directly to S3 objects. Each object supports up to 1000 annotations of up to 1MB each." > sample.txt

aws s3 cp sample.txt s3://$BUCKET_NAME/sample.txt
```

2. Wait ~10 seconds for the Lambda to process, then retrieve the annotation:

```bash
aws s3api get-object-annotation \
  --bucket $BUCKET_NAME \
  --key sample.txt \
  --annotation-name ai-enrichment \
  annotation-output.json

cat annotation-output.json
```

Expected output (example):

```json
{
  "ai_summary": "A brief description of Amazon S3 Annotations, a feature for attaching rich queryable metadata to S3 objects with support for up to 1000 annotations per object.",
  "keywords": ["S3", "annotations", "metadata", "queryable", "objects"],
  "content_type": "article",
  "model": "anthropic.claude-sonnet-4-20250514"
}
```

3. List all annotations on the object:

```bash
aws s3api list-object-annotations \
  --bucket $BUCKET_NAME \
  --key sample.txt
```

## Optional: Enable Annotation Tables for Athena Querying

To query annotations at scale across all objects using Amazon Athena, enable annotation tables:

```bash
aws s3api update-bucket-metadata-annotation-table-configuration \
  --bucket $BUCKET_NAME \
  --annotation-table-configuration '{"ConfigurationState":"ENABLED","Role":"arn:aws:iam::YOUR_ACCOUNT_ID:role/S3MetadataAnnotationRole"}'
```

> **Note**: Annotation table configuration is not yet available via AWS CloudFormation. Use the CLI or SDK to enable it.

## Cleanup

> **Warning**: This will delete the S3 bucket and all objects, including annotations.

```bash
cdk destroy
```

## Useful Commands

| Command | Description |
|---------|-------------|
| `npm install` | Install project dependencies |
| `cdk synth` | Emit the synthesized CloudFormation template |
| `cdk deploy` | Deploy the stack |
| `cdk destroy` | Remove the stack |

---

Copyright 2026 Amazon.com, Inc. or its affiliates. All Rights Reserved.

SPDX-License-Identifier: MIT-0
