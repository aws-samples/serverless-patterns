# Amazon API Gateway HTTP API to invoke AWS Step Functions Express synchronous workflow using intrinsic functions & prompt chaining to Amazon Bedrock.

The SAM template deploys an Amazon API Gateway HTTP API endpoint along with an Express State machine. This setup illustrates how we can invoke an Express State machine synchronously and using StepFunctions intrinsic functions to chain two prompts to invoke Amazon Bedrock. 
Output is return back from the execution to the client (within 29 seconds) using HTTP API. 
This no-code example demonstrates how results from the first prompt are then used to provide the second prompt with context. Chaining of these prompts augments the ability of the language model being used to deliver a highly-curated response.

Learn more about this pattern at [Serverless Land Patterns](https://serverlessland.com/patterns/apigw-rest-stepfunctions-express-sync-bedrock-sam)

Important: this application uses various AWS services and there are costs associated with these services after the Free Tier usage - please see the [AWS Pricing page](https://aws.amazon.com/pricing/) for details. You are responsible for any AWS costs incurred. No warranty is implied in this example.

## Requirements

* [Create an AWS account](https://portal.aws.amazon.com/gp/aws/developer/registration/index.html) if you do not already have one and log in. The IAM user that you use must have sufficient permissions to make necessary AWS service calls and manage AWS resources.
* [AWS CLI](https://docs.aws.amazon.com/cli/latest/userguide/install-cliv2.html) installed and configured
* [Git Installed](https://git-scm.com/book/en/v2/Getting-Started-Installing-Git)
* [AWS Serverless Application Model](https://docs.aws.amazon.com/serverless-application-model/latest/developerguide/serverless-sam-cli-install.html) (AWS SAM) installed
* [Manage Access to Amazon Bedrock Foundation Models](https://docs.aws.amazon.com/bedrock/latest/userguide/model-access.html) at the time of writing this example uses the Amazon Bedrock foundation model cohere.command-text-v14


## Deployment Instructions

1. Create a new directory, navigate to that directory in a terminal and clone the GitHub repository:
    ``` 
    git clone https://github.com/aws-samples/serverless-patterns
    ```
2. Change directory to the pattern directory:
    ```
    cd apigw-rest-stepfunctions-express-sync-bedrock-sam
    ```
3. From the command line, use AWS SAM to deploy the AWS resources for the pattern as specified in the template.yml file:
    ```
    sam deploy 
    ```
4. During the prompts:
    * Enter a stack name
    * Select the desired AWS Region
    * Allow SAM to create roles with the required permissions if needed.

5. Note the outputs from the SAM deployment process. These contain the resource names and/or ARNs which are used for testing.
 

## Testing

The stack will output the **api endpoint**. You can use *Postman* or *curl* to send a POST request to the API Gateway endpoint.
   
```
curl -H "Content-type: application/json" -X POST -d '{"prompt_one": "Write a 500 word blog post on The Beatles"}' <Your Sync WF API endpoint>

```
After runnning the above command, API Gateway will invoke the State machine and return the complete results back to the client instead of just the State machine's execution Id. 

## Cleanup
 
1. Delete the stack
    ```bash
    sam delete
    ```
2. Confirm the stack has been deleted
    ```bash
    aws cloudformation list-stacks --query "StackSummaries[?contains(StackName,'STACK_NAME')].StackStatus"
    ```
----
Copyright 2022 Amazon.com, Inc. or its affiliates. All Rights Reserved.

SPDX-License-Identifier: MIT-0