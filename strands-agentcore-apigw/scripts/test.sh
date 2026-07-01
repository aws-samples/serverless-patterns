#!/usr/bin/env bash
set -e
CLIENT_ID="4u8ka9e7dbmekuunrr9ikjna2c"
FUNCTION_NAME="dev-weather-agent"
REGION="us-east-1"
USERNAME="testuser"
PASSWORD="TestPass123!"

echo "Getting ID token..."
ID_TOKEN=$(aws cognito-idp initiate-auth \
  --auth-flow USER_PASSWORD_AUTH \
  --client-id "${CLIENT_ID}" \
  --auth-parameters USERNAME="${USERNAME}",PASSWORD="${PASSWORD}" \
  --region "${REGION}" \
  --query 'AuthenticationResult.IdToken' --output text)

if [[ -z "${ID_TOKEN}" || "${ID_TOKEN}" == "None" ]]; then
  echo "ERROR: Failed to get ID token"
  exit 1
fi
echo "Token obtained (${#ID_TOKEN} chars)"

PROMPT="${1:-What is the weather in London, UK?}"
echo "Invoking agent with: ${PROMPT}"

PAYLOAD=$(python3 -c "
import json
inner = json.dumps({'prompt': '${PROMPT}'})
outer = json.dumps({'body': inner, 'headers': {'Authorization': 'Bearer ${ID_TOKEN}'}})
print(outer)
")

aws lambda invoke \
  --function-name "${FUNCTION_NAME}" \
  --region "${REGION}" \
  --cli-binary-format raw-in-base64-out \
  --payload "${PAYLOAD}" \
  /tmp/response.json

echo ""
echo "=== Response ==="
python3 -c "
import json
with open('/tmp/response.json') as f:
    resp = json.load(f)
if 'body' in resp:
    body = json.loads(resp['body'])
    if 'response' in body:
        print(body['response'])
    elif 'error' in body:
        print(f\"ERROR: {body['error']}\")
    else:
        print(json.dumps(body, indent=2))
else:
    print(json.dumps(resp, indent=2))
"
