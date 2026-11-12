# Per-tool authorization on Amazon Bedrock AgentCore Gateway with Cedar policies

This pattern puts an Amazon Bedrock AgentCore Gateway behind a policy engine from Policy in Amazon Bedrock AgentCore, in `ENFORCE` mode. Two Cedar policies decide which tool of an AWS Lambda target a caller may use, based on the `scope` claim of an Amazon Cognito access token (OAuth 2.0 client credentials). One token is allowed `lookup_order` and denied `cancel_order`; the other token is the reverse. Compared with a gateway that only routes to a Lambda target, the policy engine adds the authorization decision, taken inside the gateway before the function is invoked. Compared with evaluating Cedar through Amazon Verified Permissions in a Lambda function, no authorization code of yours runs in the request path.

Learn more about this pattern at Serverless Land Patterns: https://serverlessland.com/patterns/agentcore-gateway-cedar-typescript-cdk

Important: this application uses various AWS services and there are costs associated with these services after the Free Tier usage - please see the [AWS Pricing page](https://aws.amazon.com/pricing/) for details. You are responsible for any AWS costs incurred. No warranty is implied in this example.

## Requirements

* [Create an AWS account](https://portal.aws.amazon.com/gp/aws/developer/registration/index.html) if you do not already have one and log in. The IAM user that you use must have sufficient permissions to make necessary AWS service calls and manage AWS resources.
* [AWS CLI](https://docs.aws.amazon.com/cli/latest/userguide/install-cliv2.html) installed and configured
* [Git Installed](https://git-scm.com/book/en/v2/Getting-Started-Installing-Git)
* [Node.js](https://nodejs.org/en/download/) 22 or later and npm installed
* [AWS Cloud Development Kit](https://docs.aws.amazon.com/cdk/v2/guide/getting-started.html) (AWS CDK) v2, and the target account and Region [bootstrapped](https://docs.aws.amazon.com/cdk/v2/guide/bootstrapping.html) (`npx cdk bootstrap` once per account and Region)
* `curl` and `jq` 1.6 or later for the Testing section
* AWS CloudFormation creates the policies with the CDK deployment role. Policy creation [calls the gateway to validate the actions](https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/policy-permissions.html), so a custom CloudFormation execution role needs `bedrock-agentcore:InvokeGateway` on the gateway, as that page states. The deployment of this pattern used the default CDK roles.

## Supported Regions

The stack has no Region-specific values and was deployed and tested in US West (Oregon) (`us-west-2`) and Europe (Frankfurt) (`eu-central-1`). Before you use another Region, check that the [AgentCore supported Regions page](https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/agentcore-regions.html) lists AgentCore Gateway and Policy there and that AWS Lambda offers the Node.js 24 runtime.

## Architecture

```
curl -u client:secret ---> Amazon Cognito token endpoint ---> access token (scope: orders/read or orders/cancel)
curl + Bearer token ---> Amazon Bedrock AgentCore Gateway (MCP, JWT authorizer: Cognito, two allowed clients)
                              |  1. verify the token
                              |  2. Policy engine (ENFORCE): Cedar permit for the tool and the scope?
                              |        yes --> 3. invoke the AWS Lambda target (lookup_order, cancel_order)
                              |        no  --> request denied, the function is not invoked
```

## How it works

1. Amazon Cognito has a resource server `orders` with the scopes `orders/read` and `orders/cancel`, and one app client per scope with the client credentials flow. Each client can request only its own scope.
2. The gateway uses a `CUSTOM_JWT` authorizer with the Cognito discovery URL and both app client IDs as allowed clients. A token from any other client is rejected by the authorizer. The authorizer checks the client only; the scope decision is made by the Cedar policies.
3. The policy engine is attached to the gateway in `ENFORCE` mode. The gateway service role gets `GetPolicyEngine` on the engine, and `AuthorizeAction` and `PartiallyAuthorizeActions` on the engine and the gateway, as the [policy permissions page](https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/policy-permissions.html) requires. The engine uses the default encryption, so no AWS KMS key is needed.
4. Cedar denies by default. The policy `permit_lookup_order` permits `OrdersTarget___lookup_order` when `principal.getTag("scope")` matches `*orders/read*`, and `permit_cancel_order` does the same for `cancel_order` and `orders/cancel`. The action ID is `<target name>___<tool name>` with three underscores. The [documentation](https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/example-policies-principal.html) describes the claims of the token as string tags of the `AgentCore::OAuthUser` principal.
5. The stack uses the constructs of `aws-cdk-lib/aws-bedrockagentcore` (`PolicyEngine`, `Gateway`, `addLambdaTarget`) and no `CfnResource`. The policy statements are raw Cedar through `PolicyStatement.fromCedar`, because the typed condition builders of aws-cdk-lib 2.274 do not express `hasTag`, `getTag` and `like`. Each policy depends on the gateway target, because policy validation checks the action names against the tools of the gateway.

## Important Notes

* **A denied call is not an HTTP error.** The gateway answers `HTTP 200` with a JSON-RPC `error` (code `-32002`), so a client must check the `error` field of the response.
* **Where the decision input comes from:** the scope that Cedar evaluates is a claim of the access token after the gateway has accepted the token. The request body, tool arguments and headers other than the token are never used for the decision.
* **`like` matches substrings.** `*orders/read*` would also match a scope such as `orders/read-all`. Keep scope names free of each other, or match the delimiters.
* **Who can reach what:** the gateway URL is a public HTTPS endpoint, but every request needs a bearer token from one of the two app clients, otherwise the response is an authentication error. Whoever can call `cognito-idp:DescribeUserPoolClient` on the user pool can read the client secrets and mint tokens for both scopes. For a gateway that is not meant to take bearer tokens, the [inbound authorization page](https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/gateway-inbound-auth.html) describes the `AWS_IAM` authorizer, where Cedar policies match `AgentCore::IamEntity` instead.
* **The gateway service role** trusts `bedrock-agentcore.amazonaws.com` with `aws:SourceAccount` and an `aws:SourceArn` condition for gateways in this account and Region. The stack supplies this role because the default role of the `Gateway` construct (aws-cdk-lib 2.274) also keeps a trust statement without those conditions. The role holds the policy evaluation actions on this engine and gateway and may invoke only that function and its versions.
* **Not covered:** per-user policies from a user sign-in, conditions on tool arguments (`context.input`), `forbid` policies, policy generation, a customer managed key for the engine and decision logging to Amazon CloudWatch Logs (the stack does not enable gateway logging).
* **Cost:** Gateway and Policy in Amazon Bedrock AgentCore are billed per request ([AgentCore pricing](https://aws.amazon.com/bedrock/agentcore/pricing/)). For the machine-to-machine app clients see [Amazon Cognito pricing](https://aws.amazon.com/cognito/pricing/).

## Deployment Instructions

1. Clone the repository:
    ```bash
    git clone https://github.com/aws-samples/serverless-patterns
    cd serverless-patterns/agentcore-gateway-cedar/typescript/cdk
    ```
2. Install the dependencies:
    ```bash
    npm install
    ```
3. Deploy the stack to the Region of your AWS CLI profile (about 2 minutes):
    ```bash
    npx cdk deploy
    ```
4. Note the outputs: `GatewayUrl`, `TokenEndpoint`, `UserPoolId`, `ReaderClientId`, `CancelerClientId` and `ToolFunctionLogGroup`. The Testing section reads them again.

## Testing

All commands assume the stack name `AgentcoreGatewayCedarStack` and the Region of the deployment, which your AWS CLI configuration or `AWS_REGION` must select. In a new shell, run step 1 first, because later steps use its variables and functions.

1. Read the outputs, define helpers and get one token per client. `GATEWAY_URL` is the `GatewayUrl` output with `/mcp` added if it is missing:
    ```bash
    out() { aws cloudformation describe-stacks --stack-name AgentcoreGatewayCedarStack --query "Stacks[0].Outputs[?OutputKey=='$1'].OutputValue" --output text; }
    GATEWAY_URL=$(out GatewayUrl); case "$GATEWAY_URL" in */mcp) ;; *) GATEWAY_URL="${GATEWAY_URL%/}/mcp";; esac
    TOKEN_URL=$(out TokenEndpoint); POOL=$(out UserPoolId); READER=$(out ReaderClientId); CANCELER=$(out CancelerClientId)
    LOG_GROUP=$(out ToolFunctionLogGroup)
    token() { curl -s -u "$1:$(aws cognito-idp describe-user-pool-client --user-pool-id "$POOL" --client-id "$1" --query UserPoolClient.ClientSecret --output text)" \
      -d grant_type=client_credentials --data-urlencode "scope=$2" "$TOKEN_URL" | jq -r .access_token; }
    mcp() { curl -s -w '\nHTTP %{http_code}\n' -X POST "$GATEWAY_URL" -H "Authorization: Bearer $1" -H 'Content-Type: application/json' \
      -H 'Accept: application/json, text/event-stream' -H 'MCP-Protocol-Version: 2025-06-18' -d "$2"; }
    call() { mcp "$1" "{\"jsonrpc\":\"2.0\",\"id\":1,\"method\":\"tools/call\",\"params\":{\"name\":\"OrdersTarget___$2\",\"arguments\":{\"orderId\":\"1001\"}}}"; }
    READ_TOKEN=$(token "$READER" orders/read); CANCEL_TOKEN=$(token "$CANCELER" orders/cancel)
    ```
2. Read the verified claim that Cedar will evaluate. Expected: `scope` is `orders/read` for the first token and `orders/cancel` for the second:
    ```bash
    for T in "$READ_TOKEN" "$CANCEL_TOKEN"; do echo "$T" | jq -R 'split(".")[1] | gsub("-";"+") | gsub("_";"/") | @base64d | fromjson | {client_id, scope}'; done
    ```
3. Call each tool with the `orders/read` token. Expected: `lookup_order` returns `isError: false` and a text that holds the order status `SHIPPED`; `cancel_order` is denied. The gateway answers `HTTP 200` with a JSON-RPC error, code `-32002`, message `Tool Execution Denied: Tool call not allowed due to policy enforcement [No policy applies to the request (denied by default).]`:
    ```bash
    call "$READ_TOKEN" lookup_order
    call "$READ_TOKEN" cancel_order
    ```
4. Call each tool with the `orders/cancel` token. Expected: the reverse. `cancel_order` returns `CANCELLED (demo only, no data is changed)`; `lookup_order` is denied:
    ```bash
    call "$CANCEL_TOKEN" cancel_order
    call "$CANCEL_TOKEN" lookup_order
    ```
5. List the tools with each token. With a policy engine attached, the list holds only the tools that the caller may call. Expected: `OrdersTarget___lookup_order` for the first token, `OrdersTarget___cancel_order` for the second:
    ```bash
    for T in "$READ_TOKEN" "$CANCEL_TOKEN"; do mcp "$T" '{"jsonrpc":"2.0","id":1,"method":"tools/list"}'; done
    ```
6. Check that the denied calls never reached the function. Expected: `2` on a fresh stack, one `START` line for each allowed call in steps 3 and 4. The count grows with every further allowed call, including the one in step 8. Amazon CloudWatch Logs can take a while to show the second one, so run the command again if it prints `1`:
    ```bash
    aws logs filter-log-events --log-group-name "$LOG_GROUP" --filter-pattern '"START RequestId"' --query 'length(events)'
    ```
7. Negative cases. A request without a token gets an authentication error (expected: `HTTP 401` with the JSON-RPC error `Missing Bearer token`). Cognito refuses a client that asks for a scope it does not have (expected: `HTTP 400` with an `invalid_grant` error), so a token never carries the scope of the other client:
    ```bash
    curl -s -w '\nHTTP %{http_code}\n' -X POST "$GATEWAY_URL" -H 'Content-Type: application/json' -d '{"jsonrpc":"2.0","id":1,"method":"tools/list"}'
    curl -s -w '\nHTTP %{http_code}\n' -u "$READER:$(aws cognito-idp describe-user-pool-client --user-pool-id "$POOL" --client-id "$READER" --query UserPoolClient.ClientSecret --output text)" -d grant_type=client_credentials -d scope=orders/cancel "$TOKEN_URL"
    ```
8. Show that the policy engine makes the decision. Deploy in `LOG_ONLY` mode (`policyMode` accepts `ENFORCE` and `LOG_ONLY`), repeat the denied call of step 3 with a fresh token (expected: it now succeeds), then restore `ENFORCE`:
    ```bash
    npx cdk deploy -c policyMode=LOG_ONLY
    READ_TOKEN=$(token "$READER" orders/read); call "$READ_TOKEN" cancel_order
    npx cdk deploy
    ```

    Do not leave the stack in `LOG_ONLY`: in this mode the gateway lets every tool call through. If the second deploy fails or you stop after the first, run `npx cdk deploy` again and repeat the denied call of step 3 to confirm that it is denied.

If a call fails unexpectedly, read the log group in `ToolFunctionLogGroup`. The gateway returns its errors in the response.

## Cleanup

1. Delete the stack:
    ```bash
    npx cdk destroy
    ```
2. Confirm the stack has been deleted. The output shows `DELETE_COMPLETE`:
    ```bash
    aws cloudformation list-stacks --query "StackSummaries[?StackName=='AgentcoreGatewayCedarStack'].StackStatus"
    ```

All resources use removal policies that delete them, and none has deletion protection, so `cdk destroy` removes the gateway, target, policy engine, policies, user pool, domain, function and the function log group. This deletes the Amazon Cognito app clients and their secrets. The zipped function code stays in the CDK bootstrap bucket.

----
Copyright 2026 Amazon.com, Inc. or its affiliates. All Rights Reserved.

SPDX-License-Identifier: MIT-0
