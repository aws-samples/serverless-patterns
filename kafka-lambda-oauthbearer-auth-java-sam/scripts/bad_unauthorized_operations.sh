#!/bin/bash
# Negative test: VALID users attempting operations they are NOT authorized for.
# All three users authenticate successfully (valid OAuth tokens) but the broker
# authorizer denies the operation because they lack the required ACL.
#
# Usage: bad_unauthorized_operations.sh [topic]
source /home/ec2-user/kafka_oauth.env
TOPIC="${1:-$KAFKA_TOPIC}"

echo "=================================================================="
echo " Negative test: VALID users, UNAUTHORIZED operations (topic=$TOPIC)"
echo "=================================================================="

PPROPS="$(/home/ec2-user/scripts/refresh_token.sh producer)"
CPROPS="$(/home/ec2-user/scripts/refresh_token.sh consumer)"

echo
echo "-- (a) PRODUCER tries to CREATE a topic (only admin may) --"
"$KAFKA_HOME"/bin/kafka-topics.sh --create --if-not-exists \
  --bootstrap-server "$BOOTSTRAP_SERVERS" --command-config "$PPROPS" \
  --replication-factor 3 --partitions 1 --topic "unauthorized-topic-$RANDOM" 2>&1 | head -8
echo ">> expected: TopicAuthorizationException / cluster authorization failed"

echo
echo "-- (b) CONSUMER tries to PRODUCE a message (needs WRITE) --"
echo "hello-from-consumer" | "$KAFKA_HOME"/bin/kafka-console-producer.sh \
  --bootstrap-server "$BOOTSTRAP_SERVERS" --producer.config "$CPROPS" --topic "$TOPIC" 2>&1 | head -8
echo ">> expected: TopicAuthorizationException (not authorized to write)"

echo
echo "-- (c) PRODUCER tries to CONSUME messages (needs READ) --"
timeout 25 "$KAFKA_HOME"/bin/kafka-console-consumer.sh \
  --bootstrap-server "$BOOTSTRAP_SERVERS" --consumer.config "$PPROPS" \
  --topic "$TOPIC" --group "bad-producer-group-$RANDOM" --from-beginning --timeout-ms 10000 2>&1 | head -8
echo ">> expected: TopicAuthorizationException (not authorized to read)"
