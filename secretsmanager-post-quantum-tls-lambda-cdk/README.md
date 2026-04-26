# AWS Secrets Manager with Post-Quantum TLS and Lambda

This pattern deploys a Lambda function that retrieves secrets from AWS Secrets Manager over hybrid post-quantum TLS connections using ML-KEM (X25519MLKEM768) key exchange.

Learn more about this pattern at Serverless Land Patterns: https://serverlessland.com/patterns/secretsmanager-post-quantum-tls-lambda-cdk

Important: this application uses various AWS services and there are costs associated with these services after the Free Tier usage - please see the [AWS Pricing page](https://aws.amazon.com/pricing/) for details. You are responsible for any AWS costs incurred. No warranty is implied in this example.

## Requirements

* [Create an AWS account](https://portal.aws.amazon.com/gp/aws/developer/registration/index.html) if you do not already have one and log in.
* [AWS CLI](https://docs.aws.amazon.com/cli/latest/userguide/install-cliv2.html) installed and configured
* [Node and NPM](https://nodejs.org/en/download/) installed
* [AWS CDK](https://docs.aws.amazon.com/cdk/latest/guide/cli.html) installed

## How it works

AWS Secrets Manager now supports hybrid post-quantum key exchange using ML-KEM (April 2026). This protects secrets against "harvest now, decrypt later" (HNDL) attacks where adversaries record encrypted traffic today to decrypt with future quantum computers.

- **Automatic protection**: The AWS SDK in Lambda runtime automatically negotiates ML-KEM hybrid key exchange — no code changes needed
- **Hybrid approach**: Combines classical X25519 with post-quantum ML-KEM-768, so security is maintained even if one algorithm is broken
- **Verification**: CloudTrail logs show `X25519MLKEM768` in the `tlsDetails.keyExchangeAlgorithm` field

```
Lambda → TLS (X25519MLKEM768 hybrid PQ key exchange) → Secrets Manager
                                                          └── GetSecretValue
```

## Deployment Instructions

1. Clone the repository and navigate to the pattern directory:
    ```bash
    git clone https://github.com/aws-samples/serverless-patterns
    cd serverless-patterns/secretsmanager-post-quantum-tls-lambda-cdk
    ```

2. Install dependencies:
    ```bash
    npm install
    ```

3. Deploy the stack:
    ```bash
    cdk deploy
    ```

## Testing

```bash
aws lambda invoke \
  --function-name <FunctionName> \
  output.json && cat output.json | python3 -m json.tool
```

## Verifying Post-Quantum TLS

Check CloudTrail for the key exchange algorithm:

```bash
aws cloudtrail lookup-events \
  --lookup-attributes AttributeKey=EventName,AttributeValue=GetSecretValue \
  --max-results 5 \
  --query 'Events[].{Time:EventTime,TLS:CloudTrailEvent}' \
  --output table
```

Look for `"keyExchangeAlgorithm": "X25519MLKEM768"` in the `tlsDetails` field.

## Cleanup

```bash
cdk destroy
```

----
Copyright 2025 Amazon.com, Inc. or its affiliates. All Rights Reserved.

SPDX-License-Identifier: MIT-0
