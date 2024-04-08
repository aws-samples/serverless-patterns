# Amazon Eventbridge Schedule to Invoke AWS Lambda

The application creates an Eventbridge Schedule for every 5 minutes that invokes a Lambda function.  The function in this example uses the Java11 runtime.  For more information on Amazon EventBridge Scheduler, please see the [User Guide](https://docs.aws.amazon.com/scheduler/latest/UserGuide/what-is-scheduler.html).

Important: this application uses various AWS services and there are costs associated with these services after the Free Tier usage - please see the AWS Pricing page for details. You are responsible for any AWS costs incurred. No warranty is implied in this example.

## Requirements
* [Create an AWS account](https://portal.aws.amazon.com/gp/aws/developer/registration/index.html) if you do not already have one and log in. The IAM user that you use must have sufficient permissions to make necessary AWS service calls and manage AWS resources.
* [AWS CLI](https://docs.aws.amazon.com/cli/latest/userguide/install-cliv2.html) installed and configured
* [Git](https://git-scm.com/book/en/v2/Getting-Started-Installing-Git) installed and configured
* [AWS CDK](https://docs.aws.amazon.com/cdk/latest/guide/cli.html) installed and configured
* [Maven](https://maven.apache.org/download.cgi) installed and configured

## Deployment Instructions

1. Create a new directory, navigate to that directory in a terminal and clone the GitHub repository:
    ``` 
    git clone https://github.com/aws-samples/serverless-patterns
    ```
1. Change directory to the pattern directory:
    ```
    cd serverless-patterns/eventbridge-schedule-to-lambda-cdk-java
    ```
1. From the command line, use Maven to build and package the project
    ```
    mvn clean package
    ```
1. Next, configure the AWS CDK.:
    ```
    cdk bootstrap <ACCOUNT-NUMBER>/<REGION>
   ```
   For example: 
    ```cdk bootstrap 1111111111/us-east-1```
    Or,
    ```cdk bootstrap --profile test 1111111111/us-east-1```

1. Deploy the stack (Accept prompt):
    ```
    cdk deploy
    ```

## How it works
This solution uses Amazon EventBridge Scheduler to create a schedule that runs every 5 minutes, invoking a Lambda function.  EventBridge Scheduler supports a [variety of scheduler types](https://docs.aws.amazon.com/scheduler/latest/UserGuide/schedule-types.html) and needs.

## Testing
1. Login to the AWS Console (ensure you are in the right region)
2. Navigate to the Lambda Service and find the function created (starts with "CdkSchedulerStack-ScheduledFunction")
3. View Lambda metrics to observe invoke every 5 minutes

## Cleanup

1. Delete the stack
```bash
   cdk destroy
```
----
Copyright 2022 Amazon.com, Inc. or its affiliates. All Rights Reserved.

SPDX-License-Identifier: MIT-0
