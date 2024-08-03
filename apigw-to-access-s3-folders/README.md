## API Gateway - Workaround for directly reading Files, Folders, and Sub-folders in AWS S3

The context and purpose of this workaround documentation is to provide a step-by-step guide and explanation for a specific approach to directly read files, folders, and sub-folders in an AWS S3 bucket using AWS API Gateway.

This would be helpful in reducing the latency of API requests, use API Gateway without a Lambda function to create Amazon S3 bucket resources. This method can also reduce costs and make your system easier to maintain and troubleshoot.

*Note: The API Gateway and S3 bucket should be in same region.*

Learn more about this pattern at Serverless Land Patterns: << Add the live URL here >>

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
    cd apigw-to-access-s3-folders
    ```
1. From the command line, use AWS SAM to deploy the AWS resources for the pattern as specified in the template.yml file:
    ```
    sam deploy --guided
    ```
1. During the prompts:
    * Enter a stack name
    * Enter the desired AWS Region
    * Allow SAM CLI to create IAM roles with the required permissions.

    Once you have run `sam deploy --guided` mode once and saved arguments to a configuration file (samconfig.toml), you can use `sam deploy` in future to use these defaults.

1. Note the outputs from the SAM deployment process. These contain the resource names and/or ARNs which are used for testing.

## Testing
**From API Gateway Console**
1. Open the API Gateway console.
2. In the **Resource** section, select your API, and then select your **GET** method.
3. In the **Test** field, please enter the following. 
* folder - S3 bucket name (eg: testbucket).
* item - Path to your file name along with your file name (eg: folder1/folder2/index.html).
3. Click **Test**.

**From Postman**

Select **GET** method from drop down and enter the Request URL in below format
```
https://apigatewayid.execute-api.us-east-1.amazonaws.com/testbucket/folder1/folder2/index.html
```

## Cleanup
 
1. Delete the stack
    ```bash
    aws cloudformation delete-stack --stack-name STACK_NAME
    ```
1. Confirm the stack has been deleted
    ```bash
    aws cloudformation list-stacks --query "StackSummaries[?contains(StackName,'STACK_NAME')].StackStatus"
    ```
----
Copyright 2023 Amazon.com, Inc. or its affiliates. All Rights Reserved.

SPDX-License-Identifier: MIT-0