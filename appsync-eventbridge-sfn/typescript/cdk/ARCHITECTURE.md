# Architecture and reference — self-service workflow catalog

A GraphQL front door for your teams' Step Functions workflows: owners opt a workflow in by
tagging it and publishing an input contract, and any authorized caller can then discover it,
trigger it by name, and track it to completion — without direct access to the underlying state
machine.

This is the deep-dive companion to the [README](./README.md) (which covers requirements,
deployment, testing, and cleanup). It explains how the system works, the request flow, the
workflow lifecycle, the input contract, the authorization and identity model, the data model,
and the security model, and includes a GraphQL operations reference.

## How it compares to calling Step Functions directly

In the usual setup, every consumer wires directly to a specific state machine — they
need its ARN, `states:StartExecution` permission, knowledge of its input shape, and
their own status tracking. That is point-to-point and consumer-owned, and it gets
unwieldy with many workflows and many callers.

This pattern replaces that wiring with one mediated front door, so discovery, access,
input validation, execution, and tracking are handled once, consistently. Adding a
new workflow or a new consumer becomes a registration, not a custom integration.

---

# How it works

This half of the document explains the design: what the construct deploys, how a request
flows through it, how workflows are registered, and the authorization, data, and security
models. If you just want to stand it up, see the [README](./README.md) for requirements,
deployment, testing, and cleanup.

## Architecture

```
Caller ──requestWorkflow──▶ AppSync ──▶ Request Handler Lambda
                                             │ validate + record (REQUESTED)
                                             ▼
                                        EventBridge  ──▶ Workflow Trigger Lambda
                                                              │ StartExecution
                                                              ▼
                                                        Step Functions
                                                              │ status-change events
                                                              ▼
                              Status Handler Lambda ◀── EventBridge
                                             │ update tracker record
                                             ▼
                                        DynamoDB (execution tracker)
                                             ▲
Caller ──getWorkflowExecution / list──▶ AppSync ──▶ Request Handler Lambda (reads)
```

Supporting pieces:

- **Registry Sync Lambda** — discovers tagged state machines via CloudTrail events and
  manages their versioned input contracts.
- **Reconciler Lambda** — runs on a schedule and repairs any execution record that got
  stuck (dropped event, failed start) by reading the true status from Step Functions.
- **Dead-letter queues + alarms** on every async Lambda.

## What gets deployed

Instantiating the construct provisions a self-contained mediation layer and the wiring between
its parts. None of this is your workflow — the pattern only provisions the layer _around_
state machines you already own.

**Resources created:**

- **AppSync GraphQL API** (`workflow-catalog-api`) — IAM auth by default, optional
  Cognito user-pool mode, X-Ray enabled; two Lambda data sources and their resolvers.
- **5 Lambda functions** (Python 3.13, ARM64, X-Ray on, each with its own one-month log
  group): request handler, workflow trigger, registry sync, status handler, reconciler.
- **2 DynamoDB tables** (on-demand billing, AWS-managed encryption, point-in-time recovery) —
  the workflow **registry** (+ a `stateMachineArn` GSI) and the execution **tracker** (+ 3
  GSIs, with a TTL on `expiresAt`).
- **1 EventBridge bus** (`WorkflowEventBus`) plus 4 rules: workflow-requested (on the custom
  bus), state-machine discovery (CloudTrail), execution-status-change, and the reconciler
  schedule.
- **4 SQS dead-letter queues** (one per async Lambda), each with a **CloudWatch alarm** on
  visible messages.
- **IAM** — a least-privilege execution role per Lambda, plus two **managed policies**
  (`WorkflowCallerAccessPolicy`, `WorkflowAdminAccessPolicy`) scoped to the API's field ARNs.
- **CloudFormation outputs** — API id/URL, both table names, the event bus name, the
  privileged field ARNs, and the two managed-policy ARNs.

**How they connect:**

- AppSync routes the caller fields to the **request handler** and the registry/catalog fields
  to the **registry sync** Lambda.
- Request handler → writes the tracker table, reads the registry, publishes a
  `Workflow Requested` event to the bus, and (for cancel) calls `StopExecution`.
- Workflow-requested rule → **trigger** Lambda → `StartExecution` (tag-scoped) on your state
  machine.
- Step Functions status-change events → status rule → **status handler** → updates the tracker.
- Step Functions CloudTrail API events → discovery rule → **registry sync** → upserts the
  registry.
