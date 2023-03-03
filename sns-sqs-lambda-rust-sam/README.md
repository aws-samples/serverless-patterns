# Amazon SNS to Amazon SQS to AWS Lambda

The SAM template deploys a SNS topic and an SQS queue a. The SQS queue is subscribed to the SNS topic. SNS invokes the SQS queue when new messages are available. When messages are sent to the SNS topic, they are delivered as a JSON event payload to the SQS queue. SQS invokes the Lambda function when new messages are available.

Learn more about this pattern at Serverless Land Patterns: [serverlessland.com/patterns/sns-sqs-lambda-rust-sam](https://serverlessland.com/patterns/sns-sqs-lambda-rust-sam)

Important: this application uses various AWS services and there are costs associated with these services after the Free Tier usage - please see the [AWS Pricing page](https://aws.amazon.com/pricing/) for details. You are responsible for any AWS costs incurred. No warranty is implied in this example.

## Requirements

* [Create an AWS account](https://portal.aws.amazon.com/gp/aws/developer/registration/index.html) if you do not already have one and log in. The IAM user that you use must have sufficient permissions to make necessary AWS service calls and manage AWS resources.
* [AWS CLI](https://docs.aws.amazon.com/cli/latest/userguide/install-cliv2.html) installed and configured
* [Git Installed](https://git-scm.com/book/en/v2/Getting-Started-Installing-Git)
* [AWS Serverless Application Model](https://docs.aws.amazon.com/serverless-application-model/latest/developerguide/serverless-sam-cli-install.html) (AWS SAM) installed
* [Rust](https://www.rust-lang.org/) 1.56.0 or higher
* [cargo-zigbuild](https://github.com/messense/cargo-zigbuild) and [Zig](https://ziglang.org/) for cross-compilation
* Make sure to run "rustup target add aarch64-unknown-linux-gnu;"

## Deployment Instructions

1. Create a new directory, navigate to that directory in a terminal and clone the GitHub repository:
    ``` 
    git clone https://github.com/aws-samples/serverless-patterns
    ```
2. Change directory to the pattern directory:
    ```
    cd sns-sqs-lambda-rust-sam
    ```
3. Install dependencies and build:
    ```
    make build
    ```
4. From the command line, use AWS SAM to deploy the AWS resources for the pattern as specified in the template.yml file:
    ```
    make deploy
    ```
5. During the prompts:
    * Enter a stack name
    * Enter the desired AWS Region
    * Allow SAM CLI to create IAM roles with the required permissions.

    Once you have run `sam deploy -guided` mode once and saved arguments to a configuration file (samconfig.toml), you can use `sam deploy` in future to use these defaults.

6. Note the outputs from the SAM deployment process. These contain the resource names and/or ARNs which are used for testing.

## Example event payload received by SQS

```
{
   "payload":"SqsEvent"{
      "records":[
         "SqsMessage"{
            "message_id":"Some(""e5590114-9769-4e09-8abc-ee7ba4424f14"")",
            "receipt_handle":"Some(""AQEBzqB0RmARy4EXXx1lppLFjB6znJenfWb/scFVhvzLa9+b0gXD+nQ0JrzLonrX/z0T/VgYvFaAybfAs6jhZ68Ja3VAnAA1icFq+KCC+QHS1Y/wgRycjzpvG6DsV/hkxSR6mBlnlU8nBT6HChMVRceNjO8G9Rk4Zm8nbpK+uAFFfJmzpIi/JzxmZgH1tth8NUyyj9nhYpLXHe1VVZLWAENZVFvDg4o22eFL0fptd00K5LeWADaRZ583kvbfCvRcEAxIEbm6JxUdV9sezNnBgoSztTks2M2R9YNSKcdoWQQI3XELDUEhJSiu4WXXee7Lxim5yMuGACc3xwN2TTobIvCSbuJjqL0PKmp02zn5cdqUCIIsEWqJfm75tNS9qyCNbVmIhLjkvUXOPJOc13S6OoPFviSHotY5zaRmvsIFqUe/OKA="")",
            "body":"Some(""{\n  \"Type\" : \"Notification\",\n  \"MessageId\" : \"1565b3e1-2535-56c3-a82b-e932106f3869\",\n  \"TopicArn\" : \"arn:aws:sns:<AWS_REGION>:<Account_ID>:<SNS_TOPIC_NAME>\",\n  \"Message\" : \"{\\n  \\\"name\\\": \\\"Daniele\\\",\\n  \\\"surname\\\": \\\"Frasca\\\"\\n}\",\n  \"Timestamp\" : \"2022-04-15T08:55:54.760Z\",\n  \"SignatureVersion\" : \"1\",\n  \"Signature\" : \"JHkTwu/ZWa2l4jXTLN8zLi6Vpn+efopcTwtz3uOPoaIdHaBHjzw8LsWMG6pTe6u56xiRTSYlPzVYRiyyew3rXtWVnLDyrkfcKfa3GD5IvqxaNiFg5ekWj91I9YwJ++H7ITXlOUJhAAwnkkfwIoqKgCjP2kOrnZGc5i80qvaHPsTWKR4F+UBSmk9qYxuzrJZVaeUtHRYu9I1H5TiTsUqZTrde8ailur0cQxj73w0Pn1Wv5kmrihjrC48oyETZp7o4dQlkdL2eg0ZhwSI0V/rKTiDcmzCmhMXUA56la0VW/d5fef0LRlI8IDlBlW4aKbCmW0ybevXW/+wc6XAf0rSN9g==\",\n  \"SigningCertURL\" : \"https://sns.<AWS_REGION>.amazonaws.com/SimpleNotificationService-7ff5318490ec183fbaddaa2a969abfda.pem\",\n  \"UnsubscribeURL\" : \"https://sns.<AWS_REGION>.amazonaws.com/?Action=Unsubscribe&SubscriptionArn=arn:aws:sns:<AWS_REGION>:<Account_ID>:<SNS_TOPIC_NAME>:819e2f00-16cf-458f-861b-e5114393b34a\"\n}"")",
            "md5_of_body":"Some(""1d0a5959e71c23ceaee1e889fc62e0c5"")",
            "md5_of_message_attributes":"None",
            "attributes":{
               "ApproximateFirstReceiveTimestamp":"1650012954798",
               "ApproximateReceiveCount":"1",
               "SenderId":"AIDAISDDSWNBEXIA6J64K",
               "SentTimestamp":"1650012954791"
            },
            "message_attributes":{
               
            },
            "event_source_arn":"Some(""arn:aws:sqs:<AWS_REGION>:<Account_ID>:<QUEUE_NAME>"")",
            "event_source":"Some(""aws:sqs"")",
            "aws_region":"Some(""<AWS_REGION>"")"
         }
      ]
   },
   "context":"Context"{
      "request_id":"5b7ed803-f589-52c6-ab0a-82d0c0da845f",
      "deadline":1650012984842,
      "invoked_function_arn":"arn:aws:lambda:<AWS_REGION>:<Account_ID>:function:<LAMBDA_NAME>",
      "xray_trace_id":"Root=1-6259331a-67d3998e087dc8d35907de4b;Parent=6e26ffcd64a2e3e3;Sampled=0",
      "client_context":"None",
      "identity":"None",
      "env_config":"Config"{
         "function_name":"<LAMBDA_NAME>",
         "memory":128,
         "version":"$LATEST",
         "log_stream":"2022/04/15/[$LATEST]2f90729801894db098d6decfcfa6e34f",
         "log_group":"/aws/lambda/<LAMBDA_NAME>"
      }
   }
}
```
### Testing

Use the [AWS CLI](https://aws.amazon.com/cli/) to send a message to the SNS topic and observe the event delivered to the Lambda function:

1. Send the SNS message:

```bash
aws sns publish --topic-arn ENTER_SNS_TOPIC_ARN --message file://event.json
```

2. Then check the logs in Cloudwatch logs, you should see something like

```bash
 { 
   name: "Daniele", 
   surname: "Frasca" 
 }
```

## Cleanup
 
1. Delete the stack
    ```bash
    make delete
    ```
2. Confirm the stack has been deleted
    ```bash
    aws cloudformation list-stacks --query "StackSummaries[?contains(StackName,'STACK_NAME')].StackStatus"
    ```
----
Copyright 2021 Amazon.com, Inc. or its affiliates. All Rights Reserved.

SPDX-License-Identifier: MIT-0
