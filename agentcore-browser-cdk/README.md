# Amazon Bedrock AgentCore Browser with AWS Lambda (CDK)

This pattern deploys an Amazon Bedrock AgentCore Browser resource with an AWS Lambda function that demonstrates starting browser sessions, navigating web pages, and extracting content for AI agents.

Learn more about this pattern at Serverless Land Patterns: https://serverlessland.com/patterns/agentcore-browser-cdk

Important: this application uses various AWS services and there are costs associated with these services after the Free Tier usage - please see the [AWS Pricing page](https://aws.amazon.com/pricing/) for details.

## Requirements

* [Create an AWS account](https://portal.aws.amazon.com/gp/aws/developer/registration/index.html) if you do not already have one and log in.
* [AWS CLI](https://docs.aws.amazon.com/cli/latest/userguide/install-cliv2.html) installed and configured
* [Node.js 20+](https://nodejs.org/en/download/) installed
* [AWS CDK v2](https://docs.aws.amazon.com/cdk/v2/guide/getting_started.html) installed (`npm install -g aws-cdk`)
* CDK bootstrapped in your account/region (`cdk bootstrap`)

## Deployment Instructions

1. Clone the repository and navigate to the pattern directory:
    ```bash
    cd agentcore-browser-cdk
    ```

2. Install dependencies:
    ```bash
    npm install
    ```

3. Build and deploy:
    ```bash
    npx cdk deploy
    ```

## How it works

Amazon Bedrock AgentCore Browser provides managed headless browser infrastructure for AI agents:

- **Session management**: Start isolated browser sessions with public network access
- **Navigation**: Navigate to any public URL and interact with page elements
- **Content extraction**: Extract text, structured data, or screenshots from web pages
- **Automatic cleanup**: Sessions are isolated and cleaned up after use

The AWS Lambda function demonstrates:
1. **browse**: Starts a session, navigates to a URL, extracts content, and stops the session
2. **list_sessions**: Lists active browser sessions

## Testing

Browse a web page:
```bash
aws lambda invoke --function-name FUNCTION_NAME \
  --payload '{"action": "browse", "url": "https://aws.amazon.com/bedrock/agentcore/"}' \
  --cli-binary-format raw-in-base64-out output.json && cat output.json
```

List active sessions:
```bash
aws lambda invoke --function-name FUNCTION_NAME \
  --payload '{"action": "list_sessions"}' \
  --cli-binary-format raw-in-base64-out output.json && cat output.json
```

## Cleanup

```bash
npx cdk destroy
```

---

Copyright 2026 Amazon.com, Inc. or its affiliates. All Rights Reserved.

SPDX-License-Identifier: MIT-0
