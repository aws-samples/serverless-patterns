# Amazon API Gateway HTTP APIs to AWS Step Functions Express Workflow, with Amazon Cloudwatch Logs enabled 

The HTTP's API endpoint can be called from an application (e.g. a web front end) to run an express workflow and return the result.

The SAM template deploys a HTTP APIs endpoint with an integration that syncronsouly invokes a Step Functions Express workflow and returns the response. The SAM template contains the minimum IAM resources required to run the application with logging enabled. 

Important: this application uses various AWS services and there are costs associated with these services after the Free Tier usage - please see the [AWS Pricing page](https://aws.amazon.com/pricing/) for details. You are responsible for any AWS costs incurred. No warranty is implied in this example.

## Requirements

* AWS CLI already configured with Administrator permission
* [NodeJS 12.x installed](https://nodejs.org/en/download/)

## Installation Instructions

1. [Create an AWS account](https://portal.aws.amazon.com/gp/aws/developer/registration/index.html) if you do not already have one and login.

1. [Install Git](https://git-scm.com/book/en/v2/Getting-Started-Installing-Git) and [install the AWS Serverless Application Model CLI](https://docs.aws.amazon.com/serverless-application-model/latest/developerguide/serverless-sam-cli-install.html) on your local machine.

1. Create a new directory, navigate to that directory in a terminal and enter ```git clone this-repo-name```.

1. From the command line, run:
```
sam deploy --guided
```
Choose a stack name, select the desired AWS Region, and allow SAM to create roles with the required permissions. Once you have run guided mode once, you can use `sam deploy` in future to use these defaults.

## How it works

* Send a `POST` request to the HTTP APIs endpoint.
* The HTTP APIs integration will start a synchronous execution of the Step Functions Express workflow.
* The Results of the Express workflow is returned via the HTTP API's request.
==============================================

## Testing

Run the following command to send an HTTP `POST` request to the HTTP APIs endpoint. Note, you must edit the {HelloWorldApi} placeholder with the URL of the deployed HTTP APIs endpoint. This is provided in the stack outputs.

```bash
curl --location --request POST '{HelloWorldApi} \
> --header 'Content-Type: application/json' \
> --data-raw '{ "IsHelloWorldExample": "Yes" }'
```

Copyright 2021 Amazon.com, Inc. or its affiliates. All Rights Reserved.

SPDX-License-Identifier: MIT-0
