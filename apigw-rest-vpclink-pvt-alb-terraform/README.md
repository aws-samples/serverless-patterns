# REST API Gateway to Private HTTP Endpoint via VPC Link V2

This Terraform template deploys a complete serverless integration pattern connecting a public REST API Gateway to a private ECS Fargate cluster via VPC Link V2.

### Prerequisites:
* An existing VPC with private subnets
* Private subnets must have internet access (via NAT Gateway or Internet Gateway) to pull container images from Docker Hub

### Deployed resources:
* Security Groups for ALB and ECS tasks
* ECS Fargate cluster with service and task definitions
* Private Application Load Balancer with listener and target group
* VPC Link V2 connecting API Gateway to the private ALB
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

This pattern allows integration of public REST API Gateway endpoint to a private Application Load Balancer with an ECS Fargate cluster behind it. It allows to build a secure pattern without exposing the private subnet resources and can be accessed only via a VPC Link V2.

The integration uses the `--integration-target` parameter with AWS CLI to properly configure the REST API Gateway with VPC Link V2, as this feature is not yet fully supported in the Terraform AWS provider.

## Testing

The stack creates and outputs the REST API endpoint. Open a browser and try out the generated API endpoint. You should see the Nginx home page.
Or, run the below command with the appropriate API endpoint. You should get a 200 response code.

```bash
curl -s -o /dev/null -w "%{http_code}" <API endpoint> ; echo
```

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
Copyright 2021 Amazon.com, Inc. or its affiliates. All Rights Reserved.

SPDX-License-Identifier: MIT-0
