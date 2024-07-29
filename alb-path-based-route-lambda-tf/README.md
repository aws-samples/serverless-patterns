# Application Load balancer with path-based routing and AWS Lambda target in Terraform

This pattern demonstrates how to create an Application Load Balancer with path-based routing along with associated listener and target as AWS Lambda. Implemented in Terraform.

Learn more about this pattern at Serverless Land Patterns: https://serverlessland.com/patterns/alb-path-based-route-lambda-tf

Important: this application uses various AWS services and there are costs associated with these services after the Free Tier usage - please see the [AWS Pricing page](https://aws.amazon.com/pricing/) for details. You are responsible for any AWS costs incurred. No warranty is implied in this example.

## Requirements

* [Create an AWS account](https://portal.aws.amazon.com/gp/aws/developer/registration/index.html) if you do not already have one and log in. The IAM user that you use must have sufficient permissions to make necessary AWS service calls and manage AWS resources.
* [AWS CLI](https://docs.aws.amazon.com/cli/latest/userguide/install-cliv2.html) installed and configured
* [Git Installed](https://git-scm.com/book/en/v2/Getting-Started-Installing-Git)
* [Terraform Installed](https://developer.hashicorp.com/terraform/downloads)

## Deployment Instructions

1. Create a new directory, navigate to that directory in a terminal and clone the GitHub repository:
    ``` 
    git clone https://github.com/aws-samples/serverless-patterns
    ```
2. Change directory to the pattern directory:
    ```
    cd alb-path-based-route-lambda-tf
    ```
3. From the command line, run:
   
    Default region (us-east-1) | Specify region (eu-west-1 example)
    ---------|----------
    ```terraform init``` | ```terraform init -var region="eu-west-1"```

4. From the command line, run:
    Default region (us-east-1) | Specify region (eu-west-1 example)
    ---------|----------
    ```terraform plan``` | ```terraform plan -var region="eu-west-1"```
5. From the command line, run:

    Default region (us-east-1) | Specify region (eu-west-1 example)
    ---------|----------
    ```terraform apply --auto-approve``` | ```terraform apply -var region="eu-west-1" --auto-approve```

## Testing

1. In the terraform output, you can see `alb_url`. When you access the url, you should see the response "Default Response from ALB" from Lambda.
2. To access the path based route from the ALB, Access `alb_url`/api/service1, you should see "Hello from Service1!!!!" and `alb_url`/api/service2, you should see ""Hello from Service2!!!!"


## Cleanup
 
1. To delete the resources, run:
    Default region (us-east-1) | Specify region (eu-west-1 example)
    ---------|----------
    ```terraform destroy --auto-approve``` | ```terraform destroy -var region="eu-west-1" --auto-approve```
----
Copyright 2023 Amazon.com, Inc. or its affiliates. All Rights Reserved.

SPDX-License-Identifier: MIT-0
