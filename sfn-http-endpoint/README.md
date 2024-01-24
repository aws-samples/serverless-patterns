# HTTP Endpoint Task From Step Function with SAM

The SAM template deploys a Step Function, the Step Function Execution Role and an Event Bridge Connection.

The HTTP Endpoint task uses an Event Bridge Connection to authenticate the request to the endpoint. The Step Functon Execution Role contains all the permissions for it to be able to get the Event Bridge Connection as well as to be able to call the specific endpoint.

Learn more about this pattern at Serverless Land Patterns: [https://serverlessland.com/patterns/sfn-http-endpoint](https://serverlessland.com/patterns/sfn-http-endpoint)

Important: this application uses various AWS services and there are costs associated with these services after the Free Tier usage - please see the [AWS Pricing page](https://aws.amazon.com/pricing/) for details. You are responsible for any AWS costs incurred. No warranty is implied in this example.

## Requirements

* [Create an AWS account](https://portal.aws.amazon.com/gp/aws/developer/registration/index.html) if you do not already have one and log in. The IAM user that you use must have sufficient permissions to make necessary AWS service calls and manage AWS resources.
* [AWS CLI](https://docs.aws.amazon.com/cli/latest/userguide/install-cliv2.html) installed and configured
* [Git Installed](https://git-scm.com/book/en/v2/Getting-Started-Installing-Git)
* [AWS Serverless Application Model](https://docs.aws.amazon.com/serverless-application-model/latest/developerguide/serverless-sam-cli-install.html) (AWS SAM) installed
* [OpenWeather API](https://openweathermap.org/api) Create free API Key
## Deployment Instructions

1. Create a new directory, navigate to that directory in a terminal and clone the GitHub repository:
    ``` 
    git clone https://github.com/aws-samples/serverless-patterns
    ```
1. Change directory to the pattern directory:
    ```
    cd sfn-http-endpoint
    ```
1. From the command line, use AWS SAM to deploy the AWS resources for the pattern as specified in the template.yml file:
    ```
    sam deploy --parameter-overrides OpenWeatherAPIKey=API_KEY
    ```
1. During the prompts:
    * Enter a stack name
    * Enter the desired AWS Region
    * Allow SAM CLI to create IAM roles with the required permissions.

1. Note the outputs from the SAM deployment process. These contain the resource names and/or ARNs which are used for testing.

## How it works
* Start the Step Function with the latitude and longitude of the location you want to get the temperature from in the input payload.
* The step function will call the API using the HTTP Endpoint task and check what type of jacket you will need.
* You will get the execution ARN and the start date.

## Testing

### AWS CLI
Run the following CLI command  
`aws stepfunctions start-execution --state-machine-arn STEP_FUNCTION_ARN --input '{\"latitude\": \"31.859343\", \"longitude\": \"-106.6068812\"}'`

Replace the state-machine-arn value with the one from given in the output of the `sam deploy` command. Default latitude and longitude are provided if you want to test a different location you can replace those values.

### AWS Console
* From the Step Function service select the one that was created by your deployment.
* Click the *Start Execution* button.
* In the prompt enter a JSON object with *latitude* and *longitude* as attributes (example below)  
```json
{
  "latitude": "31.859343",
  "longitude": "-106.6068812"
}
```
* Click the *Start Execution* button on the prompt and see the execution go.


## Cleanup
 
1. Delete the stack
    ```bash
    aws cloudformation delete-stack --stack-name STACK_NAME
    ```
1. Confirm the stack has been deleted
    ```bash
    aws cloudformation list-stacks --query "StackSummaries[?contains(StackName,'STACK_NAME')].StackStatus"
    ```
----
Copyright 2024 Amazon.com, Inc. or its affiliates. All Rights Reserved.

SPDX-License-Identifier: MIT-0