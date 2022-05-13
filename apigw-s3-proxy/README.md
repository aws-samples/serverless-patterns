# Amazon API Gateway REST API with S3 integration

The SAM template deploys an Amazon API Gateway REST API endpoint with a read-only S3 integration.

The API exposes 3 GET methods:

* Root GET method: it provides a list of the S3 buckets of the account where the stack is deployed.
* {folder} GET method: it provides a list of the objects contained in the bucket {folder}
* {item} GET method: it returns the contents of the object {item}.

The template also deploys an IAM role with S3 read-only capabilities that is used by API Gateway to integrate with S3.

Since this is API Gateway effectively acts as a proxy S3, every GET method is protected by IAM authentication to prevent public access.

Note: when deploying this pattern, *CAPABILITY_IAM* is required.

Learn more about this pattern at Serverless Land Patterns: [https://serverlessland.com/patterns/apigw-s3-proxy](https://serverlessland.com/patterns/apigw-s3-proxy)

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
    cd apigw-s3-proxy
    ```
3. From the command line, use AWS SAM to deploy the AWS resources for the pattern as specified in the template.yml file:
    ```
    sam deploy -g
    ```
1. During the prompts:
    * Enter a stack name
    * Select the desired AWS Region
    * Allow SAM to create roles with the required permissions if needed.

    Once you have run guided mode once, you can use `sam deploy` in future to use these defaults.

1. Note the outputs from the SAM deployment process. These contain the resource names and/or ARNs which are used for testing.

## Testing

The stack will output the **api endpoint**. Since all the methods are protected with IAM authentication, you can use *Postman* to send a SigV4-signed HTTP request to the API Gateway endpoint.
   
```
https://12345abcde.execute-api.{region}.amazonaws.com/Prod/mybucket/myobject.txt
```

## Cleanup
 
1. Delete the stack
    ```bash
    sam delete
    ```
1. Confirm the stack has been deleted
    ```bash
    aws cloudformation list-stacks --query "StackSummaries[?contains(StackName,'STACK_NAME')].StackStatus"
    ```
----
Copyright 2022 Amazon.com, Inc. or its affiliates. All Rights Reserved.

SPDX-License-Identifier: MIT-0