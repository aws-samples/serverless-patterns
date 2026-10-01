# AWS WAF Protection for Amazon Bedrock AgentCore Gateway with Lambda Tools and Amazon Bedrock (CDK)

This pattern deploys an AWS WAF WebACL protecting an Amazon Bedrock AgentCore Gateway that routes MCP tool calls to an AWS Lambda function invoking Amazon Bedrock for AI inference. The WAF configuration includes rate limiting, AWS Managed Rules, Bot Control, IP allowlisting, and CloudWatch logging.

Learn more about this pattern at Serverless Land Patterns: https://serverlessland.com/patterns/waf-agentcore-gateway-bedrock-cdk

Important: this application uses various AWS services and there are costs associated with these services after the Free Tier usage - please see the [AWS Pricing page](https://aws.amazon.com/pricing/) for details. You are responsible for any AWS costs incurred.

## Requirements

- [Create an AWS account](https://portal.aws.amazon.com/gp/aws/developer/registration/index.html) if you do not already have one and log in. The IAM user that you use must have sufficient permissions to make necessary AWS service calls and manage AWS resources.
- [AWS CLI](https://docs.aws.amazon.com/cli/latest/userguide/install-cliv2.html) installed and configured
- [Git Installed](https://git-scm.com/book/en/v2/Getting-Started-Installing-Git)
- [Node.js 22+](https://nodejs.org/en/download/) installed
- [AWS CDK v2](https://docs.aws.amazon.com/cdk/v2/guide/getting_started.html) installed (`npm install -g aws-cdk`)
- [AWS CDK bootstrapped](https://docs.aws.amazon.com/cdk/v2/guide/bootstrapping.html) in your account/region

## Deployment Instructions

1. Create a new directory, navigate to that directory in a terminal and clone the GitHub repository:
   ```bash
   git clone https://github.com/aws-samples/serverless-patterns
   cd serverless-patterns/waf-agentcore-gateway-bedrock-cdk/cdk
   ```

2. Install dependencies:
   ```bash
   npm install
   ```

3. Deploy the stack:
   ```bash
   cdk deploy
   ```

## Architecture

This pattern creates the following resources:

1. **AWS WAF WebACL** — A regional WebACL with five rules:
   - **AllowTrustedAgentIPs** (Priority 0): Allows traffic from a configurable IP set (internal agents/services)
   - **RateLimitPerIP** (Priority 1): Blocks IPs exceeding 100 requests per 5 minutes with a JSON 429 response
   - **AWSManagedRulesCommonRuleSet** (Priority 2): Protects against common web exploits (XSS, SQLi, etc.)
   - **AWSManagedRulesKnownBadInputsRuleSet** (Priority 3): Blocks requests with known malicious patterns
   - **AWSManagedRulesBotControlRuleSet** (Priority 4): Detects and labels bot traffic (count mode)

2. **Amazon Bedrock AgentCore Gateway** — An MCP-protocol gateway that routes tool invocations to registered targets

3. **AWS Lambda Function** — A Node.js 22 tool handler that invokes Amazon Bedrock Claude Sonnet 4 for AI inference

4. **AWS WAF Logging** — Full request logs delivered to Amazon CloudWatch Logs for security monitoring and incident response

5. **AWS WAF IP Set** — A configurable set of trusted CIDR blocks that bypass rate limiting

## How it works

When an agent or client sends a tool invocation request to the AgentCore Gateway:

1. AWS WAF evaluates the request against the WebACL rules in priority order
2. Trusted IPs (from the IP set) are immediately allowed through
3. Other requests are checked for rate limiting (100 req/5 min per IP)
4. Requests passing rate limits are evaluated against AWS Managed Rules for malicious content
5. Bot traffic is detected and labeled (count mode allows but flags)
6. Clean requests reach the Amazon Bedrock AgentCore Gateway, which routes to the AWS Lambda tool target
7. The Lambda function invokes Amazon Bedrock and returns the AI-generated response
8. All WAF decisions are logged to CloudWatch for monitoring

## Testing

After deployment, retrieve the Gateway ID from stack outputs:

```bash
aws cloudformation describe-stacks \
  --stack-name WafAgentcoreGatewayBedrockStack \
  --query 'Stacks[0].Outputs'
```

Invoke the AWS Lambda tool directly to verify Amazon Bedrock connectivity:

```bash
aws lambda invoke \
  --function-name $(aws cloudformation describe-stacks \
    --stack-name WafAgentcoreGatewayBedrockStack \
    --query 'Stacks[0].Outputs[?OutputKey==`ToolFunctionArn`].OutputValue' \
    --output text) \
  --payload '{"prompt": "What is AWS WAF and how does it protect APIs?"}' \
  --cli-binary-format raw-in-base64-out \
  /tmp/response.json && cat /tmp/response.json | python3 -m json.tool
```

Check WAF metrics in CloudWatch:

```bash
aws cloudwatch get-metric-statistics \
  --namespace AWS/WAFV2 \
  --metric-name AllowedRequests \
  --dimensions Name=WebACL,Value=agentcore-gateway-protection Name=Region,Value=us-east-1 Name=Rule,Value=ALL \
  --start-time $(date -u -d '1 hour ago' +%Y-%m-%dT%H:%M:%S) \
  --end-time $(date -u +%Y-%m-%dT%H:%M:%S) \
  --period 300 \
  --statistics Sum
```

## Cleanup

Delete the stack to remove all resources:

```bash
cdk destroy
```

**Warning:** This will delete all resources including the AWS WAF WebACL, Amazon Bedrock AgentCore Gateway, AWS Lambda function, and Amazon CloudWatch Log Group. AWS WAF logs stored in Amazon CloudWatch will also be deleted (retention is set to 7 days with DESTROY removal policy).

## Customization

- **Rate limit**: Modify the `limit` value in the `RateLimitPerIP` rule (minimum 100)
- **Trusted IPs**: Update the `addresses` array in the `TrustedAgentIPs` IP set with your CIDR blocks
- **Bot Control**: Change from `count` to `block` action on the Bot Control rule for stricter enforcement
- **Model**: Update `MODEL_ID` environment variable to use a different Amazon Bedrock foundation model

---

Copyright 2026 Amazon.com, Inc. or its affiliates. All Rights Reserved.

SPDX-License-Identifier: MIT-0
