# Amazon Route53 to Amazon API Gateway failover

This pattern creates a simple application with failover records in Route53

Learn more about this pattern at Serverless Land Patterns: [https://serverlessland.com/patterns/apigw-route53-failover](https://serverlessland.com/patterns/apigw-route53-failover)

Important: this application uses various AWS services and there are costs associated with these services after the Free Tier usage - please see the [AWS Pricing page](https://aws.amazon.com/pricing/) for details. You are responsible for any AWS costs incurred. No warranty is implied in this example.

## Requirements

* [Create an AWS account](https://portal.aws.amazon.com/gp/aws/developer/registration/index.html) if you do not already have one and log in. The IAM user that you use must have sufficient permissions to make necessary AWS service calls and manage AWS resources.
* [AWS CLI](https://docs.aws.amazon.com/cli/latest/userguide/install-cliv2.html) installed and configured
* [Git Installed](https://git-scm.com/book/en/v2/Getting-Started-Installing-Git)
* [AWS Serverless Application Model](https://docs.aws.amazon.com/serverless-application-model/latest/developerguide/serverless-sam-cli-install.html) (AWS SAM) installed

## Deployment Instructions
Before deploying this application you will need the following:
* A domain name and hosted zone
* An ACM certificate for the domain name.

### To deploy
1. Create a new directory, navigate to that directory in a terminal and clone the GitHub repository:
    ``` 
    git clone https://github.com/aws-samples/serverless-patterns
    ```
1. Change directory to the pattern directory:
    ```
    cd waf-apigw-rest
    ```
1. From the command line, use AWS SAM to deploy the AWS resources for the pattern as specified in the template.yml file:
    ```
    sam deploy --guided
    ```
    * Deploy to two seperate regions. One as the PRIMARY one as SECONDARY.
1. During the prompts:
    * Enter a stack name
    * Enter the desired AWS Region
    * Enter the **DomainName**, **ZoneId**, **CertArn**, and region **Priority** (PRIMARY | SECONDARY)
    * Allow SAM CLI to create IAM roles with the required permissions.

    Once you have run `sam deploy --guided` mode once and saved arguments to a configuration file (samconfig.toml), you can use `sam deploy` in future to use these defaults.

1. Note the outputs from the SAM deployment process. These contain the resource names and/or ARNs which are used for testing.

## How it works

The application exists in two seperate regions. One is a primary and the second is a secondary. Traffic will always be routed to the primary region unless there is an issue. If an issue with the primary region occurs, Route53 will route traffic to the secondary region. This example demonstrates the failover only and does not encompass authentication and data for the multiple regions.

## Testing

Deploy the application to bothe regions. Traffic will be routed to the primary only. Change the Lambda function to return a 500 and Route53 will then start routing to the secondary region. The function will return the ARN of the Lasmbda function invoked. The ARN contains the region.

## Cleanup (Do this in both regions)
 
1. Delete the stack
    ```bash
    sam delete --stack-name STACK_NAME
    ```
1. Confirm the stack has been deleted
    ```bash
    aws cloudformation list-stacks --query "StackSummaries[?contains(StackName,'STACK_NAME')].StackStatus"
    ```
----
Copyright 2021 Amazon.com, Inc. or its affiliates. All Rights Reserved.

SPDX-License-Identifier: MIT-0
