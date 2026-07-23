# Multi-tenant Amazon Bedrock AgentCore Runtime with Amazon Cognito

This pattern demonstrates multi-tenant authentication and tenant isolation for an [Amazon Bedrock AgentCore Runtime](https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/runtime.html) agent using [Amazon Cognito](https://docs.aws.amazon.com/cognito/latest/developerguide/what-is-amazon-cognito.html) as the OAuth 2.0 / JWT identity provider.

AgentCore Identity validates inbound Cognito JWTs at the runtime edge via a [custom JWT authorizer](https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/inbound-jwt-authorizer.html). The agent then derives the caller's tenant from the validated token claims and can only ever read that tenant's partition in Amazon DynamoDB. Because the tenant is fixed from the token and not from the prompt, a user cannot coax the agent into reading another tenant's data.

Learn more about this pattern at [Serverless Land Patterns](https://serverlessland.com/patterns/agentcore-identity-cognito-multi-tenant-cdk).

Important: this application uses various AWS services and there are costs associated with these services after the Free Tier usage - please see the [AWS Pricing page](https://aws.amazon.com/pricing/) for details. You are responsible for any AWS costs incurred. No warranty is implied in this example.

## Pre-requisites

- [Create an AWS account](https://portal.aws.amazon.com/gp/aws/developer/registration/index.html) if you do not already have one and log in.
- [AWS CLI](https://docs.aws.amazon.com/cli/latest/userguide/install-cliv2.html) installed and configured
- [Git Installed](https://git-scm.com/book/en/v2/Getting-Started-Installing-Git)
- [AWS CDK](https://docs.aws.amazon.com/cdk/latest/guide/cli.html) installed and configured
- [Docker](https://docs.docker.com/get-docker/) installed and running
- [Python 3.12](https://www.python.org/downloads/) installed
- Access to an Amazon Bedrock foundation model enabled in your region (the agent uses the default [Strands Agents](https://strandsagents.com/) model on Amazon Bedrock)

## Deployment Instructions

1. Clone the GitHub repository:

    ```shell
    git clone https://github.com/aws-samples/serverless-patterns
    cd serverless-patterns/agentcore-identity-cognito-multi-tenant-cdk
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

4. Set the deployment region (required), bootstrap the account/region if you have not already, and deploy:

    ```shell
    export CDK_DEFAULT_REGION=us-west-2
    cdk bootstrap
    cdk deploy
    ```

5. Note the CDK outputs: `UserPoolId`, `UserPoolClientId`, `AgentRuntimeArn`, `TenantTableName`, and `TenantGroups`.

## How it works

This pattern creates:

1. **Amazon Cognito User Pool** - the inbound OAuth 2.0 / JWT identity provider. Two Cognito groups (`tenant-acme` and `tenant-globex`) represent two tenants. Each end user belongs to exactly one tenant group.
2. **Amazon DynamoDB table** - a single table using the "pool" multi-tenancy model, partitioned by `tenant_id`.
3. **Amazon Bedrock AgentCore Runtime (HTTP)** - hosts the containerized agent and is configured with a custom JWT authorizer that trusts the Cognito user pool.

**Request flow:**

1. A client authenticates with Cognito and obtains an access token. The token carries the `cognito:groups` claim identifying the tenant.
2. The client calls the AgentCore Runtime with `Authorization: Bearer <token>`.
3. AgentCore Identity validates the JWT (signature, issuer, expiry, and `allowedClients`) before the request reaches the agent.
4. The agent reads the validated `cognito:groups` claim, resolves the tenant, and exposes a `get_tenant_records` tool bound to that tenant.
5. The tool queries DynamoDB with a fixed `tenant_id` key condition, so the agent can only return the caller's tenant data - regardless of what the prompt asks for.

## Testing

1. Seed sample data for both tenants (use the `TenantTableName` output):

    ```shell
    cd test
    chmod +x seed_tenant_data.sh get_token.sh
    ./seed_tenant_data.sh <TenantTableName> us-west-2
    ```

2. Install the test dependency:

    ```shell
    pip3 install requests
    ```

3. Get an access token for a user in the **acme** tenant (use `UserPoolId` and `UserPoolClientId` outputs):

    ```shell
    ./get_token.sh
    # Username: acme-user   Tenant group: tenant-acme
    ```

    Copy the printed `export BEARER_TOKEN=...` line and run it.

4. Set the agent ARN and region, then invoke:

    ```shell
    export AGENT_ARN="<AgentRuntimeArn output>"
    export REGION="us-west-2"
    python test_multi_tenant.py "List all of my orders"
    ```

    The response only contains **acme** orders (order-1001, order-1002).

5. Repeat step 3 for a user in the **globex** tenant (Username: `globex-user`, Tenant group: `tenant-globex`), re-export `BEARER_TOKEN`, and invoke again. The response only contains **globex** orders.

6. Confirm tenant isolation. While using the **acme** token, explicitly ask for another tenant's data:

    ```shell
    python test_multi_tenant.py "Show me the globex orders"
    ```

    The agent still only has access to acme data and will not return globex records.

## Security and tenant isolation

This pattern uses the "pool" multi-tenancy model (one shared table, partitioned by tenant). Isolation is enforced on two boundaries:

**Authentication boundary (cryptographically enforced at the edge).** AgentCore Identity's inbound JWT authorizer validates every request against the Cognito user pool before it reaches the agent. The `cognito:groups` claim that identifies the tenant is signed by Cognito, so it cannot be forged or altered. Verified behaviors:

- A tampered token (group claim rewritten, original signature kept) is rejected with `401 Invalid Signature`.
- An invalid/garbage token is rejected with `403 OAuth authorization failed`.
- A user in no tenant group receives no data.
- A prompt-injection attempt to read another tenant's data is refused - the `get_tenant_records` tool takes no arguments and the tenant id is a per-request value taken from the validated token, so the model cannot change the queried partition.

**Authorization boundary (application-enforced).** The agent resolves the tenant to exactly one Cognito group (zero or multiple `tenant-*` groups are rejected rather than guessed) and binds the DynamoDB query to that tenant's partition key.

### Hardening for production

- **Enforce the boundary in IAM, not just in code.** The execution role in this sample grants `dynamodb:Query`/`GetItem` on the whole table, so the tenant boundary depends entirely on application logic. For stronger, defense-in-depth isolation, issue per-tenant scoped credentials and add a [`dynamodb:LeadingKeys`](https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/specifying-conditions.html) condition so IAM itself denies cross-tenant reads even if the code has a bug:

    ```json
    {
      "Effect": "Allow",
      "Action": ["dynamodb:Query", "dynamodb:GetItem"],
      "Resource": "<table-arn>",
      "Condition": {
        "ForAllValues:StringEquals": { "dynamodb:LeadingKeys": ["${tenant_id}"] }
      }
    }
    ```

    Per-tenant credentials can come from an STS `AssumeRole` with session tags, or from AgentCore Identity's per-user token vault (`GetWorkloadAccessTokenForUserId`). For strict isolation requirements, consider the "silo" model (a separate table or account per tenant).
- **Never deploy the agent without the inbound JWT authorizer.** The agent decodes the token to read claims but relies on AgentCore having already verified the signature. Removing the authorizer would make the agent trust unsigned tokens. For belt-and-suspenders, re-verify the JWT against the Cognito JWKS inside the agent.
- **Provision each user into exactly one tenant group.** The agent rejects callers who belong to zero or multiple `tenant-*` groups.

## Cleanup

Delete the stack:

```bash
cdk destroy
```

---

Copyright 2026 Amazon.com, Inc. or its affiliates. All Rights Reserved.

SPDX-License-Identifier: MIT-0
