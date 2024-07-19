# Amazon MQ for RabbitMQ to AWS Lambda

This pattern deploys a Lambda function, an Amazon MQ for RabbitMQ queue and the IAM permissions required to run the application. RabbitMQ invokes the Lambda function when new messages are available.

Learn more about this pattern at Serverless Land Patterns: [serverlessland.com/patterns/rabbitmq-lambda-tf](https://serverlessland.com/patterns/rabbitmq-lambda-tf)

Important: this application uses various AWS services and there are costs associated with these services after the Free Tier usage - please see the [AWS Pricing page](https://aws.amazon.com/pricing/) for details. You are responsible for any AWS costs incurred. No warranty is implied in this example.

## Requirements

* [Create an AWS account](https://portal.aws.amazon.com/gp/aws/developer/registration/index.html) if you do not already have one and log in. The IAM user that you use must have sufficient permissions to make necessary AWS service calls and manage AWS resources.
* [AWS CLI](https://docs.aws.amazon.com/cli/latest/userguide/install-cliv2.html) installed and configured
* [Git Installed](https://git-scm.com/book/en/v2/Getting-Started-Installing-Git)
* [Terraform](https://learn.hashicorp.com/tutorials/terraform/install-cli?in=terraform/aws-get-started) installed

## Deployment Instructions

1. Set up your username and password for RabbitMQ access. In a new terminal window enter:
    ```
    aws secretsmanager create-secret --name MQaccess --secret-string '{"username": "your-username", "password": "your-password"}'
    ```
1. The command responds with the ARN of your new secret. 

1. Create a new directory, navigate to that directory in a terminal and clone the repository:
    ``` 
    git clone https://github.com/aws-samples/serverless-patterns
    ```
1. Change directory to this pattern's directory
    ```
    cd serverless-patterns/rabbitmq-lambda-tf
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
   

### Testing

1. Navigate to the AmazonMQ console and choose the newly created broker. 

1. In the Connections panel, locate the URL for the RabbitMQ web console.

1. Sign in with the credentials you created and stored in the Secrets Manager earlier.

1. Select Queues from the top panel and then choose Add a new queue.

1. Enter ‘myQueue’ as the name for the queue and choose Add queue. (This must match exactly as that is the name you hardcoded in the AWS terraform template). Keep the other configuration options as default.

1. In the RabbitMQ web console, choose Queues.

1. Choose the name of the queue. Under the Publish message tab, enter a message, and choose Publish message to send

1. In the MQconsumer Lambda function, select the Monitoring tab and then choose View logs in CloudWatch. The log streams show that the Lambda function is invoked by Amazon MQ and you see the message in the logs.

## Cleanup

1. Change directory to the pattern directory:
    ```
    cd rabbitmq-lambda-tf
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