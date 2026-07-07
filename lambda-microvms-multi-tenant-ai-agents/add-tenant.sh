#!/usr/bin/env bash
# Register a tenant. For Telegram push, also pass a bot token + secret and this
# script sets the webhook to <api>/tg/<tenantId>.
# Usage: ./add-tenant.sh STACK REGION TENANT_ID [BOT_TOKEN] [WEBHOOK_SECRET]
set -euo pipefail
if [ $# -lt 3 ]; then
  echo "usage: $0 STACK REGION TENANT_ID [BOT_TOKEN] [WEBHOOK_SECRET]" >&2; exit 1
fi
STACK="$1"; REGION="$2"; TID="$3"
BOT="${4:-}"; SECRET="${5:-}"
API="$(aws cloudformation describe-stacks --region "$REGION" --stack-name "$STACK" \
  --query "Stacks[0].Outputs[?OutputKey=='ApiEndpoint'].OutputValue" --output text)"

ITEM="{\"tenantId\":{\"S\":\"$TID\"},\"state\":{\"S\":\"COLD\"},\"generation\":{\"N\":\"0\"}"
[ -n "$BOT" ]    && ITEM="$ITEM,\"botToken\":{\"S\":\"$BOT\"}"
[ -n "$SECRET" ] && ITEM="$ITEM,\"webhookSecret\":{\"S\":\"$SECRET\"}"
ITEM="$ITEM}"
aws dynamodb put-item --region "$REGION" --table-name "${STACK}-tenants" --item "$ITEM"
echo "registered tenant '$TID' (state=COLD)"

if [ -n "$BOT" ] && [ -n "$SECRET" ]; then
  # Parse Telegram's response instead of dumping raw JSON: a bad bot token must
  # fail loudly (non-zero), not scroll past as {"ok":false,...}.
  curl -s "https://api.telegram.org/bot${BOT}/setWebhook" \
    --data-urlencode "url=${API}/tg/${TID}" \
    --data-urlencode "secret_token=${SECRET}" \
    --data-urlencode "drop_pending_updates=true" | python3 -c '
import json, sys
d = json.load(sys.stdin)
if d.get("ok"):
    print("setWebhook: ok")
else:
    print("ERROR: setWebhook failed:", d.get("description", d), file=sys.stderr)
    print("       Check the bot token (from @BotFather) and try again.", file=sys.stderr)
    sys.exit(1)
'
  echo "webhook -> ${API}/tg/${TID}"
fi
