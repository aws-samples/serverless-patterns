# RabbitMQ to AWS Lambda

The SAM template deploys a Lambda function, a RabbitMQ queue and the IAM permissions required to run the application. RabbitMQ invokes the Lambda function when new messages are available.

Learn more about this pattern at Serverless Land Patterns: [serverlessland.com/patterns/rabbitmq-lambda](https://serverlessland.com/patterns/rabbitmq-lambda)

Important: this application uses various AWS services and there are costs associated with these services after the Free Tier usage - please see the [AWS Pricing page](https://aws.amazon.com/pricing/) for details. You are responsible for any AWS costs incurred. No warranty is implied in this example.

## Requirements

* [Create an AWS account](https://portal.aws.amazon.com/gp/aws/developer/registration/index.html) if you do not already have one and log in. The IAM user that you use must have sufficient permissions to make necessary AWS service calls and manage AWS resources.
* [AWS CLI](https://docs.aws.amazon.com/cli/latest/userguide/install-cliv2.html) installed and configured
* [Git Installed](https://git-scm.com/book/en/v2/Getting-Started-Installing-Git)
* [AWS Serverless Application Model](https://docs.aws.amazon.com/serverless-application-model/latest/developerguide/serverless-sam-cli-install.html) (AWS SAM) installed

## Deployment Instructions

1. Set up your username and password for RabbitMQ access. In a new terminal window enter:
    ```
    aws secretsmanager create-secret --name MQaccess --secret-string '{"username": "your-username", "password": "your-password"}'
    ```
1. The command responds with the ARN of your new secret. Copy the ARN and paste it in the last line of the SAM template where it says `<your_secret_arn>`.

1. Create a new directory, navigate to that directory in a terminal and clone the GitHub repository:
    ``` 
    git clone https://github.com/aws-samples/serverless-patterns
    ```
1. Change directory to the pattern directory:
    ```
    cd rabbitmq-lambda
    ```
1. From the command line, use AWS SAM to deploy the AWS resources for the pattern as specified in the template.yml file:
    ```
    sam deploy --guided
    ```
1. During the prompts:
    * Enter a stack name
    * Enter the desired AWS Region
    * Allow SAM CLI to create IAM roles with the required permissions.

    Once you have run `sam deploy -guided` mode once and saved arguments to a configuration file (samconfig.toml), you can use `sam deploy` in future to use these defaults.

1. Note the outputs from the SAM deployment process. These contain the resource names and/or ARNs which are used for testing.
   

### Testing

1. Navigate to the AmazonMQ console and choose the newly created broker. 

1. In the Connections panel, locate the URL for the RabbitMQ web console.

1. Sign in with the credentials you created and stored in the Secrets Manager earlier.

1. Select Queues from the top panel and then choose Add a new queue.

1. Enter ‘myQueue’ as the name for the queue and choose Add queue. (This must match exactly as that is the name you hardcoded in the AWS SAM template). Keep the other configuration options as default.

1. In the RabbitMQ web console, choose Queues.

1. Choose the name of the queue. Under the Publish message tab, enter a message, and choose Publish message to send

1. In the MQconsumer Lambda function, select the Monitoring tab and then choose View logs in CloudWatch. The log streams show that the Lambda function is invoked by Amazon MQ and you see the message in the logs.

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
