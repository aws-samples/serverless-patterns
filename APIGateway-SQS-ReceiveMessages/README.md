## AWS API Gateway to AWS SQS

This pattern creates a REST API Gateway that directly integrates with AWS SQS to read messages.
Learn more about this pattern at Serverless Land Patterns: https://serverlessland.com/

**Important**: This application uses various AWS services that incur costs beyond the Free Tier usage. Please review the [AWS Pricing page](https://aws.amazon.com/pricing/) for details. You are responsible for any AWS costs incurred. No warranty is implied in this example.

## Requirements

- An [AWS account](https://portal.aws.amazon.com/gp/aws/developer/registration/index.html) with appropriate IAM permissions to make service calls and manage AWS resources
- [AWS CLI](https://docs.aws.amazon.com/cli/latest/userguide/install-cliv2.html) installed and configured
- [Git](https://git-scm.com/book/en/v2/Getting-Started-Installing-Git) installed
- [AWS Serverless Application Model](https://docs.aws.amazon.com/serverless-application-model/latest/developerguide/serverless-sam-cli-install.html) (AWS SAM) installed

## Deployment Instructions

1. Clone the GitHub repository:
```git clone https://github.com/aws-samples/serverless-patterns```

2. Navigate to the pattern directory:
```cd APIGateway-SQS-ReceiveMessages```

3. Deploy using AWS SAM:
```sam deploy --guided```

During the prompts:
    - Enter a stack name
    - Select your desired AWS Region
    - Allow SAM CLI to create IAM roles with required permissions

After initial deployment with sam deploy --guided, subsequent deployments can use sam deploy with the saved configuration (samconfig.toml).

Note the outputs from the deployment process, as they contain resource names and/or ARNs needed for testing.

## How it works

This pattern creates an Amazon API Gateway REST API endpoint that directly connects to Amazon SQS using service integrations. Users can retrieve messages by calling the GET method of the invoke URL (API Gateway) provided in the Stack Output.

The invoke URL supports query string parameters such as MaxNumberOfMessages=5, VisibilityTimeout=15, and AttributeName=All to customize the response.

For detailed parameter definitions, refer to the [AWS API Reference Documentation](https://docs.aws.amazon.com/AWSSimpleQueueService/latest/APIReference/API_ReceiveMessage.html).

## Usage Example and Consideration

This pattern is ideal for scenarios where you need to retrieve messages from SQS via HTTPS without using AWS SDK. Common use cases include:
Web applications that need to poll SQS queues for new messages, Mobile applications requiring secure access to SQS messages, Third-party integrations where direct AWS SDK access isn't practical, Legacy system integrations that support only HTTP/HTTPS protocols, Development environments where simplified queue access is preferred.

Please review [API Gateway](https://docs.aws.amazon.com/apigateway/latest/developerguide/limits.html) and [SQS Quotas](https://docs.aws.amazon.com/AWSSimpleQueueService/latest/SQSDeveloperGuide/sqs-quotas.html) for service limits before implementation.

## Testing

Follow these steps to test the integration:

1. First, send test messages to the queue:
    ```chmod +x send_message_to_queue.sh```
   
    ```./send_message_to_queue.sh {queueURL} {number of messages}```

    Example:
    ```./send_message_to_queue.sh https://sqs.us-east-1.amazonaws.com/210987654321/myQueue 3```

2. Then, retrieve messages using the API Gateway endpoint:

    Basic retrieval:
    ```curl --location --request GET '{ApiEndpoint output value}'```

    Advanced retrieval with parameters:
    ```curl --location --request GET '{ApiEndpoint output value}?MaxNumberOfMessages=5&VisibilityTimeout=15&AttributeName=All'```

    Parameter details are available in the [AWS API Reference Documentation](
    https://docs.aws.amazon.com/AWSSimpleQueueService/latest/APIReference/API_ReceiveMessage.html).

## Expected Output

When Queue is Empty:
```json
{
    "ReceiveMessageResponse": {
        "ReceiveMessageResult": {
            "messages": null
        },
        "ResponseMetadata": {
            "RequestId": "RequestId"
        }
    }
}
```

When Queue has Messages:
```json
{
    "ReceiveMessageResponse": {
        "ReceiveMessageResult": {
            "messages": [
                {
                    "Attributes": null,
                    "Body": "messageBody",
                    "MD5OfBody": "MD5OfBody",
                    "MD5OfMessageAttributes": null,
                    "MessageAttributes": null,
                    "MessageId": "Queue Message ID",
                    "ReceiptHandle": "ReceiptHandle"
                }
            ]
        },
        "ResponseMetadata": {
            "RequestId": "requestID"
        }
    }
}
```

## Cleanup

Delete the stack using SAM:
```
sam delete
```

Confirm when prompted to delete the stack and its resources.

Note: You can also use `sam delete --no-prompts` to skip confirmation steps.

---

Copyright 2024 Amazon.com, Inc. or its affiliates. All Rights Reserved.
SPDX-License-Identifier: MIT-0
