#!/bin/bash
#
# Seeds the DynamoDB tenant table with sample records for two tenants so you can
# observe tenant isolation. Get the table name from the CDK output "TenantTableName".
#
# Usage: ./seed_tenant_data.sh <table-name> [region]

set -euo pipefail

TABLE_NAME=${1:-}
REGION=${2:-${AWS_DEFAULT_REGION:-us-west-2}}

if [ -z "$TABLE_NAME" ]; then
  echo "Usage: ./seed_tenant_data.sh <table-name> [region]"
  exit 1
fi

put() {
  local tenant=$1 record=$2 desc=$3
  aws dynamodb put-item \
    --table-name "$TABLE_NAME" \
    --region "$REGION" \
    --item "{\"tenant_id\":{\"S\":\"$tenant\"},\"record_id\":{\"S\":\"$record\"},\"description\":{\"S\":\"$desc\"}}"
  echo "  put $tenant / $record"
}

echo "Seeding tenant data into $TABLE_NAME ($REGION)..."
put "acme"   "order-1001" "Acme order 1001: 500 anvils"
put "acme"   "order-1002" "Acme order 1002: 20 rocket skates"
put "globex" "order-2001" "Globex order 2001: 1000 widgets"
put "globex" "order-2002" "Globex order 2002: 3 fusion reactors"
echo "Done."
