#!/bin/bash
# Mint an AWS IAM Outbound web-identity (OIDC) token for a role and write a Kafka
# client.properties that authenticates to the brokers with SASL/OAUTHBEARER.
#
# Usage: refresh_token.sh <admin|producer|consumer> [output-file]
# Prints the path of the written properties file on stdout.
#
# NOTE (under development): the exact `aws sts get-web-identity-token` CLI shape and
# response field are not finalized. Adjust the command / --query below if they differ.
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

# Assume the role, then mint a web-identity token as that role's identity so the
# token subject (the Kafka principal) differs per role.
CREDS_JSON="$(aws sts assume-role --role-arn "$ROLE_ARN" --role-session-name "kafka-$ROLE" --query 'Credentials' --output json)"
export AWS_ACCESS_KEY_ID="$(echo "$CREDS_JSON" | jq -r .AccessKeyId)"
export AWS_SECRET_ACCESS_KEY="$(echo "$CREDS_JSON" | jq -r .SecretAccessKey)"
export AWS_SESSION_TOKEN="$(echo "$CREDS_JSON" | jq -r .SessionToken)"

TOKEN="$(aws sts get-web-identity-token --audience "$OUTBOUND_AUDIENCE" --signing-algorithm RS256 --query 'WebIdentityToken' --output text)"
if [ -z "$TOKEN" ] || [ "$TOKEN" = "None" ]; then
  echo "ERROR: could not mint a web-identity token for role '$ROLE'" >&2
  exit 1
fi

cat > "$OUT" <<EOF
bootstrap.servers=$BOOTSTRAP_SERVERS
security.protocol=SASL_SSL
sasl.mechanism=OAUTHBEARER
ssl.truststore.location=$KAFKA_TRUSTSTORE
ssl.truststore.password=changeit
ssl.truststore.type=PKCS12
sasl.login.callback.handler.class=io.strimzi.kafka.oauth.client.JaasClientOauthLoginCallbackHandler
sasl.jaas.config=org.apache.kafka.common.security.oauthbearer.OAuthBearerLoginModule required oauth.access.token="$TOKEN" ;
EOF
echo "$OUT"