- The schedule → **reconciler** → repairs stuck tracker records (reads Step Functions,
  re-publishes requests).
- Any async Lambda that exhausts its retries → its **DLQ** → **alarm**.

## Request flow

1. A caller invokes the `requestWorkflow` mutation. The request handler validates the
   workflow is registered, enabled, Standard-type, that the caller is authorized
   (`allowedCallers`), and that the parameters match the published JSON Schema. It
   writes a `REQUESTED` tracker record and publishes a `Workflow Requested` event.
2. An EventBridge rule invokes the workflow trigger, which claims the record
   (`REQUESTED → STARTING`) and calls `StartExecution` with `name = executionId`
   (deterministic, so retries don't start duplicates), then marks it `RUNNING`.
3. Step Functions emits execution-status-change events; the status handler updates the
   tracker record (to `SUCCEEDED`/`FAILED`/etc., with output or error).
4. The caller polls `getWorkflowExecution` or `listWorkflowExecutions`.

## Workflow lifecycle

A workflow becomes callable in three steps:

1. The owner tags their Standard state machine with `workflowType=<name>`. This is what
   makes it discoverable **and** what the trigger's IAM policy checks before it is
   allowed to start it.
2. Auto-discovery registers it as `PENDING_CONTRACT` / disabled. Tagging alone gets the
   workflow into the registry, but it is **not callable yet** — it has no input contract,
   so `enabled` stays `false` and `requestWorkflow` rejects it until step 3.
3. An admin calls `registerWorkflowContract` with a versioned JSON Schema (and
   optionally `allowedCallers`) to activate it (`contractStatus = ACTIVE`,
   `enabled = true`). Because the workflow is already in the registry, you omit
   `stateMachineArn` — it is resolved from the discovered record.

Normally that is the whole flow: **tag the state machine and it registers itself; an admin
then activates the contract.** The owner never needs to know or paste the ARN. (The concrete
commands are in the [README](./README.md) Testing section.)

### Registering directly (passing `stateMachineArn`)

`registerWorkflowContract` also accepts a `stateMachineArn`, which both registers **and**
activates a workflow in one call without waiting for discovery. This is the fallback for
the cases where auto-discovery does not run:

- **CloudTrail management-event logging is not enabled in the Region.** Discovery is driven
  by Step Functions CloudTrail API events, and the pattern does not enable CloudTrail. With no
  CloudTrail, no discovery event ever fires, so every workflow must be registered directly with
  its ARN.
- **The state machine predates the pattern (brownfield adoption).** Discovery fires on
  `CreateStateMachine` / `UpdateStateMachine` events going forward; a state machine that
  already existed when the pattern was deployed emitted its create event in the past and is
  never discovered until someone updates or re-tags it. Register such workflows directly, or
  re-touch each one to emit a fresh event.
- **You want to register synchronously.** CloudTrail management events can lag by minutes (or
  occasionally drop). Passing the ARN registers and activates in a single call instead of
  waiting for the `PENDING_CONTRACT` record to appear.
- **A registry record was deleted while the state machine still exists.** The sync handler
  removes a registration on `DeleteStateMachine`; a direct call restores it without touching
  the state machine.

> If CloudTrail management-event logging is on and workflows are created after the pattern is
> deployed, discovery always lands the `PENDING_CONTRACT` record first, so activation is just
> the ARN-less call in step 3. Direct registration is the escape hatch, not the normal path.

### Updating a workflow's schema

Schemas are versioned, and a version is **immutable**. To change a workflow's input contract,
call `registerWorkflowContract` again with the **same `workflowType`**, a **new
`schemaVersion`**, and the updated `inputSchema` (omit `stateMachineArn` — it is resolved from
the record). The registry holds one contract per workflow, so this overwrites the active schema
in place and takes effect for the **next** `requestWorkflow` immediately. In-flight and past
executions are unaffected: each stored its own already-validated payload, and the schema is
only consulted at request time.

- Re-submitting the **same version with identical schema content** is a safe no-op (an
  idempotent retry).
- Re-submitting an **existing version number with changed content** is rejected — bump the
  version instead. This stops a version's meaning from silently changing underneath callers.

Two things to keep in mind: the registry stores only the current contract (one record per
`workflowType`), so there is no retained history or automatic rollback of prior versions —
versioning here guards against in-place edits, it is not a version archive. And keep the schema
and the state machine's first state in sync: if you add or rename a required field, update both.

## Workflow input contract

This is the contract every workflow — existing or new — must satisfy to plug into the
pattern. It defines what the pattern **sends** to your state machine and, therefore, what your
state machine must be built to **receive**.

**What the pattern sends.** When a request is accepted, the trigger calls Step Functions
`StartExecution` with the caller's validated `parameters` object as the execution input,
**verbatim**. The pattern adds nothing: there is no wrapper, no `executionId`, no
`workflowType`, no metadata. The execution input is exactly the JSON the caller submitted.

So a request with:

```json
{ "employeeId": "E123", "employeeFirstName": "Ada" }
```

produces a Step Functions execution whose input is exactly:

```json
{ "employeeId": "E123", "employeeFirstName": "Ada" }
```

**What your state machine must expect.** Treat the execution input as a flat object of your
parameters and read fields from the top level:

- ✅ JSONPath: `$.employeeId`
- ✅ JSONata: `{% $states.input.employeeId %}`
- ✅ Or pass the whole input straight to a task and parse it there (`"Payload.$": "$"`)
- ❌ Do **not** read `$.parameters.employeeId` or `$.workflowType` — the pattern never sends a
  wrapper, so those keys do not exist and the state will see them as missing.

**Making a workflow conform:**

- **New state machines** — author the first state to read parameters at the top level. That
  flat shape **is** the `inputSchema` you supply when you activate the contract — the schema
  and the state machine's first state are two views of the same contract, so keep them in sync.
  There is no separate "register a schema" step beyond activating the contract (see
  [Workflow lifecycle](#workflow-lifecycle)).
- **Existing state machines** — if a workflow was written to expect a wrapper (e.g. an
  EventBridge-style `$.detail.*`, or `$.parameters.*`), point its first state at the top-level
  fields instead, or add a leading pass-through that hands the raw input to a task that parses
  it. No change is needed on the caller side — the caller always just sends the parameters.

**Caller side (for completeness).** Callers submit only `parameters`, which the request
handler validates against the registered `inputSchema` and rejects if it doesn't match. The
same `parameters` object is what reaches the state machine — one object, described once by the
schema, delivered unchanged.

**You do not need `executionId` inside the workflow for tracking.** The trigger starts the
execution with `name = executionId`, so the Step Functions execution name _is_ the tracker
`executionId`, and status changes flow back to the tracker automatically via
execution-status-change events. A workflow only needs the id passed in if it wants to emit its
own correlated signals. The pattern sends raw parameters only; supporting an envelope
(`{ executionId, workflowType, parameters }`) would require updating the pattern's trigger
code and redeploying. Raw parameters is the deliberate default.

### Writing the `inputSchema`

The `inputSchema` you register is a standard **JSON Schema** document describing the flat
`parameters` object. The request handler compiles it and validates every submission against it,
so it is both the contract callers must satisfy and the type-check applied at request time.

**Hard requirements (enforced at registration — a schema that breaks these is rejected):**

- It must be a **JSON object with a top-level `"type": "object"`**. The parameters payload is
  always a flat object, so array/string/number root schemas are refused.
- It must be a **valid JSON Schema** — the handler compiles it and rejects anything malformed.
- If present, **`required` must be an array of property-name strings**. Those names are stored
  as the workflow's `requiredParameters` and are what callers must supply. `required` is
  optional; omit it for a workflow with no mandatory fields.
- The serialized schema must be **≤ ~128 KB**.
- It is passed as `AWSJSON` (a stringified JSON object — see
  [GraphQL operations](#graphql-operations)) and always paired with a **`schemaVersion`**
  (1–64 characters).

**What to put in it:**

- **`properties`** — each accepted field and its type/constraints (`"type": "string"`,
  `"type": "number"`, nested objects/arrays, etc.).
- **`required`** — the subset of properties a caller must send.
- **`additionalProperties`** — set to `false` to reject unknown fields, or `true` / omit to
  allow extras. (Discovery's auto-inferred schema uses `true`.)
- Any other standard keywords — `enum`, `format`, `minLength`, `minimum`, pattern, nested
  schemas — are all enforced, because the whole schema is evaluated.

Keep the schema in sync with the state machine's first state: every field the workflow reads at
the top level should appear in `properties`, and anything the workflow can't run without should
be in `required`.

**Annotated example** (shown as plain JSON; stringify it for the `AWSJSON` argument):

```json
{
  "type": "object", // required: parameters must be an object
  "required": ["employeeId"], // employeeId must be present
  "properties": {
    "employeeId": { "type": "string" },
    "employeeFirstName": { "type": "string" },
    "startDate": { "type": "string", "format": "date" },
    "level": { "type": "integer", "minimum": 1 }
  },
  "additionalProperties": false // reject any field not listed above
}
```

With this contract, `{ "employeeId": "E123" }` is accepted, `{ "employeeId": 123 }` is rejected
(wrong type), `{ "employeeFirstName": "Ada" }` is rejected (missing `employeeId`), and
`{ "employeeId": "E123", "nickname": "A" }` is rejected (unknown field, because
`additionalProperties` is `false`).

## Authorization and identity

### Authorization modes

- **IAM (default).** Every caller is an authenticated AWS principal. Best for
  service-to-service and backend callers.
- **Cognito User Pool (optional).** Added as an _additional_ mode when you pass an
  existing pool to the construct. Best for frontend users who log in with Cognito;
  AppSync validates their JWT and exposes `sub` + groups to the resolver.

The pattern never provisions a user pool — a consumer passes in one they already own
(see the [README](./README.md) for how to wire in a Cognito user pool).

### Identity model

Every execution records two distinct identities:

| Field                | Meaning                                                                                                                                                                                                     | Value by caller type                                                               |
| -------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------- |
| `requesterSubject`   | _Who to attribute ownership to._ The most specific stable identity available. Drives ownership checks, per-requester listing, and the idempotent `executionId`.                                             | Cognito user → `sub`; identity-pool user → `cognitoIdentityId`; service → role ARN |
| `requesterPrincipal` | _What they authenticated as._ Recorded for audit only — this stored copy is never read back. Authorization is evaluated at request time from the live principal (and groups), before the record is written. | Cognito user → username; service → role ARN                                        |

`requesterSubject` is derived by priority: `cognitoIdentityId` → `sub` → IAM principal
(role ARN). It always comes from the authenticated request context, never from the
request payload, so it cannot be spoofed. For a service, subject and principal coincide
on the role ARN — a role is the only identity a service has.

### Per-workflow authorization (`allowedCallers`)

A contract may carry an optional `allowedCallers` list. When present and non-empty, the
caller must match at least one entry; when absent or empty, the workflow is open to any
authorized API caller.

A caller is matched by:

- an **IAM principal / role ARN** (both the STS `assumed-role` and the IAM `role` form), or
- any **Cognito group** they belong to — listed as the bare group name or `group:<name>`.

Authorization is by **role or group only** — never by an individual identity. Two things
are intentionally not matchable:

- **Bare Cognito usernames** — a username can be deleted and recreated (reused) with a new
  `sub`, so a username entry could let a different person inherit access.
- **The per-user subject** (`sub` / `cognitoIdentityId`) — pinning individual users into a
  workflow contract is the wrong model; put the user in a group instead.

Services remain matchable because a service's principal _is_ its role ARN.
`requesterPrincipal` stores the username (for user-pool callers) only as a readable audit
value — it never grants access.

### Admin vs caller fields

| Field                                                                                                                                                  | Who     | Notes                                                                                                                                                |
| ------------------------------------------------------------------------------------------------------------------------------------------------------ | ------- | ---------------------------------------------------------------------------------------------------------------------------------------------------- |
| `requestWorkflow`, `cancelWorkflowExecution`, `getWorkflowExecution`, `listWorkflowExecutions`, `getWorkflowRegistration`, `listWorkflowRegistrations` | callers | self-service; execution read/cancel are scoped to the caller's own subject, catalog reads (`get`/`listWorkflowRegistrations`) are the shared catalog |
| `registerWorkflowContract`                                                                                                                             | admins  | registers/activates a contract                                                                                                                       |
| `listWorkflowExecutionsByType`                                                                                                                         | admins  | lists executions of a workflow type **across all callers**                                                                                           |

Admin access is granted the way that matches how the caller authenticated:

- **IAM callers** — via the emitted `WorkflowAdminAccessPolicy` (field-level IAM). The
  construct also emits `WorkflowCallerAccessPolicy` for the caller fields. Attach the admin
  policy to admin roles and the caller policy to everyone else (or pass role ARNs via
  `callerRoleArns` / `adminRoleArns` and the construct attaches them for you).
- **Cognito (frontend) callers** — via membership in an admin **group** you designate with
  the `adminGroups` prop. By default (`adminGroups` empty) the admin fields are **IAM-only**
  and no user-pool caller can reach them, so enabling a user pool does not accidentally
  expose admin operations. When you set `adminGroups`, the admin fields are additionally
  exposed to the user pool and the resolver enforces that the caller belongs to one of those
  groups; everyone else is denied.

> Because AppSync IAM authorization is additive, the IAM policies grant least-privilege
> access but cannot _prevent_ a broader policy (e.g. `AdministratorAccess`) from also
> reaching the admin fields. The resolver-level group check gives user-pool admins a hard
> gate regardless; scope broad IAM grants accordingly.

## Data model

### Workflow registry table

Partition key `workflowType`. Key attributes: `stateMachineArn`, `stateMachineType`,
`enabled`, `contractStatus` (`PENDING_CONTRACT` | `ACTIVE` | `UNSUPPORTED_WORKFLOW_TYPE`),
`schemaVersion`, `schemaHash`, `schemaSource`, `inputSchema`, `inferredInputSchema`,
`requiredParameters`, `allowedCallers` (optional), `registrationSource`,
`contractUpdatedBy`. GSI: `stateMachineArn-index`.

### Execution tracker table

Partition key `executionId`. Key attributes:

- `workflowType`, `requestPayload`, `clientRequestToken`
- `requestHash` — SHA-256 of the canonicalized parameters. Backs idempotency: reusing a
  `clientRequestToken` with _different_ parameters is rejected; same token + same params
  returns the existing execution.
- `requesterSubject`, `requesterPrincipal` — see identity model above.
- `requesterWorkflowType` — composite `{requesterSubject}#{workflowType}`; partition key
  for the per-requester listing index.
- `status` (`REQUESTED` | `STARTING` | `RUNNING` | `SUCCEEDED` | `FAILED` | `TIMED_OUT` |
  `ABORTED` | `REJECTED` | `DISPATCH_FAILED` | `START_FAILED` | `PENDING_REDRIVE`)
- `requestedAt`, `startedAt`, `finishedAt`, `lastUpdatedAt`, `executionArn`,
  `stateMachineArn`, `output`, `error`, `cause`
- `expiresAt` — TTL for automatic cleanup of terminal records.

GSIs:

- `requesterWorkflowType-requestedAt-index` — a caller's own runs of a workflow type.
- `workflowType-requestedAt-index` — all runs of a workflow type (admin listing).
- `status-lastUpdatedAt-index` — used internally by the reconciler.

### `clientRequestToken`

A caller-supplied idempotency key (1–128 chars). The `executionId` is a deterministic
`uuid5(requesterSubject + workflowType + clientRequestToken)`, so retrying with the same
token and parameters returns the same execution instead of starting a new run. Frontends
typically use a fresh UUID per distinct submission.

## Security model (layered)

1. **Opt-in by tag** — a workflow is reachable only if its owner tags it `workflowType`.
   Untagged machines are invisible to discovery and un-startable by IAM.
2. **Admin contract activation** — a discovered workflow is not callable until an admin
   activates its contract.
3. **API access control** — callers are authenticated principals; privileged fields are
   scoped to admins via the emitted managed policies.
4. **Scoped `StartExecution`** — the trigger's IAM policy only allows starting state
   machines carrying a `workflowType` tag, bounding blast radius.
5. **Input validation** — requests are validated against the published JSON Schema.
6. **Per-caller isolation** — callers read only their own executions (by `requesterSubject`).

---

# Reference

## GraphQL operations

All operations run against the AppSync GraphQL endpoint under IAM or Cognito user-pool auth
(see [Authorization and identity](#authorization-and-identity)). Arguments typed `AWSJSON`
(`inputSchema`, `parameters`) are **stringified JSON** — note the escaped quotes.

**Register / activate a workflow** (admin). `allowedCallers` is optional:

```graphql
mutation Register {
  registerWorkflowContract(
    workflowType: "employee-onboarding"
    stateMachineArn: "arn:aws:states:us-east-1:111122223333:stateMachine:employee-onboarding"
    schemaVersion: "v1"
    inputSchema: "{\"type\":\"object\",\"required\":[\"employeeId\"],\"properties\":{\"employeeId\":{\"type\":\"string\"}}}"
    allowedCallers: ["group:onboarding-team"]
  ) {
    workflowType
    contractStatus
    enabled
    allowedCallers
  }
}
```

**Activate an already-discovered workflow** (admin). A tagged state machine
auto-registers as `PENDING_CONTRACT`, so you only supply the schema — `stateMachineArn`
is resolved from the registry record:

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

**Browse the catalog** (any caller):

```graphql
query ListCatalog {
  listWorkflowRegistrations(limit: 25) {
    items {
      workflowType
      contractStatus
      enabled
      requiredParameters
    }
    nextToken
  }
}
```

**Inspect one workflow** (any caller):

```graphql
query GetRegistration {
  getWorkflowRegistration(workflowType: "employee-onboarding") {
    workflowType
    inputSchema
    enabled
    allowedCallers
  }
}
```

**Request a run.** `parameters` must match the workflow's `inputSchema`; `clientRequestToken`
is a caller-supplied idempotency key:

```graphql
mutation Run {
  requestWorkflow(
    workflowType: "employee-onboarding"
    parameters: "{\"employeeId\":\"E123\",\"employeeFirstName\":\"Ada\"}"
    clientRequestToken: "run-001"
  ) {
    executionId
    workflowType
    status
    requestedAt
  }
}
```

**Check status** (owner only):

```graphql
query GetExecution {
  getWorkflowExecution(executionId: "PASTE_EXECUTION_ID") {
    status
    output
    error
    startedAt
    finishedAt
  }
}
```

**List your own runs of a workflow** (scoped to the caller):

```graphql
query ListMine {
  listWorkflowExecutions(workflowType: "employee-onboarding", limit: 25) {
    items {
      executionId
      status
      requestedAt
    }
    nextToken
  }
}
```

**Cancel a run** (owner only):

```graphql
mutation Cancel {
  cancelWorkflowExecution(executionId: "PASTE_EXECUTION_ID") {
    executionId
    status
  }
}
```

**List all runs of a workflow across callers** (admin):

```graphql
query ListAll {
  listWorkflowExecutionsByType(workflowType: "employee-onboarding", limit: 50) {
    items {
      executionId
      requesterSubject
      requesterPrincipal
      status
    }
    nextToken
  }
}
```

## Construct props

All props are optional. Pass them in the object given to `new WorkflowCatalog(this, "WorkflowCatalog", { ... })`.

| Prop                     | Purpose                                                                         |
| ------------------------ | ------------------------------------------------------------------------------- |
| `userPool`               | Existing `cognito.IUserPool` to add as an additional auth mode                  |
| `adminGroups`            | Cognito group names allowed to call admin fields (required for frontend admins) |
| `adminRoleArns`          | Role ARNs to attach the admin access policy to                                  |
| `callerRoleArns`         | Role ARNs to attach the caller access policy to                                 |
| `executionRetention`     | How long terminal execution records are kept (TTL)                              |
| `reconciliationInterval` | How often the reconciler runs                                                   |
| `requireWorkflowTypeTag` | Require the `workflowType` tag for discovery (default true)                     |
| `requireExplicitSchema`  | Require an explicit contract before enabling (default true)                     |
| `verboseApiLogging`      | Log full request/response content to CloudWatch (default false; see note below) |
| `removalPolicy`          | Removal policy for tables/log groups (default `DESTROY`; use `RETAIN` for prod) |
| `deletionProtection`     | AWS deletion protection on the DynamoDB tables (default false; see note below)  |
| `resourceNamePrefix`     | Prefix for physical resource names                                              |

> `verboseApiLogging` defaults to **false** on purpose. The caller's `parameters` payload is
> arbitrary workflow input that may contain sensitive data, and it is already persisted
> (encrypted, with a TTL) in the execution tracker table — logging it again to CloudWatch
> widens exposure for little benefit. Field-level `ERROR` logging and X-Ray tracing stay on
> regardless. Enable it only for debugging or audit regimes on known-low-sensitivity workflows.

> **Teardown vs. production:** `removalPolicy` defaults to `DESTROY` and `deletionProtection` to
> `false` so the sample tears down cleanly with `cdk destroy`. For production, set
> `removalPolicy: RemovalPolicy.RETAIN` and `deletionProtection: true` to protect the
> execution/registry data (with deletion protection on, you must set it back to `false` and
> redeploy before a later `cdk destroy`).
