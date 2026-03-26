# CloudFront to Amazon Bedrock AgentCore Runtime

This pattern demonstrates how to proxy requests to Amazon Bedrock AgentCore Runtime through CloudFront with OAuth 2.0 authentication, supporting A2A, HTTP, and MCP protocols of the [AgentCore Runtime service contract](https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/runtime-service-contract.html).

Benefits of using CloudFront in front of AgentCore Runtime:
- Global edge caching and low-latency access
- DDoS protection via AWS Shield Standard (included)
- Optional AWS WAF integration for IP rate limiting, geo-blocking, and bot protection
- Custom domain support with SSL/TLS certificates
- Request/response transformation via Amazon CloudFront Functions
- Centralized access logging and monitoring

Learn more about this pattern at [Serverless Land Patterns](https://serverlessland.com/patterns/cloudfront-agentcore-runtime-cdk)

Important: this application uses various AWS services and there are costs associated with these services after the Free Tier usage - please see the AWS Pricing page for details. You are responsible for any AWS costs incurred. No warranty is implied in this example.

## Pre-requisites

- [Create an AWS account](https://portal.aws.amazon.com/gp/aws/developer/registration/index.html) if you do not already have one and log in.
- [AWS CLI](https://docs.aws.amazon.com/cli/latest/userguide/install-cliv2.html) installed and configured
- [Git Installed](https://git-scm.com/book/en/v2/Getting-Started-Installing-Git)
- [AWS CDK](https://docs.aws.amazon.com/cdk/latest/guide/cli.html) installed and configured
- [Docker](https://docs.docker.com/get-docker/) installed and running
- [Python 3.12](https://www.python.org/downloads/) installed

## Deployment Instructions

1. Clone the GitHub repository:

    ```shell
    git clone https://github.com/aws-samples/serverless-patterns
    cd serverless-patterns/cloudfront-agentcore-runtime-cdk
    ```

2. Create and activate a Python virtual environment:

    ```shell
    python3 -m venv .venv
    source .venv/bin/activate
    ```

3. Install the required dependencies:

    ```shell
    pip3 install -r requirements.txt
    ```

4. Deploy the stacks:

    ```shell
    cdk deploy --all
    ```

5. After `cdk deploy --all` completes, verify the deployment:
    1. Check the CDK outputs for `UserPoolId`, `UserPoolClientId`, and `DistributionUrl`.
    2. Verify the CloudFront distribution is deployed:
        ```shell
        aws cloudfront list-distributions --query "DistributionList.Items[*].[Id,Status,DomainName]" --output table  --no-cli-pager 
        ```
    3. Confirm the distribution status shows "Deployed".

## How it works

This pattern creates:

1. **Amazon Bedrock AgentCore Runtimes** - Three agents supporting A2A, HTTP, and MCP protocols
2. **Amazon Cognito User Pool** for JWT authentication
3. **CloudFront Distribution** that proxies requests to AgentCore Runtimes:
   - `/a2a/*` - A2A protocol agent
   - `/rest/*` - HTTP protocol agent
   - `/mcp/*` - MCP protocol agent

**Architecture Flow:**
1. Client sends request to CloudFront with Bearer token
2. CloudFront Function strips path prefix (/a2a, /rest, /mcp)
3. Request is forwarded to the appropriate AgentCore Runtime
4. AgentCore validates JWT token
5. Response is returned through the same path

## Testing

1. Get Pool ID, Client ID, and CloudFront URL from the CDK outputs after running the `cdk deploy` command. Look for `UserPoolId`, `UserPoolClientId`, and `DistributionUrl` in the outputs.

2. Get a bearer token:

    ```shell
    cd test
    ./get_token.sh
    ```

    Example output:
    ```
    Cognito Token Generator
    Get Pool ID and Client ID from CDK stack outputs

    Pool ID []: us-west-2_xxxxxx
    Client ID []: xxxxxxxxxxxxxxxxxx
    Username []: testuser
    Password: 
    Region [us-west-2]: 
    export BEARER_TOKEN="eyJraWQiOi..."
    ```

3. Set environment variables (get DistributionUrl from AgentcoreCloudFrontStack outputs):

    ```shell
    export CF_URL="https://<distribution-id>.cloudfront.net"
    export BEARER_TOKEN="<token-from-step-2>"
    ```

4. Test A2A protocol:

    ```shell
    python test_a2a.py
    ```

    You can also use tools like [A2A Inspector](https://a2a-inspector.vercel.app/) with the agent card URL:
    ```
    https://<distribution-id>.cloudfront.net/a2a/
    ```

5. Test HTTP protocol:

    ```shell
    python test_http.py
    ```

6. Test MCP protocol (requires `mcp` package):

    ```shell
    python test_mcp.py
    ```

## Optional: Update A2A Agent Card URL

By default, the A2A agent card advertises the direct AgentCore Runtime endpoint, which bypasses CloudFront and its benefits (edge caching, DDoS protection, WAF integration). If you want A2A clients to discover your agent via CloudFront instead of the direct AgentCore Runtime URL, run this script after deployment. 

```shell
cd ..
./scripts/update_a2a_cloudfront_url.sh
```

This configures the A2A agent to advertise the CloudFront URL in its agent card (`/a2a/.well-known/agent-card.json`). This is required when using A2A-compatible clients that rely on the agent card for endpoint discovery.

You can verify the agent card is accessible via CloudFront using tools like [A2A Inspector](https://github.com/a2aproject/a2a-inspector) with the agent card URL:
```
https://<distribution-id>.cloudfront.net/a2a/.well-known/agent-card.json
```
Set the Bearer token in the request header for authentication.

## Cleanup

Delete the stacks:

```bash
cdk destroy --all
```

---

Copyright 2026 Amazon.com, Inc. or its affiliates. All Rights Reserved.

SPDX-License-Identifier: MIT-0
