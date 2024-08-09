Amazon EventBridge to trigger AWS Lambda function to exports all the REST API Gateway resources along with either the backend integrations or authorizers based on choice and store this in a S3 bucket.

The AWS SAM template deploys an Amazon EventBridge Scheduler to trigger an AWS Lambda function based on a user schedule to exports all the REST API Gateway resources along with either the backend integrations or authorizers based on choice and store this in a S3 bucket.

The template contains a sample Lambda function that exports all the REST API Gateway resources along with either the backend integrations or authorizers based on choice, stores these backup files with the API Key ID appended to the file name, on the folder within the chosen S3 bucket. Notifies the users, using a SNS topic once the backup has been successfully secured or with the information containing the reason for failure.

Important: this application uses various AWS services and there are costs associated with these services after the Free Tier usage - please see the [AWS Pricing page](https://aws.amazon.com/pricing/) for details. You are responsible for any AWS costs incurred. No warranty is implied in this example.

Requirements
------------
- [Create an AWS account](https://portal.aws.amazon.com/gp/aws/developer/registration/index.html) if you do not already have one and log in. The IAM user that you use must have sufficient permissions to make necessary AWS service calls and manage AWS resources.
- [AWS CLI](https://docs.aws.amazon.com/cli/latest/userguide/install-cliv2.html) installed and configured
- [Git Installed](https://git-scm.com/book/en/v2/Getting-Started-Installing-Git)
- [AWS Serverless Application Model](https://docs.aws.amazon.com/serverless-application-model/latest/developerguide/serverless-sam-cli-install.html) (AWS SAM) installed
- Make sure that you have the [S3 bucket](https://docs.aws.amazon.com/AmazonS3/latest/userguide/creating-bucket.htmlhttps://docs.aws.amazon.com/AmazonS3/latest/userguide/creating-bucket.html) name to save the backup files, email address for sending notification via [SNS](https://docs.aws.amazon.com/sns/latest/dg/welcome.html), cronjob expression for [Event bridge scheduler](https://docs.aws.amazon.com/scheduler/latest/UserGuide/what-is-scheduler.html).
- You have an option to export the [API Gateway](https://docs.aws.amazon.com/apigateway/latest/developerguide/welcome.html) resource [integrations](https://docs.aws.amazon.com/apigateway/latest/developerguide/how-to-integration-settings.html) or the [authorizers](https://docs.aws.amazon.com/apigateway/latest/developerguide/apigateway-control-access-to-api.html) attached to the resources. The default value is integration. You can have two seperate deployments if you wish to export both the API Gateway resource integrations and the authorizers attached to the resources.

Deployment Instructions:
-------------------------

1. Create a new directory, navigate to that directory in a terminal and clone the GitHub repository:

```
git clone https://github.com/aws-samples/serverless-patterns
```
2. Change directory to the pattern directory:

```
cd eventbridge-lambda-apigateway-backup-export-S3
```
3. From the command line, use AWS SAM to deploy the AWS resources for the pattern as specified in the template.yml file:

```
sam deploy --guided --capabilities CAPABILITY_AUTO_EXPAND CAPABILITY_IAM CAPABILITY_NAMED_IAM
```

4. During the prompts enter the values corresponding to each field. The values in the square brackets are the default values, which can be overwritten once you enter the inputs.

```
Stack Name [sam-app]:    
AWS Region [us-east-1]: 
Parameter CronSchedule [Default = [0 0/6 **?*] every six hours]:
Parameter Email []:
#Enter your choise of export here beteween integrations and authorizers
Parameter Choice [integrations]:
#Enter the S3 bucket name where you would like have your API gateway exports stored.
Parameter S3BucketName []:
#Shows you resources changes to be deployed and require a 'Y' to initiate deploy
Confirm changes before deploy [y/N]:
#SAM needs permission to be able to create roles to connect to the resources in your template
Allow SAM CLI IAM role creation [Y/n]:
#Preserves the state of previously provisioned resources when an operation fails
Disable rollback [y/N]:
Save arguments to configuration file [Y/n]:
SAM configuration file [samconfig.toml]:
SAM configuration environment [default]: 
```

4. Allow SAM CLI to create IAM roles with the required permissions.
Once you have run sam deploy --guided mode once and saved arguments to a configuration file (samconfig.toml), you can use sam deploy in future to use these defaults.

6. Note the outputs from the SAM deployment process. These contain the resource names and/or ARNs which are used for later review.

How it works:
-------------

This pattern sets up the following resources:

- An Amazon EventBridge Scheduler that triggers a [Lambda](https://docs.aws.amazon.com/lambda/latest/dg/welcome.html) function based on the schedule defined by the customer
- A Lambda function to export the REST API Gateway resources along with the integrations or authorizers and store in the S3 bucket on the same account and region, based on the customer's input.
- IAM roles for each of the above service with minimum permission to perform the task.
- An SNS topic that notifies for any failures while creating snapshots.

Testing:
--------

- In the Outputs tab of the AWS CloudFormation console, note the SNSTopic , EventBridgeScheduler , EventBridgeSchedulerRole , LambdaExecutionRole, LambdaFunction outputs. 
- Kindly provide all the requested details. Based on the provided schedule, monitor the CloudWatch logs for Lambda function and S3 bucket where the API Gateway backups will be stored.
- The Lambda will automatically send notifications for any kinds of failures within the API calls to the configured email ID.
- Once you receive the first email from the SNS, kindly ensure that you have accepted the subscription. 


Cleanup:
--------

Delete the stack:

```
sam delete
```

Copyright 2023 Amazon.com, Inc. or its affiliates. All Rights Reserved.

SPDX-License-Identifier: MIT-0
