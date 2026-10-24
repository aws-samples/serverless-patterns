#!/usr/bin/env bash
# Deploys a Lambda Web Function with an IamAuth endpoint, then puts a CloudFront
# distribution in front of it with an Origin Access Control that signs every
# origin request. The function's resource policy trusts only that distribution.
# Re-running the script is safe: every step checks for the resource first.
set -euo pipefail
cd "$(dirname "$0")"

export AWS_REGION="${AWS_REGION:-us-east-1}"
STACK="${STACK:-lambda-web-cloudfront-oac}"
CALLER_ARN=$(aws sts get-caller-identity --query Arn --output text)
PARTITION=$(echo "$CALLER_ARN" | cut -d: -f2)
ACCOUNT_ID=$(echo "$CALLER_ARN" | cut -d: -f5)

echo "1/6 Web Function with an IamAuth endpoint"
aws lambda-web deploy --name "$STACK" --code src --auth-type IamAuth --create
ORIGIN_DOMAIN=$(aws lambda-web get-web-function-endpoint --function-name "$STACK" --endpoint-name dev \
  --query domainName --output text)
FUNCTION_ARN="arn:${PARTITION}:lambda:${AWS_REGION}:${ACCOUNT_ID}:web-function/${STACK}"

echo "2/6 Cache policy (cache key: path, query string and the viewer's Authorization header)"
# The managed CachingOptimized policy leaves query strings and Authorization out
# of the cache key, and CloudFront forwards Authorization to the origin only when
# the cache policy includes it. This policy keeps CachingOptimized's TTLs and
# compression and adds both, so each signed-in viewer gets their own cache entries.
CACHE_POLICY_ID=$(aws cloudfront list-cache-policies --type custom \
  --query "CachePolicyList.Items[?CachePolicy.CachePolicyConfig.Name=='${STACK}'].CachePolicy.Id | [0]" --output text)
if [ -z "$CACHE_POLICY_ID" ] || [ "$CACHE_POLICY_ID" = "None" ]; then
  CACHE_POLICY_ID=$(aws cloudfront create-cache-policy --cache-policy-config "{
    \"Name\": \"${STACK}\",
    \"Comment\": \"Path, query string and Authorization header in the cache key\",
    \"MinTTL\": 1, \"DefaultTTL\": 86400, \"MaxTTL\": 31536000,
    \"ParametersInCacheKeyAndForwardedToOrigin\": {
      \"EnableAcceptEncodingGzip\": true,
      \"EnableAcceptEncodingBrotli\": true,
      \"HeadersConfig\": { \"HeaderBehavior\": \"whitelist\",
        \"Headers\": { \"Quantity\": 1, \"Items\": [\"Authorization\"] } },
      \"CookiesConfig\": { \"CookieBehavior\": \"none\" },
      \"QueryStringsConfig\": { \"QueryStringBehavior\": \"all\" }
    }
  }" --query CachePolicy.Id --output text)
fi

echo "3/6 Origin Access Control (type lambda, SigV4 on every request)"
OAC_ID=$(aws cloudfront list-origin-access-controls \
  --query "OriginAccessControlList.Items[?Name=='${STACK}'].Id | [0]" --output text)
if [ -z "$OAC_ID" ] || [ "$OAC_ID" = "None" ]; then
  OAC_ID=$(aws cloudfront create-origin-access-control --origin-access-control-config "{
    \"Name\": \"${STACK}\",
    \"Description\": \"Signs CloudFront requests to the ${STACK} web function\",
    \"SigningProtocol\": \"sigv4\",
    \"SigningBehavior\": \"always-amz-auth\",
    \"OriginAccessControlOriginType\": \"lambda\"
  }" --query OriginAccessControl.Id --output text)
fi

echo "4/6 CloudFront distribution"
DIST_ID=$(aws cloudfront list-distributions \
  --query "DistributionList.Items[?Comment=='${STACK}'].Id | [0]" --output text)
if [ -z "$DIST_ID" ] || [ "$DIST_ID" = "None" ]; then
  # The cache policy from step 2, plus the managed AllViewerExceptHostHeader
  # origin request policy (forward viewer headers and query strings; Lambda
  # routes on Host, so the Host header must be the origin domain).
  DIST_ID=$(aws cloudfront create-distribution --distribution-config "{
    \"CallerReference\": \"${STACK}-$(date +%s)\",
    \"Comment\": \"${STACK}\",
    \"Enabled\": true,
    \"PriceClass\": \"PriceClass_100\",
    \"Origins\": { \"Quantity\": 1, \"Items\": [{
      \"Id\": \"web-function\",
      \"DomainName\": \"${ORIGIN_DOMAIN}\",
      \"OriginAccessControlId\": \"${OAC_ID}\",
      \"CustomOriginConfig\": {
        \"HTTPPort\": 80, \"HTTPSPort\": 443,
        \"OriginProtocolPolicy\": \"https-only\",
        \"OriginSslProtocols\": { \"Quantity\": 1, \"Items\": [\"TLSv1.2\"] }
      }
    }]},
    \"DefaultCacheBehavior\": {
      \"TargetOriginId\": \"web-function\",
      \"ViewerProtocolPolicy\": \"redirect-to-https\",
      \"AllowedMethods\": { \"Quantity\": 7,
        \"Items\": [\"GET\",\"HEAD\",\"OPTIONS\",\"PUT\",\"POST\",\"PATCH\",\"DELETE\"],
        \"CachedMethods\": { \"Quantity\": 2, \"Items\": [\"GET\",\"HEAD\"] } },
      \"CachePolicyId\": \"${CACHE_POLICY_ID}\",
      \"OriginRequestPolicyId\": \"b689b0a8-53d0-40ab-baf2-68738e2966ac\",
      \"Compress\": true
    }
  }" --query Distribution.Id --output text)
fi
DIST_DOMAIN=$(aws cloudfront get-distribution --id "$DIST_ID" --query Distribution.DomainName --output text)

echo "5/6 Resource policy: only distribution ${DIST_ID} may invoke the endpoint"
aws lambda-web put-resource-policy --resource-arn "$FUNCTION_ARN" --policy "{
  \"Version\": \"2012-10-17\",
  \"Statement\": [{
    \"Effect\": \"Allow\",
    \"Principal\": { \"Service\": \"cloudfront.amazonaws.com\" },
    \"Action\": \"lambda:InvokeWebFunctionEndpoint\",
    \"Resource\": \"${FUNCTION_ARN}/endpoint/dev\",
    \"Condition\": { \"StringEquals\": {
      \"AWS:SourceArn\": \"arn:${PARTITION}:cloudfront::${ACCOUNT_ID}:distribution/${DIST_ID}\" } }
  }]
}" > /dev/null

echo "6/6 Waiting for the distribution to deploy (a few minutes)"
aws cloudfront wait distribution-deployed --id "$DIST_ID"

echo
echo "CloudFront: https://${DIST_DOMAIN}/whoami"
echo "Origin:     https://${ORIGIN_DOMAIN}/whoami  (returns 403 when called directly)"
