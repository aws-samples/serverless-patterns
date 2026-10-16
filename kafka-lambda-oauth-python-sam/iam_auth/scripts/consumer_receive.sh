#!/bin/bash
# Consumer client: consume JSON messages from a topic and print each one parsed,
# using the consumer user's OAuth token. This user is only allowed to READ.
#
# Usage: consumer_receive.sh <topic> [group-id]
set -eo pipefail
source /home/ec2-user/kafka_oauth.env

TOPIC="${1:?usage: consumer_receive.sh <topic> [group-id]}"
GROUP="${2:-kafka-oauth-consumer-group}"
PROPS="$(/home/ec2-user/scripts/refresh_token.sh consumer)"

python3 "$KAFKA_JSON_APPS_DIR/consumer.py" "$PROPS" "$TOPIC" "$GROUP"
