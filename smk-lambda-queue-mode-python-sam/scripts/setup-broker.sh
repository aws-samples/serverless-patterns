#!/usr/bin/env bash
# setup-broker.sh — Install and start Kafka on the broker EC2 instance via SSM
#
# This script installs Apache Kafka 4.2.x on the EC2 instance deployed by
# stacks/2-broker.yaml. It uses SSM Run Command so no SSH or bastion host
# is required. Each step runs sequentially and reports progress.
#
# Usage:
#   ./scripts/setup-broker.sh --region <region> --profile <profile>
#
# Prerequisites:
#   - stacks/1-network.yaml and stacks/2-broker.yaml must be deployed
#   - AWS CLI configured with appropriate credentials

set -euo pipefail

REGION="${AWS_DEFAULT_REGION:-us-east-1}"
PROFILE="${AWS_PROFILE:-default}"
BROKER_STACK="kafka-queue-broker"
KAFKA_VERSION="4.2.0"

while [[ $# -gt 0 ]]; do
  case $1 in
    --region)  REGION="$2";  shift 2 ;;
    --profile) PROFILE="$2"; shift 2 ;;
    *) echo "Unknown option: $1"; exit 1 ;;
  esac
done

echo "=== Kafka broker setup ==="
echo "  Region:  $REGION"
echo "  Profile: $PROFILE"
echo "  Version: $KAFKA_VERSION"
echo ""

# ── Get instance ID from stack output ────────────────────────
INSTANCE_ID=$(aws cloudformation describe-stacks \
  --stack-name "$BROKER_STACK" --profile "$PROFILE" --region "$REGION" \
  --query "Stacks[0].Outputs[?OutputKey=='BrokerInstanceId'].OutputValue" \
  --output text)

if [ -z "$INSTANCE_ID" ] || [ "$INSTANCE_ID" = "None" ]; then
  echo "ERROR: Could not get instance ID from stack $BROKER_STACK"
  exit 1
fi
echo "Instance: $INSTANCE_ID"
echo ""

# ── Wait for SSM agent ────────────────────────────────────────
echo "Waiting for SSM agent..."
for i in $(seq 1 30); do
  STATUS=$(aws ssm describe-instance-information \
    --filters "Key=InstanceIds,Values=$INSTANCE_ID" \
    --profile "$PROFILE" --region "$REGION" \
    --query 'InstanceInformationList[0].PingStatus' \
    --output text 2>/dev/null || echo "None")
  if [ "$STATUS" = "Online" ]; then
    echo "SSM agent ready."
    break
  fi
  echo "  [$i/30] Waiting... ($STATUS)"
  sleep 10
done

# ── Helper: run SSM command and wait ─────────────────────────
run_ssm() {
  local STEP="$1"
  local CMD="$2"
  local TIMEOUT="${3:-300}"

  echo "[$STEP]"
  CMD_ID=$(aws ssm send-command \
    --instance-ids "$INSTANCE_ID" \
    --document-name AWS-RunShellScript \
    --parameters "commands=[\"$CMD\"]" \
    --profile "$PROFILE" --region "$REGION" \
    --query 'Command.CommandId' --output text)

  # Poll until complete
  for i in $(seq 1 $((TIMEOUT / 10))); do
    sleep 10
    STATUS=$(aws ssm get-command-invocation \
      --command-id "$CMD_ID" --instance-id "$INSTANCE_ID" \
      --profile "$PROFILE" --region "$REGION" \
      --query 'Status' --output text 2>/dev/null || echo "Pending")
    if [ "$STATUS" = "Success" ]; then
      OUT=$(aws ssm get-command-invocation \
        --command-id "$CMD_ID" --instance-id "$INSTANCE_ID" \
        --profile "$PROFILE" --region "$REGION" \
        --query 'StandardOutputContent' --output text 2>/dev/null)
      [ -n "$OUT" ] && echo "  $OUT"
      echo "  Done."
      return 0
    elif [ "$STATUS" = "Failed" ] || [ "$STATUS" = "TimedOut" ]; then
      ERR=$(aws ssm get-command-invocation \
        --command-id "$CMD_ID" --instance-id "$INSTANCE_ID" \
        --profile "$PROFILE" --region "$REGION" \
        --query 'StandardErrorContent' --output text 2>/dev/null)
      echo "  ERROR: $ERR"
      exit 1
    fi
    echo "  [$((i * 10))s] $STATUS..."
  done
  echo "  ERROR: Timed out after ${TIMEOUT}s"
  exit 1
}

