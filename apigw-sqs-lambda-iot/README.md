# Amazon API Gateway (REST API) to Amazon SQS to AWS Lambda to AWS IOT 

This pattern explains how to deploy a serverless application using SAM. The pattern connects Amazon API Gateway (REST API), Amazon SQS, AWS Lambda, and AWS IOT

This pattern is useful to accept and respond to requests quickly but offloading the processing as asynchronous process. Once the request is placed in SQS, API gateway responds back to the caller immediately without waiting for those messages to be processed.

When an HTTP POST request is made to the Amazon API Gateway endpoint, request payload is sent to Amazon Simple Queue Service. AWS Lambda function consumes event from the Queue and post the event/payload as MQTT message to AWS IoT Topic. 

Key Benefits:

Operations: AWS services used in this pattern can scale easily and quickly based on incoming traffic.
Security: The APIs created with Amazon API Gateway expose HTTPS endpoints only.
Cost: Pay only for what you use. No minimum fee.
Important: this application uses various AWS services and there are costs associated with these services after the Free Tier usage - please see the AWS Pricing page for details. You are responsible for any AWS costs incurred. No warranty is implied in this example.

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
1. Change directory to the pattern directory:
    ```
    cd apigw-sqs-lambda-iot
    ```
1. From the command line, use AWS SAM to deploy the AWS resources for the pattern as specified in the template.yml file:
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
The API Gateway handles the incoming API requests and send the $request.body.MessageBody as a message to SQS queue. The Lambda fucntion consumes the message from the SQS queue and extracts the topic from the request. Post the message in request body to the IOT topic on the topic name in request.
 

## Testing

1. Go to AWS IOT Core Console -> Create MQTT Test Client -> Subscribe to a topic "MyTopic"

2. Copy the API gateway endpoint to send request from deploy output
    ex: https://********..amazonaws.com/Prod

5. Create a JSON Request 
    ex: {
            "topic": "devicenewitem",
            "message": "sample message from input"
        }

6. Make a HTTP post request to the endpoint captured using a REST client like postman

7. You should get a 200 Success SendMessageResponse. You can check the MQTT Test client showing the request you passed to a dynamic client

## Cleanup
 
1. Delete the stack
    ```bash
    sam delete
    ```

----
Copyright 2023 Amazon.com, Inc. or its affiliates. All Rights Reserved.

SPDX-License-Identifier: MIT-0