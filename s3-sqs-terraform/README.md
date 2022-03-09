# AWS S3 to AWS SQS 

Sends notifications from S3 to SQS when an object is created

Learn more about this pattern at Serverless Land Patterns: [https://serverlessland.com/patterns/s3-sqs](https://serverlessland.com/patterns/s3-sqs)

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
    cd s3-sqs-terraform
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

## How it works

This template creates an S3 bucket, allows you to upload objects to that bucket, and will send you notifications from S3 to SQS when an object is created in that bucket.

## Example event payload from EventBridge to SQS
```
{
    "Messages": [
        {
            "Body": "{\"Records\":[{\"eventVersion\":\"2.1\",\"eventSource\":\"aws:s3\",\"awsRegion\":\"us-east-1\",\"eventTime\":\"2022-03-08T16:05:00.346Z\",\"eventName\":\"ObjectCreated:Put\",\"userIdentity\":{\"principalId\":\"AWS:AROAV3HPQRS4DCLCF333I:i-1234567890\"},\"requestParameters\":{\"sourceIPAddress\":\"1.1.1.1\"},\"responseElements\":{\"x-amz-request-id\":\"8E48JWWWWWXHY65\",\"x-amz-id-2\":\"3QiK7dwWWgAJkrT0r374ONYvUHVzJLPgX3qRBGhK3SJQ2LV/AO0wl3hdUU+OdPcWkXis3rPYhegSAXXdcQxJIytl+Qeqta5oKlhjomKTk=\"},\"s3\":{\"s3SchemaVersion\":\"1.0\",\"configurationId\":\"tf-s3-queue-20220308160319846800000003\",\"bucket\":{\"name\":\"serverlessland-terraform-s3-sqs-123456789100\",\"ownerIdentity\":{\"principalId\":\"A3TQVHWWWWJRXR\"},\"arn\":\"arn:aws:s3:::serverlessland-terraform-s3-sqs-123456789100\"},\"object\":{\"key\":\"README.md\",\"size\":2663,\"eTag\":\"6f9e107ffe28d4ff6wewe37a592f130b6\",\"sequencer\":\"006229999AC4E668A16\"}}}]}", 
            "ReceiptHandle": "AQEBQhdUK6MGfKpMDQSNtVssi/i5L9R3EHHpks85r4sAaxocQguy4fmn4Ux9jSSesBKO/J7C46ttWXwwwwm6h++QvxJkxrcB/HzFSCFuvYQWF5oVo2cE4LSecWwHO9JV83KYRPmkplMKEomwoT/5eAKUf2ht4u3GhX5V8WWsqERV80whyl3/S7Om3ex8zP0Ci5x118Apqo6GgIQsqNmSx2H/FnWPZhMniNIA/wUHtDABr2zZ2ymk8DGiNMda5CyOtR8g1dNXpbiuG9BXMkgBzFmdavJTCe55yVUgj+3+kNDsUHVudqcBRKbUUemsr5mKPZmyJb6uk/dEh3UjvO4euTaE/3UkTErL/Nq/jzpzn4KNZEsoN7FxgBLB9c47YGdOq0l/fqvqMCt57bmo8tLf0fRZFMGRmjQQbPJd7rpEjV8LsL74=", 
            "MD5OfBody": "bc3ca7772533df39aw7f7800163dd8ac", 
            "MessageId": "62086638-761d-420a-a331-3dd106c504b7"
        }
    ]
}
```

## Testing

1. Upload an object to the S3 bucket created by the deployment.
1. You can also use the below command to upload a file:
    ```bash
    aws s3 cp README.md s3://ENTER_YOUR_S3_BUCKET_NAME
    ```
1. Retrieve the message from the SQS queue, using the queue URL from the deployment outputs:
    ```bash
    aws sqs receive-message --queue-url ENTER_YOUR_QUEUE_URL
    ```

## Cleanup
 
1. Change directory to the pattern directory:
    ```
    cd s3-sqs-terraform
    ```
1. Delete all files from the S3 bucket
1. Delete all created resources
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
Copyright 2022 Amazon.com, Inc. or its affiliates. All Rights Reserved.

SPDX-License-Identifier: MIT-0
