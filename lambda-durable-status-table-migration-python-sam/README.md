# Migrate a long-running job from a status table and poller to Lambda durable functions (Python)

You have a job that is too long or too fragile for one Lambda invocation, so you built the usual workaround: write a row to a "jobs" table, have a poller pick it up, run the steps, and update the row after each one so a crash can be resumed. Clients poll `GET /jobs/{id}` to see where it is.

This pattern shows the same job twice. `before/` is that status-table version. `after/` is the same job as a Lambda durable function: each step is checkpointed by the runtime, retries use a built-in policy, and the public `job_id` is the durable execution name, so the API and its clients do not change. Both halves deploy side by side (`/v1` and `/v2`) so you can cut over without downtime, then remove the old half with one parameter.

### What is a durable function?

A normal Lambda invocation is all or nothing: crash at minute eight and it restarts from line one. A *durable execution* is one logical run of a Lambda function that the runtime can pause, resume and retry across many invocations. You wrap each unit of work in `context.step(...)`. When a step returns, the runtime writes a *checkpoint* (the step's result). If the execution is interrupted, the runtime *replays* your function from the top; each `context.step()` whose checkpoint exists returns the saved result without running the body, so execution picks up at the first unfinished step.

Every execution has a *name*, unique per function. Invoking again with a name that already exists returns the existing execution instead of starting a second one. This pattern uses the public `job_id` as that name, which is the idempotency the `before/` code gets only from its `attribute_not_exists(job_id)` conditional put.

Learn more about this pattern at Serverless Land Patterns: [https://serverlessland.com/patterns/lambda-durable-status-table-migration-python-sam](https://serverlessland.com/patterns/lambda-durable-status-table-migration-python-sam)

Important: this application uses various AWS services and there are costs associated with these services after the Free Tier usage - please see the [AWS Pricing page](https://aws.amazon.com/pricing/) for details. You are responsible for any AWS costs incurred. No warranty is implied in this example.

## Requirements

- [Create an AWS account](https://portal.aws.amazon.com/gp/aws/developer/registration/index.html) if you do not already have one and log in. The IAM user that you use must have sufficient permissions to make necessary AWS service calls and manage AWS resources.
- [AWS CLI](https://docs.aws.amazon.com/cli/latest/userguide/install-cliv2.html) installed and configured
- [Git Installed](https://git-scm.com/book/en/v2/Getting-Started-Installing-Git)
- [AWS Serverless Application Model](https://docs.aws.amazon.com/serverless-application-model/latest/developerguide/serverless-sam-cli-install.html) (AWS SAM) installed
- [Python 3.13](https://www.python.org/downloads/) installed and available in your PATH

## Deployment Instructions

1. Create a new directory, navigate to that directory in a terminal and clone the GitHub repository:
   ```
   git clone https://github.com/aws-samples/serverless-patterns
   ```
1. Change directory to the pattern directory:
   ```
   cd lambda-durable-status-table-migration-python-sam
   ```
1. From the command line, use AWS SAM to build and deploy the AWS resources for the pattern as specified in the template.yaml file:
   ```
   sam build
   sam deploy --guided
   ```
1. During the prompts:
   - Enter a stack name
   - Enter the desired AWS Region
   - Allow SAM CLI to create IAM roles with the required permissions.

   Once you have run `sam deploy --guided` once and saved arguments to a configuration file (samconfig.toml), you can use `sam deploy` in future to use these defaults.

1. Note the `ApiUrl` output. `/v1/jobs` is the status-table version, `/v2/jobs` is the durable version.

## How it works

Both halves run the same three business steps from `steps.py`: `fetch_source`, `transform`, and `publish_result`. Only the orchestration around them changes.

`transform` raises a `TransientError` on attempt 1 for any input containing the word `flaky`, then succeeds on attempt 2. It stands in for a throttle or timeout from a dependency. It is keyed off the attempt number the caller passes in (the hand-kept `attempts` counter in `before/`, `step.attempt` from the runtime in `after/`), so it behaves the same whether the retry lands in a warm or a cold execution environment.

| | Before: status table + poller | After: durable function |
|---|---|---|
| Start a job | `PUT` a `PENDING` row | `Invoke` with `DurableExecutionName=job_id` |
| Run the steps | A scheduled poller scans for `PENDING` rows, claims one with a conditional update, runs the steps | The durable function runs the steps; the runtime checkpoints each `context.step()` |
| Survive a crash | Poller checks for stale `RUNNING` rows and re-runs, skipping steps whose output is already in the row | Runtime replays the function and skips completed steps |
| Retry a flaky step | Hand-written attempt counter, no backoff | `StepConfig(retry_strategy=RetryPresets.transient())` |
| Read status | `GET` the row | `GetDurableExecution` on the stored execution ARN |
| Current step | `step` field in the row | Not in the status response; read it from `get-durable-execution-history` |
| What the table holds | Status, current step, every step's output, attempts, error, result | `job_id -> execution_arn` only |

`before/worker.py` is about 120 lines, almost all of it bookkeeping. `after/job.py` is about 65, almost all of it the steps.

```
                    +------------------------+
   client --------> |  API Gateway  /prod    |
                    |  /v1/jobs   /v2/jobs   |
                    +-----+-------------+----+
                          |             |
            BEFORE        v             v        AFTER
     +--------------------+--+     +----+-----------------------+
     | LegacyJobApiFunction  |     | JobApiFunction             |
     | put PENDING / get row |     | Invoke(DurableExecution-   |
     +-----------+-----------+     |   Name=job_id) / GetDurable|
                 |                 |   Execution(arn)           |
   rate(1 min)   v                 +----+------------------+----+
  +--------------+--------+             |                  |
  | LegacyJobWorkerFunction|            v                  |
  | scan, claim, run steps,|   +--------+----------+       |
  | checkpoint each step   |   | JobFunction (durable) |   |
  +-----------+------------+   | step fetch_source     |   |
              |                | step transform  (retry)|  |
              |                | step publish_result   |   |
              |                +--------+--------------+   |
              v                         |  checkpoints held |
     +--------+-------------------------v-------------------v-+
     | JobsTable (DynamoDB, TTL 3d)                            |
     | BEFORE row: status, step, outputs, attempts, result     |
     | AFTER  row: execution_arn only                          |
     +---------------------------------------------------------+
```

What replay looks like against this code: if the execution is interrupted right after `transform` finishes, the runtime re-invokes the function. `context.step(..., name="fetch_source")` and `name="transform"` return their checkpoints without running; only `publish_result` executes. The `before/` equivalent is the three `if "x" not in outputs` guards in `worker.py`. The durable runtime is doing that bookkeeping for you.

Two things the runtime does not do for you:

- **At-least-once steps.** A step whose invocation dies between the body finishing and the checkpoint landing runs again on replay. `publish_result` is safe here because the stand-in has no external effect. A real publish to a non-idempotent sink needs an idempotency key minted in an earlier step, or `StepConfig(step_semantics=StepSemantics.AT_MOST_ONCE_PER_RETRY, ...)`.
- **No automatic retry of a failed execution.** Unlike a plain async Lambda invoke, a durable execution that ends `FAILED`, `TIMED_OUT` or `STOPPED` is not re-run. The triggering event goes to `JobDeadLetterQueue` instead; the `before/` poller would have requeued it, so the queue is where that work now lands.

### Cutover with no API change

1. Deploy. Both `/v1` and `/v2` are live and share the jobs table.
2. Point clients' `POST` at `/v2/jobs`. Leave their `GET` polling as is: `/v2/jobs/{id}` answers for both old rows (no execution ARN, served from the row, marked `"legacy": true`) and new jobs (served from the durable execution). The response keeps the `job_id`, `status`, `result` and `error` fields. The `step` field is only present for legacy rows: for durable jobs, step progress lives in the execution history, not the status call.
3. The old poller keeps running and drains in-flight `/v1` jobs. When the table has no rows without an `execution_arn`, redeploy with `--parameter-overrides EnableLegacy=false`. That removes the `/v1` API and the poller; nothing else changes.

In-flight executions keep running on the function version they started on; a redeploy moves the `live` alias so only new jobs get new code. Do not rename or change the behaviour of the three steps while jobs are in flight: replay matches steps by name, and a renamed step cannot resume.

The shared table has a 3-day TTL set at job creation and never refreshed. A `/v1` job that sits in the queue or retries for longer than that is deleted mid-flight, and a deleted row also makes the table look drained when it is not. Keep the TTL longer than the longest a legacy job can take, or drop it until cutover is done.

Durable execution status is mapped back to the old API's words (`SUCCEEDED -> DONE`, `TIMED_OUT`/`STOPPED` -> `FAILED`) so existing clients need no change.

## Testing

### Locally, without deploying

The durable half runs in the SDK's in-memory test runner. This proves the step wiring and the retry without an AWS account:

```
pip install -r tests/requirements.txt
pytest tests/
```

The second test submits a `flaky` input and asserts the `transform` step reports `attempt == 2` while its neighbours ran once.

### Deployed

Set the base URL from the stack output:

```
API=$(aws cloudformation describe-stacks --stack-name <stack-name> --query "Stacks[0].Outputs[?OutputKey=='ApiUrl'].OutputValue" --output text)
```

1. Start a job on each half with the same input:
   ```
   curl -s -X POST $API/v1/jobs -d '{"job_id":"old-1","input":"this one is flaky"}'
   curl -s -X POST $API/v2/jobs -d '{"job_id":"new-1","input":"this one is flaky"}'
   ```
1. Poll both. The `/v1` job waits for the next one-minute poll, fails once on `transform`, goes back to `PENDING`, and finishes on the following poll (two to three minutes). The `/v2` job retries within seconds:
   ```
   curl -s $API/v1/jobs/old-1
   curl -s $API/v2/jobs/new-1
   ```
1. Retry the `/v2` start with the same `job_id`. It is idempotent: no second execution is created.
   ```
   curl -s -X POST $API/v2/jobs -d '{"job_id":"new-1","input":"this one is flaky"}'
   FN=$(aws cloudformation describe-stacks --stack-name <stack-name> --query "Stacks[0].Outputs[?OutputKey=='JobFunctionAlias'].OutputValue" --output text)
   aws lambda list-durable-executions-by-function --function-name ${FN%:live} --durable-execution-name new-1 --query 'length(DurableExecutions)'
   ```
   Prints `1`.
1. Confirm the cutover path: read the `/v1` job through the `/v2` endpoint.
   ```
   curl -s $API/v2/jobs/old-1
   ```
   The response carries `"legacy": true` and is served from the row.
1. Inspect the durable execution's step history. This is where the current step lives now. Look for `StepFailed` then `StepSucceeded` on `transform`:
   ```
   TABLE=$(aws cloudformation describe-stacks --stack-name <stack-name> --query "Stacks[0].Outputs[?OutputKey=='JobsTableName'].OutputValue" --output text)
   ARN=$(aws dynamodb get-item --table-name $TABLE --key '{"job_id":{"S":"new-1"}}' --query 'Item.execution_arn.S' --output text)
   aws lambda get-durable-execution-history --durable-execution-arn $ARN --query 'Events[].EventType'
   ```
1. Finish the cutover: remove the `/v1` half.
   ```
   sam deploy --parameter-overrides EnableLegacy=false
   ```

## Cleanup

1. Delete the stack
   ```
   sam delete
   ```

----
Copyright 2026 Amazon.com, Inc. or its affiliates. All Rights Reserved.

SPDX-License-Identifier: MIT-0
