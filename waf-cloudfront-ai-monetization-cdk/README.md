# AWS WAF AI Traffic Monetization with Amazon CloudFront (CDK)

This pattern deploys an Amazon CloudFront distribution protected by AWS WAF with AI traffic monetization enabled. AI bots that access your content are automatically charged via the x402 payment protocol using USDC stablecoins.

Learn more about this pattern at Serverless Land Patterns: https://serverlessland.com/patterns/waf-cloudfront-ai-monetization-cdk

Important: this application uses various AWS services and there are costs associated with these services after the Free Tier usage - please see the [AWS Pricing page](https://aws.amazon.com/pricing/) for details. You are responsible for any AWS costs incurred. No warranty is implied in this example.

## Requirements

* [Create an AWS account](https://portal.aws.amazon.com/gp/aws/developer/registration/index.html) if you do not already have one and log in. The IAM user that you use must have sufficient permissions to make necessary AWS service calls and manage AWS resources.
* [AWS CLI](https://docs.aws.amazon.com/cli/latest/userguide/install-cliv2.html) installed and configured
* [Git Installed](https://git-scm.com/book/en/v2/Getting-Started-Installing-Git)
* [Node.js 20+](https://nodejs.org/en/download/) installed
* [AWS CDK v2](https://docs.aws.amazon.com/cdk/v2/guide/getting_started.html) installed and bootstrapped

## Deployment Instructions

1. Create a new directory, navigate to that directory in a terminal and clone the GitHub repository:
    ```
    git clone https://github.com/aws-samples/serverless-patterns
    ```
2. Change directory to the pattern directory:
    ```
    cd serverless-patterns/waf-cloudfront-ai-monetization-cdk
    ```
3. Install dependencies:
    ```
    npm install
    ```
4. Deploy the stack (must deploy to us-east-1 for Amazon CloudFront):
    ```
    cdk deploy
    ```

## How it works

This pattern creates:

1. **Amazon S3 bucket** — stores your content (HTML, APIs, data) that AI bots want to access.
2. **Amazon CloudFront distribution** — serves content globally with HTTPS.
3. **AWS WAF WebACL** (CLOUDFRONT scope) with:
   - **Bot Control managed rule group** — uses machine learning to classify bots into categories (AI, scraper, crawler, etc.)
   - **MonetizeAction rule** — matches bots labeled `awswaf:managed:aws:bot-control:bot:category:ai` and returns HTTP 402 with an x402 payment manifest
   - **MonetizationConfig** — configures the x402 payment network (Base Sepolia testnet by default), wallet address, and USDC pricing

### Flow

```
AI Bot Request
    │
    ▼
CloudFront Distribution
    │
    ▼
AWS WAF Bot Control (classifies bot category)
    │
    ├── Human browser → Allow (200 OK)
    │
    └── AI Bot (GPTBot, ClaudeBot, etc.)
            │
            ▼
        MonetizeAction → HTTP 402 Payment Required
            │                (x402 price manifest)
            │
            ├── Bot pays USDC → Request replayed → 200 OK
            │
            └── Bot doesn't pay → Blocked
```

### Test Mode

The pattern deploys in **TEST mode** using Base Sepolia testnet. No real money is involved. To switch to production:

1. Replace the wallet address with your production USDC wallet (Base or Solana)
2. Change `CurrencyMode` from `TEST` to `LIVE`
3. Change `Chain` from `BASE_SEPOLIA` to `BASE` (or `SOLANA`)

## Testing

1. Upload sample content:
    ```bash
    echo '<h1>Premium Content</h1>' > index.html
    aws s3 cp index.html s3://$(aws cloudformation describe-stacks \
      --stack-name WafCloudfrontAiMonetizationStack \
      --query 'Stacks[0].Outputs[?OutputKey==`ContentBucketName`].OutputValue' \
      --output text)/index.html --content-type text/html
    ```

2. Test with a normal browser (should return 200 OK):
    ```bash
    curl -s -o /dev/null -w "%{http_code}" \
      https://$(aws cloudformation describe-stacks \
        --stack-name WafCloudfrontAiMonetizationStack \
        --query 'Stacks[0].Outputs[?OutputKey==`DistributionDomainName`].OutputValue' \
        --output text)/index.html
    ```

3. Test with an AI bot User-Agent (should return 402 Payment Required):
    ```bash
    curl -s -D - -H 'User-Agent: GPTBot/1.0' \
      https://$(aws cloudformation describe-stacks \
        --stack-name WafCloudfrontAiMonetizationStack \
        --query 'Stacks[0].Outputs[?OutputKey==`DistributionDomainName`].OutputValue' \
        --output text)/index.html
    ```
    The response headers will include the x402 payment manifest with pricing details.

## Cleanup

```bash
cdk destroy
```

**Warning**: The Amazon S3 bucket has a DESTROY removal policy. All objects in the bucket will be permanently deleted when the stack is destroyed.

----
Copyright 2026 Amazon.com, Inc. or its affiliates. All Rights Reserved.

SPDX-License-Identifier: MIT-0
