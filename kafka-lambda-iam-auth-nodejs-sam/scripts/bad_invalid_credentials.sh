#!/bin/bash
# Negative test: an IAM identity that cannot authenticate to MSK.
#
# NOTE on the AWS_MSK_IAM library: if you specify an `awsRoleArn` that cannot be
# assumed, the aws-msk-iam-auth client does NOT fail - it silently falls back to
# the default credential chain (here, the client EC2 instance profile, which CAN
# authenticate). That masks the failure. To genuinely exercise a failed SASL/IAM
# handshake we instead feed the default chain GARBAGE static credentials (bogus
# access key/secret, no session token) and use the plain IAMLoginModule. MSK then
# rejects the SigV4 signature and the handshake fails.
source /home/ec2-user/kafka_oauth.env

echo "=================================================================="
echo " Negative test: invalid IAM credentials (bad SigV4 signature)"
echo "=================================================================="
BADPROPS=/tmp/bad-iam.properties
cat > "$BADPROPS" <<EOF
bootstrap.servers=$BOOTSTRAP_SERVERS
security.protocol=SASL_SSL
sasl.mechanism=AWS_MSK_IAM
sasl.jaas.config=software.amazon.msk.auth.iam.IAMLoginModule required awsStsRegion="$AWS_REGION";
sasl.client.callback.handler.class=software.amazon.msk.auth.iam.IAMClientCallbackHandler
EOF

# Force the default credential chain to use bogus static keys (env vars take
# precedence over the instance profile). Unset the session token so no valid
# temporary credentials are picked up.
env AWS_ACCESS_KEY_ID=AKIAINVALIDINVALID00 \
    AWS_SECRET_ACCESS_KEY=THIS/IS/AN/INVALID/SECRET/KEYbadbadbad00 \
    AWS_SESSION_TOKEN= \
    AWS_PROFILE= \
    "$KAFKA_HOME"/bin/kafka-topics.sh --list \
      --bootstrap-server "$BOOTSTRAP_SERVERS" --command-config "$BADPROPS" 2>&1 | head -15
echo ">> expected: SASL authentication failure (invalid SigV4 signature / not authorized)"
