#!/bin/bash
#
# Creates (or reuses) a Cognito user, assigns it to a tenant group, and prints
# an access token for that user. The access token carries the "cognito:groups"
# claim that the agent uses to determine the caller's tenant.
#
# Get Pool ID, Client ID, and the tenant group names from the CDK stack outputs.

set -euo pipefail

echo "Cognito Multi-Tenant Token Generator"
echo ""

CONFIG_FILE=".cognito_config"
if [ -f "$CONFIG_FILE" ]; then
  # shellcheck disable=SC1090
  source "$CONFIG_FILE"
fi

read -r -p "Pool ID [${POOL_ID:-}]: " input && POOL_ID=${input:-${POOL_ID:-}}
read -r -p "Client ID [${CLIENT_ID:-}]: " input && CLIENT_ID=${input:-${CLIENT_ID:-}}
read -r -p "Username [${USERNAME:-}]: " input && USERNAME=${input:-${USERNAME:-}}
read -r -p "Tenant group (e.g. tenant-acme) [${TENANT_GROUP:-}]: " input && TENANT_GROUP=${input:-${TENANT_GROUP:-}}
echo "Password requires: min 8 chars"
read -r -sp "Password: " PASSWORD
echo
read -r -p "Region [${REGION:-us-west-2}]: " input && REGION=${input:-${REGION:-us-west-2}}

cat > "$CONFIG_FILE" << EOF
POOL_ID=$POOL_ID
CLIENT_ID=$CLIENT_ID
USERNAME=$USERNAME
TENANT_GROUP=$TENANT_GROUP
REGION=$REGION
EOF

aws cognito-idp admin-create-user \
  --user-pool-id "$POOL_ID" \
  --username "$USERNAME" \
  --region "$REGION" \
  --message-action SUPPRESS > /dev/null 2>&1 || true

aws cognito-idp admin-set-user-password \
  --user-pool-id "$POOL_ID" \
  --username "$USERNAME" \
  --password "$PASSWORD" \
  --region "$REGION" \
  --permanent > /dev/null 2>&1 || true

aws cognito-idp admin-add-user-to-group \
  --user-pool-id "$POOL_ID" \
  --username "$USERNAME" \
  --group-name "$TENANT_GROUP" \
  --region "$REGION" > /dev/null 2>&1 || true

BEARER_TOKEN=$(aws cognito-idp initiate-auth \
  --client-id "$CLIENT_ID" \
  --auth-flow USER_PASSWORD_AUTH \
  --auth-parameters USERNAME="$USERNAME",PASSWORD="$PASSWORD" \
  --region "$REGION" | jq -r '.AuthenticationResult.AccessToken')

echo ""
echo "export BEARER_TOKEN=\"$BEARER_TOKEN\""
