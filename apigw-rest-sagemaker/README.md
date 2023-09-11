# AWS API Gateway REST Edge-Optimized API to Amazon SageMaker

This pattern creates an Amazon API Gateway REST Edge-Optimized API with an Amazon SageMaker integration. It deploys a SageMaker Jumpstart model (Flan T5 XL) endpoint that is used for the integration.

Learn more about this pattern at Serverless Land Patterns: <add-serverlessland-url-after-publication>

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
2. Change directory to the pattern directory:
    ```
    cd apigw-rest-sagemaker
    ```
3. From the command line, use AWS SAM to deploy the AWS resources for the pattern as specified in the template.yml file:
    ```
    sam deploy --guided
    ```
4. During the prompts:
    * Enter a stack name
    * Enter the desired AWS Region
    * Allow SAM CLI to create IAM roles with the required permissions.

    Once you have run `sam deploy --guided` mode once and saved arguments to a configuration file (samconfig.toml), you can use `sam deploy` in future to use these defaults.

5. Note the output from the SAM deployment process. It contains the API endpoint.

## How it works

1. This pattern deploys a SageMaker Jumpstart model (Flan T5 XL from HuggingFace) endpoint using Amazon SageMaker. To deploy the solution with a different model, replace the ModelData and ImageURI parameters in the template.yaml file.

2. The pattern also adds an API Gateway query the endpoint.

3. The API Gateway is protected using an API Key. To query the Api Gateway, ```x-api-key``` header needs to be added to the HTTP request.

## Testing

Once the application is deployed, retrieve the API URL provided as output and append the resource name "/text". Then make the request from Postman or from a terminal. The URL should look like this : https://[api-id].execute-api.[api-region].amazonaws.com/v1/text

Postman Example
    ```bash
    https://aabbccddee.execute-api.eu-west-1.amazonaws.com/text
    ```

OR open a terminal and execute the curl command

Example
    ```bash
    curl -X POST 'https://aabbccddee.execute-api.eu-west-1.amazonaws.com/v1/text' \
--header 'x-api-key: Q425Bv0mFe7s6C4jRrCAlazVkSlXXXXXXXXXXXXX' \
--header 'Content-Type: application/json' \
--data '{
     "text_inputs": "Translate to Spanish:  My dog is very beautiful",
     "max_length": 5000
}'
    ```
The expected response is : 'Yo nac en Madrid'


## Cleanup
 
1. Delete the stack
    ```bash
    aws cloudformation delete-stack --stack-name STACK_NAME
    ```
1. Confirm the stack has been deleted
    ```bash
    aws cloudformation list-stacks --query "StackSummaries[?contains(StackName,'STACK_NAME')].StackStatus"
    ```
## Author bio

Nabanita Paul,
https://www.linkedin.com/in/nabanita-paul/
Cloud Support Engineer II
----
Copyright 2023 Amazon.com, Inc. or its affiliates. All Rights Reserved.

SPDX-License-Identifier: MIT-0