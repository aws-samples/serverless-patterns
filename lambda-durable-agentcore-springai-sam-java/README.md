# Human-in-the-loop AI review with AWS Lambda durable functions and Amazon Bedrock AgentCore

This pattern shows how an AWS Lambda durable function written in Java can orchestrate a Spring AI agent hosted on Amazon Bedrock AgentCore Runtime, and pause partway through to wait for a person to approve or reject the agent's work.

The durable function asks the agent to draft a summary of a document, then suspends. It resumes only when a human sends a decision, and asks the agent for a final version if the review was approved. While suspended the function consumes no compute and can wait for days.

Learn more about this pattern at Serverless Land Patterns: << Add the live URL here >>

Important: this application uses various AWS services and there are costs associated with these services after the Free Tier usage - please see the [AWS Pricing page](https://aws.amazon.com/pricing/) for details. You are responsible for any AWS costs incurred. No warranty is implied in this example.

## Requirements

* [Create an AWS account](https://portal.aws.amazon.com/gp/aws/developer/registration/index.html) if you do not already have one and log in. The IAM user that you use must have sufficient permissions to make necessary AWS service calls and manage AWS resources.
* [AWS CLI](https://docs.aws.amazon.com/cli/latest/userguide/install-cliv2.html) installed and configured
* [Git Installed](https://git-scm.com/book/en/v2/Getting-Started-Installing-Git)
* [AWS Serverless Application Model](https://docs.aws.amazon.com/serverless-application-model/latest/developerguide/serverless-sam-cli-install.html) (AWS SAM) installed, **version 1.161.0 or later**
* [Java 21](https://docs.aws.amazon.com/corretto/latest/corretto-21-ug/downloads-list.html) and [Apache Maven](https://maven.apache.org/install.html) 3.9 or later
* [Docker](https://docs.docker.com/get-docker/), [Finch](https://runfinch.com/), nerdctl or Podman, to build the agent container image
* An Amazon Bedrock model available in the target Region. The default is `us.anthropic.claude-sonnet-4-5-20250929-v1:0`. Check availability with `aws bedrock get-foundation-model-availability --model-id <id> --region <region>`; if it reports anything other than `AUTHORIZED`, enable it under **Model access** in the Amazon Bedrock console.

## Deployment Instructions

1. Create a new directory, navigate to that directory in a terminal and clone the GitHub repository:

    ```bash
    git clone https://github.com/aws-samples/serverless-patterns
    ```

1. Change directory to the pattern directory:

    ```bash
    cd serverless-patterns/lambda-durable-agentcore-springai-sam-java
    ```

1. Build and push the agent container image. AgentCore Runtime can host plain source code only for Python and Node runtimes, so the Java agent is delivered as an ARM64 container image:

    ```bash
    ./scripts/build-agent-image.sh
    ```

    The script prints the image URI it pushed. Copy it - you need it in the next step.

    > The image must exist in Amazon ECR before the stack is deployed, because `AWS::BedrockAgentCore::Runtime` refers to it directly. `sam build` cannot produce it: SAM's `Metadata: Dockerfile` support applies only to `PackageType: Image` Lambda functions and builds for the host architecture.

1. Build the durable function and deploy:

    ```bash
    sam build
    sam deploy --guided
    ```

    Accept the defaults, and paste the image URI from the previous step when prompted for `AgentImageUri`. Answer `y` when asked to allow SAM CLI to create IAM roles.

1. Note the `WorkflowFunctionName` output - the testing commands below use it.

## How it works

```
aws lambda invoke  ──►  ReviewWorkflowFunction (durable)
                              │
                              │  step "analyze-document"
                              │      └──►  AgentCore Runtime
                              │            (Spring AI agent, ARM64 container)
                              │
                              │  waitForCallback "await-human-review"
                              │
                              ⋮   ~~ suspended: no compute billed ~~
                              │
aws lambda send-durable- ─────┤  resumes with the decision
execution-callback-success    │
                              │  step "finalize-document"   (only if approved)
                              │
                              ▼
                          returns ReviewResult
```

The workflow is [`DocumentReviewWorkflow.java`](orchestrator/src/main/java/com/example/durableagent/DocumentReviewWorkflow.java). In Java the durable programming model is based on inheritance rather than annotations: the handler extends `DurableHandler<I, O>` and receives a `DurableContext`.

### Steps

Every durable operation in Java takes an explicit name and a result type token:

```java
String draft = ctx.step("analyze-document", String.class,
        stepCtx -> agent.invoke(documentId, "analyze", request.documentText(), null, null));
```

The name is how replay matches a new invocation to previously checkpointed state, so names must be stable across deployments. Once a step has completed its result is recorded, and later invocations reuse that value instead of running the body again - which is what stops an expensive agent call from being repeated.

### Waiting for a human

`waitForCallback` creates a callback, runs a submitter that hands the callback ID to the outside world, and then suspends the execution:

```java
Decision decision = ctx.waitForCallback("await-human-review", Decision.class,
        (callbackId, stepCtx) -> announceReviewRequest(callbackId, request, draft),
        WaitForCallbackConfig.builder()
                .callbackConfig(CallbackConfig.builder()
                        .timeout(Duration.ofHours(24))
                        .build())
                .build());
```

Note that `WaitForCallbackConfig` nests a `CallbackConfig` rather than taking a timeout directly. Because the submitter runs as a step, the SDK retries it if it fails.

To keep the pattern focused, the submitter simply writes the callback ID and the agent's draft to the function log, and you resume the workflow with the AWS CLI. A production workflow would notify the reviewer out of band - email, chat, a ticket.

If you add a notification with an approval link, do not let the link itself record the decision. Mail clients and security scanners prefetch URLs, so a `GET` that decides will be actioned by a scanner rather than by your approver. Render a confirmation page on `GET` and act only on the `POST` it submits.

#### Approve and reject are both callback successes

Both decisions are delivered with `SendDurableExecutionCallbackSuccess`. The success/failure axis of the callback API describes whether a decision was *obtained*, not whether the answer was favourable - a reviewer who rejects a document has successfully decided. `SendDurableExecutionCallbackFailure` is for the case where no decision can be produced at all, such as an abandoned review, and surfaces in the workflow as a thrown exception rather than a value.

The workflow keeps those two ideas in separate fields, so "the reviewer said no" is never confused with "nobody answered":

| Field | Values | Meaning |
|---|---|---|
| `outcome` | `DECIDED`, `EXPIRED` | Was a decision obtained at all? |
| `decision` | `APPROVED`, `REJECTED`, null | What the reviewer chose. Null when `outcome` is `EXPIRED`. |

Carrying the verdict as data also keeps replay deterministic: the workflow branches on the checkpointed callback result, so every replay takes the same path.

### Where the state lives

There is no table to provision. Lambda checkpoints every durable operation - step results, the pending callback, and the handler's return value - into storage the service manages, kept for `DurableConfig.RetentionPeriodInDays` after the execution ends. `get-durable-execution` and `get-durable-execution-history` read it back.

### The agent

[`ReviewAgentController`](agent/src/main/java/com/example/agent/ReviewAgentController.java) is an ordinary Spring `@RestController`. The [`spring-ai-agentcore-runtime-starter`](https://github.com/spring-ai-community/spring-ai-agentcore) auto-configures the `POST /invocations` and `GET /ping` endpoints that AgentCore requires, so the agent is a single annotated method:

```java
@AgentCoreInvocation
public String handleInvocation(AgentRequest request, AgentCoreContext agentCoreContext) { ... }
```

Returning a `String` rather than a `Flux` produces a single non-streaming response, which is what the calling step expects. One runtime serves both steps: the request carries a `mode` of `analyze` or `finalize` and the controller selects the system prompt.

Both agent calls reuse one `runtimeSessionId`, so the agent still has the analyze turn in context when it writes the final version. AgentCore requires session IDs of at least 33 characters; `AgentClient.sessionIdFor` prefixes the document ID and right-pads it to that length, keeping the document ID legible at the front for anyone reading AgentCore's logs. It has to be a pure function of the document ID - a fresh `UUID` would hand the agent a different session on every replay, losing the earlier turn.

Note that the AgentCore starter is a community project under `org.springaicommunity`, published to Maven Central and Apache-2.0 licensed - not an official Spring AI or AWS module - and it requires Spring Boot 4.1 or later. To avoid the dependency, write the two endpoints yourself as plain Spring Web handlers: the contract is a `POST` that takes and returns JSON, and a `GET` that returns `{"status":"Healthy"}`, on port 8080.

### Timeouts

`DurableConfig.ExecutionTimeout` is 7 days and the callback timeout is 24 hours. The execution timeout must always exceed the longest callback timeout, otherwise the execution would expire while still waiting for a decision. If nobody responds in 24 hours the callback raises `CallbackTimeoutException`, which the workflow catches and reports as `outcome: EXPIRED`.

## Testing

### Run the unit tests

The durable execution SDK ships an in-memory test runner, so all three outcomes can be verified with no AWS account:

```bash
cd orchestrator && mvn test
```

These drive the workflow through approve, reject and timeout, and assert that the agent's analyze step runs exactly once even though the handler body executes again after the callback resumes it - that is, that replay really does skip completed work.

### Start a review

Use the `WorkflowFunctionName` from the stack outputs. `--durable-execution-name` names the execution so you can find it again; `--invocation-type Event` starts it asynchronously so the CLI returns immediately.

```bash
aws lambda invoke \
    --function-name <WorkflowFunctionName>:live \
    --region <your-region> \
    --invocation-type Event \
    --durable-execution-name review-001 \
    --payload fileb://events/submit-document.json \
    response.json
```

### Find the callback ID

Give the workflow a moment first. The agent call takes roughly 10-15 seconds, and the callback only exists once `analyze-document` has finished - so this query returns nothing if you run it immediately. Wait about 30 seconds, and retry if the output is empty.

Run these in the same shell, since `$ARN` is reused by the commands below.

```bash
ARN=$(aws lambda list-durable-executions-by-function \
    --function-name <WorkflowFunctionName> \
    --region <your-region> \
    --durable-execution-name review-001 \
    --query 'DurableExecutions[0].DurableExecutionArn' --output text)

aws lambda get-durable-execution-history \
    --durable-execution-arn "$ARN" \
    --region <your-region> \
    --query 'Events[?EventType==`CallbackStarted`].CallbackStartedDetails.CallbackId' \
    --output text
```

To confirm the workflow is suspended and waiting rather than still working, check its status - `RUNNING` with `analyze-document` already succeeded means it is parked at the callback:

```bash
aws lambda get-durable-execution --durable-execution-arn "$ARN" \
    --region <your-region> --query 'Status' --output text
```

The agent's draft is also printed to the function log, along with ready-to-paste approve and reject commands:

```bash
sam logs --stack-name <your-stack-name> --region <your-region> --tail
```

### Approve

Write whatever comments the draft actually warrants - they are passed to the agent for the finalize step, so this is where you see the agent do something with your input. The draft ends with a list of concerns for the reviewer to check; answering some of those is the most interesting thing to put here, because you can then watch those answers appear in the final summary and the questions themselves disappear.

```bash
aws lambda send-durable-execution-callback-success \
    --region <your-region> \
    --callback-id <callback-id> \
    --cli-binary-format raw-in-base64-out \
    --result '{"decision":"approved","comments":"<your review comments>"}'
```

Comments are optional - `"comments":""` works, and the finalize step then just polishes the draft rather than incorporating anything.

### Reject

Reject is also a callback *success* - the decision is data, not a failure. Again, the comments are yours to write; they are recorded on the result, though the agent is not called again because the finalize step is skipped:

```bash
aws lambda send-durable-execution-callback-success \
    --region <your-region> \
    --callback-id <callback-id> \
    --cli-binary-format raw-in-base64-out \
    --result '{"decision":"rejected","comments":"<why you are rejecting it>"}'
```

To abandon a review instead of deciding it, send a failure:

```bash
aws lambda send-durable-execution-callback-failure \
    --region <your-region> \
    --callback-id <callback-id> \
    --error ErrorType=ReviewAbandoned,ErrorMessage="No reviewer available"
```

### Read the result

```bash
aws lambda get-durable-execution --durable-execution-arn "$ARN" \
    --region <your-region> --query '[Status,Result]' --output text
```

An approved review returns `outcome: DECIDED`, `decision: APPROVED` and a `finalSummary`. A rejected one returns `decision: REJECTED` with no `finalSummary`, because the finalize step is skipped. A review nobody answered returns `outcome: EXPIRED` with a null `decision`. Confirm the branching in the history - `finalize-document` appears only on approval:

```bash
aws lambda get-durable-execution-history --durable-execution-arn "$ARN" \
    --region <your-region> --query 'Events[?EventType==`StepStarted`].Name' --output text
```

Run a few reviews with different `--durable-execution-name` values and decide them differently to see both paths.

### Test the agent on its own

The agent is a normal Spring Boot application, so you can exercise the AgentCore container contract locally before building an image:

```bash
cd agent && mvn package
java -jar target/document-review-agent.jar
```

```bash
curl localhost:8080/ping
# {"time_of_last_update":...,"status":"Healthy"}

curl -X POST localhost:8080/invocations \
    -H 'Content-Type: application/json' \
    -H 'X-Amzn-Bedrock-AgentCore-Runtime-Session-Id: local-test-session-0000000000000000' \
    -d '{"mode":"analyze","document":"Q3 budget: 4 more engineers, 620k USD."}'
```

This needs AWS credentials in the shell, because the agent calls Amazon Bedrock.

## Cleanup

1. Delete the stack:

    ```bash
    sam delete
    ```

1. Delete the agent images and repository, which the build script created outside the stack:

    ```bash
    aws ecr delete-repository --repository-name document-review-agent \
        --region <your-region> --force
    ```

----

Copyright 2025 Amazon.com, Inc. or its affiliates. All Rights Reserved.

SPDX-License-Identifier: MIT-0
