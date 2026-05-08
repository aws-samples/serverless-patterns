# Amazon CloudFront with KeyValueStore

This pattern deploys a CloudFront distribution with KeyValueStore for edge configuration (redirects, feature flags, A/B testing) without origin round-trips.

Learn more about this pattern at Serverless Land Patterns: https://serverlessland.com/patterns/cloudfront-kvs-lambda-cdk

Important: this application uses various AWS services and there are costs associated with these services after the Free Tier usage - please see the [AWS Pricing page](https://aws.amazon.com/pricing/) for details.

## Requirements

* [AWS CLI](https://docs.aws.amazon.com/cli/latest/userguide/install-cliv2.html) installed and configured
* [Node.js 22+](https://nodejs.org/en/download/) installed
* [AWS CDK v2](https://docs.aws.amazon.com/cdk/v2/guide/getting-started.html) installed

## Architecture

```
┌──────────┐     ┌─────────────────────┐     ┌──────────────────┐
│  Client  │────▶│  CloudFront         │────▶│  S3 Origin       │
│          │     │  Function (JS 2.0)  │     │                  │
└──────────┘     └─────────────────────┘     └──────────────────┘
                         │
                         ▼
                  ┌──────────────────┐
                  │  KeyValueStore   │
                  │  (Edge Config)   │
                  └──────────────────┘
```

## How it works

1. CloudFront Function executes on every viewer request at the edge.
2. The function reads configuration from KeyValueStore (sub-millisecond, no origin call).
3. If a redirect rule exists for the URI, returns 302 immediately.
4. If A/B testing is enabled, adds a variant header to the request.

## Deployment

```bash
npm install
cdk deploy
```

## Testing

```bash
# Seed the KeyValueStore with redirect rules
node src/seed-kvs.js <KeyValueStoreArn>

# Test redirect (should return 302)
curl -I "https://<DistributionUrl>/old-page"

# Test normal path (passes through to origin)
curl -I "https://<DistributionUrl>/normal-page"
```

## Cleanup

```bash
cdk destroy
```
