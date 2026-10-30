# AWS IAM Identity Center change ledger with Amazon EventBridge, AWS Lambda and Amazon DynamoDB

This pattern records every user, group and group membership change in AWS IAM Identity Center Identity Store in an Amazon DynamoDB table; changes to the identity store itself are not recorded. The native change events reach the default Amazon EventBridge bus, an AWS Lambda function reads the current user or group attributes with the Identity Store Describe APIs (the events carry IDs only), and a conditional write keeps the ledger correct when an event is delivered twice.

Learn more about this pattern at Serverless Land Patterns: https://serverlessland.com/patterns/identitystore-eventbridge-lambda-typescript-cdk

Important: this application uses various AWS services and there are costs associated with these services after the Free Tier usage - please see the [AWS Pricing page](https://aws.amazon.com/pricing/) for details. You are responsible for any AWS costs incurred. No warranty is implied in this example. Nothing in this stack bills by the hour: the table is on-demand and the rest is charged per request.

## Requirements

* [Create an AWS account](https://portal.aws.amazon.com/gp/aws/developer/registration/index.html) if you do not already have one and log in. The IAM user that you use must have sufficient permissions to make necessary AWS service calls and manage AWS resources.
* [AWS CLI](https://docs.aws.amazon.com/cli/latest/userguide/install-cliv2.html) version 2 installed and configured
* [Node.js 22 or later](https://nodejs.org/en/download/) and [Git](https://git-scm.com/book/en/v2/Getting-Started-Installing-Git) installed
* [AWS CDK v2](https://docs.aws.amazon.com/cdk/v2/guide/getting_started.html) prerequisites met; the commands below use `npx cdk`
* AWS IAM Identity Center must already be enabled. The stack cannot enable it, and you need your identity store ID (`d-` followed by 10 characters, or a UUID).

## Supported Regions

Deploy in the account and Region where Identity Center is enabled: the events arrive on the default event bus there, and according to the Identity Center documentation a rule in another Region does not receive them. For an organization instance that account is the management account, where production workloads do not belong. Use an account instance in a sandbox or follow [Receive events in other accounts and Regions](https://docs.aws.amazon.com/singlesignon/latest/userguide/receive-events-other-accounts-regions.html). Only an organization instance in a sandbox management account in us-east-1 was tested; an account instance in a member account was not. The sample events in `events/` are modelled on events captured there, with placeholder IDs.

## Architecture

```
Identity Store change --> Amazon EventBridge (default bus) --> AWS Lambda --> Amazon DynamoDB
(user, group, membership)  rule: 8 detail-types, one store     |   |          ledger, key = event id
                                                               |   +--> Identity Store DescribeUser / DescribeGroup
                                      Amazon SQS dead-letter queue <--+  (failed deliveries and failed invocations)
```

## How it works

1. Identity Center sends `User` and `Group` `Created`, `Updated` and `Deleted` events, and `GroupMembership` `Created` and `Deleted` events, to the default event bus. The rule lists the eight detail-types and the identity store ID you pass in. AWS CloudTrail also sends Identity Store API calls to EventBridge with the same source (`aws.identitystore`) and detail-type `AWS API Call via CloudTrail`; a rule on the source alone would deliver those too.
2. The function reads the `detail` of the event. For `Created` and `Updated` events it calls `DescribeUser` and `DescribeGroup`. A membership event describes both the member and the group. `Deleted` events skip the calls because the resource is gone. A `ResourceNotFoundException` (deleted after the event was sent) is stored as `attributes: null`.
3. The function writes one row with `PutItem` and `attribute_not_exists(eventId)`. The EventBridge event ID is the key, so a duplicate delivery fails the condition, is logged and counts as success. Query by user, group or membership ID through the `resource-index` secondary index, sorted by event time.
4. Events that the function cannot process (the retries ran out, or its concurrency is stopped) go to the Amazon SQS dead-letter queue as Lambda failure records with the original event in `requestPayload`. The rule uses the same queue for events that EventBridge cannot deliver; that path was not exercised. The queue is plumbing, so the pattern is four services (Identity Center, EventBridge, Lambda and DynamoDB) plus the queue.

## Important Notes

* Events are delivered at least once and may arrive out of order. `Updated` events do not say what changed, so a row shows the attributes at processing time, not at change time.
* Only user name, display name and group display name are stored. E-mail addresses and other personal data stay in Identity Center.
* Delivery is forward-looking: changes made before the rule exists are not replayed. A new rule can take about a minute to match (the documentation advises waiting that long).
* The Lambda role may call `DescribeUser` and `DescribeGroup` on this identity store only; user and group ARNs contain no store ID, so those two resources use a wildcard.

## Deployment Instructions

1. Clone the repository:
    ```bash
    git clone https://github.com/aws-samples/serverless-patterns
    cd serverless-patterns/identitystore-eventbridge-lambda/typescript/cdk
    ```
2. Install dependencies and build:
    ```bash
    npm install
    npm run build
    ```
3. Look up your identity store ID. If this account and Region have never been used with CDK, bootstrap them once (the stack needs the ID even for this command):
    ```bash
    IDENTITY_STORE_ID=$(aws sso-admin list-instances --no-paginate --query 'Instances[0].IdentityStoreId' --output text)
    npx cdk bootstrap -c identityStoreId=$IDENTITY_STORE_ID
    ```
4. Deploy the stack:
    ```bash
    npx cdk deploy -c identityStoreId=$IDENTITY_STORE_ID
    ```
5. Wait about a minute before the tests so that the new rule is active.

## Testing

Use the same account and Region as the deployment. The CLI examples create and delete a throwaway user and group in your identity store, so use a sandbox. They use AWS CLI v2 (version 2.31.3 was used to capture the sample events); the "Expected" lines are what the test run showed.

1. Read the stack outputs (`FunctionName`, `TableName`, `DeadLetterQueueUrl`, `LogGroupName`) and define a query helper:
    ```bash
    out() { aws cloudformation describe-stacks --stack-name IdentitystoreEventbridgeLambdaStack --query "Stacks[0].Outputs[?OutputKey=='$1'].OutputValue" --output text; }
    TABLE=$(out TableName); FN=$(out FunctionName); DLQ=$(out DeadLetterQueueUrl); LOG_GROUP=$(out LogGroupName)
    IDENTITY_STORE_ID=$(aws sso-admin list-instances --no-paginate --query 'Instances[0].IdentityStoreId' --output text)
    ledger() { aws dynamodb query --table-name $TABLE --index-name resource-index --key-condition-expression 'resourceId = :id' --expression-attribute-values "{\":id\":{\"S\":\"$1\"}}" --query 'Items[].[eventTime.S,detailType.S,attributes.M.userName.S,attributes.M.displayName.S]' --output text; }
    ```
2. Create a user, a group and a membership, then read the user row:
    ```bash
    N=$(date +%s)
    USER_ID=$(aws identitystore create-user --identity-store-id $IDENTITY_STORE_ID --user-name ledger-demo-$N --display-name "Ledger Demo $N" --name "GivenName=Ledger,FamilyName=Demo" --query UserId --output text)
    GROUP_ID=$(aws identitystore create-group --identity-store-id $IDENTITY_STORE_ID --display-name ledger-demo-$N --query GroupId --output text)
    MEMBERSHIP_ID=$(aws identitystore create-group-membership --identity-store-id $IDENTITY_STORE_ID --group-id $GROUP_ID --member-id "UserId=$USER_ID" --query MembershipId --output text)
    sleep 30; ledger $USER_ID; ledger $MEMBERSHIP_ID
    ```
   Expected: one `User Created` row with the user name and display name, and one `GroupMembership Created` row. The helper prints `None` in the two attribute columns of a membership row, because membership rows keep the member and the group under `attributes.user` and `attributes.group` (names), not `userName` and `displayName`; the row itself is the proof. Each change appears once even though CloudTrail reports the same API calls to EventBridge, because the rule matches only the eight detail-types.
3. Update the user, then read the rows again. The `--operations` value must be JSON; the shorthand syntax does not support the document-typed attribute value:
    ```bash
    aws identitystore update-user --identity-store-id $IDENTITY_STORE_ID --user-id $USER_ID --operations '[{"AttributePath":"displayName","AttributeValue":"Ledger Demo Updated"}]'
    sleep 30; ledger $USER_ID
    ```
   Expected: a `User Updated` row after the `User Created` row, with the new display name.
4. Delete the three identities and read the rows:
    ```bash
    aws identitystore delete-group-membership --identity-store-id $IDENTITY_STORE_ID --membership-id $MEMBERSHIP_ID
    aws identitystore delete-group --identity-store-id $IDENTITY_STORE_ID --group-id $GROUP_ID
    aws identitystore delete-user --identity-store-id $IDENTITY_STORE_ID --user-id $USER_ID
    sleep 30; ledger $USER_ID; ledger $MEMBERSHIP_ID
    ```
   Expected: `User Deleted` and `GroupMembership Deleted` rows without attributes (the Describe calls are skipped).
5. Duplicate delivery. Invoke the function twice with the same sample event, after pointing the sample at your identity store:
    ```bash
    sed "s/d-0123456789/$IDENTITY_STORE_ID/g" events/user-created.json > /tmp/user-created.json
    for i in 1 2; do aws lambda invoke --function-name $FN --payload fileb:///tmp/user-created.json /tmp/response.json --query '[StatusCode,FunctionError]' --output text; cat /tmp/response.json; echo; done
    ledger aaaaaaaa-1111-2222-3333-abcdefabcdef
    ```
   Expected: the first call returns `"status":"stored"`, the second `"status":"duplicate"`, and the query shows one row; running the step again returns `"status":"duplicate"` twice, because the table already holds that event ID. The sample user does not exist, so `DescribeUser` returns `ResourceNotFoundException`, which the function stores as `attributes` null. If a call returns a function error instead, check the log group for the error name before assuming the duplicate check is broken. Read the function logs with `aws logs tail $LOG_GROUP --since 10m`.
6. Check that the dead-letter queue is empty, then stop the function from running, change something and read the queue (Lambda sends each event it cannot run to the queue), then restore the function:
    ```bash
    aws sqs get-queue-attributes --queue-url $DLQ --attribute-names ApproximateNumberOfMessages
    aws lambda put-function-concurrency --function-name $FN --reserved-concurrent-executions 0
    sleep 20
    DLQ_USER=$(aws identitystore create-user --identity-store-id $IDENTITY_STORE_ID --user-name dlq-demo-$(date +%s) --display-name "Dlq Demo" --name "GivenName=Dlq,FamilyName=Demo" --query UserId --output text)
    aws identitystore delete-user --identity-store-id $IDENTITY_STORE_ID --user-id $DLQ_USER
    sleep 20
    aws sqs get-queue-attributes --queue-url $DLQ --attribute-names ApproximateNumberOfMessages
    aws sqs receive-message --queue-url $DLQ --max-number-of-messages 10 --wait-time-seconds 10 --query 'Messages[].Body' --output text | grep -o '"condition":"[A-Za-z]*"'
    aws lambda delete-function-concurrency --function-name $FN
    ```
   Expected: a count of 0 first, then a count of 2 (the `User Created` and `User Deleted` events), and `"condition":"ZeroReservedConcurrency"` for each message the receive call returns (one call can return fewer than both).

## Cleanup

1. In a new terminal, look up the identity store ID again:
    ```bash
    IDENTITY_STORE_ID=$(aws sso-admin list-instances --no-paginate --query 'Instances[0].IdentityStoreId' --output text)
    ```
2. If a test stopped before step 4, delete the identities it created with `delete-group-membership`, `delete-group` and `delete-user` as shown above. List them with `aws identitystore list-users --identity-store-id $IDENTITY_STORE_ID`.
3. Delete the stack. This deletes the table with all ledger rows, the dead-letter queue and the log group:
    ```bash
    npx cdk destroy -c identityStoreId=$IDENTITY_STORE_ID
    ```

----
Copyright 2026 Amazon.com, Inc. or its affiliates. All Rights Reserved.

SPDX-License-Identifier: MIT-0
