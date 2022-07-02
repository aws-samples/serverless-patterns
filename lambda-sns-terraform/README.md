# AWS Lambda to Amazon SNS

The Terraform template deploys a Lambda function, an SNS topic and the IAM permissions required to run the application. The Lambda function publishes a message to the SNS topic when invoked.

Learn more about this pattern at Serverless Land Patterns: https://serverlessland.com/patterns/lambda-sns-terraform/.

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
    cd lambda-sns-terraform
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

## Example payload from SNS

```
{
  "Type" : "Notification",
  "MessageId" : "12345678-2045-5567-8d78-1234567890",
  "TopicArn" : "arn:aws:sns:us-east-1:123456789012:patterns-lambda-to-sns-MySnsTopic-1234567890",
  "Subject" : "New message from publisher",
  "Message" : "Message at Wed Feb 10 2021 13:28:10 GMT+0000 (Coordinated Universal Time)",
  "Timestamp" : "2021-02-10T13:28:11.255Z",
  "SignatureVersion" : "1",
  "Signature" : "ks1BRXk41234567890ZvJWznlw1234567890rjioy/G4Br1234567890ll1JEVF1234567890jjyb/lPxIFg123456789025pbdlD2C1234567890L2L0cq2g1234567890afD5BAkbC1234567890+aHMG1234567890jmiMmhTl1234567890r1L9ENgT1234567890U+ROFyh12345678901WeFD1234567890PqpiR0A43T+6Cz7N1234567890wlzln4m5gAw123456781234567890YN/1234567890/1234567890+f/1234567890==",
  "SigningCertURL" : "https://sns.us-east-1.amazonaws.com/SimpleNotificationService-1234567890636cd94b1234567890.pem",
  "UnsubscribeURL" : "https://sns.us-east-1.amazonaws.com/?Action=Unsubscribe&SubscriptionArn=arn:aws:sns:us-east-1:123456789012:patterns-lambda-to-sns-MySnsTopic-1234567890:1234567890-88ee-4bf8-a788-1234567890"
}

```

### Testing

Use the [AWS CLI](https://aws.amazon.com/cli/) to invoke the Lambda function. The function name is in the outputs of the Terraform deployment (the key is `TopicPublisherFunction`):

1. Invoke the Lambda function to publish a message to SNS:

```bash
aws lambda invoke --function-name ENTER_YOUR_FUNCTION_NAME response.json
```

## Cleanup
 
1. Change directory to the pattern directory:
    ```
    cd lambda-sns-terraform
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
