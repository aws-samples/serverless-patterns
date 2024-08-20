# Amazon API Gateway to AWS Fargate

This project contains a terraform template for deploying an AWS Fargate service running on an Amazon Elastic Container Service (ECS) cluster with a private Application Load Balancer in-front. The Application Load Balanced Fargate Service is integrated with Amazon API Gateway HTTP API to expose the endpoint. This template uses public standard nginx image without having to pre-push the image to Amazon Elastic Container Registry (ECR) or another container library. 

Learn more about this pattern at Serverless Land Patterns: https://serverlessland.com/patterns/apigw-fargate-terraform.

Important: this application uses various AWS services and there are costs associated with these services after the Free Tier usage - please see the [AWS Pricing page](https://aws.amazon.com/pricing/) for details. You are responsible for any AWS costs incurred. No warranty is implied in this example.

## Requirements

* [Create an AWS account](https://portal.aws.amazon.com/gp/aws/developer/registration/index.html) if you do not already have one and log in. The IAM user that you use must have sufficient permissions to make necessary AWS service calls and manage AWS resources.
* [AWS CLI](https://docs.aws.amazon.com/cli/latest/userguide/install-cliv2.html) installed and configured
* [Git Installed](https://git-scm.com/book/en/v2/Getting-Started-Installing-Git)
* [Terraform](https://learn.hashicorp.com/tutorials/terraform/install-cli?in=terraform/aws-get-started) installed


## Deployment Instructions

1. Create a new directory, navigate to that directory in a terminal and clone the GitHub repository:
   ```bash
   git clone https://github.com/aws-samples/serverless-patterns
   ```
2. Change directory to the pattern directory:
   ```bash
   cd serverless-patterns/apigw-fargate-terraform
   ```
3. From the command line, initialize terraform to download and install the providers defined in the configuration:
    ```
    terraform init
    ```
4. From the command line, apply the configuration in the main.tf file:
    ```
    terraform apply
    ```
5. During the prompts:
    * Enter yes
6. Note the outputs from the deployment process. These contain the resource names and/or URLs which are used for testing.

## How it works

- The VPC and subnets are created
- The ECS cluster is created
- The Task Definitions are created
- The API Gateway Integration, Route, and VPC Link are created
- The Fargate Service is created

## Testing

Retrieve the API Gateway URL from the `cdk deploy` output. Example of the output is:

```
APIGatewayUrl = "https://abcd123efg.execute-api.eu-west-1.amazonaws.com"
```

For reference:

```bash
Outputs:
APIGatewayUrl = "https://abcd123efg.execute-api.eu-west-1.amazonaws.com"
MyFargateServiceLoadBalancer = "internal-MyApp-ALB-XXXXX.eu-west-1.elb.amazonaws.com"
MyFargateServiceServiceURL = "http://internal-MyApp-ALB-XXXXX.eu-west-1.elb.amazonaws.com"
```

The API Gateway allows a GET request to `/`. To call it, run the following:

```bash
curl --location --request GET '<REPLACE WITH API GATEWAY URL>'
# Example
curl --location --request GET 'https://abcd123efg.execute-api.ap-southeast-2.amazonaws.com/'
```

Running the request above should produce the following output:

```bash
~ % curl --location --request GET 'https://abcd123efg.execute-api.ap-southeast-2.amazonaws.com/'
<!DOCTYPE html>
<html>
<head>
<title>Welcome to nginx!</title>
(...)
````

## Cleanup
 
1. Change directory to the pattern directory:
    ```
    cd apigw-fargate-terraform
    ```
2. Delete all created resources by terraform
    ```bash
    terraform destroy
    ```
3. During the prompts:
    * Enter yes
4. Confirm all created resources has been deleted
    ```bash
    terraform show
    ```
5. Navigate to ECR in the AWS console and delete the container images created

## Documentation and useful references

- [GitHub issue where one of the contributors provided an example with a pre-built image and any type of request](https://github.com/aws/aws-cdk/issues/8066)
- [CDK documentation for ApplicationLoadBalancedFargateService](https://docs.aws.amazon.com/cdk/api/latest/docs/@aws-cdk_aws-ecs-patterns.ApplicationLoadBalancedFargateService.html)
- [CDK documentation for APIGatewayv2 CfnIntegration](https://docs.aws.amazon.com/cdk/api/latest/docs/@aws-cdk_aws-apigatewayv2.CfnIntegration.html)
- [CDK documentation for APIGatewayv2 CfnRoute](https://docs.aws.amazon.com/cdk/api/latest/docs/@aws-cdk_aws-apigatewayv2.CfnRoute.html)
- [CDK documentation for APIGatewayv2 HttpApi](https://docs.aws.amazon.com/cdk/api/latest/docs/@aws-cdk_aws-apigatewayv2.HttpApi.html)
- [CDK documentation for CDK Core CfnResource](https://docs.aws.amazon.com/cdk/api/latest/docs/@aws-cdk_core.CfnResource.html)

---

Copyright 2024 Amazon.com, Inc. or its affiliates. All Rights Reserved.

SPDX-License-Identifier: MIT-0

