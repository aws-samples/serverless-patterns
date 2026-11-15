#!/bin/bash

# Create/update API key for a tenant
# Usage: ./create-api-key tenant-1

tenant_id=$1
if [ -z "$tenant_id" ]; then
  echo "Error: Tenant ID is required"
  exit 1
fi

# Generate random 32-character API key
api_key=$(openssl rand -hex 16)

# Store the secret with the API key as the identifier
aws secretsmanager create-secret \
  --name "api-key-${api_key}" \
  --secret-string "{\"tenantId\":\"${tenant_id}\"}" \
  --no-cli-pager

echo "API key for tenant ${tenant_id} created: ${api_key}"
