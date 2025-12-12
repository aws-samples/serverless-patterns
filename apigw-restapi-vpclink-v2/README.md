# AWS Service 1 to AWS Service 2

This pattern deploys an Amazon API Gateway REST with a VPC Link V2 integration. The new feature of November 2025 now allows REST APIs to be integrated directly with ALBs through a VPC Link V2 integration (without having to use a NLB in the middle). I aslo allows HTTP APIs to integrate with a Network Load Balancer through the same VPC Link V2. 
Learn more about this pattern at Serverless Land Patterns: https://serverlessland.com/patterns/apigw-restapi-vpclink-v2

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
    cd _patterns-model
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

## How it works

    The VPC Link V2 now supports both Network Load Balancer and Application Load Balancers, and can be used for both REST APIs and HTTP APIs.

    **For REST APIs :**
    When using HTTPS/SSL over port 443, the integration URI in the REST API resource should match the DNS name covered by the certificate on the listener.
    For instance, if my ALB has the DNS Name "internal-alb-abcd.eu-west-1.elb.amazonaws.com" and has an HTTPS listener on port 443 using the certificate with DNS Name "*.hello.world.com" - the integration URI should be "https://slay.hello.world.com" or match any subdomain of "*.hello.world.com". This is true for both ALB and NLBs.
    The integration URI is only used for the SSL handshake, it will also define the value of the Host Header. 

    However, for request made on port 80 over HTTP/TCP, any URI can be used in the REST API integration, as the VPC Link will always point to the Load Balancer under the hood.
    For instance, if my ALB has the DNS Name "internal-alb-abcd.eu-west-1.elb.amazonaws.com" and has an HTTP listener on port 80 - the integration URI could be "http://internal-alb-abcd.eu-west-1.elb.amazonaws.com" or "http://my.name.is.alice.com", any value will work. The integration URI will be used to define the Host Header.

     **For HTTP APIs :**
     It is not possible to define an integration URI so the above does not apply.

     The template will also create a Security Group for the VPC Link. Its inbound rule do not matter as no traffic will be sent inbound to the VPC Link, only the outbound rule need to allow access to the Load Balancer. In this template, by default the outbound rule is open to all.

     The API also has a test resource called "mock" which is a simple 200 response. 
    

## Testing

When deploying the template, you will be prompted the enter the below parameters:
  * LoadBalancerArn: The ARN of the private ALB or NLB used with the VPC Link
  * IntegrationUri: the integration URI as described above
  * VpcId: ID of the Virtual Private Cloud (VPC) where the Load Balancer resides
  * PrivateSubnetIds: 2 existing private subnets which are also used on the Load Balancer

The template can take a few minutes to create because of the VPC Link resource.

Once it is deployed, the output will show the REST API Gateway invocation URL.

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
Copyright 2025 Amazon.com, Inc. or its affiliates. All Rights Reserved.

SPDX-License-Identifier: MIT-0
