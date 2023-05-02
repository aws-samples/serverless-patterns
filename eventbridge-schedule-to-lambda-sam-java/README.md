# Amazon Eventbridge Schedule to Invoke AWS Lambda

The application creates an Eventbridge Schedule for every 5 minutes that invokes a Lambda function.  The function in this example uses the Java11 runtime.  For more information on Amazon EventBridge Scheduler, please see the [User Guide](https://docs.aws.amazon.com/scheduler/latest/UserGuide/what-is-scheduler.html).    

Important: this application uses various AWS services and there are costs associated with these services after the Free Tier usage - please see the AWS Pricing page for details. You are responsible for any AWS costs incurred. No warranty is implied in this example.

## Requirements
* [Create an AWS account](https://portal.aws.amazon.com/gp/aws/developer/registration/index.html) if you do not already have one and log in. The IAM user that you use must have sufficient permissions to make necessary AWS service calls and manage AWS resources.
* [AWS CLI](https://docs.aws.amazon.com/cli/latest/userguide/install-cliv2.html) installed and configured
* [Git](https://git-scm.com/book/en/v2/Getting-Started-Installing-Git) installed and configured
* [AWS SAM](https://docs.aws.amazon.com/serverless-application-model/latest/developerguide/serverless-sam-cli-install.html) installed and configured
* [Maven](https://maven.apache.org/download.cgi) installed and configured

## Deployment Instructions

1. Create a new directory, navigate to that directory in a terminal and clone the GitHub repository:
    ``` 
    git clone https://github.com/aws-samples/serverless-patterns
    ```
1. Change directory to the pattern directory:
    ```
    cd serverless-patterns/eventbridge-schedule-to-lambda-sam-java
    ```
1. From the command line, use AWS SAM to deploy the AWS resources for the pattern as specified in the template.yaml file:
    ```
    sam deploy --guided
    ```
1. During the prompts:
    * Enter a stack name
    * Enter the desired AWS Region
    * Allow SAM CLI to create IAM roles with the required permissions.

    Once you have run `sam deploy --guided` mode once and saved arguments to a configuration file (samconfig.toml), you can use `sam deploy` in future to use these defaults.

1. Note the outputs from the SAM deployment process. These contain the resource names and/or ARNs which are used for testing.

## How it works
This solution uses Amazon EventBridge Scheduler to create a schedule that runs every 5 minutes, inovoking a Lambda function.  EventBridge Scheduler supports a [variety of scheduler types](https://docs.aws.amazon.com/scheduler/latest/UserGuide/schedule-types.html) and needs. 


## Testing
Check the logs for the Lambda function using the `sam logs` command. Change the stack name to your stack name.
```bash
sam logs --stack-name <your stack name> --tail
```

## Cleanup
 
1. Delete the stack
```bash
   sam delete
```
----
Copyright 2022 Amazon.com, Inc. or its affiliates. All Rights Reserved.

SPDX-License-Identifier: MIT-0
