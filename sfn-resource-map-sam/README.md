# Mapping AWS Step Functions present in a region using SAM

This pattern creates a Amazon S3 bucket, two AWS Lambda functions and AWS Step Functions state machine. The lambda functions are responsible for mapping the state machines across a region in the AWS account and store the results as a CSV file in the S3 bucket. The created state machine orchestrates the entire process.

Learn more about this pattern at Serverless Land Patterns: https://serverlessland.com/patterns/sfn-resource-map-sam


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
    cd sfn-resource-map-sam
    ```
3. From the command line, use AWS SAM to deploy the AWS resources for the pattern as specified in the template.yml file:
    ```
    sam deploy --guided
    ```
4. During the prompts:
    * Enter a stack name
    * Enter the desired AWS Region
    * Enter the S3 Bucket Name to be used
    * Confirm changes before deploy
    * Allow SAM CLI to create IAM roles with the required permissions.
    * Deploy changes after creation of changeset

    Once you have run `sam deploy --guided` mode once and saved arguments to a configuration file (samconfig.toml), you can use `sam deploy` in future to use these defaults.

5. Note the outputs from the SAM deployment process. These contain the resource names and/or ARNs which are used for testing.

## How it works

Once the template creates all the resources, the state machine that was created is used to orchestrate the process of mapping all the state machines present in that particular region. The state machine invokes the two lambda functions in a specific order which are responsible for placing the necessary API calls to fetch the list of all the state machines present along with a list of its integrated AWS services.

Currently, this workflow/pattern maps the state machines present in a region and also gives the details of errors and throttles for the past 7 days, but it can be further modified to extend the duration.

## Testing

1. Under stack resources, open the state machine created
2. Start the execution of that state machine with default/empty input
3. Once the state machine execution is successful, navigate to the created S3 bucket to view the result which consists of a CSV file with details of the state machines present in that region.

## Cleanup

```
 sam delete
 ```
 
----
Copyright 2024 Amazon.com, Inc. or its affiliates. All Rights Reserved.

SPDX-License-Identifier: MIT-0