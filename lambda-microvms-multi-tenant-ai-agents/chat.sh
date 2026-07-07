#!/usr/bin/env bash
# Synchronous test chat for a tenant (cold-starts the VM if needed). Invokes the
# orchestrator worker directly so it isn't bound by API Gateway's 30s timeout —
# handy for validating cold starts (~90s) from a terminal.
# Usage: ./chat.sh STACK REGION TENANT_ID "message" [sessionKey]
set -euo pipefail
if [ $# -lt 4 ]; then
  echo "usage: $0 STACK REGION TENANT_ID \"message\" [sessionKey]" >&2; exit 1
fi
STACK="$1"; REGION="$2"; TID="$3"; MSG="$4"; SESS="${5:-cli}"
FN="${STACK}-orchestrator"

# Heads-up before the blocking invoke: a cold tenant means a ~90s MicroVM cold start,
# which would otherwise look like a silent hang.
STATE="$(aws dynamodb get-item --region "$REGION" --table-name "${STACK}-tenants" \
  --key "{\"tenantId\":{\"S\":\"$TID\"}}" --query 'Item.state.S' --output text 2>/dev/null || true)"
if [ "$STATE" != "RUNNING" ]; then
  echo "Tenant is cold — starting MicroVM, first turn takes ~90s ..."
fi
PAYLOAD="$(python3 -c 'import json,sys; print(json.dumps({"_worker":{"tenantId":sys.argv[1],"update":{"message":{"chat":{"id":sys.argv[2]},"text":sys.argv[3]}}}}))' "$TID" "$SESS" "$MSG")"
OUT="$(mktemp)"
aws lambda invoke --region "$REGION" --function-name "$FN" \
  --cli-binary-format raw-in-base64-out --payload "$PAYLOAD" \
  --cli-read-timeout 300 "$OUT" >/dev/null
python3 -c 'import json,sys; d=json.load(open(sys.argv[1])); print("cold:",d.get("cold"),"| reply:",d.get("reply"))' "$OUT"
