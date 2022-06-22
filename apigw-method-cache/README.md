# Amazon API Gateway REST API with cache enabled

The SAM template deploys an Amazon API Gateway REST API endpoint with a method-level cache.
The GET method on the root resource / is enabled with a cache and TTL (Time-To-Live) of 10 seconds.
Any requests made within this 10 second period will be a cache hit and the cached response will be returned by API Gateway immediately without invoking the Lambda integration.
The Lambda integration returns a timestamp in the header so that it is easy to visualize whether a particular response is being returned as a cached response or as a response from the Lambda integration.


Note: when deploying this pattern, *CAPABILITY_IAM* is required.

Learn more about this pattern at Serverless Land Patterns: [https://serverlessland.com/patterns/apigw-method-cache](https://serverlessland.com/patterns/apigw-method-cache)

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
    cd apigw-method-cache
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

The stack will output the **api endpoint**. Please allow a few minutes for the cache to be created. Once the Cache status has switched from **CREATE_IN_PROGRESS** to **AVAILABLE**, you can make an HTTP request to the endpoint using *curl* to test the method-level cache.

```
curl -i https://{apiId}.execute-api.{region}.amazonaws.com/Prod
```
The *-i* flag will output the returned headers. Check the header *timestamp* to determine whether the response is cached or a fresh response from the Lambda integration.   

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