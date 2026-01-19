# REST Amazon API Gateway to Private HTTP Endpoint via Amazon VPC Link V2

This pattern demonstrates direct integration between REST API Gateway and a private Application Load Balancer using VPC Link V2. Previously, connecting REST API Gateway to a private ALB required VPC Link V1 with an intermediary Network Load Balancer, adding complexity and cost. VPC Link V2 eliminates this requirement, enabling direct ALB integration for simplified architecture and reduced operational overhead.

This Terraform template deploys a REST API Gateway with Amazon VPC Link V2 integration to a private Amazon Application Load Balancer and Amazon ECS Fargate cluster.

### Prerequisites:
* An existing VPC with private subnets
* Private subnets must have internet access (via NAT Gateway) to pull container images from Docker Hub

### Deployed resources:
* Security Groups for ALB and ECS tasks
* ECS Fargate cluster with service and task definitions
* Private Application Load Balancer with listener and target group
* Amazon VPC Link V2 connecting API Gateway to the private ALB
* REST API Gateway with proxy integration to the ALB

Learn more about this pattern at Serverless Land Patterns: https://serverlessland.com/patterns/apigw-rest-vpclink-pvt-alb-terraform/

Important: this application uses various AWS services and there are costs associated with these services after the Free Tier usage - please see the [AWS Pricing page](https://aws.amazon.com/pricing/) for details. You are responsible for any AWS costs incurred. No warranty is implied in this example.

## Requirements

* [Create an AWS account](https://portal.aws.amazon.com/gp/aws/developer/registration/index.html) if you do not already have one and log in. The IAM user that you use must have sufficient permissions to make necessary AWS service calls and manage AWS resources.
* [AWS CLI](https://docs.aws.amazon.com/cli/latest/userguide/install-cliv2.html) installed and configured
* [Git](https://git-scm.com/book/en/v2/Getting-Started-Installing-Git) installed and configured
* [Terraform](https://learn.hashicorp.com/tutorials/terraform/install-cli) installed

## Deployment Instructions

1. Create a new directory, navigate to that directory in a terminal and clone the GitHub repository:
    ``` 
    git clone https://github.com/aws-samples/serverless-patterns
    ```
2. Change directory to the pattern directory:
    ```
    cd serverless-patterns/apigw-rest-vpclink-pvt-alb-terraform
    ```
3. Update the `terraform.tfvars` file with your VPC ID and private subnet IDs:
    ```hcl
    vpc_id = "vpc-xxxxxxxxx"
    
    private_subnets = [
      "subnet-xxxxxxxxx",
      "subnet-yyyyyyyyy"
    ]
    ```
4. Run the below command to initialize, download, and install the defined providers. In case you are not already familiar with the Terraform CLI, refer Terraform [documentation](https://www.terraform.io/cli/commands) to learn more about the various commands.
    ```
    terraform init
    ```
5. Deploy the AWS resources for the pattern as specified in the `main.tf` file. Input variables are configured in `variables.tf`. But, there are different ways to pass variables to the CLI.

    Use the below command to review the changes before deploying.
    ```
    terraform plan
    ```
    Deploy:
    ```
    terraform apply --auto-approve
    ```
6. Note the output from the Terraform deployment process. These contain the resource names and/or ARNs which are used for testing.

## How it works

This pattern demonstrates secure integration between a public REST API Gateway endpoint and a private Application Load Balancer with an ECS Fargate cluster. Traffic flows through Amazon VPC Link V2, which provides a secure, private connection from API Gateway to the internal ALB without exposing backend resources to the public internet.

The integration uses the `--integration-target` parameter with AWS CLI (via Terraform null_resource) to properly configure the REST API Gateway with Amazon VPC Link V2, as this feature requires explicit ALB ARN specification. The ALB distributes traffic to ECS Fargate tasks running in private subnets.

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
 
1. Change to the below directory inside the cloned git repo:
    ```
    cd serverless-patterns/apigw-rest-vpclink-pvt-alb-terraform
    ```
2. Delete the resources
    ```bash
    terraform destroy
    ```
3. Enter 'yes' when prompted.

4. Check if all the resources were deleted successfully.
    ```bash
    terraform show
    ```
----
Copyright 2026 Amazon.com, Inc. or its affiliates. All Rights Reserved.

SPDX-License-Identifier: MIT-0
