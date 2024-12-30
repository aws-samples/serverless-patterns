# Amazon EventBridge Scheduler to invoke an AWS Step Function to get the list of inactive AWS Lambda functions

This pattern will create an Amazon EventBridge Scheduler rule targeting an AWS Step Function state machine. The Step Function invokes an AWS Lambda using `ListFunctions` and `GetFunctions` API using the SDK integration in Step Functions. It then publishes the list of inactive functions to an Amazon SNS Topic.

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
    cd eventbridge-stepfunction-lambda-getfunctionstatus
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


    * Enter **stack name**.
    * Enter desired **AWS Region**.
    * Enter your **Email Address** (e.g. abcd@xyz.com) for the EmailAddress parameter.
    * Allow SAM CLI to create IAM roles with the required permissions.

    Once you have run `sam deploy --guided` mode once and saved arguments to a configuration file (samconfig.toml), you can use `sam deploy` in future to use these defaults.

6. Note the outputs from the SAM deployment process. These contain the resource names and/or ARNs which are used for testing.

7. **Important** : Once the SNS topic & subscription is created, verify the subscription by clicking the 'Confirm subscription' link received on your email. 


## How it works

1. When the stack is deployed it creates a state machine, an Event Bridge Scheduler, an SNS topic with email subscription, a Lambda function and required IAM roles.

2. Event Bridge Scheduler invokes the state machine with a defined schedule. The default schedule invokes the state machine daily at 00:00 UTC with the below mentioned payload. Modify the schedule as per your requirement.

    ```json
    {
        "Function_ARN_List_existing": {
        "lambda_arn_list_combined": []
        },
        "NextMarker": null
    }
    ```

3) In state machine, the 1st step is to get the list of all lambda functions in the current region using the ListFunctions API, ListFunctions API is called multiple times as it returns max 50 functions list in a single API call along with NextMarker pagination parameter. Using NextMarker token state machine retrieves list of all the function ARNs.

4) Lambda Invoke Combine data Step : This a custom Lambda function python script to create a combined JSON array of Lambda function ARNs retrieved in step 1.

5) Map - loop functions state: In this state, the GetFunction API is called for each Lambda ARN taken as input from the previous step, and the status of each function is checked and appended to the output.

6) Filter inactive functions state: This filters out the active functions from the JSON array and passes only the list of inactive functions to the next step.

7) SNS publish : List of inactive functions is published to the SNS Topic.


## Cleanup
 
1. Delete the stack
    ```bash
    sam delete
    ```

2. Also, you have to manually delete any schedules you created if required.

----
Copyright 2024 Amazon.com, Inc. or its affiliates. All Rights Reserved.

SPDX-License-Identifier: MIT-0