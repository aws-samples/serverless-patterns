#!/bin/bash
# Producer client: publish N Faker-generated JSON "person" messages to a topic
# using the producer user's OAuth token. This user is only allowed to WRITE.
#
# Usage: producer_send.sh <topic> <count>
set -eo pipefail
source /home/ec2-user/kafka_oauth.env

TOPIC="${1:?usage: producer_send.sh <topic> <count>}"
COUNT="${2:?usage: producer_send.sh <topic> <count>}"
PROPS="$(/home/ec2-user/scripts/refresh_token.sh producer)"

python3 "$KAFKA_JSON_APPS_DIR/producer.py" "$PROPS" "$TOPIC" "$COUNT"
