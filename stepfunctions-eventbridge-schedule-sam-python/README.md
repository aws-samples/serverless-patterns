# Step Functions to EventBridge Scheduler with SAM and Python

This pattern will create a one time schedule in EventBridge Scheduler with AWS Lambda as target using SDK integration in Step Functions.

Important: this application uses various AWS services and there are costs associated with these services after the Free Tier usage - please see the [AWS Pricing page](https://aws.amazon.com/pricing/) for details. You are responsible for any AWS costs incurred. No warranty is implied in this example.

## Requirements

* [Create an AWS account](https://portal.aws.amazon.com/gp/aws/developer/registration/index.html) if you do not already have one and log in. The IAM user that you use must have sufficient permissions to make necessary AWS service calls and manage AWS resources.
* [AWS CLI](https://docs.aws.amazon.com/cli/latest/userguide/install-cliv2.html) installed and configured
* [Git Installed](https://git-scm.com/book/en/v2/Getting-Started-Installing-Git)
* [AWS Serverless Application Model](https://docs.aws.amazon.com/serverless-application-model/latest/developerguide/serverless-sam-cli-install.html) (AWS SAM) installed

## Deployment Instructions

1. Create a new directory, navigate to that directory in a terminal and clone the GitHub repository:
    ``` 
    git clone https://github.com/aws-samples/serverless-patterns
    ```
2. Change directory to the pattern directory:
    ```
    cd stepfunctions-eventbridge-schedule-sam-python
    ```
3. Build the dependencies:
    ```
    sam build
    ```
4. From the command line, use AWS SAM to deploy the AWS resources for the pattern as specified in the template.yml file:
    ```
    sam deploy --guided
    ```
5. During the prompts:
    * Enter a stack name
    * Enter the desired AWS Region
    * Allow SAM CLI to create IAM roles with the required permissions.

    Once you have run `sam deploy --guided` mode once and saved arguments to a configuration file (samconfig.toml), you can use `sam deploy` in future to use these defaults.

6. Note the outputs from the SAM deployment process. These contain the resource names and/or ARNs which are used for testing.

## How it works

1. When the stack is deployed it creates a Step Functions state machine, an EventBridge Scheduler Group, a Lambda Function and required IAM roles. 

2. In the state machine, there is one step to create a one time schedule with the Lambda function as the target using SDK integration.

3. When a Step Function execution initialized with a payload with below structure, it will create a one time schedule.
    ```json
    {
      "scheduleDate": "YYYY-MM-DD",
      "scheduleTime": "hh:mm:ss"
    }
    ```

## Cleanup
 
1. Delete the stack
    ```bash
    sam delete
    ```

2. Also, you have to manually delete any schedules you created if required.

----
Copyright 2022 Amazon.com, Inc. or its affiliates. All Rights Reserved.

SPDX-License-Identifier: MIT-0