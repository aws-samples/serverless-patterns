#!/bin/bash
# Admin: create a Kafka topic and grant least-privilege ACLs to the producer and
# consumer role principals.
#
# Because every client here authenticates with an AWS web-identity token whose
# subject is only known after the token is minted, admin operations run over the
# brokers' INTERNAL PLAINTEXT listener (where ANONYMOUS is a broker super user),
# so no token is needed to manage topics/ACLs. The producer/consumer principals
# are derived at runtime by decoding the 'sub' claim of their minted tokens.
#
# Usage: admin_create_topic.sh <topic> [partitions]
set -eo pipefail
source /home/ec2-user/kafka_oauth.env

TOPIC="${1:?usage: admin_create_topic.sh <topic> [partitions]}"
PARTITIONS="${2:-3}"
BS="$INTERNAL_BOOTSTRAP"   # PLAINTEXT internal listener; ANONYMOUS = broker super user

# Print the Kafka principal (token 'sub') for a role by minting its web-identity token.
principal_of() {
  local role="$1" props jwt payload
  props="$(/home/ec2-user/scripts/refresh_token.sh "$role" "/tmp/${role}.properties")"
  jwt="$(sed -n 's/.*oauth.access.token="\([^"]*\)".*/\1/p' "$props")"
  payload="$(printf '%s' "$jwt" | cut -d. -f2)"
  python3 -c "import sys,base64,json; p=sys.argv[1]; p+='='*(-len(p)%4); print(json.loads(base64.urlsafe_b64decode(p)).get('sub',''))" "$payload"
}

echo "Creating topic '$TOPIC' (partitions=$PARTITIONS, replication=3) via internal listener..."
"$KAFKA_HOME"/bin/kafka-topics.sh --create --if-not-exists \
  --bootstrap-server "$BS" --replication-factor 3 --partitions "$PARTITIONS" --topic "$TOPIC"

PRODUCER_PRINCIPAL="$(principal_of producer)"
CONSUMER_PRINCIPAL="$(principal_of consumer)"
echo "Granting WRITE to '$PRODUCER_PRINCIPAL' and READ to '$CONSUMER_PRINCIPAL' on '$TOPIC'..."
"$KAFKA_HOME"/bin/kafka-acls.sh --bootstrap-server "$BS" --add \
  --allow-principal "User:$PRODUCER_PRINCIPAL" --operation Write --topic "$TOPIC"
"$KAFKA_HOME"/bin/kafka-acls.sh --bootstrap-server "$BS" --add \
  --allow-principal "User:$CONSUMER_PRINCIPAL" --operation Read --topic "$TOPIC"
"$KAFKA_HOME"/bin/kafka-acls.sh --bootstrap-server "$BS" --add \
  --allow-principal "User:$CONSUMER_PRINCIPAL" --operation Read --group '*'

echo
echo "Topic '$TOPIC' is ready:"
"$KAFKA_HOME"/bin/kafka-topics.sh --describe --bootstrap-server "$BS" --topic "$TOPIC"
