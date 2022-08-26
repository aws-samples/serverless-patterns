# Amazon API Gateway HTTP API to Amazon EventBridge

This pattern creates an HTTP API endpoint that directly integrates with Amazon EventBridge

Learn more about this pattern at Serverless Land Patterns: https://serverlessland.com/patterns/apigw-http-api-eventbridge-python

Important: this application uses various AWS services and there are costs associated with these services after the Free Tier usage - please see the [AWS Pricing page](https://aws.amazon.com/pricing/) for details. You are responsible for any AWS costs incurred. No warranty is implied in this example.

## Requirements

- [Create an AWS account](https://portal.aws.amazon.com/gp/aws/developer/registration/index.html) if you do not already have one and log in. The IAM user that you use must have sufficient permissions to make necessary AWS service calls and manage AWS resources.
- [AWS CLI](https://docs.aws.amazon.com/cli/latest/userguide/install-cliv2.html) installed and configured
- [Git Installed](https://git-scm.com/book/en/v2/Getting-Started-Installing-Git)
- [AWS Serverless Application Model](https://docs.aws.amazon.com/serverless-application-model/latest/developerguide/serverless-sam-cli-install.html) (AWS SAM) installed

## Deployment Instructions

1. Create a new directory, navigate to that directory in a terminal and clone the GitHub repository:
   ```
   git clone https://github.com/aws-samples/serverless-patterns
   ```
2. Change directory to the pattern directory:
   ```
   cd serverless-patterns/apigw-http-api-eventbridge-python
   ```
3. Create a virtual environment for Python:
   ```
   python3 -m venv .venv
   ```
4. Activate the virtual environment
   ```
   source .venv/bin/activate
   ```
   For a Windows platform, activate the virtualenv like this:
   ```
   .venv\Scripts\activate.bat
   ```
5. Install the Python required dependencies:
   ```
   pip install -r requirements.txt
   ```
6. Review the CloudFormation template the cdk generates for you stack using the following AWS CDK CLI command:
   ```
   cdk synth
   ```
7. From the command line, use AWS CDK to deploy the AWS resources for the serverless application as specified in the app.py file:
   ```
   cdk deploy
   ```
8. Note the outputs from the CDK deployment process. These contain the API Gateway ID which is used for testing.

## How it works

This pattern creates an Amazon API gateway HTTP API endpoint. The endpoint uses service integrations to directly connect to Amazon EventBridge.

## Testing

To test the endpoint first send data using the following command. Be sure to update the endpoint with endpoint of your stack.

```
   curl --location --request POST '<your api endpoint>' --header 'Content-Type: application/json' \
--data-raw '{
    "Detail":{
        "message": "This is my test"
    }
}'
```

If everything works as expected EventBridge will return the result of sending the message operation and APIGateway will proxy the payload to the client application. The payload should looks like something like the following payload:

```
{
    "Entries": [
        {
            "EventId": "{UNIQUE_UUID}"
        }
    ],
    "FailedEntryCount": 0 // <- This indicates that the message was successfully sent
}
```

## Cleanup

Run the given command to delete the resources that were created. It might take some time for the CloudFormation stack to get deleted.

```
cdk destroy
```

---

Copyright 2021 Amazon.com, Inc. or its affiliates. All Rights Reserved.

SPDX-License-Identifier: MIT-0
