# Send SMS with AWS End User Messaging using Amazon API Gateway and AWS Lambda

This pattern deploys an Amazon API Gateway REST API and an AWS Lambda function with AWS SAM. The function validates a phone number with the Amazon Pinpoint [phone number validate](https://docs.aws.amazon.com/pinpoint/latest/apireference/phone-number-validate.html) API, then sends an SMS message with the AWS End User Messaging SMS [SendTextMessage](https://docs.aws.amazon.com/pinpoint/latest/apireference_smsvoicev2/API_SendTextMessage.html) API.

Amazon Pinpoint SMS sending through `SendMessages` is only available to existing Pinpoint customers. AWS End User Messaging SMS is the service AWS recommends for sending SMS. See [Amazon Pinpoint end of support](https://docs.aws.amazon.com/pinpoint/latest/userguide/migrate.html).

The API uses IAM authorization, so callers must sign requests with AWS Signature Version 4. This stops anyone on the internet sending SMS messages at your cost.

Learn more about this pattern at Serverless Land Patterns: << Add the live URL here >>

Important: this application uses various AWS services and there are costs associated with these services after the Free Tier usage - please see the [AWS Pricing page](https://aws.amazon.com/pricing/) for details. You are responsible for any AWS costs incurred. No warranty is implied in this example.

## Requirements

* [Create an AWS account](https://portal.aws.amazon.com/gp/aws/developer/registration/index.html) if you do not already have one and log in. The IAM user that you use must have sufficient permissions to make necessary AWS service calls and manage AWS resources.
* [AWS CLI](https://docs.aws.amazon.com/cli/latest/userguide/install-cliv2.html) installed and configured
* [Git Installed](https://git-scm.com/book/en/v2/Getting-Started-Installing-Git)
* [AWS Serverless Application Model](https://docs.aws.amazon.com/serverless-application-model/latest/developerguide/serverless-sam-cli-install.html) (AWS SAM) installed
* An origination identity in AWS End User Messaging SMS: a phone number, a pool or a sender ID, in the Region you deploy to. See [Origination identities](https://docs.aws.amazon.com/sms-voice/latest/userguide/phone-numbers.html). New accounts start in the SMS sandbox, where you can only send to [verified destination numbers](https://docs.aws.amazon.com/sms-voice/latest/userguide/verify-destination-phone-number.html).

## Deployment Instructions

1. Create a new directory, navigate to that directory in a terminal and clone the GitHub repository:
    ```
    git clone https://github.com/aws-samples/serverless-patterns
    ```
1. Change directory to the pattern directory:
    ```
    cd serverless-patterns/apigw-lambda-pinpoint
    ```
1. Find the ARN of your origination identity, for example a phone number:
    ```
    aws pinpoint-sms-voice-v2 describe-phone-numbers --query "PhoneNumbers[].[PhoneNumber,PhoneNumberArn]"
    ```
1. From the command line, use AWS SAM to deploy the AWS resources for the pattern as specified in the template.yaml file:
    ```
    sam deploy --guided
    ```
1. During the prompts:
    * Enter a stack name
    * Enter the desired AWS Region
    * Enter the `OriginationIdentityArn` from the previous step
    * Allow SAM CLI to create IAM roles with the required permissions.

    Once you have run `sam deploy --guided` mode once and saved arguments to a configuration file (samconfig.toml), you can use `sam deploy` in future to use these defaults.

1. Note the `SendMessageUrl` output from the SAM deployment process. You use it for testing.

## How it works

1. A caller sends a signed POST request with a destination phone number to the `/send_message` endpoint.
2. The Lambda function checks the number with the Amazon Pinpoint `PhoneNumberValidate` API, which is still supported for all accounts. It returns a 400 response if the number is invalid.
3. The function sends a sample one-time passcode message with the AWS End User Messaging SMS `SendTextMessage` API, from the origination identity you chose at deploy time, and returns the message ID.

The function role can call `sms-voice:SendTextMessage` only for that origination identity, plus the account's configuration sets and protect configurations, which the API also checks.

## Testing

1. Send a request signed with your AWS credentials. Use a number in E.164 format, which must be verified while your account is in the SMS sandbox:

    ```
    curl -X POST "<SendMessageUrl>" \
      --aws-sigv4 "aws:amz:<region>:execute-api" \
      --user "$AWS_ACCESS_KEY_ID:$AWS_SECRET_ACCESS_KEY" \
      -H "x-amz-security-token: $AWS_SESSION_TOKEN" \
      -H "Content-Type: application/json" \
      -d '{"destination_number": "+14255550100"}'
    ```

2. If the message is sent, you receive this response and the SMS arrives on the phone:

    ```
    Message sent! Message ID: <message id>.
    ```

3. An unsigned request returns `403 Forbidden` with a `Missing Authentication Token` message.

You can change the message text in `src/lambda_function.py`.

## Cleanup
 
1. Delete the stack
    ```bash
    sam delete --stack-name STACK_NAME
    ```
1. Confirm the stack has been deleted
    ```bash
    aws cloudformation list-stacks --query "StackSummaries[?contains(StackName,'STACK_NAME')].StackStatus"
    ```
1. If you requested a phone number only for this pattern, release it in the AWS End User Messaging SMS console, because phone numbers have a monthly fee.

----
Copyright 2023 Amazon.com, Inc. or its affiliates. All Rights Reserved.

SPDX-License-Identifier: MIT-0
