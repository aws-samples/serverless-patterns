# AWS AppSync to AWS Step Functions via Amazon EventBridge

This pattern deploys a self-service workflow catalog: a single AWS AppSync GraphQL API in front of your teams' AWS Step Functions workflows. A workflow owner opts a Standard state machine in by tagging it `workflowType`; it is discovered and registered in an Amazon DynamoDB catalog, and an admin activates it by publishing a versioned JSON Schema input contract. Any authorized caller can then trigger the workflow by name through the API and track it to completion — without direct access to the underlying state machine. Requests flow through Amazon EventBridge, execution state is tracked in DynamoDB, and a scheduled reconciler repairs any dropped events.

Learn more about this pattern at Serverless Land Patterns: << Add the live URL here >>

Important: this application uses various AWS services and there are costs associated with these services after the Free Tier usage - please see the [AWS Pricing page](https://aws.amazon.com/pricing/) for details. You are responsible for any AWS costs incurred. No warranty is implied in this example.

## Requirements

- [Create an AWS account](https://portal.aws.amazon.com/gp/aws/developer/registration/index.html) if you do not already have one and log in. The IAM user that you use must have sufficient permissions to make necessary AWS service calls and manage AWS resources.
- [AWS CLI](https://docs.aws.amazon.com/cli/latest/userguide/install-cliv2.html) installed and configured
- [Git Installed](https://git-scm.com/book/en/v2/Getting-Started-Installing-Git)
- [Node.js 18 or later](https://nodejs.org/en/download/) installed
- [Python 3.11 or later](https://www.python.org/downloads/) installed (the build bundles the Lambda dependency)
- [AWS Cloud Development Kit (AWS CDK)](https://docs.aws.amazon.com/cdk/v2/guide/getting_started.html) installed

## Deployment Instructions

1. Create a new directory, navigate to that directory in a terminal and clone the GitHub repository:
   ```
   git clone https://github.com/aws-samples/serverless-patterns
   ```
1. Change directory to the pattern directory:
   ```
   cd serverless-patterns/appsync-eventbridge-sfn/typescript/cdk
   ```
1. Install dependencies:
   ```
   npm install
   ```
1. Build the project. This compiles the TypeScript into `dist/` (which the CDK app entry in `cdk.json` loads), copies the GraphQL schema, and vendors the `fastjsonschema` Lambda dependency. It must run before any `cdk` command:
   ```
   npm run build
   ```
1. If this account/Region has not been bootstrapped for CDK, bootstrap it:
   ```
   npx cdk bootstrap
   ```
1. Deploy the stack. Use `npm run deploy` (not a bare `cdk deploy`) — it re-runs the build and then `cdk deploy`:
   ```
   npm run deploy
   ```
1. Note the outputs from the deployment process. These contain the GraphQL API URL, the DynamoDB table names, the event bus name, the privileged field ARNs, and the two managed-policy ARNs used for access and testing.

### (Optional) Add Amazon Cognito user-pool authentication

By default the API uses **IAM** authorization. To also accept your users' Amazon Cognito JWTs, pass an **existing** user pool to the construct in `lib/workflow-catalog-stack.ts` before deploying (the pattern never creates a pool):

```typescript
import { Stack, StackProps } from "aws-cdk-lib";
import { Construct } from "constructs";
import * as cognito from "aws-cdk-lib/aws-cognito";
import { WorkflowCatalog } from "./workflow-catalog";

export class WorkflowCatalogStack extends Stack {
  public constructor(scope: Construct, id: string, props?: StackProps) {
    super(scope, id, props);

    const userPool = cognito.UserPool.fromUserPoolId(
      this,
      "ConsumerUserPool",
      "us-east-1_abc123", // your existing pool id
    );

    new WorkflowCatalog(this, "WorkflowCatalog", {
      userPool,
      adminGroups: ["platform-admins"], // optional: Cognito groups allowed to call the admin fields
    });
  }
}
```

IAM stays the default mode; Cognito is added as an additional mode. You bring your own pool, app client, and groups — the admin fields stay IAM-only unless you set `adminGroups`. See [ARCHITECTURE.md](./ARCHITECTURE.md) for the full authorization and identity model.

### (Optional) Protect data for production

So the sample tears down cleanly with `cdk destroy`, the two DynamoDB tables default to `removalPolicy: DESTROY` and `deletionProtection: false`. For production, flip both so the registry/tracker data survives a stack deletion and can't be dropped by accident:

```typescript
import { RemovalPolicy, Stack, StackProps } from "aws-cdk-lib";
import { Construct } from "constructs";
import { WorkflowCatalog } from "./workflow-catalog";

export class WorkflowCatalogStack extends Stack {
  public constructor(scope: Construct, id: string, props?: StackProps) {
    super(scope, id, props);

    new WorkflowCatalog(this, "WorkflowCatalog", {
      removalPolicy: RemovalPolicy.RETAIN,
      deletionProtection: true,
    });
  }
}
```

With `deletionProtection: true`, you must set it back to `false` and redeploy before a later `cdk destroy` can remove the tables.

## How it works

The construct provisions a mediation layer around Step Functions state machines you already own:

- **AppSync GraphQL API** (IAM auth by default; optional Amazon Cognito user-pool auth) with two AWS Lambda data sources.
- **Request handler Lambda** — validates the `requestWorkflow` call (workflow enabled, caller authorized, parameters match the registered JSON Schema), writes a `REQUESTED` record to the DynamoDB execution tracker, and publishes a `Workflow Requested` event to a custom EventBridge bus.
- **Workflow trigger Lambda** — invoked by the EventBridge rule, calls `StartExecution` on the state machine. The trigger's IAM policy is scoped by the `workflowType` tag, so it can only start machines that opted in.
- **Registry sync Lambda** — discovers tagged state machines from Step Functions CloudTrail events (via EventBridge) and manages the versioned input contracts in the DynamoDB workflow registry. It also backs the `registerWorkflowContract` admin mutation.
- **Status handler Lambda** — updates the tracker from Step Functions execution status-change events.
- **Reconciler Lambda** — runs on a schedule and repairs any execution record left stale by a dropped event, reading the true status from Step Functions.
- **DynamoDB** — a workflow registry (the catalog) and an execution tracker (per-request status, with a TTL).
- **Amazon SQS** dead-letter queues (one per async Lambda) with CloudWatch alarms.

Callers read results with `getWorkflowExecution` / `listWorkflowExecutions`. Authorization can be restricted per workflow with an optional `allowedCallers` list (by IAM role ARN or Cognito group).

For the full detail — request flow, the workflow discovery/activation lifecycle, the input-contract (`inputSchema`) spec, the authorization and identity model, the data model, the security model, and a GraphQL operations reference — see [ARCHITECTURE.md](./ARCHITECTURE.md).

## Testing

After deploying, make one workflow callable and run it. The quickest path is the AWS AppSync console **Queries** editor (it signs requests for you); the `Register*` mutation requires admin access via the emitted `WorkflowAdminAccessPolicy` (or a Cognito group in `adminGroups`).

1. **Provide a Standard Step Functions state machine** whose first state reads its input at the top level (e.g. `$.employeeId`). To just try the pattern, create a trivial one (a single `Pass` state).
1. **Tag it** so the trigger can start it and discovery can see it:
   ```
   aws stepfunctions tag-resource --resource-arn <state-machine-arn> --tags key=workflowType,value=employee-onboarding
   ```
   With CloudTrail management-event logging on in the Region, it auto-registers within a minute or two as `PENDING_CONTRACT`. (Without CloudTrail, pass `stateMachineArn` to `registerWorkflowContract` to register directly.)
1. **Activate the contract** (admin) by calling the `registerWorkflowContract` mutation with a `schemaVersion` and an `inputSchema` describing the flat parameters, e.g.:
   ```graphql
   mutation Activate {
     registerWorkflowContract(
       workflowType: "employee-onboarding"
       schemaVersion: "v1"
       inputSchema: "{\"type\":\"object\",\"required\":[\"employeeId\"],\"properties\":{\"employeeId\":{\"type\":\"string\"}}}"
     ) {
       workflowType
       contractStatus
       enabled
     }
   }
   ```
   `contractStatus` should return `ACTIVE` and `enabled` `true`.
1. **Request a run:**
   ```graphql
   mutation Run {
     requestWorkflow(
       workflowType: "employee-onboarding"
       parameters: "{\"employeeId\":\"E123\"}"
       clientRequestToken: "run-001"
     ) {
       executionId
       status
     }
   }
   ```
   Copy the returned `executionId`.
1. **Confirm it ran:** a new Step Functions execution whose name equals the `executionId` should appear in the Step Functions console, and polling returns a terminal status:
   ```graphql
   query Status {
     getWorkflowExecution(executionId: "PASTE_EXECUTION_ID") {
       status
       output
       error
     }
   }
   ```
   A successful run shows `status: SUCCEEDED` with the workflow output.

## Cleanup

1. Delete the stack:
   ```bash
   npx cdk destroy
   ```
1. Confirm the stack has been deleted:
   ```bash
   aws cloudformation list-stacks --query "StackSummaries[?contains(StackName,'WorkflowCatalogStack')].StackStatus"
   ```

---

Copyright 2025 Amazon.com, Inc. or its affiliates. All Rights Reserved.

SPDX-License-Identifier: MIT-0
