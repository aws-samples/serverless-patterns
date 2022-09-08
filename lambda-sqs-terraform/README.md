# AWS Lambda to Amazon SQS

The Terraform template deploys a Lambda function, an SQS queue and the IAM permissions required to run the application. The Lambda function publishes a message to the SQS queue when invoked.

Learn more about this pattern at Serverless Land Patterns: https://serverlessland.com/patterns/lambda-sqs-terraform/

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
    cd lambda-sqs-terraform
    ```
1. From the command line, initialize terraform to  to downloads and installs the providers defined in the configuration:
    ```
    terraform init
    ```
1. From the command line, apply the configuration in the main.tf file:
    ```
    terraform apply
    ```
1. During the prompts:
    * Enter yes
1. Note the outputs from the deployment process. These contain the resource names and/or ARNs which are used for testing.

## Example payload from SQS

```
{                                                                                                                   
    "Messages": [
        {
            "MessageId": "12345678-876d-41f7-b32c-1234567890",
            "ReceiptHandle": "AQEBZfn1234567890O78Kn0C1234567890/z1+1234567890f2bQYOvD9RL1234567890Srr7+XQ/U1234567890j7nL+uaDVnJL1234567890mASoiwI/yQ1234567890gv/h17BW12345678908Pry0JM1234567890DfHE1g1234567890aMisj1234567890M+rC+ZF21234567890QdQpEwrX01234567890Fw6w2+Po0OA1234567890DkKgGuEmebp1234567890w7nNXujzSnzIXj1234567890CqfDOb2D1234567890kCk841+01234567890OaYzXV1234567890C+ruRXj1234567890AR5+vj8+U1234567890SJplJLjd1234567890YWV8o1234567890gJXb12345678901234567890",
            "MD5OfBody": "1234567890eb64e60d1234567890",
            "Body": "Message at Wed Feb 10 2021 13:47:31 GMT+0000 (Coordinated Universal Time)"
        }
    ]
}

```

### Testing

Use the [AWS CLI](https://aws.amazon.com/cli/) to invoke the Lambda function. The function name is in the outputs of the Terraform deployment (the key is `QueuePublisherFunction`):

1. Invoke the Lambda function to publish a message to the SQS queue:

```bash
aws lambda invoke --function-name ENTER_YOUR_FUNCTION_NAME response.json
```
2. Retrieve the message from the SQS queue, using the queue URL from the Terraform deployment outputs:
```bash
aws sqs receive-message --queue-url ENTER_YOUR_QUEUE_URL
```

## Cleanup
 
1. Change directory to the pattern directory:
    ```
    cd lambda-sqs-terraform
    ```
1. Delete all files from the S3 bucket
1. Delete all created resources by terraform
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
Copyright 2021 Amazon.com, Inc. or its affiliates. All Rights Reserved.

SPDX-License-Identifier: MIT-0
