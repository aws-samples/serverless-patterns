#!/bin/bash

echo "Cognito Token Generator"
echo "Get Pool ID and Client ID from CDK stack outputs"
echo ""

CONFIG_FILE=".cognito_config"

if [ -f "$CONFIG_FILE" ]; then
  source "$CONFIG_FILE"
fi

read -p "Pool ID [$POOL_ID]: " input && POOL_ID=${input:-$POOL_ID}
read -p "Client ID [$CLIENT_ID]: " input && CLIENT_ID=${input:-$CLIENT_ID}
read -p "Username [$USERNAME]: " input && USERNAME=${input:-$USERNAME}
read -sp "Password: " PASSWORD
echo
read -p "Region [${REGION:-us-west-2}]: " input && REGION=${input:-${REGION:-us-west-2}}

cat > "$CONFIG_FILE" << EOF
POOL_ID=$POOL_ID
CLIENT_ID=$CLIENT_ID
USERNAME=$USERNAME
REGION=$REGION
EOF

aws cognito-idp admin-create-user \
  --user-pool-id $POOL_ID \
  --username $USERNAME \
  --region $REGION \
  --message-action SUPPRESS > /dev/null 2>&1 || true

aws cognito-idp admin-set-user-password \
  --user-pool-id $POOL_ID \
  --username $USERNAME \
  --password $PASSWORD \
  --region $REGION \
  --permanent > /dev/null 2>&1 || true

BEARER_TOKEN=$(aws cognito-idp initiate-auth \
  --client-id "$CLIENT_ID" \
  --auth-flow USER_PASSWORD_AUTH \
  --auth-parameters USERNAME=$USERNAME,PASSWORD=$PASSWORD \
  --region $REGION | jq -r '.AuthenticationResult.AccessToken')

echo "export BEARER_TOKEN=\"$BEARER_TOKEN\""
