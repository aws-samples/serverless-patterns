# SQS Dead Letter Queue with CloudWatch Alarm and SNS Notification

This pattern creates an Amazon SQS Dead Letter Queue (DLQ) that is monitored by CloudWatch. When more than 3 messages accumulate in the DLQ, a CloudWatch Alarm triggers and sends a notification through SNS.

Learn more about this pattern at Serverless Land Patterns: https://serverlessland.com/patterns/sqs-dlq-cloudwatch-sns

Important: this application uses various AWS services and there are costs associated with these services after the Free Tier usage - please see the [AWS Pricing page](https://aws.amazon.com/pricing/) for details.

## Requirements

* [Create an AWS account](https://portal.aws.amazon.com/gp/aws/developer/registration/index.html) if you do not already have one and log in. The IAM user that you use must have sufficient permissions to make necessary AWS service calls and manage AWS resources.
* [AWS CLI](https://docs.aws.amazon.com/cli/latest/userguide/install-cliv2.html) installed and configured
* [Git Installed](https://git-scm.com/book/en/v2/Getting-Started-Installing-Git)

## Deployment Instructions

1. Create a new directory, navigate to that directory in a terminal and clone the GitHub repository:
    ```
    git clone https://github.com/aws-samples/serverless-patterns
    ```
2. Change directory to the pattern directory:
    ```
    cd sqs-dlq-cloudwatch-sns
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

5. Note the outputs from the SAM deployment process. These contain the resource names and/or ARNs which are used for testing.

## How it works

This pattern deploys an Amazon SQS queue as a Dead Letter Queue (DLQ), a CloudWatch alarm that monitors the number of messages in the DLQ, and an SNS topic that receives notifications when the alarm triggers. When more than 3 messages accumulate in the DLQ, the CloudWatch alarm will trigger and send a notification through SNS.

## Testing

1. Subscribe to the SNS topic created by the stack (you can find the ARN in the stack outputs)
2. Send more than 3 messages to the DLQ
3. Wait for approximately 5 minutes (the CloudWatch alarm evaluation period)
4. You should receive a notification through SNS

## Cleanup
 
1. Delete the stack
    ```bash
    aws cloudformation delete-stack --stack-name STACK_NAME
    ```
2. Confirm the stack has been deleted
    ```bash
    aws cloudformation list-stacks --query "StackSummaries[?contains(StackName,'STACK_NAME')].StackStatus"
    ```

## Contributing

We welcome community contributions! Please refer to [CONTRIBUTING.md](./CONTRIBUTING.md) for guidelines.

## Resources

* [AWS SQS Documentation](https://docs.aws.amazon.com/AWSSimpleQueueService/latest/SQSDeveloperGuide/welcome.html)
* [AWS CloudWatch Documentation](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/WhatIsCloudWatch.html)
* [AWS SNS Documentation](https://docs.aws.amazon.com/sns/latest/dg/welcome.html)
