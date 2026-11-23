# Amazon EventBridge Webhook Events to AWS Step Functions and Amazon DynamoDB

This pattern receives HMAC-signed webhooks from a third-party provider on an HTTPS URL that Amazon EventBridge hosts, with no Amazon API Gateway, function URL or verifier function. EventBridge checks the signature and timestamp of each request, drops repeats of the same content, and puts the request body on an EventBridge Custom Event Bus (not a Custom Event Bus - Classic). A subscriber starts an AWS Step Functions workflow that stores each known event type once in Amazon DynamoDB and skips the rest. The synthesized template contains no AWS Lambda function.

Learn more about this pattern at Serverless Land Patterns: https://serverlessland.com/patterns/eventbridge-webhook-sfn-typescript-cdk

Important: this application uses various AWS services and there are costs associated with these services after the Free Tier usage - please see the [AWS Pricing page](https://aws.amazon.com/pricing/) for details. You are responsible for any AWS costs incurred. No warranty is implied in this example.

## Requirements

* [Create an AWS account](https://portal.aws.amazon.com/gp/aws/developer/registration/index.html) if you do not already have one and log in. The IAM user that you use must have sufficient permissions to make necessary AWS service calls and manage AWS resources.
* [AWS CLI](https://docs.aws.amazon.com/cli/latest/userguide/install-cliv2.html) installed and configured
* [Git](https://git-scm.com/book/en/v2/Getting-Started-Installing-Git) installed
* [Node.js](https://nodejs.org/en/download/) and npm installed. `npm install` installs the AWS CDK CLI that the `npx cdk` commands use
* The target account and Region [bootstrapped](https://docs.aws.amazon.com/cdk/v2/guide/bootstrapping.html) for the AWS CDK (`npx cdk bootstrap` once per account and Region)
* `curl` and `openssl` for the tests

## Supported Regions

The [launch announcement](https://aws.amazon.com/about-aws/whats-new/2026/11/amazon-eventbridge-webhook-events/) says Webhook Events are available in every Region that has the Custom Event Bus; see the Custom Event Bus column of [EventBridge feature availability](https://docs.aws.amazon.com/eventbridge/latest/userguide/feature-availability.html). The stack has no Region-specific values and takes the Region from your AWS CLI configuration. It was tested in us-west-2 and us-east-1.

## How it works

1. The stack creates an `AWS::EventsV2::EventSource` with a webhook configuration. EventBridge generates the URL and an HMAC secret, stores the secret in Secrets Manager in your account and returns only its ARN. A provider signs `<X-Timestamp>.<raw body>` with HMAC-SHA256 (hex) and sends the result in `X-Signature`. Unsigned or wrongly signed requests, and requests whose timestamp is more than 300 seconds off, get `403 Forbidden`.
2. EventBridge assumes the webhook role to read the secret and to put accepted bodies on the bus. With `CONTENT_BASED` deduplication a second request with the same content within 5 minutes still gets `200 OK`, but no second event reaches the bus.
3. The subscriber delivers events whose body has an `id` and a `type` field, in batches of up to 10, and starts one Standard workflow per batch. The execution input is a JSON array of the raw request bodies.
4. For each body, `order.created` and `order.shipped` are written to the table with the event `id` as the key (a number is stored as its string form) and the condition `attribute_not_exists(pk)`. A later copy of the same event, for example a provider retry after the 5 minute window, fails the condition and is reported as `duplicate`; the stored item is not overwritten. Other types, and bodies whose `id` is not a string or a number, are reported as `ignored`. Transient DynamoDB errors are retried; any other write error ends the execution in the `EventNotStored` Fail state. The subscriber starts executions asynchronously (`InvocationType` `EVENT`), so a failed execution is not redelivered: the event stays in that execution's history.

The nearest patterns are `eventbridge-webhooks/2-github`, which runs a Lambda function URL and a function that checks the HMAC before it calls `PutEvents`, and `eventbridge-custom-bus-dynamodb`, where each subscriber calls DynamoDB from a universal target, so a write that fails a condition would count as a failed delivery. Here Step Functions records a later copy as `duplicate`, continues with the rest of the batch and reports the result of each event.

## Important Notes

* The webhook URL is a public HTTPS endpoint by design. The URL together with the secret is the credential: keep both out of logs and tickets. The `WebhookUrl` stack output is visible to anyone who may call `cloudformation:DescribeStacks` in the account. Rotate the secret with `RotateWebhookCredentials`; the URL does not change.
* The aws-cdk-lib version this project uses (2.278.0) types only the AWS service and partner variants of the event source, so the stack sets the webhook configuration with `addPropertyOverride` and reads the URL and secret ARN with `getAtt`.
* The subscriber uses the default retry policy (5 attempts within 300 seconds) and has no dead-letter queue, so an event that cannot start a workflow is dropped after the retries, although the provider got `200`. Add an Amazon SQS queue as `OnFailureConfiguration` for production.
* A Step Functions execution input is limited to 256 KiB and holds up to 10 bodies. EventBridge closes a batch early when it reaches the target's payload limit, so large bodies arrive in smaller batches. EventBridge accepts requests of up to 1 MB, but a body over 256 KiB cannot start an execution at any batch size; if your provider can send one, add the `OnFailureConfiguration` queue or store large bodies elsewhere.
* Per the [launch announcement](https://aws.amazon.com/about-aws/whats-new/2026/11/amazon-eventbridge-webhook-events/), webhook events are billed as standard Custom Event Bus ingress with no additional charge for the webhook, and Step Functions and DynamoDB bill per use. The secret that EventBridge creates in AWS Secrets Manager may bill per secret-month; see [AWS Secrets Manager pricing](https://aws.amazon.com/secrets-manager/pricing/).

## Deployment Instructions

1. Clone the repository:
    ```bash
    git clone https://github.com/aws-samples/serverless-patterns
    cd serverless-patterns/eventbridge-webhook-sfn/typescript/cdk
    ```
2. Install the dependencies and build:
    ```bash
    npm install
    npm run build
    ```
3. Bootstrap the account and Region once, then deploy:
    ```bash
    npx cdk bootstrap
    npx cdk deploy
    ```

## Testing

Run these commands in bash or zsh on a single-user machine or in AWS CloudShell. The first block reads the stack outputs and the secret into a variable without printing it, but `openssl` takes the key as a command-line argument, so other local users can see it in `ps` while `send` runs. The block defines helpers: `send` signs and posts a body, `done_runs` waits up to 2 minutes until the given number of executions have finished, and `latest` prints the status and output of the newest execution. In a new terminal, run it again.

```bash
out() { aws cloudformation describe-stacks --stack-name EventbridgeWebhookSfnStack --query "Stacks[0].Outputs[?OutputKey=='$1'].OutputValue" --output text; }
URL=$(out WebhookUrl); SM=$(out StateMachineArn); TABLE=$(out TableName); SECRET_ARN=$(out SecretArn)
SECRET=$(aws secretsmanager get-secret-value --secret-id "$SECRET_ARN" --query SecretString --output text)
send() { TS=${2:-$(date +%s)}; SIG=$(printf '%s' "$TS.$1" | openssl dgst -sha256 -hmac "$SECRET" | awk '{print $NF}')
  curl -s -o /dev/null -w '%{http_code}\n' -X POST "$URL" -H 'Content-Type: application/json' -H "X-Timestamp: $TS" -H "X-Signature: $SIG" --data-raw "$1"; }
runs() { aws stepfunctions list-executions --state-machine-arn "$SM" --query "length(executions[?status!='RUNNING'])" --output text; }
done_runs() { i=0; while [ "$(runs)" -lt "$1" ] && [ $i -lt 24 ]; do sleep 5; i=$((i+1)); done; runs; }
latest() { aws stepfunctions describe-execution --query '[status,output]' --output text --execution-arn "$(aws stepfunctions list-executions --state-machine-arn "$SM" --max-results 1 --query 'executions[0].executionArn' --output text)"; }
```

1. Requests without a valid signature are rejected. Expected: `403` twice.
    ```bash
    curl -s -o /dev/null -w '%{http_code}\n' -X POST "$URL" -H 'Content-Type: application/json' --data-raw '{"id":"evt-1001","type":"order.created"}'
    curl -s -o /dev/null -w '%{http_code}\n' -X POST "$URL" -H 'Content-Type: application/json' -H "X-Timestamp: $(date +%s)" -H 'X-Signature: 00' --data-raw '{"id":"evt-1001","type":"order.created"}'
    ```
2. Send a signed `order.created` event and read the item from DynamoDB. Expected: `200`, then `1`, then `SUCCEEDED [{"id":"evt-1001","type":"order.created","result":"stored"}]`, then `order.created` and the ARN of that execution.
    ```bash
    BODY='{"id":"evt-1001","type":"order.created","orderId":"o-1"}'; TS1=$(date +%s)
    send "$BODY" "$TS1"; done_runs 1; latest
    aws dynamodb get-item --table-name "$TABLE" --key '{"pk":{"S":"evt-1001"}}' --query 'Item.[eventType.S,executionId.S]' --output text
    ```
3. Send exactly the same signed request again, within 5 minutes of step 2; later, the timestamp is outside the 300 second tolerance and the request gets `403`. Expected: `200`, and after 30 seconds still `1` execution.
    ```bash
    send "$BODY" "$TS1"; sleep 30; runs
    ```
4. Send the same event id with a different body, as a provider does that adds a delivery attempt field. Expected: `200`, `2`, `SUCCEEDED [{"id":"evt-1001","type":"order.created","result":"duplicate"}]`, and the same execution ARN on the item as in step 2.
    ```bash
    send '{"id":"evt-1001","type":"order.created","orderId":"o-1","attempt":2}'; done_runs 2; latest
    aws dynamodb get-item --table-name "$TABLE" --key '{"pk":{"S":"evt-1001"}}' --query 'Item.executionId.S' --output text
    ```
5. Send an unknown type, then a body without an `id`. Expected: `200`, `3`, `SUCCEEDED [{"id":"evt-1002","type":"customer.updated","result":"ignored"}]`, then `200` and, after 30 seconds, still `3`, because the subscriber filter does not deliver the second body.
    ```bash
    send '{"id":"evt-1002","type":"customer.updated"}'; done_runs 3; latest
    send '{"type":"order.created"}'; sleep 30; runs
    ```
6. A correctly signed request with a timestamp 15 minutes old is rejected. Expected: `403`.
    ```bash
    send "$BODY" $(( $(date +%s) - 900 ))
    ```

## Cleanup

1. Delete the stack. This deletes the table with its items, the bus, the subscriber and the event source; EventBridge deletes the secret with the event source. Answer `y` at the prompt.
    ```bash
    npx cdk destroy
    ```
2. Clear the secret from your shell and confirm that the stack and the secret are gone. Expected: the first command reports that the stack does not exist, and the second either reports that the secret does not exist or shows a `DeletedDate` (`SECRET_ARN` is set by the first Testing block).
    ```bash
    unset SECRET
    aws cloudformation describe-stacks --stack-name EventbridgeWebhookSfnStack
    aws secretsmanager describe-secret --secret-id "$SECRET_ARN"
    ```

----
Copyright 2026 Amazon.com, Inc. or its affiliates. All Rights Reserved.

SPDX-License-Identifier: MIT-0
