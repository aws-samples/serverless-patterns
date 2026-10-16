#!/bin/bash
# Fetch a Cognito access token for a role and write a Kafka client.properties file
# that authenticates to the brokers with SASL/OAUTHBEARER.
#
# Usage: refresh_token.sh <admin|producer|consumer> [output-file]
# Prints the path of the written properties file on stdout.
set -eo pipefail
source /home/ec2-user/kafka_oauth.env

ROLE="${1:?usage: refresh_token.sh <admin|producer|consumer> [output-file]}"
case "$ROLE" in
  admin)    USERNAME="$ADMIN_USERNAME";    SECRET="$ADMIN_SECRET_NAME" ;;
  producer) USERNAME="$PRODUCER_USERNAME"; SECRET="$PRODUCER_SECRET_NAME" ;;
  consumer) USERNAME="$CONSUMER_USERNAME"; SECRET="$CONSUMER_SECRET_NAME" ;;
  *) echo "Unknown role: $ROLE (expected admin|producer|consumer)" >&2; exit 2 ;;
esac
OUT="${2:-/home/ec2-user/kafka/config/${ROLE}.properties}"

PASSWORD="$(aws secretsmanager get-secret-value --region "$AWS_REGION" --secret-id "$SECRET" --query SecretString --output text | jq -r .password)"
TOKEN="$(aws cognito-idp initiate-auth --region "$AWS_REGION" --auth-flow USER_PASSWORD_AUTH \
  --client-id "$APP_CLIENT_ID" \
  --auth-parameters USERNAME="$USERNAME",PASSWORD="$PASSWORD" \
  --query 'AuthenticationResult.AccessToken' --output text)"
if [ -z "$TOKEN" ] || [ "$TOKEN" = "None" ]; then
  echo "ERROR: could not obtain a Cognito access token for role '$ROLE'" >&2
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
