# AWS Service 1 to AWS Service 2

This pattern creates a CloudFront distribution with an S3 origin secured with origin access control (OAC).

Learn more about this pattern at Serverless Land Patterns: https://serverlessland.com/patterns/cloudfront-s3-oac-sam

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
    cd cloudfront-s3-oac-sam
    ```
1. From the command line, use AWS SAM to deploy the AWS resources for the pattern as specified in the template.yml file:
    ```
    sam deploy --guided
    ```
1. During the prompts:
    * Enter a stack name
    * Enter the desired AWS Region
    * Enter the DeploymentName parameter
    * Allow SAM CLI to create IAM roles with the required permissions.

    Once you have run `sam deploy --guided` mode once and saved arguments to a configuration file (samconfig.toml), you can use `sam deploy` in future to use these defaults.

1. Note the outputs from the SAM deployment process. These contain the resource names and/or ARNs which are used for testing.

## How it works

The CloudFront distribution has an S3 origin configured with OAC. The S3 bucket has a policy applied allowing read-only access only from the CloudFront distribution OAC.

## Testing

1. Copy the sample site to the S3 bucket.
    ```
    aws s3 cp sample-site/index.html s3://<<YOUR BUCKET NAME HERE>>/index.html
    ```

1. In a web browser, navigate to the CloudFront distribution domain name (`CloudFrontDomain`) from the stack outputs.

## Cleanup
 
1. Delete the sample site from the S3 bucket.
    ```
    aws s3 rm s3://<<YOUR BUCKET NAME HERE>>/index.html
    ```

1. Delete the stack
    ```
    sam delete
    ```

----
Copyright 2023 Amazon.com, Inc. or its affiliates. All Rights Reserved.

SPDX-License-Identifier: MIT-0