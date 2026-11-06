# Amazon EventBridge custom event bus cross-account sharing with AWS RAM

This pattern shows how to run one Amazon EventBridge custom event bus in an owner account and share it with other accounts in your AWS Organizations organization using AWS Resource Access Manager (AWS RAM). A consumer account creates its own subscriber on the shared bus and delivers matching events to an AWS Lambda function, with an Amazon SQS dead-letter queue for failed deliveries.

Deploy the single template once per account: `Role=Owner` creates the bus and the RAM share; `Role=Consumer` creates the Lambda target, the dead-letter queue, the delivery role, and the subscriber.

Learn more about this pattern at Serverless Land Patterns: https://serverlessland.com/patterns/eventbridge-custom-bus-cross-account

Important: this application uses various AWS services and there are costs associated with these services after the Free Tier usage - please see the [AWS Pricing page](https://aws.amazon.com/pricing/) for details. You are responsible for any AWS costs incurred. No warranty is implied in this example.

## Requirements

* [Create an AWS account](https://portal.aws.amazon.com/gp/aws/developer/registration/index.html) if you do not already have one and log in. This pattern uses **two accounts** in the same AWS Organizations organization: one that owns the bus and one that consumes from it. The IAM identity you deploy with in each account must have sufficient permissions to make the necessary AWS service calls and manage AWS resources.
* [AWS CLI](https://docs.aws.amazon.com/cli/latest/userguide/install-cliv2.html) (latest) installed and configured, with a named profile for each account.
* [Git Installed](https://git-scm.com/book/en/v2/Getting-Started-Installing-Git)
* [AWS Serverless Application Model](https://docs.aws.amazon.com/serverless-application-model/latest/developerguide/serverless-sam-cli-install.html) (AWS SAM) installed
* [Sharing with AWS Organizations enabled in AWS RAM](https://docs.aws.amazon.com/ram/latest/userguide/getting-started-sharing.html#getting-started-sharing-orgs), enabled once from the organization's management account.

## Deployment Instructions

These examples deploy to the us-west-2 Region. Change the value of `--region` in the commands below to your preferred Region, and use the same Region for both deploys. The custom event bus and its subscribers must be co-located.


1. Create a new directory, navigate to that directory in a terminal and clone the GitHub repository:
    ```
    git clone https://github.com/aws-samples/serverless-patterns
    ```
1. Change directory to the pattern directory:
    ```
    cd serverless-patterns/eventbridge-custom-bus-cross-account/python/sam
    ```
1. Deploy the **owner** side using the owner account's credentials. Note the `BusArn` output.
    ```
    sam deploy --stack-name xacct-bus-owner --profile <owner-profile> --region us-west-2 \
    --resolve-s3 --no-confirm-changeset \
    --parameter-overrides Role=Owner EventBusName=cross-account-orders SharePrincipal=<CONSUMER_ACCOUNT_ID>
    ```
1. Deploy the **consumer** side using the consumer account's credentials, passing the `BusArn` from the previous step. Allows SAM to create IAM roles.
    ```
    sam deploy --stack-name xacct-bus-consumer --profile <consumer-profile> --region us-west-2 \
    --capabilities CAPABILITY_IAM \
    --parameter-overrides Role=Consumer SharedBusArn=<BUS_ARN_FROM_OWNER_OUTPUT>
    ```
1. Note the outputs from each deployment. They contain the bus ARN, the consumer Lambda function name, and the subscriber ARN used for testing.

## How it works

The owner account creates an EventBridge custom event bus (`AWS::EventsV2::EventBus`) with a retention period, and shares it with the account or an OU through an AWS RAM resource share (`AWS::RAM::ResourceShare`) that grants the `AWSRAMEventBridgeEventBusV2SubscribeOnly` managed permission.

The consumer account creates a subscriber (`AWS::EventsV2::Subscriber`) on the shared bus. The subscriber delivers events to an AWS Lambda function using an IAM delivery role that EventBridge assumes (`lambda:InvokeFunction` on the function). Events that fail delivery after the retry policy is exhausted are written to an Amazon SQS dead-letter queue, the same delivery role grants `sqs:SendMessage` on that queue. Each consumer account owns and manages its own subscribers; the bus owner configures no routing on their behalf.

A producer with publish access (the owner account, or an account granted the PublishOnly permission) publishes events to the bus with `PutEvents` or `PutRawEvents`. EventBridge routes each event to every matching subscriber and retains a copy for the configured retention period.

## Testing

1. Publish a test event from the owner account to the bus:
    ```bash
    BUS_ARN=<BUS_ARN_FROM_OWNER_OUTPUT>
    DATA_B64=$(printf '{"detail":{"orderId":"A-1001","status":"PLACED","total":42}}' | base64)
    aws eventsv2 put-raw-events --event-bus-arn "$BUS_ARN" \
      --entries '[{"Data":"'"$DATA_B64"'","SystemMetadata":{"ContentType":"application/json"}}]' \
      --profile <owner-profile> --region us-west-2
    ```
2. In the consumer account, open the consumer Lambda function's Amazon CloudWatch log group and confirm a log line containing the published event (`Received event: ...`). A successful publish only means the bus stored the event, so always confirm at the target.

## Cleanup

1. Delete the consumer stack first (so the subscriber is removed before the bus), then the owner stack:
    ```bash
    sam delete --stack-name xacct-bus-consumer --profile <consumer-profile> --region us-west-2
    sam delete --stack-name xacct-bus-owner --profile <owner-profile> --region us-west-2
    ```
1. Confirm each stack has been deleted:
    ```bash
    aws cloudformation list-stacks --region us-west-2 --query "StackSummaries[?contains(StackName,'xacct-bus')].StackStatus"
    ```

----
Copyright 2026 Amazon.com, Inc. or its affiliates. All Rights Reserved.

SPDX-License-Identifier: MIT-0