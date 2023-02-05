# Amazon SQS batch error handling with AWS Lambda

The SAM template deploys a Lambda function, an SQS queue and the IAM permissions required to run the application. SQS invokes the Lambda function when new messages are available.

Learn more about this pattern at Serverless Land Patterns: [serverlessland.com/patterns/sqs-lambda-partial-batch-rust-sam](https://serverlessland.com/patterns/sqs-lambda-partial-batch-rust-sam)

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
    cd sqs-lambda-partial-batch-rust-sam
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

## Example event payload from SQS to Lambda

```
{
   "payload":"SqsEvent"{
      "records":[
         "SqsMessage"{
            "message_id":"Some(""7697a58e-fab7-4721-818b-7e0483324012"")",
            "receipt_handle":"Some(""AQEB8Eh+8C+Jp9VolnTbHSAY0szz5cHO7kOS6Far2HDlvdjqvT46biZwf6UX1zSJdY/AUaoM+B3g0IdF9xhKqFZkYoGp2FhPN4rZ9hb40YAK1U/818PIznkGjG8iGsoqFrmxY9D85Ip9+82tuTv79vc5jbn3w2LANU9V2fe+0Ge1XRwgHUf3l/677AYp77pWy2/nPGpRJ2EEGRh37OwQHr5HXM2rQK5Wercm9B6+FrSf+k/Vnza+rUwNhaCd/XUgiPu7DtQGQzN5Ooc3we+8bKuhzjlA9onINOdi/NiSMHASsU5cGQgvLDYC3PE7naeoBP/l8bFb/XuhVMC86aV4krQmgT4YVlE9Ptr+ftpBgsNXyqi3jGKxXLum3fMfZAWRCJ1w1KCDjb857C/z3jMmPdj5NmnTbJqaDzc/cishAFy5R/4="")",
            "body":"Some(""{\"to_error\":\"Boom\",\"surname\":\"Kaboom\"}"")",
            "md5_of_body":"Some(""7ac8a6db4f6530a9e634d14d975e0c3a"")",
            "md5_of_message_attributes":"None",
            "attributes":{
               "SenderId":"AROAYKMZLNCDSKNYVGYUR:botocore-session-1650176085",
               "SentTimestamp":"1650176093155",
               "ApproximateReceiveCount":"1",
               "ApproximateFirstReceiveTimestamp":"1650176093156"
            },
            "message_attributes":{
               
            },
            "event_source_arn":"Some(""arn:aws:sqs:<AWS_REGION>:<AWS_ACCOUNT_ID>:<QUEUE_NAME>"")",
            "event_source":"Some(""aws:sqs"")",
            "aws_region":"Some(""<AWS_REGION>"")"
         }
      ]
   },
   "context":"Context"{
      "request_id":"92d6a05d-d85f-532b-94b4-fa886ad0ff36",
      "deadline":1650176123407,
      "invoked_function_arn":"arn:aws:lambda:<AWS_REGION>:<AWS_ACCOUNT_ID>:function:<LAMBDA_NAME>",
      "xray_trace_id":"Root=1-625bb05d-1a3aa99c0aad77281463141e;Parent=66a523bf7ff75ec5;Sampled=0",
      "client_context":"None",
      "identity":"None",
      "env_config":"Config"{
         "function_name":"<LAMBDA_NAME>",
         "memory":128,
         "version":"$LATEST",
         "log_stream":"2022/04/17/[$LATEST]c989cfef07364511a0a628e8bbdb40a1",
         "log_group":"/aws/lambda/<LAMBDA_NAME>"
      }
   }
}
```
### Testing

Use the [AWS CLI](https://aws.amazon.com/cli/) to send a message to the SNS topic and observe the event delivered to the Lambda function:

1. Send the SQS message:

```bash
aws sqs send-message-batch --queue-url ENTER_YOUR_SQS_QUEUE_URL --entries file://event.json

```

2. Then check the logs in Cloudwatch logs, you should see something like

```bash
do_something MyStruct { name: "Daniele", surname: "Frasca" }
```

3. Then check the dead letter, you should see one message there

```bash
  {
    "to_error": "Boom",
    "surname": "Kaboom"
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
