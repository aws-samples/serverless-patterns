#!/bin/bash

#!/bin/bash

# PingOne Configuration from environment variables
CLIENT_ID="${CLIENT_ID}"
CLIENT_SECRET="${CLIENT_SECRET}"
ENVIRONMENT_ID="${ENVIRONMENT_ID}"
REDIRECT_URI="${REDIRECT_URI:-http://localhost:3000/callback}"

# Validate required environment variables
if [ -z "$CLIENT_ID" ] || [ -z "$CLIENT_SECRET" ] || [ -z "$ENVIRONMENT_ID" ]; then
    echo "❌ Error: Missing required environment variables!"
    echo "Please set the following environment variables:"
    echo "- CLIENT_ID"
    echo "- CLIENT_SECRET" 
    echo "- ENVIRONMENT_ID"
    echo ""
    echo "Example:"
    echo "export CLIENT_ID=your-client-id"
    echo "export CLIENT_SECRET=your-client-secret"
    echo "export ENVIRONMENT_ID=your-environment-id"
    echo "export REDIRECT_URI=http://localhost:3000/callback  # optional"
    exit 1
fi

# Create base64 encoded credentials
CREDENTIALS=$(echo -n "${CLIENT_ID}:${CLIENT_SECRET}" | base64)

echo "🔐 PingOne Token via Curl"
echo "========================="
echo ""
echo "Your Configuration:"
echo "- Environment ID: ${ENVIRONMENT_ID}"
echo "- Client ID: ${CLIENT_ID}"
echo "- Redirect URI: ${REDIRECT_URI}"
echo ""

echo "Step 1: Get Authorization Code"
echo "============================="
echo "Open this URL in your browser:"
echo ""
echo "https://auth.pingone.com/${ENVIRONMENT_ID}/as/authorize?client_id=${CLIENT_ID}&response_type=code&redirect_uri=${REDIRECT_URI}&scope=openid%20profile%20email"
echo ""

if [ $# -eq 0 ]; then
    echo "Usage: $0 <authorization_code>"
    echo ""
    echo "After getting the code from the browser, run:"
    echo "$0 YOUR_AUTH_CODE"
    exit 1
fi

AUTH_CODE=$1

echo "Step 2: Exchange Code for Token"
echo "==============================="
echo "Using authorization code: ${AUTH_CODE:0:20}..."
echo ""

# Exchange code for token
RESPONSE=$(curl --silent --location --request POST "https://auth.pingone.com/${ENVIRONMENT_ID}/as/token" \
--header 'Content-Type: application/x-www-form-urlencoded' \
--header "Authorization: Basic ${CREDENTIALS}" \
--data-urlencode 'grant_type=authorization_code' \
--data-urlencode "code=${AUTH_CODE}" \
--data-urlencode "redirect_uri=${REDIRECT_URI}")

echo "Response:"
echo "${RESPONSE}" | python3 -m json.tool 2>/dev/null || echo "${RESPONSE}"
echo ""

# Extract access token
ACCESS_TOKEN=$(echo "${RESPONSE}" | python3 -c "import sys, json; data=json.load(sys.stdin); print(data.get('access_token', 'NOT_FOUND'))" 2>/dev/null)

if [ "${ACCESS_TOKEN}" != "NOT_FOUND" ] && [ "${ACCESS_TOKEN}" != "" ]; then
    echo "Success! Access Token Retrieved"
    echo "================================="
    echo ""
    echo "Access Token:"
    echo "${ACCESS_TOKEN}"
    echo ""
    echo "🧪 Test your API:"
    echo "curl -H 'Authorization: Bearer ${ACCESS_TOKEN}' https://<API_GATEWAY_ID>.execute-api.<REGION>.amazonaws.com/prod/user"
else
    echo "Failed to get access token"
    echo "Check the authorization code and try again"
fi
