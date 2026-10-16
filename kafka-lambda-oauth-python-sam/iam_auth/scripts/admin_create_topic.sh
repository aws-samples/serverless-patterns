#!/bin/bash
# Admin: create a Kafka topic on the MSK cluster using SASL/AWS_MSK_IAM.
#
# With MSK IAM authentication, authorization is enforced by IAM policies on each
# client role (granted by the CloudFormation template) - there are no Kafka ACLs
# to set here. This just creates the topic as the admin role.
#
# Usage: admin_create_topic.sh <topic> [partitions]
set -eo pipefail
source /home/ec2-user/kafka_oauth.env

TOPIC="${1:?usage: admin_create_topic.sh <topic> [partitions]}"
PARTITIONS="${2:-3}"
PROPS="$(/home/ec2-user/scripts/refresh_token.sh admin)"

echo "Creating topic '$TOPIC' (partitions=$PARTITIONS, replication=3) as admin (AWS_MSK_IAM)..."
"$KAFKA_HOME"/bin/kafka-topics.sh --create --if-not-exists \
  --bootstrap-server "$BOOTSTRAP_SERVERS" --command-config "$PROPS" \
  --replication-factor 3 --partitions "$PARTITIONS" --topic "$TOPIC"

echo
echo "Topics on the cluster:"
"$KAFKA_HOME"/bin/kafka-topics.sh --list --bootstrap-server "$BOOTSTRAP_SERVERS" --command-config "$PROPS"