# ── Step 1: Install Java ──────────────────────────────────────
run_ssm "1/6 Install Java" \
  "dnf install -y java-21-amazon-corretto-headless && java -version 2>&1 | head -1" \
  180

# ── Step 2: Download Kafka ────────────────────────────────────
run_ssm "2/6 Download Kafka $KAFKA_VERSION (this takes ~20 min)" \
  "wget -q --timeout=1800 --tries=3 https://archive.apache.org/dist/kafka/${KAFKA_VERSION}/kafka_2.13-${KAFKA_VERSION}.tgz -O /tmp/kafka.tgz && ls -lh /tmp/kafka.tgz" \
  2400

# ── Step 3: Extract ───────────────────────────────────────────
run_ssm "3/6 Extract Kafka" \
  "mkdir -p /opt/kafka && tar -xzf /tmp/kafka.tgz -C /opt/kafka --strip-components=1 && echo extracted" \
  120

# ── Step 4: Write config and format storage ───────────────────
run_ssm "4/6 Configure and format storage" \
  "INSTANCE_IP=\$(curl -s http://169.254.169.254/latest/meta-data/local-ipv4) && mkdir -p /var/kafka-logs && printf '%s\n' process.roles=broker,controller node.id=1 controller.quorum.voters=1@localhost:9093 'listeners=CONTROLLER://localhost:9093,PLAINTEXT://0.0.0.0:9092' \"advertised.listeners=PLAINTEXT://\$INSTANCE_IP:9092\" listener.security.protocol.map=CONTROLLER:PLAINTEXT,PLAINTEXT:PLAINTEXT controller.listener.names=CONTROLLER inter.broker.listener.name=PLAINTEXT log.dirs=/var/kafka-logs num.partitions=3 default.replication.factor=1 offsets.topic.replication.factor=1 transaction.state.log.replication.factor=1 transaction.state.log.min.isr=1 auto.create.topics.enable=true group.coordinator.rebalance.protocols=classic,consumer,share share.coordinator.state.topic.replication.factor=1 share.coordinator.state.topic.min.isr=1 group.share.partition.max.record.locks=100 group.share.record.lock.duration.ms=30000 group.share.delivery.count.limit=3 group.share.max.size=10 > /tmp/kraft-server.properties && CLUSTER_ID=\$(/opt/kafka/bin/kafka-storage.sh random-uuid) && /opt/kafka/bin/kafka-storage.sh format -t \$CLUSTER_ID -c /tmp/kraft-server.properties && echo formatted" \
  60

# ── Step 5: Start Kafka and wait for ready ────────────────────
run_ssm "5/6 Start Kafka broker" \
  "export KAFKA_HEAP_OPTS='-Xmx512m -Xms256m' && nohup /opt/kafka/bin/kafka-server-start.sh /tmp/kraft-server.properties > /var/log/kafka.log 2>&1 & sleep 20 && for i in \$(seq 1 12); do /opt/kafka/bin/kafka-broker-api-versions.sh --bootstrap-server localhost:9092 > /dev/null 2>&1 && echo broker_ready && break || sleep 5; done" \
  180

# ── Step 6: Enable share groups ──────────────────────────────
run_ssm "6/6 Enable KIP-932 share groups" \
  "/opt/kafka/bin/kafka-features.sh --bootstrap-server localhost:9092 upgrade --feature share.version=1 2>&1" \
  30

# ── Done ─────────────────────────────────────────────────────
BOOTSTRAP=$(aws cloudformation describe-stacks \
  --stack-name "$BROKER_STACK" --profile "$PROFILE" --region "$REGION" \
  --query "Stacks[0].Outputs[?OutputKey=='BootstrapServers'].OutputValue" \
  --output text)

echo ""
echo "=== Kafka broker ready ==="
echo "  Bootstrap servers: $BOOTSTRAP"
echo ""
echo "Next step: deploy the application stack"
echo "  sam build --template stacks/3-app.yaml"
echo "  sam deploy --stack-name kafka-queue-app \\"
echo "    --template-file .aws-sam/build/template.yaml \\"
echo "    --capabilities CAPABILITY_IAM --resolve-s3 \\"
echo "    --profile $PROFILE --region $REGION"
