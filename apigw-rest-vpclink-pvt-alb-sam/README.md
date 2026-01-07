# Amazon API Gateway REST API to Private HTTP Endpoint via Amazon VPC Link V2

This pattern demonstrates direct integration between API Gateway REST API and a private Application Load Balancer using VPC link V2. Previously, connecting REST API Gateway to a private ALB required VPC link V1 with an intermediary Network Load Balancer, adding complexity and cost. VPC Link V2 eliminates this requirement, enabling direct ALB integration for simplified architecture and reduced operational overhead.

This AWS SAM template deploys a REST API Gateway with Amazon VPC link V2 integration to a private Amazon Application Load Balancer and Amazon ECS Fargate cluster. The API definition is provided via an external OpenAPI specification file (api.yaml).

### Prerequisites:
* An existing VPC with private subnets
* Private subnets must have internet access (via NAT Gateway) to pull container images from Docker Hub

### Deployed resources:
* Security Groups for ALB and ECS tasks
* ECS Fargate cluster with service and task definitions
* Private Application Load Balancer with listener and target group
* Amazon VPC link V2 connecting API Gateway to the private ALB
* API Gateway REST API (AWS::Serverless::Api) with proxy integration to the ALB

Learn more about this pattern at Serverless Land Patterns: https://serverlessland.com/patterns/apigw-rest-vpclink-pvt-alb-sam/

Important: this application uses various AWS services and there are costs associated with these services after the Free Tier usage - please see the [AWS Pricing page](https://aws.amazon.com/pricing/) for details. You are responsible for any AWS costs incurred. No warranty is implied in this example.

## Requirements

* [Create an AWS account](https://portal.aws.amazon.com/gp/aws/developer/registration/index.html) if you do not already have one and log in. The IAM user that you use must have sufficient permissions to make necessary AWS service calls and manage AWS resources.
* [AWS CLI](https://docs.aws.amazon.com/cli/latest/userguide/install-cliv2.html) installed and configured
* [Git](https://git-scm.com/book/en/v2/Getting-Started-Installing-Git) installed and configured
* [AWS SAM CLI](https://docs.aws.amazon.com/serverless-application-model/latest/developerguide/serverless-sam-cli-install.html) installed

## Deployment Instructions

1. Create a new directory, navigate to that directory in a terminal and clone the GitHub repository:
    ``` 
    git clone https://github.com/aws-samples/serverless-patterns
    ```
2. Change directory to the pattern directory:
    ```
    cd serverless-patterns/apigw-rest-vpclink-pvt-alb-sam
    ```
3. From the command line, use AWS SAM to deploy the AWS resources for the pattern. You will be prompted for the VPC ID and private subnet IDs:
    ```
    sam deploy --guided --capabilities CAPABILITY_NAMED_IAM
    ```
4. During the prompts:
    * Enter a stack name
    * Enter the desired AWS Region
    * Enter your VPC ID for the VpcId parameter
    * Enter your first private subnet ID for the PrivateSubnet1 parameter
    * Enter your second private subnet ID for the PrivateSubnet2 parameter
    * Allow SAM CLI to create IAM roles with the required permissions
    * Accept the defaults for the remaining prompts

    Once you have run `sam deploy --guided` mode once and saved arguments to a configuration file (samconfig.toml), you can use `sam deploy` in future to use these defaults.

5. Note the outputs from the SAM deployment process. These contain the resource names and/or ARNs which are used for testing.

## How it works

This pattern demonstrates secure integration between a public REST API Gateway endpoint and a private Application Load Balancer with an ECS Fargate cluster. The pattern uses AWS::Serverless::Api resource with an external OpenAPI definition (api.yaml) that leverages AWS::Include transform to support CloudFormation intrinsic functions.

Traffic flows through Amazon VPC Link V2, which provides a secure, private connection from API Gateway to the internal ALB without exposing backend resources to the public internet. The ALB distributes traffic to ECS Fargate tasks running in private subnets.

## Testing

The stack outputs the REST API endpoint. Test it by accessing any path through the API:

```bash
curl https://<API-ENDPOINT>/index.html
```

You should see the nginx welcome page HTML. To check just the status code:

```bash
curl -s -o /dev/null -w "%{http_code}" https://<API-ENDPOINT>/index.html ; echo
```

Expected response: **200**

## Cleanup
 
1. Delete the stack:
    ```bash
    sam delete
    ```
2. Confirm the stack has been deleted:
    ```bash
    aws cloudformation list-stacks --query "StackSummaries[?contains(StackName,'STACK_NAME')].StackStatus"
    ```
----
Copyright 2026 Amazon.com, Inc. or its affiliates. All Rights Reserved.

SPDX-License-Identifier: MIT-0
