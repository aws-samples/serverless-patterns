# API Gateway Integration with AWS Lambda and Amazon Bedrock Nova Micro (Terraform)

## Overview

This pattern demonstrates how to create a serverless API leveraging Amazon Bedrock Nova Micro through AWS Lambda. The solution uses an Amazon API Gateway REST endpoint to process requests and return AI-generated responses using Nova Micro's text-to-text capabilities.

Learn more about this pattern at [Serverless Land Patterns](https://serverlessland.com/patterns/apigw-lambda-bedrock-nova-terraform).

Important: this application uses various AWS services and there are costs associated with these services after the Free Tier usage - please see the [AWS Pricing page](https://aws.amazon.com/pricing/) for details. You are responsible for any AWS costs incurred. No warranty is implied in this example.

## Requirements

* [Create an AWS account](https://portal.aws.amazon.com/gp/aws/developer/registration/index.html) if you do not already have one and log in. The IAM user that you use must have sufficient permissions to make necessary AWS service calls and manage AWS resources.
* [AWS CLI](https://docs.aws.amazon.com/cli/latest/userguide/install-cliv2.html) installed and configured
* [Git Installed](https://git-scm.com/book/en/v2/Getting-Started-Installing-Git)
* [Terraform](https://learn.hashicorp.com/tutorials/terraform/install-cli?in=terraform/aws-get-started) installed

## Deployment Instructions

1. Clone the project to your local working directory

   ```sh
   git clone https://github.com/aws-samples/serverless-patterns/ 
   ```

2. Change the working directory to this pattern's directory

   ```sh
   cd serverless-patterns/apigw-lambda-bedrock-nova-terraform
   ```

3. From the command line, run each of the command mentioned in the create_lambda_layer.sh file, this file contains the commands to create the Lambda Layer as well zip the bedrock_integration.py which invokes the Amazon Nova model.

4. From the command line, initialize terraform to  to downloads and installs the providers defined in the configuration:
    ```
    terraform init
    ```

5. From the command line, apply the configuration in the main.tf file:
    ```
    terraform apply
    ```

6. During the prompts:
   - Enter yes

## How it works

The pattern creates an API Gateway endpoint that accepts POST requests containing prompts. These requests are forwarded to a Lambda function that processes the input and interacts with Amazon Bedrock's Nova Micro model.

Key components:

* API Gateway REST API endpoint
* Lambda function with Nova Micro integration
* IAM roles and policies for Lambda and Bedrock access
* Lambda layer for boto3 dependencies
* Nova Micro Request Format:
    ```
    
    {
    "system": [
        {
            "text": "You are a helpful AI assistant that provides accurate and concise information."
        }
    ],
    "messages": [
        {
            "role": "user",
            "content": [
                {
                    "text": "<your-prompt>"
                }
            ]
        }
    ],
    "inferenceConfig": {
        "maxTokens": 1024,
        "temperature": 0.7,
        "topP": 0.9,
        "topK": 50,
        "stopSequences": []
    }
    }
    
    ```

## Testing

   Using Curl:

    ```
    curl -X POST \
    -H "Content-Type: application/json" \
    -d '{"prompt": "What are the key benefits of using AWS services?"}' \
    https://YOUR-API-ENDPOINT/dev/generate_content
    
    ```

## Viewing Test Results
   ```
   {
    "generated-text": "<Model generated response>"
   }
   ```

## Cleanup

1. Change directory to the pattern directory:
    ```sh
    cd serverless-patterns/apigw-lambda-bedrock-nova-terraform
    ```

2. Delete all created resources
    ```sh
    terraform destroy
    ```

3. During the prompts:
    * Enter yes

4. Confirm all created resources has been deleted
    ```sh
    terraform show
    ```

## Reference

- [Amazon Bedrock Nova Models](https://docs.aws.amazon.com/bedrock/latest/userguide/model-parameters-nova.html)
- [AWS Lambda with API Gateway](https://docs.aws.amazon.com/apigateway/latest/developerguide/getting-started-with-lambda-integration.html)
- [Amazon API Gateway REST APIs](https://docs.aws.amazon.com/apigateway/latest/developerguide/apigateway-rest-api.html)

----
Copyright 2025 Amazon.com, Inc. or its affiliates. All Rights Reserved.

SPDX-License-Identifier: MIT-0