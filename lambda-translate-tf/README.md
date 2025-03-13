# Translate Text in real-time using AWS Lambda and Amazon Translate

This pattern contains source code and supporting files for a serverless application deployable with Terraform. The pattern demonstrates how to create an AWS Lambda function that integrates with Amazon Translate to perform real-time text translation between languages.

Learn more about this pattern at Serverless Land Patterns: https://serverlessland.com/patterns/lambda-translate-tf

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
2. Change directory to the pattern directory:
    ```
    cd serverless-patterns/lambda-translate-tf
    ```
3. From the command line, initialize Terraform to downloads and install the providers defined in the configuration:
    ```
    terraform init
    ```
4. From the command line, apply the configuration in the main.tf file:
    ```
    terraform apply
    ```
5. Note the outputs from the deployment process. These contain the resource names and/or ARNs which are used for testing.

## How it works

The pattern uses an AWS Lambda function that integrates with Amazon Translate to perform real-time text translation. When invoked via the AWS CLI, the Lambda function takes three parameters (source text, source language, and target language) and uses Amazon Translate to convert the text from one language to another (for example English to German).

"The example demonstrates translation from English to German language. For a complete list of supported languages, please refer to the [Amazon Translate documentation](https://docs.aws.amazon.com/translate/latest/dg/what-is-languages.html)."


## Testing

Replace "{LambdaFunctionName}" with the function name as seen in the output of terraform template

```
aws lambda invoke  --function-name {LambdaFunctionName} --invocation-type RequestResponse --cli-binary-format raw-in-base64-out --payload "{\"text\":\"I am very happy\", \"sl\":\"en\",\"tl\":\"de\"}" response.json
```

After running the command, open the generated response.json file to see the translated output:
```
Ich freue mich sehr
```

## Cleanup

1. Delete all created resources by Terraform
    ```bash
    terraform destroy
    ```
2. Confirm all created resources has been deleted
    ```bash
    terraform show
    ```
----
Copyright 2025 Amazon.com, Inc. or its affiliates. All Rights Reserved.

SPDX-License-Identifier: MIT-0
