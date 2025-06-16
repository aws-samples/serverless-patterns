# REST API Integration with Private ALB - Workaround

This pattern explains how to integrate an API Gateway REST API with an Application Load Balancer.

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
    cd rest-api-alb-integration-workaround
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

## Background

Currently, integration between REST APIs and Application Load Balancers (ALBs) has some limitations. Direct integration is only possible with public ALBs using API Gateway's HTTP integration feature. Private ALBs cannot be directly integrated with API Gateway.

To work around this limitation for private ALBs, a multi-step approach is necessary. First, create an API Gateway VPC link. Then, connect the VPC link to a private Network Load Balancer (NLB). Finally, configure the NLB to forward incoming requests from API Gateway to the private ALB. This setup allows API Gateway to communicate with private ALBs indirectly, enabling the use of private ALBs in API architectures while maintaining the benefits of API Gateway management.

## Prerequisites

1. Active Route 53 Hosted Zone for your domain.
2. Valid ACM (AWS Certificate Manager) certificate that covers the domain managed by your Route 53 Hosted Zone.

## Workaround

1. Use an API Gateway VPC to integrate your API with a private Network Load Balancer.

2. Use the Network Load Balancer to forward the API request to the private Application Load Balancer.

3. Application Load Balancer will forward the traffic to Lambda Function configured on HTTPS listener.


```
Workflow: REST API >> VPC Link >> NLB (TCP listener) >> ALB (HTTPS listener) >> Lambda
```

## Testing

Once the application is deployed, retrieve the API URL provided as output and open it in a browser page.

## Cleanup
 
1. Delete the stack
    ```bash
    sam delete --stack-name STACK_NAME
    ```
1. Confirm the stack has been deleted
    ```bash
    aws cloudformation list-stacks --query "StackSummaries[?contains(StackName,'STACK_NAME')].StackStatus"
    ```
----
Copyright 2024 Amazon.com, Inc. or its affiliates. All Rights Reserved.

SPDX-License-Identifier: MIT-0
