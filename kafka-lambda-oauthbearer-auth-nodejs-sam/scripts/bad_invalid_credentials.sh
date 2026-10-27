#!/bin/bash
# Negative test: a bad actor with INVALID credentials / token.
#  (a) Cognito rejects a bogus username/password (no token is issued).
#  (b) The brokers reject a connection presenting an invalid OAuth token.
source /home/ec2-user/kafka_oauth.env

echo "=================================================================="
echo " Negative test: INVALID credentials / token"
echo "=================================================================="

echo
echo "-- (a) initiate-auth with a bogus username/password --"
aws cognito-idp initiate-auth --region "$AWS_REGION" --auth-flow USER_PASSWORD_AUTH \
  --client-id "$APP_CLIENT_ID" \
  --auth-parameters USERNAME=not-a-real-user,PASSWORD=WrongPassword123 \
  --query 'AuthenticationResult.AccessToken' --output text
echo ">> expected: NotAuthorizedException / UserNotFoundException, no token issued"

echo
echo "-- (b) connect to Kafka with an invalid OAuth token --"
BADPROPS=/tmp/bad-token.properties
cat > "$BADPROPS" <<EOF
security.protocol=SASL_PLAINTEXT
sasl.mechanism=OAUTHBEARER
sasl.login.callback.handler.class=io.strimzi.kafka.oauth.client.JaasClientOauthLoginCallbackHandler
sasl.jaas.config=org.apache.kafka.common.security.oauthbearer.OAuthBearerLoginModule required oauth.access.token="not.a.valid.jwt.token" ;
EOF
"$KAFKA_HOME"/bin/kafka-topics.sh --list \
  --bootstrap-server "$BOOTSTRAP_SERVERS" --command-config "$BADPROPS" 2>&1 | head -15
echo ">> expected: SASL/OAUTHBEARER authentication failure (token rejected by the brokers)"
