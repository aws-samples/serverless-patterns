# Process Amazon SNS notification messages with AWS Lambda (Python)

This patterns shows how to process Amazon SNS messages using AWS Lambda. The AWS SAM template deploys an AWS Lambda function, an Amazon SNS topic, and the IAM permissions required to run the application. Lambda subscribes to the SNS topic to process notifications messages. When you publish a message to the SNS topic, SNS sends the message to the Lambda service asynchronously. The Lambda service invokes the the Lambda function.

- Processing results are logged to Amazon CloudWatch Logs

Learn more about this pattern at Serverless Land Patterns: [https://serverlessland.com/patterns/sns-lambda-python-sam](https://serverlessland.com/patterns/sns-lambda-python-sam)

:heavy_exclamation_mark: Important: this application uses various AWS services and there are costs associated with these services after the Free Tier usage - please see the [AWS Pricing page](https://aws.amazon.com/pricing/) for details. You are responsible for any AWS costs incurred. No warranty is implied in this example.

## Requirements

* [Create an AWS account](https://portal.aws.amazon.com/gp/aws/developer/registration/index.html) if you do not already have one and log in. The IAM user that you use must have sufficient permissions to make necessary AWS service calls and manage AWS resources.
* [AWS CLI](https://docs.aws.amazon.com/cli/latest/userguide/install-cliv2.html) installed and configured
* [Git Installed](https://git-scm.com/book/en/v2/Getting-Started-Installing-Git)
* [AWS Serverless Application Model](https://docs.aws.amazon.com/serverless-application-model/latest/developerguide/serverless-sam-cli-install.html) (AWS SAM) installed

## Download Instructions

If you download this pattern as part of the AWS Toolkit for your IDE, the toolkit downloads the files into the directory you specify.

To download the patterns yourself: 
1. Create a new directory, navigate to that directory in a terminal and clone the GitHub repository:
    ``` 
    git clone https://github.com/aws-samples/serverless-patterns
    ```
1. Change directory to the pattern directory:
    ```
    cd sns-lambda-python-sam
    ```

## Deployment Instructions

*For additional information on features to help you author, build, debug, test, and deploy Lambda applications more efficiently when using Visual Studio Code, see [Introducing an enhanced local IDE experience for AWS Lambda developers](https://aws.amazon.com/blogs/compute/introducing-an-enhanced-local-ide-experience-for-aws-lambda-developers?trk=2dd77e51-cb93-4970-a61a-5993781e5576&sc_channel=el).*

1. From the command line, use AWS SAM to deploy the AWS resources for the pattern as specified in the `template.yaml` file:
    ```
    sam deploy --guided
    ```
1. During the prompts:

1. During the prompts:
    * Enter a stack name.
    * Enter the desired AWS Region.
    * Allow AWS SAM CLI to create IAM roles with the required permissions.

    Once you have run `sam deploy -guided` mode once and saved arguments to a configuration file `samconfig.toml`, you can use `sam deploy` in future to use these defaults.

1. Note the outputs from the AWS SAM deployment process. These contain the resource names and/or ARNs to use for testing.
   
## Example event payload from SNS to Lambda

```
{
    "Records": [
      {
        "EventVersion": "1.0",
        "EventSubscriptionArn": "arn:aws:sns:us-east-1:123456789012:sns-lambda:21be56ed-a058-49f5-8c98-aedd2564c486",
        "EventSource": "aws:sns",
        "Sns": {
          "SignatureVersion": "1",
          "Timestamp": "2019-01-02T12:45:07.000Z",
          "Signature": "tcc6faL2yUC6dgZdmrwh1Y4cGa/ebXEkAi6RibDsvpi+tE/1+82j...65r==",
          "SigningCertURL": "https://sns.us-east-1.amazonaws.com/SimpleNotificationService-ac565b8b1a6c5d002d285f9598aa1d9b.pem",
          "MessageId": "95df01b4-ee98-5cb9-9903-4c221d41eb5e",
          "Message": "Hello from SNS!",
          "MessageAttributes": {
            "Test": {
              "Type": "String",
              "Value": "TestString"
            },
            "TestBinary": {
              "Type": "Binary",
              "Value": "TestBinary"
            }
          },
          "Type": "Notification",
          "UnsubscribeUrl": "https://sns.us-east-1.amazonaws.com/?Action=Unsubscribe&amp;SubscriptionArn=arn:aws:sns:us-east-1:123456789012:test-lambda:21be56ed-a058-49f5-8c98-aedd2564c486",
          "TopicArn":"arn:aws:sns:us-east-1:123456789012:sns-lambda",
          "Subject": "TestInvoke"
        }
      }
    ]
  }

```
There is also a sample file `\events\test-event.json` which contains a sample event payload.

### Testing

Use the [AWS CLI](https://aws.amazon.com/cli/) to send a message to the SNS topic and observe the event delivered to the Lambda function:

1. Send 10 messages to the SNS topic:

#### Bash
```bash
for i in {1..10}; do aws sns publish --topic-arn <<ENTER_YOUR_SNS_TOPIC_ARN>> --message "{\"message\": \"Test message-$i\"}"; done
```

##### PowerShell
```PowerShell
1..10 | ForEach-Object { aws sns publish --topic-arn <<ENTER_YOUR_SNS_TOPIC_ARN>> --message "{`"message`": `"Test message-$_`"}" }
```

2. Retrieve the logs from the Lambda function:
```bash
sam logs -n ENTER_YOUR_CONSUMER_FUNCTION_NAME
```

## Cleanup
 
1. Delete the stack
    ```bash
    sam delete --stack-name STACK_NAME
    ```
1. Confirm the stack has been deleted
    ```bash
    aws cloudformation list-stacks --query "StackSummaries[?contains(StackName,'STACK_NAME')].StackStatus"
    ```
----
Copyright 2025 Amazon.com, Inc. or its affiliates. All Rights Reserved.

SPDX-License-Identifier: MIT-0