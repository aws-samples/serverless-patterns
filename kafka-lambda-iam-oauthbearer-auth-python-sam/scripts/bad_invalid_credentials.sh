#!/bin/bash
# Negative test: a bad actor presenting an INVALID web-identity token.
# The brokers reject any token they cannot validate against the AWS STS OIDC JWKS.
source /home/ec2-user/kafka_oauth.env

echo "=================================================================="
echo " Negative test: INVALID token"
echo "=================================================================="
BADPROPS=/tmp/bad-token.properties
cat > "$BADPROPS" <<EOF
bootstrap.servers=$BOOTSTRAP_SERVERS
security.protocol=SASL_SSL
sasl.mechanism=OAUTHBEARER
ssl.truststore.location=$KAFKA_TRUSTSTORE
ssl.truststore.password=changeit
ssl.truststore.type=PKCS12
sasl.login.callback.handler.class=io.strimzi.kafka.oauth.client.JaasClientOauthLoginCallbackHandler
sasl.jaas.config=org.apache.kafka.common.security.oauthbearer.OAuthBearerLoginModule required oauth.access.token="not.a.valid.token" ;
EOF
"$KAFKA_HOME"/bin/kafka-topics.sh --list \
  --bootstrap-server "$BOOTSTRAP_SERVERS" --command-config "$BADPROPS" 2>&1 | head -15
echo ">> expected: SASL/OAUTHBEARER authentication failure (token rejected by the brokers)"
