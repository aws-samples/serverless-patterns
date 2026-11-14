# Amazon API Gateway REST API to AWS Lambda and Amazon SES

This pattern deploys an Amazon API Gateway REST API with a GET method, defined in an OpenAPI file (`src/api.yml`). The method invokes an AWS Lambda function, which sends an email with a text and an HTML body through Amazon SES in the function's own Region.

You set the sender and recipient addresses as stack parameters. The function's IAM policy allows `ses:SendEmail` only for those two SES identities.

Learn more about this pattern at Serverless Land Patterns: https://serverlessland.com/patterns/api-lambda-ses-sam-python

Important: this application uses various AWS services and there are costs associated with these services after the Free Tier usage - please see the [AWS Pricing page](https://aws.amazon.com/pricing/) for details. You are responsible for any AWS costs incurred. No warranty is implied in this example.

## Requirements

* [Create an AWS account](https://portal.aws.amazon.com/gp/aws/developer/registration/index.html) if you do not already have one and log in. The IAM user that you use must have sufficient permissions to make necessary AWS service calls and manage AWS resources.
* [AWS CLI](https://docs.aws.amazon.com/cli/latest/userguide/install-cliv2.html) installed and configured
* [Git Installed](https://git-scm.com/book/en/v2/Getting-Started-Installing-Git)
* [AWS Serverless Application Model](https://docs.aws.amazon.com/serverless-application-model/latest/developerguide/serverless-sam-cli-install.html) (AWS SAM) installed
* A [verified email address in Amazon SES](https://docs.aws.amazon.com/ses/latest/dg/creating-identities.html#verify-email-addresses-procedure) for the sender, in the Region you deploy to. While your account is in the [SES sandbox](https://docs.aws.amazon.com/ses/latest/dg/request-production-access.html), verify the recipient address too.

## Deployment Instructions

1. Create a new directory, navigate to that directory in a terminal and clone the GitHub repository:
    ```
    git clone https://github.com/aws-samples/serverless-patterns
    ```
1. Change directory to the pattern directory:
    ```
    cd serverless-patterns/api-lambda-ses
    ```
1. Build the function:
    ```
    sam build
    ```
1. Deploy the stack, with your verified sender and recipient addresses:
    ```
    sam deploy --guided --parameter-overrides SENDER=sender@example.com RECIPIENT=recipient@example.com
    ```
1. During the prompts:
    * Enter a stack name
    * Enter the AWS Region where you verified the email addresses
    * Allow SAM CLI to create IAM roles with the required permissions.

    Once you have run `sam deploy --guided` mode once and saved arguments to a configuration file (samconfig.toml), you can use `sam deploy` in future to use these defaults.

1. Note the outputs from the SAM deployment process. These contain the resource names and/or ARNs which are used for testing.

## How it works

API Gateway receives a GET request on `/` and invokes the Lambda function with a proxy integration. The function calls the SES `SendEmail` API with the sender and recipient from its environment variables, and returns the SES message ID. If SES rejects the request, for example because an address isn't verified, the function returns status 500 with the SES error code and logs the error message.

## Testing

Send a GET request to the `apiGatewayInvokeURL` stack output:

```
curl https://<api_id>.execute-api.<region>.amazonaws.com/s1/
```

The response is `Email sent! Message ID: <id>`, and the email arrives in the recipient's inbox.

## Cleanup

1. Delete the stack:
    ```
    sam delete
    ```

----
Copyright 2023 Amazon.com, Inc. or its affiliates. All Rights Reserved.

SPDX-License-Identifier: MIT-0
