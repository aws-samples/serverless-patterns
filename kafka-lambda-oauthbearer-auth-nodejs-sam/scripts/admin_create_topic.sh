#!/bin/bash
# Admin client: create a Kafka topic and grant least-privilege ACLs so the
# producer user can WRITE to it and the consumer user can READ from it.
# Only the admin user (a Kafka super user) is allowed to do this.
#
# Usage: admin_create_topic.sh <topic> [partitions]
set -eo pipefail
source /home/ec2-user/kafka_oauth.env

TOPIC="${1:?usage: admin_create_topic.sh <topic> [partitions]}"
PARTITIONS="${2:-3}"
PROPS="$(/home/ec2-user/scripts/refresh_token.sh admin)"

echo "Creating topic '$TOPIC' (partitions=$PARTITIONS, replication=3) as admin..."
"$KAFKA_HOME"/bin/kafka-topics.sh --create --if-not-exists \
  --bootstrap-server "$BOOTSTRAP_SERVERS" --command-config "$PROPS" \
  --replication-factor 3 --partitions "$PARTITIONS" --topic "$TOPIC"

echo "Granting ACLs: WRITE to '$PRODUCER_USERNAME', READ to '$CONSUMER_USERNAME' on topic '$TOPIC'..."
"$KAFKA_HOME"/bin/kafka-acls.sh --bootstrap-server "$BOOTSTRAP_SERVERS" --command-config "$PROPS" \
  --add --allow-principal "User:$PRODUCER_USERNAME" --operation Write --topic "$TOPIC"
"$KAFKA_HOME"/bin/kafka-acls.sh --bootstrap-server "$BOOTSTRAP_SERVERS" --command-config "$PROPS" \
  --add --allow-principal "User:$CONSUMER_USERNAME" --operation Read --topic "$TOPIC"

echo
echo "Topic '$TOPIC' is ready:"
"$KAFKA_HOME"/bin/kafka-topics.sh --describe \
  --bootstrap-server "$BOOTSTRAP_SERVERS" --command-config "$PROPS" --topic "$TOPIC"
