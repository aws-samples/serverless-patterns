# Regional API with Edge-Optimized domain name to Lambda

This pattern creates an Amazon API Gateway Regional rest API with an Edge-Optimized domain name. The API is integrated with a Lambda function in python3.9.

Learn more about this pattern at Serverless Land Patterns: https://serverlessland.com/patterns/apigw-domain-edge-lambda

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
    cd apigw-domain-edge-lambda
    ```
1. From the command line, use AWS SAM to deploy the AWS resources for the pattern as specified in the template.yml file:
    ```
    sam deploy --guided
    ```
1. During the prompts:
    * Enter a stack name
    * Allow SAM CLI to create IAM roles with the required permissions.

    Once you have run `sam deploy --guided` mode once and saved arguments to a configuration file (samconfig.toml), you can use `sam deploy` in future to use these defaults.

1. Note the outputs from the SAM deployment process. These contain the resource names and/or ARNs which are used for testing.

## How it works

This patterns creates an edge-optimized custom domain name associated with a regional REST API with a lambda integration.

You will need :

* A route53 [Hosted zone](https://docs.aws.amazon.com/Route53/latest/DeveloperGuide/CreatingHostedZone.html)
* An ACM Certificate in the US-EAST-1 region. See how to request a public certificate [here](https://docs.aws.amazon.com/acm/latest/userguide/gs-acm-request-public.html).
* The domain name choosen needs to match or be a subdomain of the domain name on the certificate. See more [here](https://docs.aws.amazon.com/apigateway/latest/developerguide/how-to-edge-optimized-custom-domain-name.html).

## Testing

Enter the ARN of the certificate (which is in us-east-1) and the custom domain name in the parameters of the template. 

Create a [new record](https://docs.aws.amazon.com/Route53/latest/DeveloperGuide/routing-to-api-gateway.html) in your Hosted zone in route53 :
* enter the same name you chose for your API domain name
* check the alias tick box
* route traffic to API Gateway/ the region where your API is /your API endpoint which should look like [distribution-id].cloudfront.net
* create records

Then try to make a request to the custom domain name from your browser, postman or using the curl command. 

Eg : 
```bash
curl https://yourdomainname/com
```

The expected answer is : "Hello World! This is the edge-optimized custom domain name and the regional API"

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
