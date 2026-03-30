# Amazon S3 to AWS Lambda to Amazon Bedrock AgentCore
This pattern creates an AWS Lambda function to invoke an agent in AgentCore Runtime when an object is uploaded to the Amazon S3 bucket.

This Terraform template creates 2 S3 buckets (input and output), an AWS Lambda Function, and an agent in AgentCore Runtime.

Learn more about this pattern at Serverless Land Patterns: https://serverlessland.com/patterns/s3-lambda-agentcore

Important: this application uses various AWS services and there are costs associated with these services after the Free Tier usage - please see the AWS Pricing page for details. You are responsible for any AWS costs incurred. No warranty is implied in this example.

## Requirements

* [Create an AWS account](https://portal.aws.amazon.com/gp/aws/developer/registration/index.html) if you do not already have one and log in. The IAM user that you use must have sufficient permissions to make necessary AWS service calls and manage AWS resources.
* [AWS CLI](https://docs.aws.amazon.com/cli/latest/userguide/install-cliv2.html) installed and configured
* [Git Installed](https://git-scm.com/book/en/v2/Getting-Started-Installing-Git)
* [Terraform](https://developer.hashicorp.com/terraform/tutorials/aws-get-started/install-cli) (Terraform) installed
* [Docker](https://docs.docker.com/get-docker/) installed and running (required for building the agent container image)

## Deployment Instructions

1. Create a new directory, navigate to that directory in a terminal and clone the GitHub repository:

`git clone https://github.com/aws-samples/serverless-patterns`

2. Change directory to the pattern directory:

`cd serverless-patterns/s3-lambda-agentcore`

3. From the command line, initialize terraform to download and install the providers defined in the configuration:

`terraform init`

4. From the command line, apply the configuration in the deploy.tf file:

`terraform apply`

1. When prompted, enter `yes` to confirm the deployment

2. Note the outputs from the deployment process, these contain the resource names and/or ARNs which are used for testing.

## How it works 

S3 will invoke the Lambda function when an object is created or updated. It will pass metadata about the new object in the event argument of the Lambda invocation.

The lambda function will invoke the agent and pass a uri for the s3 file. 

The agent will categorize the file as architecture, runbook, or other and identify some metadata. Then it will send the results back to the Lambda function as JSON. 

The Lambda function will write the metadata to the S3 output bucket.

## Testing

Ensure you're in the correct directory (`cd serverless-patterns/s3-lambda-agentcore`). Then run the following script to test with files in the `./test-files` folder. 

```bash
# upload test files to the input bucket
aws s3 cp ./test-files/ s3://$(terraform output -raw s3_input_bucket)/ --recursive
# wait for the agent to process the files
sleep 10
# download the metadata from the output bucket
aws s3 cp s3://$(terraform output -raw s3_output_bucket)/ ./metadata/  --recursive
```
You can view the metadata in `./metadata`

## Cleanup

1. Ensure you're in the correct directory (`cd serverless-patterns/s3-lambda-agentcore`)

2. Delete all created resources: 

`terraform destroy`

3. When prompted, enter `yes` to confirm the destruction

4. Confirm all created resources has been deleted: 

`terraform show`

---

Copyright 2026 Amazon.com, Inc. or its affiliates. All Rights Reserved.

SPDX-License-Identifier: MIT-0