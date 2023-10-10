# AWS Lambda to Amazon Comprehend

The SAM template creates an AWS Lambda function that calls Amazon Comprehend to do sentiment analysis.

Learn more about this pattern at Serverless Land Patterns: https://serverlessland.com/patterns/lambda-comprehend

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
1. Change directory to the pattern directory:
    ```
    cd lambda-comprehend
    ```
1. From the command line, use AWS SAM to deploy the AWS resources for the pattern as specified in the template.yml file:
    ```
    sam deploy --guided
    ```
1. During the prompts:
    * Enter a stack name
    * Enter the desired AWS Region
    * Allow SAM CLI to create IAM roles with the required permissions.

    Once you have run `sam deploy --guided` mode once and saved arguments to a configuration file (samconfig.toml), you can use `sam deploy` in future to use these defaults.

1. Note the outputs from the SAM deployment process. These contain the resource names and/or ARNs which are used for testing.

## How it works

* Use the AWS CLI to asynchronously invoke the Lambda function.

==============================================

## Testing

### Success Testing

Replace "{LambdaFunctionName}" with the function name as seen in the output of CloudFormation template

```bash
aws lambda invoke --function-name {LambdaFunctionName} --invocation-type RequestResponse --cli-binary-format raw-in-base64-out --payload "{\"text\":\"I am very happy\"}" response.json
```

The command above returns the following output:

```bash
{
    "comprehend_prediction": "POSITIVE", 
    "comprehend_scores": {
        "Positive": 0.9995189905166626,
        "Negative": 7.40763935027644e-05,
        "Neutral": 0.0002747899852693081,
        "Mixed": 0.00013210243196226656
    }
}
```
## Cleanup
 
1. Delete the stack
    ```bash
    aws cloudformation delete-stack --stack-name STACK_NAME
    ```
1. Confirm the stack has been deleted
    ```bash
    aws cloudformation list-stacks --query "StackSummaries[?contains(StackName,'STACK_NAME')].StackStatus"
    ```
----
Copyright 2021 Amazon.com, Inc. or its affiliates. All Rights Reserved.

SPDX-License-Identifier: MIT-0
