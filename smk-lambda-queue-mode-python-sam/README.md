# Self-managed Apache Kafka Queue mode to AWS Lambda (KIP-932)

This pattern deploys an AWS Lambda function that consumes from a self-managed Apache Kafka 4.2+ cluster using **Queue consumption mode** (KIP-932 Share Groups). Queue mode allows multiple Lambda pollers to process records from the same partition concurrently — parallelism is decoupled from partition count.

Learn more about this pattern at Serverless Land: https://serverlessland.com/patterns/smk-lambda-queue-mode-python-sam

> **Important:** Queue consumption mode requires Apache Kafka 4.2 or later with share groups enabled. This is a preview feature — `ConsumptionMode: Queue` is not yet available in the SAM or CloudFormation schema. The ESM is created via a script that calls the Lambda API directly.

## Architecture

```
Producer Lambda ──► Kafka topic (3 partitions)
                         │
              ┌──────────┼──────────┐
         Poller 1    Poller 2    Poller 3..10
              │           │           │
         (same partition can be served by multiple pollers)
              └──────────┼──────────┘
                         │
                  Worker Lambda
                  ├── DynamoDB (idempotency)
                  └── SQS DLQ (failed records)
```

## Prerequisites

- [AWS CLI](https://docs.aws.amazon.com/cli/latest/userguide/install-cliv2.html) installed and configured
- [AWS SAM CLI](https://docs.aws.amazon.com/serverless-application-model/latest/developerguide/serverless-sam-cli-install.html) installed
- [Python 3.12](https://www.python.org/downloads/)
- curl >= 7.75 (for `--aws-sigv4` support)
- Apache Kafka 4.2+ cluster (see Deployment Path A to provision one automatically)

## Costs

This pattern uses EC2 (t3.medium), Lambda, DynamoDB, SQS, CloudWatch, and VPC resources. See [AWS Pricing](https://aws.amazon.com/pricing/) for details. There are costs associated with these services beyond the Free Tier.

---

## Deployment

Choose the path that matches your setup:

| Path | When to use |
|------|------------|
| **A — Full** | Starting from scratch — provisions VPC, Kafka EC2 broker, and Lambda app |
| **B — Bring your own Kafka** | You have an existing Kafka 4.2+ cluster; need VPC and Lambda app |
| **C — Bring your own Kafka + VPC** | You have an existing Kafka 4.2+ cluster and VPC |

### Clone the repository

```bash
git clone https://github.com/aws-samples/serverless-patterns
cd serverless-patterns/smk-lambda-queue-mode-python-sam
```

---

### Path A: Full deployment (VPC + Kafka broker + Lambda app)

**Step 1: Deploy the network stack**

```bash
aws cloudformation deploy \
  --stack-name kqd-network \
  --template-file stacks/1-network.yaml \
  --region <region>
```

**Step 2: Deploy the Kafka broker**

```bash
aws cloudformation deploy \
  --stack-name kqd-broker \
  --template-file stacks/2-broker.yaml \
  --capabilities CAPABILITY_IAM \
  --region <region>
```

This provisions a t3.medium EC2 instance running Apache Kafka 4.2.x in KRaft mode with share groups enabled. The stack signals CloudFormation when Kafka is ready (~10 minutes).

**Step 3: Build and deploy the application**

```bash
sam build --template stacks/3-app.yaml
sam deploy \
  --stack-name kqd-app \
  --template-file .aws-sam/build/template.yaml \
  --capabilities CAPABILITY_IAM \
  --resolve-s3 \
  --region <region>
```

**Step 4: Deploy observability (optional)**

```bash
aws cloudformation deploy \
  --stack-name kqd-observability \
  --template-file stacks/4-observability.yaml \
  --region <region>
```

---

### Path B: Bring your own Kafka cluster

Skip Steps 1 and 2. Provide your Kafka bootstrap servers, VPC subnet IDs, and security group at deploy time:

```bash
sam build --template stacks/3-app.yaml
sam deploy \
  --stack-name kqd-app \
  --template-file .aws-sam/build/template.yaml \
  --capabilities CAPABILITY_IAM \
  --resolve-s3 \
  --parameter-overrides \
    UseExistingInfra=true \
    BootstrapServers="broker1.example.com:9092,broker2.example.com:9092" \
    VpcSubnetIds="subnet-aaa111,subnet-bbb222,subnet-ccc333" \
    VpcSecurityGroupId="sg-eee555" \
  --region <region>
```

Your Kafka cluster must:
- Run Apache Kafka 4.2 or later
- Have `group.coordinator.rebalance.protocols=classic,consumer,share` in `server.properties`
- Have `share.version` upgraded to 1 via `kafka-features.sh upgrade --feature share.version=1`
- Be reachable from the Lambda VPC subnets on the configured port

---

### Path C: Bring your own Kafka cluster and VPC

Same as Path B — `UseExistingInfra=true` handles both cases.

---

## Create the Queue mode ESM

After deploying the application stack, create the Event Source Mapping with `ConsumptionMode: Queue`:

```bash
chmod +x scripts/create-esm.sh
./scripts/create-esm.sh --region <region> --profile <profile>
```

Wait ~60 seconds for the ESM to reach `State: Enabled`.

> **Note:** The script uses `curl --aws-sigv4` to call the Lambda API directly because `ConsumptionMode: Queue` is not yet in the SAM or AWS CLI service model. Update to the latest AWS CLI or SAM when this field becomes available to use standard tooling.

---

## Testing

**Produce 20 records:**

```bash
aws lambda invoke \
  --function-name kqd-app-producer \
  --region <region> \
  --cli-binary-format raw-in-base64-out \
  --payload '{"count": 20}' /dev/stdout
```

Every 7th record (`taskIndex % 7 == 0`) has `shouldFail: true` to demonstrate the RELEASE/retry/DLQ path.

**Watch the worker Lambda logs:**

```bash
aws logs tail /aws/lambda/kqd-app-worker \
  --follow \
  --filter-pattern KAFKA_RECORD \
  --region <region>
```

You should see `KAFKA_RECORD` log entries with `topic`, `partition`, `offset`, and `payload`. Records with `shouldFail: true` log a warning and return in `batchItemFailures`, causing the broker to RELEASE them for retry.

**Test locally:**

```bash
sam local invoke WorkerFunction \
  --template stacks/3-app.yaml \
  --event events/kafka-event.json
```

---

## Verifying Queue mode behavior

**Confirm the share group exists on the broker:**

```bash
# On the Kafka broker (via SSM or SSH)
bin/kafka-share-groups.sh --bootstrap-server localhost:9092 --list
# Should show your consumer group ID

bin/kafka-share-groups.sh --bootstrap-server localhost:9092 \
  --describe --group kqd-queue-group-<timestamp>
# Shows per-partition lag with multiple pollers assigned
```

**Confirm share groups are enabled:**

```bash
bin/kafka-features.sh --bootstrap-server localhost:9092 describe | grep share
# Should show: FinalizedVersionLevel: 1
```

---

## Broker-side prerequisites

Before Queue mode can work, ensure your Kafka 4.2+ broker has:

```properties
# Required: enables the share rebalance protocol
group.coordinator.rebalance.protocols=classic,consumer,share

# Required for single-broker setups (default is 3)
share.coordinator.state.topic.replication.factor=1
share.coordinator.state.topic.min.isr=1

# Queue mode tuning parameters
group.share.partition.max.record.locks=100
group.share.record.lock.duration.ms=30000
group.share.delivery.count.limit=3
group.share.max.size=10
```

And run after broker start:

```bash
bin/kafka-features.sh --bootstrap-server localhost:9092 \
  upgrade --feature share.version=1
```

---

## Cleanup

Delete stacks in reverse order:

```bash
# 1. Delete the ESM first (get UUID from create-esm.sh output or console)
aws lambda delete-event-source-mapping --uuid <esm-uuid> --region <region>

# 2. Delete application stacks
aws cloudformation delete-stack --stack-name kqd-observability --region <region>
aws cloudformation delete-stack --stack-name kqd-app --region <region>

# 3. Delete broker (if deployed)
aws cloudformation delete-stack --stack-name kqd-broker --region <region>

# 4. Delete network (if deployed)
aws cloudformation delete-stack --stack-name kqd-network --region <region>
```

---

## Pattern details

| Property | Value |
|----------|-------|
| Kafka version required | Apache Kafka 4.2+ |
| Lambda runtime | Python 3.12 |
| IaC framework | AWS SAM + AWS CloudFormation |
| Delivery semantics | At-least-once |
| Ordering guarantees | None (Queue mode) |
| Authentication | PLAINTEXT (see notes for SASL/SCRAM) |
| Region | Configurable |

## Author

**Vaibhav Jain**
AWS — Senior Delivery Consultant
[LinkedIn](https://www.linkedin.com/in/vaibhavjainv/)
