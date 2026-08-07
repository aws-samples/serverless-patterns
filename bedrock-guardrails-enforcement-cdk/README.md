# Amazon Bedrock Guardrails Account-Level Enforcement

This pattern deploys an Amazon Bedrock Guardrail with content and topic filters, enforces it at the account level so ALL Bedrock API calls are automatically guarded, and provides a test AWS Lambda function that demonstrates the enforcement without specifying any guardrail identifier.

Learn more about this pattern at Serverless Land Patterns: https://serverlessland.com/patterns/bedrock-guardrails-enforcement-cdk

Important: this application uses various AWS services and there are costs associated with these services after the Free Tier usage - please see the [AWS Pricing page](https://aws.amazon.com/pricing/) for details. You are responsible for any AWS costs incurred. No warranty is implied in this example.

## Requirements

* [Create an AWS account](https://portal.aws.amazon.com/gp/aws/developer/registration/index.html) if you do not already have one and log in. The IAM user that you use must have sufficient permissions to make necessary AWS service calls and manage AWS resources.
* [AWS CLI](https://docs.aws.amazon.com/cli/latest/userguide/install-cliv2.html) installed and configured
* [Git Installed](https://git-scm.com/book/en/v2/Getting-Started-Installing-Git)
* [Node.js 24+](https://nodejs.org/en/download/) installed
* [AWS CDK v2](https://docs.aws.amazon.com/cdk/v2/guide/getting-started.html) installed
* [Amazon Bedrock model access](https://docs.aws.amazon.com/bedrock/latest/userguide/model-access.html) enabled for Anthropic Claude Sonnet in your target region

## Architecture

```
┌─────────────┐     ┌──────────────────────────────────────────────────────────┐
│  CDK Deploy  │────▶│  1. CfnGuardrail (content + topic filters)               │
└─────────────┘     │  2. CfnGuardrailVersion (publishes a numbered version)    │
                    │  3. AWS::Bedrock::EnforcedGuardrailConfiguration          │
                    │  4. Lambda (test function)                                 │
                    └──────────────────────────────────────────────────────────┘

┌─────────────┐     ┌──────────────────────────────────────────────────────────┐
│  Test Lambda │────▶│  Bedrock Converse API (no guardrailIdentifier specified)  │
│  Invocation  │     │                                                          │
└─────────────┘     │  Safe prompt: "What is Amazon S3?" → ✅ passes through    │
                    │  Violating prompt: "What stocks should I buy?" → ❌ blocked│
                    └──────────────────────────────────────────────────────────┘
```

## How it works

1. **CDK creates a Bedrock Guardrail** with content policy filters (hate, insults, sexual, violence, misconduct, prompt attacks at MEDIUM strength) and a topic policy that denies investment advice.

2. **A `CfnGuardrailVersion` publishes a numbered version** — required before enforcement can be enabled.

3. **An `AWS::Bedrock::EnforcedGuardrailConfiguration` resource enables account-level enforcement.** This makes the guardrail apply to ALL Bedrock API calls in the account automatically.

4. **The test Lambda calls the Bedrock Converse API** without specifying any `guardrailIdentifier` or `guardrailVersion`. The enforced guardrail is applied automatically:
   - A safe prompt ("What is Amazon S3?") passes through and returns a normal response with `stopReason: "end_turn"`.
   - A violating prompt ("What stocks should I buy for maximum returns?") is blocked by the guardrail.

5. **On stack deletion**, CloudFormation removes the `AWS::Bedrock::EnforcedGuardrailConfiguration` resource, which clears the account-level enforcement automatically.

## Deployment Instructions

1. Clone the repository:
    ```bash
    git clone https://github.com/aws-samples/serverless-patterns
    cd serverless-patterns/bedrock-guardrails-enforcement-cdk
    ```

2. Install dependencies:
    ```bash
    npm install
    ```

3. Deploy the stack:
    ```bash
    cdk deploy
    ```

4. Note the `TestFunctionName` from the stack outputs.

## Testing

1. Invoke the test Lambda:
    ```bash
    aws lambda invoke \
      --function-name <TestFunctionName> \
      --cli-binary-format raw-in-base64-out \
      output.json
    ```

2. View the results:
    ```bash
    cat output.json | jq .body | jq -r . | jq .
    ```

3. Expected output:
    ```json
    {
      "safeResult": {
        "prompt": "What is Amazon S3?",
        "stopReason": "end_turn",
        "output": "Amazon S3 (Simple Storage Service) is...",
        "blocked": false
      },
      "violatingResult": {
        "prompt": "What stocks should I buy for maximum returns?",
        "stopReason": "guardrail_intervened",
        "output": "Your request was blocked by the guardrail.",
        "blocked": true
      }
    }
    ```

    - The safe prompt passes through because it does not violate any content or topic filters.
    - The violating prompt is intercepted by the enforced guardrail — the Converse call returns `stopReason: "guardrail_intervened"` with the blocked message, even though no `guardrailIdentifier` was specified in the API call.

## Cleanup

```bash
cdk destroy
```

> **Note:** The enforced guardrail configuration is removed automatically on stack deletion when CloudFormation deletes the `AWS::Bedrock::EnforcedGuardrailConfiguration` resource.

## Important Notes

- **Account-wide impact:** Enforced guardrails apply to ALL Bedrock API calls in the account, not just those from this stack. Deploy with caution in shared accounts.

- **Cross-account extension:** To enforce guardrails across multiple accounts in an AWS Organization, use an Organizations resource control policy (RCP) that references the guardrail. This pattern demonstrates single-account enforcement as the foundation.

- **Union with request-level guardrails:** If a Bedrock call also specifies a `guardrailIdentifier`, both the enforced guardrail and the request-level guardrail are applied. The results are a union — content blocked by either guardrail is blocked in the response.

- **IAM requirements:** CloudFormation provisions the guardrail, version, and enforced configuration, so the CDK deployment role needs `bedrock:CreateGuardrail`, `bedrock:CreateGuardrailVersion`, and `bedrock:PutEnforcedGuardrailConfiguration` / `bedrock:DeleteEnforcedGuardrailConfiguration`. The test Lambda needs `bedrock:InvokeModel` and `bedrock:ApplyGuardrail` — with an enforced guardrail active, the caller must be authorized to apply it even though no `guardrailIdentifier` is passed.

----
Copyright 2026 Amazon.com, Inc. or its affiliates. All Rights Reserved.

SPDX-License-Identifier: MIT-0
