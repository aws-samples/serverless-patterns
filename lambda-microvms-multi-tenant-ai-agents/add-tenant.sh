#!/usr/bin/env bash
# Register a tenant. For Telegram push, also pass a bot token + secret and this
# script sets the webhook to <api>/tg/<tenantId>.
# Usage: ./add-tenant.sh REGION STACK TENANT_ID [BOT_TOKEN] [WEBHOOK_SECRET]
#   e.g. ./add-tenant.sh us-east-1 openclaw-mt tenant1
#        ./add-tenant.sh us-east-1 openclaw-mt tenant3 <BOT_TOKEN> <WEBHOOK_SECRET>
# Region is first (see deploy.sh) so switching region reads consistently across scripts.
set -euo pipefail
if [ $# -lt 3 ]; then
  echo "usage: $0 REGION STACK TENANT_ID [BOT_TOKEN] [WEBHOOK_SECRET]" >&2; exit 1
fi
REGION="$1"; STACK="$2"; TID="$3"
BOT="${4:-}"; SECRET="${5:-}"
# Fail closed: a Telegram-bound tenant MUST carry a webhook secret. Without one the
# /tg/<tenantId> webhook would accept unauthenticated POSTs (anyone who learns the URL
# could drive billable agent turns). The router enforces the matching check.
if [ -n "$BOT" ] && [ -z "$SECRET" ]; then
  echo "ERROR: a WEBHOOK_SECRET is required when a BOT_TOKEN is supplied." >&2
  echo "       (pick any hard-to-guess string; Telegram sends it back on every webhook call.)" >&2
  exit 1
fi
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
