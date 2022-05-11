# Amazon API Gateway REST API with VPC Link integration

The SAM template deploys an Amazon API Gateway REST API endpoint with a VPC Link integration.

Since REST APIs only support VPC Links associated with NLBs (Network Load Balancers), this pattern assumes that an internal NLB already exists in a VPC in the same Region.

Note: when deploying this pattern, *CAPABILITY_IAM* is required.

Learn more about this pattern at Serverless Land Patterns: [https://serverlessland.com/patterns/apigw-rest-api-vpclink](https://serverlessland.com/patterns/apigw-rest-api-vpclink)

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
    cd apigw-rest-api-vpclink
    ```
3. From the command line, use AWS SAM to deploy the AWS resources for the pattern as specified in the template.yml file:
    ```
    sam deploy -g
    ```
1. During the prompts:
    * Enter a stack name
    * Select the desired AWS Region
    * Enter the DNS name for the internal NLB (NlbInternalDns)
    * Enter the ARN for the internal NLB (NlbInternalArn)
    * Allow SAM to create roles with the required permissions if needed.

    Once you have run guided mode once, you can use `sam deploy` in future to use these defaults.

1. Note the outputs from the SAM deployment process. These contain the resource names and/or ARNs which are used for testing.

## Testing

The stack will output the **api endpoint**. You can use *curl* to send a HTTP request to the API Gateway endpoint to test the VPC Link integration.
   
```
curl https://12345abcde.execute-api.{region}.amazonaws.com/Prod/
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