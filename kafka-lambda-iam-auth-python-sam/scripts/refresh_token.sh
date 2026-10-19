#!/bin/bash
# Write a Kafka client.properties that authenticates to MSK with SASL/AWS_MSK_IAM,
# assuming the IAM role for the requested logical client so authorization differs
# per role. No token to fetch - the aws-msk-iam-auth library signs with SigV4.
#
# Usage: refresh_token.sh <admin|producer|consumer> [output-file]
# Prints the path of the written properties file on stdout.
set -eo pipefail
source /home/ec2-user/kafka_oauth.env

ROLE="${1:?usage: refresh_token.sh <admin|producer|consumer> [output-file]}"
case "$ROLE" in
  admin)    ROLE_ARN="$ADMIN_ROLE_ARN" ;;
  producer) ROLE_ARN="$PRODUCER_ROLE_ARN" ;;
  consumer) ROLE_ARN="$CONSUMER_ROLE_ARN" ;;
  *) echo "Unknown role: $ROLE (expected admin|producer|consumer)" >&2; exit 2 ;;
esac
OUT="${2:-/home/ec2-user/kafka/config/${ROLE}.properties}"

cat > "$OUT" <<EOF
bootstrap.servers=$BOOTSTRAP_SERVERS
security.protocol=SASL_SSL
sasl.mechanism=AWS_MSK_IAM
sasl.jaas.config=software.amazon.msk.auth.iam.IAMLoginModule required awsRoleArn="$ROLE_ARN" awsStsRegion="$AWS_REGION";
sasl.client.callback.handler.class=software.amazon.msk.auth.iam.IAMClientCallbackHandler
EOF
echo "$OUT"
