# Amazon API Gateway to Amazon CloudWatch Logs

This pattern creates an Amazon API Gateway REST API that proxies requests directly to Amazon CloudWatch Logs using an AWS service integration. Clients can put log events into, and get log events from, a CloudWatch Logs log stream over HTTPS.

Learn more about this pattern at Serverless Land Patterns: https://serverlessland.com/patterns/apigw-cloudwatch-logs

Important: this application uses various AWS services and there are costs associated with these services after the Free Tier usage - please see the [AWS Pricing page](https://aws.amazon.com/pricing/) for details. You are responsible for any AWS costs incurred. No warranty is implied in this example.

## Requirements

* [Create an AWS account](https://portal.aws.amazon.com/gp/aws/developer/registration/index.html) if you do not already have one and log in. The AWS Identity and Access Management (AWS IAM) user that you use must have sufficient permissions to make necessary AWS service calls and manage AWS resources.
* [AWS CLI](https://docs.aws.amazon.com/cli/latest/userguide/install-cliv2.html) installed and configured
* [Git Installed](https://git-scm.com/book/en/v2/Getting-Started-Installing-Git)
* [curl](https://curl.se/) installed, to call the API in the testing steps
* [AWS Serverless Application Model](https://docs.aws.amazon.com/serverless-application-model/latest/developerguide/serverless-sam-cli-install.html) (AWS SAM) installed

## Deployment Instructions

1. Create a new directory, navigate to that directory in a terminal and clone the GitHub repository:
    ```
    git clone https://github.com/aws-samples/serverless-patterns
    ```
1. Change directory to the pattern directory:
    ```
    cd serverless-patterns/apigw-cloudwatch-logs/sam
    ```
1. From the command line, use AWS SAM to deploy the AWS resources for the pattern as specified in the template.yaml file:
    ```
    sam deploy --guided
    ```
1. During the prompts:
    * Enter a stack name
    * Enter the desired AWS Region
    * Allow SAM CLI to create IAM roles with the required permissions.

    Once you have run `sam deploy --guided` mode once and saved arguments to a configuration file (samconfig.toml), you can use `sam deploy` in future to use these defaults.

1. Note the outputs from the SAM deployment process. These contain the API endpoints and the log group and stream names used for testing.

## Architecture

```
Client
  |  HTTPS (POST /putLog, POST /getLog)
  v
Amazon API Gateway REST API (AWS service integration + mapping templates)
  |  assumes
  v
IAM role (logs:PutLogEvents, logs:GetLogEvents on one log stream)
  |
  v
Amazon CloudWatch Logs
  - PutLogEvents
  - GetLogEvents
```

## How it works

This pattern deploys an API Gateway REST API that talks directly to the Amazon CloudWatch Logs API.

* A CloudWatch Logs log group named after the stack (`<stack name>-logs`) and a log stream (`log-stream-1`) are created.
* An IAM role is created that API Gateway assumes. It allows `logs:GetLogEvents` and `logs:PutLogEvents` on the created log stream above, and includes `apigateway.amazonaws.com` in its trust relationship.
* `POST /putLog` uses an `AWS` service integration to call the CloudWatch Logs `PutLogEvents` action. It sets the `X-Amz-Target: Logs_20140328.PutLogEvents` and `Content-Type: application/x-amz-json-1.1` headers and uses a mapping template to build the request from the client body. The template builds the JSON with `$input.json`, which encodes each value as valid JSON.
* `POST /getLog` uses an `AWS` service integration to call the CloudWatch Logs `GetLogEvents` action, setting `X-Amz-Target: Logs_20140328.GetLogEvents`.

This sample API has no authorization, so anyone who has the URL can write to and read the log stream. Use it only for testing and delete the stack when you finish. Before you use this pattern for anything else, add an authorizer such as AWS IAM authorization, an Amazon Cognito user pool or a Lambda authorizer.

## Testing

Replace `STACK_NAME` in the commands below with the stack name you chose during `sam deploy --guided` (for example, `apigw-cloudwatch-logs`).

After deployment, capture the endpoint URLs from the stack outputs:

```bash
PUT_LOG_URL=$(aws cloudformation describe-stacks --stack-name STACK_NAME \
  --query "Stacks[0].Outputs[?OutputKey=='PutLogUrl'].OutputValue" --output text)
GET_LOG_URL=$(aws cloudformation describe-stacks --stack-name STACK_NAME \
  --query "Stacks[0].Outputs[?OutputKey=='GetLogUrl'].OutputValue" --output text)
```

1. Put a log event. For testing, the `ts` value uses `$(date +%s000)` to generate the current time in UNIX epoch milliseconds:

    ```bash
    curl -X POST "$PUT_LOG_URL" \
      -H 'content-type: application/json' \
      -d '{
        "ts": '$(date +%s000)',
        "message": "Example Event 1"
      }'
    ```

    Expected output: HTTP 200 with a JSON response body like this one. The response must not contain `rejectedLogEventsInfo`. If it does, the timestamp was rejected (see the note on timestamps below).

    ```json
    {"nextSequenceToken":"49671362743309268969545043233477408264136326463823471824"}
    ```

2. Put a second log event:

    ```bash
    curl -X POST "$PUT_LOG_URL" \
      -H 'content-type: application/json' \
      -d '{
        "ts": '$(date +%s000)',
        "message": "Example Event 2"
      }'
    ```

    Expected output: HTTP 200 with a JSON response body in the same format as the previous step:

    ```json
    {"nextSequenceToken":"49673454859525455767868366410015381822815935189916753074"}
    ```

3. Get the log events back from the stream:

    ```bash
    curl -X POST "$GET_LOG_URL" \
      -H 'content-type: application/json' \
      -d '{}'
    ```

    New events can take a few seconds to become readable. If `events` is empty, wait a few seconds and run the command again.

    Expected output: HTTP 200 with a JSON body that contains the events you put, along with `nextBackwardToken` and `nextForwardToken`:

    ```json
    {
      "events": [
        {
          "eventId": "40026256600529950992839528837354237837843593648939567825",
          "ingestionTime": 1795112433518,
          "message": "Example Event 1",
          "timestamp": 1795112433000
        },
        {
          "eventId": "40026256600529950992839528837323739125584810966536395771",
          "ingestionTime": 1795112433871,
          "message": "Example Event 2",
          "timestamp": 1795112433000
        }
      ],
      "nextBackwardToken": "b/40026256600529950992839528837354237837843593648939567825/s",
      "nextForwardToken": "f/40026256600529950992839528837323739125584810966536395771/s"
    }
    ```

4. Verify in the console. Navigate to CloudWatch Logs in the AWS Console and confirm that the log group from the `LogGroupName` output, the `log-stream-1` log stream and the log events exist.

The timestamp (`ts`) must be in UNIX epoch time with milliseconds. CloudWatch Logs rejects events whose timestamp is more than 14 days in the past or more than 2 hours in the future. Rejected events are reported in a `rejectedLogEventsInfo` field (for example `tooOldLogEventEndIndex`) instead of being stored. See [InputLogEvent](https://docs.aws.amazon.com/AmazonCloudWatchLogs/latest/APIReference/API_InputLogEvent.html) and [PutLogEvents](https://docs.aws.amazon.com/AmazonCloudWatchLogs/latest/APIReference/API_PutLogEvents.html) for more detail.

## Cleanup

Replace `STACK_NAME` in the commands below with the stack name you chose during `sam deploy --guided` (for example, `apigw-cloudwatch-logs`).

1. Delete the stack
    ```bash
    sam delete --stack-name STACK_NAME
    ```
1. Confirm the stack has been deleted
    ```bash
    aws cloudformation list-stacks --query "StackSummaries[?contains(StackName,'STACK_NAME')].StackStatus"
    ```
----
Copyright 2026 Amazon.com, Inc. or its affiliates. All Rights Reserved.

SPDX-License-Identifier: MIT-0
