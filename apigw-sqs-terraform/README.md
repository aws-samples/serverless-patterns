# AWS API Gateway HTTP APIs to Amazon SQS for buffering

In this pattern, called "Queue based leveling", a serverless queue is introduced between your API Gateway and your workers, which can be a Lambda function for example. 

The queue acts as a buffer to alleviate traffic spikes and ensure your workload can sustain the arriving load by buffering all the requests durably. It also helps downstream consumers to process the incoming requests at a consistent pace.

Learn more about this pattern at Serverless Land Patterns: https://serverlessland.com/patterns/apigw-sqs-terraform

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
    cd apigw-sqs-terraform
    ```
1. If you are using apigateway and you have an existing cloudwatch role ARN set to your account delete the `aws_api_gateway_account` block, the `aws_iam_role` block & the `aws_iam_role_policy` block, from line 188 to line 235.
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

## How it works

The API Gateway handles incoming requests, but instead of invoking for example a Lambda function directly, it stores them in an SQS queue which serves as a buffer. Then workers, for example a Lambda functions, can process the requests in a batch manner.

## Example Message retrived from SQS:
```
{
    "Messages": [
        {
            "Body": "{ \\\"TestMessage\\\": \\\"Hello From ApiGateway!\\\" }", 
            "ReceiptHandle": "AQEBiYRgfpaOuV96ttrJbJMIQGZXjihOCtC2x0YmiURO8LfFGFAvMgmYmy0wLBW5DgB+dzJEySUwoIPT/1ZTgvZ5kLOBNO5ITjekAjprHqf9dKFzh4TvCtwmkTyt+2EWZ6yATHXP6ibazwr38JxXabZz49UK9KHCEobuKcMLS0nEcYqMYur2eoCs9g3HbnQWg+dvyODWqhpfi+VcMhvFsuLOrbhoFo6aGLZZS/w2pdHviAI6oXC1AmhOjLFStm7y5709+RvSKPhQOVS5XPGByc4cWxa97b7CYlClQni1IfDlOAr6bpr3GOWA0VNgNyydtbXd0fp0IY3mYv5LYyx2wlgee5sgNWbKWiuvaogHDUIYuIbucpcly0utgZzw+TSifOZCWNTbDlFJp0dwBAPF1CHjvf53EH1A5oU1NcVzhu5rebM=", 
            "MD5OfBody": "baabcabde1c3c3f23cijdf13f1a9ff45", 
            "MessageId": "e2f935f3-d57d-4660-88c8-f48cf89b7860"
        }
    ]
}
```

## Testing

1. Run the following command to send an HTTP `POST` request to the HTTP APIs endpoint. Note, you must edit the {MyHttpAPI} placeholder with the URL of the deployed HTTP APIs endpoint. This is provided in the terraform outputs. You can also find the same command automatically generated in the terraform output.
    ```bash
    curl --location --request POST '{MyHttpAPI}/submit'
    > --header 'Content-Type: application/json' \
    > --data-raw '{ "isMessageReceived": "Yes" }'
    ```
1. Retrieve the message from the SQS queue, using the queue URL from the deployment outputs. You can also find the same command automatically generated in the terraform output:
    ```bash
    aws sqs receive-message --queue-url ENTER_YOUR_QUEUE_URL
    ```

## Cleanup

1. Change directory to the pattern directory:
    ```
    cd apigw-sqs-terraform
    ```
1. Delete all files from the S3 bucket
1. Delete all created resources
    ```bash
    terraform destroy
    ```
1. During the prompts:
    * Enter yes
1. **Important Note:** As there is no API method for deleting API Gateway account settings or resetting it to defaults, destroying this resource will keep your account settings intact
1. Confirm all created resources has been deleted
    ```bash
    terraform show
    ```
----
Copyright 2022 Amazon.com, Inc. or its affiliates. All Rights Reserved.

SPDX-License-Identifier: MIT-0
