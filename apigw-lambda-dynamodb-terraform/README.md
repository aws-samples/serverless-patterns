# Amazon API Gateway to AWS Lambda to Amazon DynamoDB

This pattern explains how to deploy a sample application using Amazon API Gateway, AWS Lambda, and Amazon DynamoDB with terraform. When an HTTP POST request is made to the Amazon API Gateway endpoint, the AWS Lambda function is invoked and inserts an item into the Amazon DynamoDB table.

Learn more about this pattern at [Serverless Land Patterns](https://serverlessland.com/patterns/apigw-lambda-dynamodb-terraform).

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
    cd serverless-patterns/apigw-lambda-dynamodb-terraform
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
1. Note the outputs from the deployment process, these contain the resource names and/or ARNs which are used for testing.

## How it works

When an HTTP POST request is sent to the Amazon API Gateway endpoint, the AWS Lambda function is invoked and inserts an item into the Amazon DynamoDB table.

## Testing

Once the stack is deployed, retrieve the HttpApiEndpoint value from the outputs of the terraform apply, then make a call the /movies endpoint using curl or Postman.
Check the dynamodb table to make sure new items have been created.


```
# Send an HTTP POST request without a request body and the lambda function will add a default item to the dynamodb table

curl -X POST '<your http api endpoint>'/movies

#sample output

{
  "message": "Successfully inserted data!"
}
```

```
# Send an HTTP POST request an include a request body in the format below and the lambda function will create a new item in the dynamodb table

curl -X POST '<your http api endpoint>'/movies \
> --header 'Content-Type: application/json' \
> -d '{"year":1977, "title":"Starwars"}' 

#sample output

{
  "message": "Successfully inserted data!"
}
```


## Cleanup
 
1. Change directory to the pattern directory:
    ```
    cd serverless-patterns/apigw-lambda-dynamodb-terraform
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