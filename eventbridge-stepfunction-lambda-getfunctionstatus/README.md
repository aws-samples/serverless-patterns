# EventBridge scheduler to invoke step function to get the list of inactive lambda functions

This pattern will create a one time schedule in EventBridge scheduler with state machine as target & invoke the lambda ListFunctions & GetFunction API using the SDK integration in step functions and publish the list of inactive functions to SNS Topic.

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

7. **Imp** : Once the SNS topic & subscription is created, verify the subscription by clicking the 'Confirm subscription' link received on your email. 


## How it works

1. When the stack is deployed it creates a state machine, an eventBridge scheduler,a SNS topic with email subscription, a Lambda Function and required IAM roles. 

2. Event Bridge scheduler invokes the State machine on defined schedule, Default schedule invokes the state machine daily at 00::00 UTC with the below mentioned payload. Modify the schedule as per your requirement.

    ```json
    {
        "Function_ARN_List_existing": {
        "lambda_arn_list_combined": []
        },
        "NextMarker": null
    }
    ```

3) In state machine, the 1st step is to get the list of all lambda functions in the current region using the ListFunctions API, ListFunctions API is called multiple times as it returns max 50 functions list in a single API call along with NextMarker pagination parameter. Using NextMarker token state machine retrieves list of all the function ARN's.

4) Lambda Invoke Combine data Step : This a custom lambda function python script to create a combined json array of Lambda function ARN's retrieved in step 1.

5) Map - Loop Functions State : In this state, GetFunction API is called for each Lambda ARN taken as input from previous step & status of each function is checked and appended to the output.

6) Filter Inactive Functions State : This filters out the Active functions from the Json array and passes only the Inactive functions list to the next step.

7) SNS Publish : List of Inactive functions is published to the SNS Topic.


## Cleanup
 
1. Delete the stack
    ```bash
    sam delete
    ```

2. Also, you have to manually delete any schedules you created if required.

----
Copyright 2022 Amazon.com, Inc. or its affiliates. All Rights Reserved.

SPDX-License-Identifier: MIT-0