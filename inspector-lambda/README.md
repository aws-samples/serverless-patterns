# Amazon Inspector to AWS Lambda

This pattern demonstrates how to use an AWS Lambda to filter and process Amazon Inspector Findings, then send them to S3 for archiving or analysis.

Amazon Inspector is a vulnerability management service that continuously scans your AWS workloads for software vulnerabilities and unintended network exposure. Amazon Inspector automatically discovers and scans running Amazon EC2 instances, container images in Amazon Elastic Container Registry (Amazon ECR), and AWS Lambda functions for known software vulnerabilities and unintended network exposure.

Amazon Inspector creates a finding when it discovers a software vulnerability or network configuration issue. A finding describes the vulnerability, identifies the affected resource, rates the severity of the vulnerability, and provides remediation guidance.

This pattern deploys two Amazon EventBridge rules that forward Amazon Inspector Findings and Initial Scan events to Lambda functions. There are two Lambda functions, one that processes Amazon Inspector Findings, and one that processes Amazon Inspector initial scans. The Lambda functions send the processed events to a partitioned S3 Bucket.

Learn more about this pattern at Serverless Land Patterns: [Serverless Land](https://serverlessland.com/patterns/inspector-lambda)

Important: this application uses various AWS services and there are costs associated with these services after the Free Tier usage - please see the [AWS Pricing page](https://aws.amazon.com/pricing/) for details. You are responsible for any AWS costs incurred. No warranty is implied in this example.

## Requirements

* [Create an AWS account](https://portal.aws.amazon.com/gp/aws/developer/registration/index.html) if you do not already have one and log in. The IAM user that you use must have sufficient permissions to make necessary AWS service calls and manage AWS resources.
* [AWS CLI](https://docs.aws.amazon.com/cli/latest/userguide/install-cliv2.html) installed and configured
* [Git Installed](https://git-scm.com/book/en/v2/Getting-Started-Installing-Git)
* [AWS Cloud Development Kit](https://docs.aws.amazon.com/cdk/v2/guide/getting_started.html) (AWS CDK) installed

## Deployment Instructions

1. Create a new directory, navigate to that directory in a terminal and clone the GitHub repository:
    ``` 
    git clone https://github.com/aws-samples/serverless-patterns
    ```
2. Change directory to the pattern directory:
    ```
    cd inspector-lambda
    ```
3. If you have not deployed a CDK application in your account yet, bootstap the CDK environment:
    ```
    cdk bootstrap
    ```
4. From the command line, use AWS CDK to deploy the AWS resources for the pattern as specified in the app.py file:
    ```
    cdk deploy
    ```

5. Note the outputs from the CDK deployment process. These contain the resource names and/or ARNs which are used for testing.

The CDK template does not enable Amazon Inspector in the deployment account. To use this pattern, ensure that Amazon Inspector is already enabled. 

## How it works

Explain how the service interaction works.

## Testing

To determine that the pattern deployment was successful confirm that the stack was successfully deployed via the CLI output. 

To test the functionality, deploy a new Lambda Function in the test account. Verify in the AWS Console the Amazon Inspector is monitoring the new Lambda Function. In the console, navigate to CloudFormation and view the Resources associated with the InspectorCdkStack stack. Navigate to the S3 bucket deployed by the CDK stack, confirm that there are Inspector initial scan results in the S3 bucket. 

You can also confirm this from the CLI:
```
aws s3 ls s3://{destination bucket name} --recursive --human-readable --summarize
```

## Cleanup
 
1. Delete the stack
    ```bash
    cdk destroy
    ```

----
Copyright 2023 Amazon.com, Inc. or its affiliates. All Rights Reserved.

SPDX-License-Identifier: MIT-0
