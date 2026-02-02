# Amazon API Gateway data validation models

This pattern creates an Amazon API Gateway that handles simple data validation at the endpoint without invoking the Lambda function when the data validation fails.

Learn more about this pattern at Serverless Land Patterns: [https://serverlessland.com/patterns/apigw-custom-resource-policy](https://serverlessland.com/patterns/apigw-custom-resource-policy)

Important: this application uses various AWS services and there are costs associated with these services after the Free Tier usage - please see the [AWS Pricing page](https://aws.amazon.com/pricing/) for details. You are responsible for any AWS costs incurred. No warranty is implied in this example.

## Requirements

* [Create an AWS account](https://portal.aws.amazon.com/gp/aws/developer/registration/index.html) if you do not already have one and log in. The IAM user that you use must have sufficient permissions to make necessary AWS service calls and manage AWS resources.
* [AWS CLI](https://docs.aws.amazon.com/cli/latest/userguide/install-cliv2.html) installed and configured
* [Git Installed](https://git-scm.com/book/en/v2/Getting-Started-Installing-Git)
* [Terraform](https://learn.hashicorp.com/tutorials/terraform/install-cli?in=terraform/aws-get-started) installed

## Deployment Instructions

1. Create a new directory, navigate to that directory in a terminal and clone the repository:
    ``` 
    git clone https://github.com/aws-samples/serverless-patterns
    ```
1. Change directory to this pattern's directory
    ```
    cd serverless-patterns/apigw-data-validation-tf
    ```
1. From the command line, initialize Terraform to downloads and install the providers defined in the configuration:
    ```
    terraform init
    ```
1. From the command line, apply the configuration in the main.tf file:
    ```
    terraform apply
    ```
1. Note the outputs from the deployment process. These contain the resource names and/or ARNs which are used for testing.

## API Endpoint

After running `terraform apply`, you will see outputs including the API endpoint URL. You'll need this URL for testing. The output will look similar to:
```
api_endpoint = "https://xxxxx.execute-api.us-east-1.amazonaws.com/Prod"
```

Note: When testing, append `/123?order=ORD12345` to this base URL. For example, if your API endpoint is `https://xxxxx.execute-api.us-east-1.amazonaws.com/Prod`, your full testing URL would be:
```
`https://xxxxx.execute-api.us-east-1.amazonaws.com/Prod/123?order=ORD12345`
```

## How it works

The data model is declared in the API Gateway resource. The Lambda function then requires the request body to be validated against this model.

## Testing

After the application is deployed try the following scenarios.

### Create a new vehicle entering valid data:
```
curl --location --request POST 'https://t9nde3gpp2.execute-api.us-east-1.amazonaws.com/Prod/123?order=ORD12345' \
--header 'Content-Type: application/json' \
--header 'custom-agent: MyMobileApp/1.0' \
--data-raw '{
    "make":"MINI",
    "model":"Countryman",
    "year": 2010
}'
```
Expected response: `{"message": "Data validation succeded", "data": {"make": "MINI", "model": "Countryman", "year": 2010}}`
### Now enter a year less than 2010
```
curl --location --request POST 'https://t9nde3gpp2.execute-api.us-east-1.amazonaws.com/Prod/123?order=ORD12345' \
--header 'Content-Type: application/json' \
--header 'custom-agent: MyMobileApp/1.0' \
--data-raw '{
    "make":"MINI",
    "model":"Countryman",
    "year": 2002
}'
```
Expected response: `{"message": "Invalid request body"}`

Try some other combinations and see what you get!

## Cleanup

1. Change directory to the pattern directory:
    ```
    cd apigw-data-validation-tf
    ```
1. Delete all created resources by Terraform
    ```bash
    terraform destroy
    ```
1. Confirm all created resources has been deleted
    ```bash
    terraform show
    ```

----
Copyright 2024 Amazon.com, Inc. or its affiliates. All Rights Reserved.

SPDX-License-Identifier: MIT-0
