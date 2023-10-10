# AWS API Gateway HTTP API to AWS Lambda to RDS Proxy

This pattern sets up an API Gateway HTTP API using AWS Lambda function as an integration that connects to an RDS Proxy endpoint. The RDS Proxy is configured 
with force IAM Authentication enabled. Using IAM Authentication removes the need to embed or read credentials in your function code.

The setup assumes you already have an RDS Aurora MySQL cluster up and running together with the RDS proxy instance using 
force IAM authentication enabled. If you do not have the set-up for database and proxy you can optionally follow [these steps](#deploy-rds-aurora-clustermysql-with-rds-proxy)
to have RDS Aurora cluster and RDS proxy setup.

Learn more about this pattern at Serverless Land Patterns: https://serverlessland.com/patterns/apigw-http-api-lambda-rds-proxy-terraform

Important: this application uses various AWS services and there are costs associated with these services after the Free Tier usage - please see the [AWS Pricing page](https://aws.amazon.com/pricing/) for details. You are responsible for any AWS costs incurred. No warranty is implied in this example.

## Requirements

* [Create an AWS account](https://portal.aws.amazon.com/gp/aws/developer/registration/index.html) if you do not already have one and log in. The IAM user that you use must have sufficient permissions to make necessary AWS service calls and manage AWS resources.
* [AWS CLI](https://docs.aws.amazon.com/cli/latest/userguide/install-cliv2.html) installed and configured
* [Git Installed](https://git-scm.com/book/en/v2/Getting-Started-Installing-Git)
* [Terraform](https://learn.hashicorp.com/tutorials/terraform/install-cli?in=terraform/aws-get-started) installed

## Deployment Instructions

1. Create a new directory, navigate to that directory in a terminal and clone the GitHub repository:
    ``` 
    git clone https://github.com/aws-samples/serverless-patterns
    ```
1. Change directory to the pattern directory:
    ```
    cd serverless-patterns/apigw-http-api-lambda-rds-proxy-terraform
    ```
1. From the command line, initialize terraform to download and install the providers defined in the configuration:
    ```
    terraform init
    ```
1. From the command line, apply the configuration in the main.tf file:
    ```
    terraform apply
    ```
1. During the prompts, Enter the following information:
    * rds_proxy_resourceid (last part of the RDS proxy ARN; e.g. prx-<hash>)
    * rds_proxy_endpoint
    * vpc_id
    * vpc_subnets - using this format `["sg-abc123","sg-abc456"]`
    * security_group
    * secret_name (the name of the Secrets Manager secret that stores the database user credentials)
    * Alternative approach: Enter this information in the variables defined under the variables.tf file
1. Note the outputs from the deployment process, these contain the resource names and/or ARNs which are used for testing.

## Deploy RDS Aurora Cluster(Mysql) with RDS Proxy

**Note:** If you have already provisioned RDS Aurora cluster with RDS Proxy, you can skip 
this step and follow [these steps](#deployment-instructions) instead.

This module will provision an RDS Aurora(Mysql) cluster together with RDS proxy using force IAM authentication deployed in a 
a VPC with 3 private database subnets. Required parameters needed by [deployment step](#deployment-instructions) are also 
provided as part of the module output.

1. Change directory to the module directory:
    ```
    cd vpc-rds-setup
    ```

1. From the command line, initialize terraform to download and install the providers defined in the configuration:
    ```
    terraform init
    ```
1. From the command line, apply the configuration in the main.tf file:
    ```
    terraform apply
    ```
1. During the prompts:
    * Enter yes


## How it works

When an HTTP POST request is sent to the Amazon API Gateway endpoint, the AWS Lambda function is invoked to issue a database query against an RDS proxy endpoint. The lambda function retrieves a temporary token from IAM to authenticate instead of using native database credentials. 
The RDS proxy will then establish a connection to the database, the lambda function will borrow this database connection for the next query/transaction.


## Testing

Once the stack is deployed, retrieve the `apigwy_url` value from the output of terraform apply, use curl or postman to issue a request.
   
   ```bash
    curl '<apigwy_url>'
   ```

This should result in a json payload which returns session user information. Session User is returned by [querying](src/app.py#L67) RDS Aurora(MySql) database 
for current date.

   ```
 {
  "status": "Success",
  "message": "Information retrieved",
  "results": [
    {
      "session_user()": "lambda@{proxy ip address}"
    }
  ]
}
   ```
   
Review the CloudWatch Logs for the lambda function to get additional insight.

## Cleanup
 
1. Change directory to the pattern directory:
    ```
    cd serverless-patterns/apigw-http-api-lambda-rds-proxy-terraform
    ```
1. Delete all created resources
    ```bash
    terraform destroy
    ```
1. During the prompts:
    * Enter yes
1. Confirm all created resources has been deleted
    ```bash
    terraform show
    ```
----
Copyright 2022 Amazon.com, Inc. or its affiliates. All Rights Reserved.

SPDX-License-Identifier: MIT-0
