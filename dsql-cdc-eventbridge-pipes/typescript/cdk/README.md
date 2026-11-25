# Amazon Aurora DSQL CDC to Amazon EventBridge with Amazon EventBridge Pipes

This pattern turns the change records of Amazon Aurora DSQL into routed events without a function in the data path. An Amazon EventBridge pipe reads the records from Amazon Kinesis Data Streams, keeps complete records, uses each record's operation code as the event type and reshapes the change into the event detail. Rules on a custom event bus send every change, inserts and deletes to separate Amazon SQS queues, with a dead-letter queue on each hop.

Learn more about this pattern at Serverless Land Patterns: https://serverlessland.com/patterns/dsql-cdc-eventbridge-pipes-typescript-cdk

Important: this application uses various AWS services and there are costs associated with these services after the Free Tier usage - please see the [AWS Pricing page](https://aws.amazon.com/pricing/) for details. Amazon Aurora DSQL and Amazon Kinesis Data Streams bill while they exist, so run the Cleanup section when you are done. You are responsible for any AWS costs incurred. No warranty is implied in this example.

## Requirements

- [Create an AWS account](https://portal.aws.amazon.com/gp/aws/developer/registration/index.html) if you do not already have one and log in.
- [AWS CLI](https://docs.aws.amazon.com/cli/latest/userguide/install-cliv2.html) installed and configured. The tests use `aws dsql get-stream`; if your AWS CLI does not have that command, update it.
- [Git](https://git-scm.com/book/en/v2/Getting-Started-Installing-Git) installed
- [Node.js](https://nodejs.org/) with npm
- [AWS CDK v2](https://docs.aws.amazon.com/cdk/v2/guide/getting_started.html) with your account and Region [bootstrapped](https://docs.aws.amazon.com/cdk/v2/guide/bootstrapping.html) (`npx cdk bootstrap`). The commands use `npx cdk`, so no global install is needed.
- `psql` (a PostgreSQL client) and `jq`

## How it works

1. Amazon Aurora DSQL writes one change record for each committed row change to Amazon Kinesis Data Streams. Delivery is at-least-once and unordered, so consumers deduplicate on `txId` plus `recordId` and order by `commitTimestampNs`.
2. The pipe reads the stream with these settings:

    | Setting | Value | Why |
    |---|---|---|
    | Filter | `{"data":{"type":["full"]}}` | Keeps complete records. Chunked and fragment records (records whose JSON is larger than 9 MiB) and payloads that are not JSON are dropped: no event, no dead-letter message. |
    | Event type | `DetailType: $.data.op` | The record's operation code becomes the event type: `c` (insert), `u` (update) or `d` (delete). A pipe cannot translate the codes. |
    | Batch | 10 records | The most an event bus accepts in one request. Each record becomes one event. |
    | Retries and age | 3 retries, 1 hour | The pipe default is unlimited retries. |
    | Bisect | `AUTOMATIC_BISECT` | Halves a failing batch until only the failing record is left. |
    | Dead-letter queue | Amazon SQS queue | Holds one message for each record the pipe gave up on. |
    | Logs | level `ERROR` | The log group keeps one week. |

3. The input template turns the record into the event `detail`: `tableName`, `operation`, `newImage`, `oldImage`, `txId`, `recordId`, `timestamp` (commit time in milliseconds) and `commitTimestampNs` (commit time in nanoseconds, as a string).
4. Three rules on the custom event bus pick the events up: one sends every change to the audit queue, one sends inserts (`c`) to the validation queue and one sends deletes (`d`) to the alerts queue. An update reaches the audit queue only. Each rule target retries 3 times within 1 hour and then moves the event to the rule-target dead-letter queue. To go further, add rules that target AWS Step Functions or Amazon SNS; the stack does not deploy them.
5. A message in the pipe dead-letter queue means the record never became an event. A message in the rule-target dead-letter queue means the event reached the bus but one rule target did not accept it; the message attributes name the rule and the target.

## Important Notes

- A pipe cannot target the newer Custom Event Bus type ([Amazon EventBridge Pipes targets](https://docs.aws.amazon.com/eventbridge/latest/userguide/eb-pipes-event-target.html)). This pattern uses a classic custom event bus, the kind that has rules.
- The event type is the raw operation code (`c`, `u`, `d`), not a name such as `INSERT`.
- AWS CloudFormation has no resource type for a CDC stream, so the stack creates it with one `createStream` call through the CDK `AwsCustomResource` ([Aurora DSQL CDC guide](https://docs.aws.amazon.com/aurora-dsql/latest/userguide/cdc-streams.html)). That construct adds a CDK-managed AWS Lambda function that is not in the data path.
- A record that is not `full` is dropped. A `full` record above 1 MB cannot become an event, because an Amazon EventBridge request is limited to 1 MB: after the retries it ends in the pipe dead-letter queue (step 5).
- The pipe dead-letter message holds no record, only the shard and the sequence number of the batch. Read the record back within the 24 hour retention of the stream with `aws kinesis get-shard-iterator --shard-iterator-type AT_SEQUENCE_NUMBER` and `aws kinesis get-records`.
- Deployed and tested in `us-west-2` and `us-east-1`.

## Deployment Instructions

1. Clone the repository and change to the pattern folder:

    ```bash
    git clone https://github.com/aws-samples/serverless-patterns
    cd serverless-patterns/dsql-cdc-eventbridge-pipes/typescript/cdk
    ```

2. Create an Amazon Aurora DSQL cluster in the Region you deploy to, and wait until it is `ACTIVE`:

    ```bash
    export AWS_REGION=us-west-2
    export CLUSTER_ID=$(aws dsql create-cluster --query identifier --output text)
    aws dsql wait cluster-active --identifier $CLUSTER_ID
    ```

3. Install the dependencies, check the code and deploy (2 to 3 minutes):

    ```bash
    npm install
    npm run build
    npx cdk deploy --parameters DsqlClusterId=$CLUSTER_ID
    ```

## Testing

1. In every new shell, set the Region and the cluster identifier (`aws dsql list-clusters` lists them) and define two helpers. `events` prints one line per event (type, table, record id) and removes the messages it shows from the queue:

    ```bash
    export AWS_REGION=us-west-2
    export CLUSTER_ID=YOUR_CLUSTER_ID
    out() { aws cloudformation describe-stacks --stack-name DsqlCdcEventbridgePipesStack \
      --query "Stacks[0].Outputs[?OutputKey=='$1'].OutputValue" --output text; }
    events() { while M=$(aws sqs receive-message --queue-url "$1" --max-number-of-messages 10 --wait-time-seconds 5 --output json) && [ -n "$M" ]; do
        echo "$M" | jq -r '.Messages[] | (.Body | fromjson | [."detail-type", .detail.tableName, .detail.recordId] | @tsv)'
        echo "$M" | jq -r '.Messages[].ReceiptHandle' | while read -r H; do aws sqs delete-message --queue-url "$1" --receipt-handle "$H"; done
      done | sort -u; }
    ```

2. Check that the CDC stream and the pipe are ready. Expected: `ACTIVE` and `RUNNING`.

    ```bash
    aws dsql get-stream --cluster-identifier $CLUSTER_ID --stream-identifier "$(out CdcStreamId)" --query status --output text
    aws pipes describe-pipe --name "$(out PipeName)" --query CurrentState --output text
    ```

3. Connect with `psql` and run the SQL as separate statements: each `INSERT`, `UPDATE` and `DELETE` is its own transaction and one change record (`CREATE TABLE` produces none). The token is valid for 15 minutes.

    ```bash
    export ENDPOINT=$CLUSTER_ID.dsql.$AWS_REGION.on.aws
    export PGPASSWORD=$(aws dsql generate-db-connect-admin-auth-token --hostname $ENDPOINT)
    export PGSSLMODE=require
    psql --username admin --dbname postgres --host $ENDPOINT
    ```

    ```sql
    CREATE TABLE orders (
      id UUID DEFAULT gen_random_uuid() PRIMARY KEY,
      customer_name TEXT NOT NULL,
      amount DECIMAL(10,2),
      created_at TIMESTAMP DEFAULT now()
    );

    INSERT INTO orders (customer_name, amount) VALUES ('AnyCompany', 1250.00);
    UPDATE orders SET amount = 1500.00 WHERE customer_name = 'AnyCompany';
    DELETE FROM orders WHERE customer_name = 'AnyCompany';
    ```

4. Read each queue. Expected: `c`, `u` and `d` in the audit queue, `c` in the validation queue and `d` in the alerts queue. The first events after a deployment can take a minute or two (later ones a few seconds), so run the commands again if a queue is empty:

    ```bash
    echo audit;      events "$(out AuditQueueUrl)"
    echo validation; events "$(out ValidationQueueUrl)"
    echo alerts;     events "$(out AlertsQueueUrl)"
    ```

5. Make the pipe fail with a row whose event is above the 1 MB limit (two columns of 700000 characters). In `psql`, insert it and then an ordinary row:

    ```sql
    CREATE TABLE big_rows (id UUID DEFAULT gen_random_uuid() PRIMARY KEY, a TEXT, b TEXT);
    INSERT INTO big_rows (a, b) VALUES (repeat('x', 700000), repeat('y', 700000));
    INSERT INTO orders (customer_name, amount) VALUES ('After the big row', 1.00);
    ```

    Wait a minute, then read the pipe dead-letter queue, the pipe log and the audit queue:

    ```bash
    aws sqs receive-message --queue-url "$(out PipeDlqUrl)" --wait-time-seconds 20 --output json
    aws logs tail "$(out PipeLogGroup)" --since 30m --format short
    events "$(out AuditQueueUrl)"
    ```

    Expected: one dead-letter message with `condition` `RetryAttemptsExhausted` and a `KinesisBatchInfo` (shard, sequence numbers), `TargetInvocationFailed` log lines with `Total size of the entries in the request is over the limit`, and only the ordinary row (`c`) in the audit queue: the big row made no event and did not hold up the row behind it.

6. Make a rule target fail: remove the alerts queue policy so that Amazon EventBridge cannot deliver, delete a row, read the rule-target dead-letter queue and restore the policy:

    ```bash
    ALERTS_URL=$(out AlertsQueueUrl)
    aws sqs get-queue-attributes --queue-url "$ALERTS_URL" --attribute-names Policy --query Attributes --output json > alerts-policy.json
    aws sqs set-queue-attributes --queue-url "$ALERTS_URL" --attributes '{"Policy":""}'
    sleep 10
    ```

    ```sql
    INSERT INTO orders (customer_name, amount) VALUES ('Example Corp', 5.00);
    DELETE FROM orders WHERE customer_name = 'Example Corp';
    ```

    ```bash
    aws sqs receive-message --queue-url "$(out RuleTargetDlqUrl)" --wait-time-seconds 20 --message-attribute-names All --output json
    aws sqs set-queue-attributes --queue-url "$ALERTS_URL" --attributes file://alerts-policy.json
    rm -f alerts-policy.json
    ```

    Expected: the delete event as the message body and the attributes `ERROR_CODE` `NO_PERMISSIONS`, `ERROR_MESSAGE`, `RULE_ARN` (the deletes rule) and `TARGET_ARN` (the alerts queue), within seconds because a missing permission skips the retries.

## Cleanup

> **Warning:** this deletes the stack with its stream, the queues and their messages, and the Amazon Aurora DSQL cluster with all its data.

1. Delete any rules you added to the event bus outside the stack, because an [event bus can't be deleted while it has rules](https://docs.aws.amazon.com/eventbridge/latest/APIReference/API_DeleteEventBus.html).

2. Delete the stack. This also deletes the CDC stream:

    ```bash
    npx cdk destroy
    ```

3. Delete the Amazon Aurora DSQL cluster. A new cluster has deletion protection turned on, so turn it off first. If you used an existing cluster, keep it and drop only the tables you created for this test (`orders` and `big_rows`) in `psql` instead:

    ```bash
    aws dsql update-cluster --identifier $CLUSTER_ID --no-deletion-protection-enabled
    aws dsql delete-cluster --identifier $CLUSTER_ID
    ```

4. The helper function of the custom resource writes its last log lines after AWS CloudFormation deletes its log group, so AWS Lambda creates the group again without retention. Delete it:

    ```bash
    for g in $(aws logs describe-log-groups --log-group-name-prefix DsqlCdcEventbridgePipesStack-CdcStreamCrLogs \
      --query 'logGroups[].logGroupName' --output text); do aws logs delete-log-group --log-group-name $g; done
    ```

----
Copyright 2026 Amazon.com, Inc. or its affiliates. All Rights Reserved.

SPDX-License-Identifier: MIT-0
