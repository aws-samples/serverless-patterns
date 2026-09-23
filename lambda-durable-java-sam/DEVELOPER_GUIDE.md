# Lambda Durable Functions in Java - Developer Guide

## Table of Contents

1. [Architecture Overview](#architecture-overview)
2. [The Durable Execution Model](#the-durable-execution-model)
3. [Java SDK Reference](#java-sdk-reference)
4. [DurableHandler Base Class](#durablehandler-base-class)
5. [Durable Operations](#durable-operations)
6. [Error Handling and Retries](#error-handling-and-retries)
7. [Deployment Model](#deployment-model)
8. [Best Practices](#best-practices)
9. [Testing](#testing)
10. [Common Pitfalls](#common-pitfalls)

> **Tip:** For visual step-by-step flow diagrams of each pattern, see [DIAGRAMS.md](DIAGRAMS.md).

---

## Architecture Overview

```
┌─────────────────────────────────────────────────────────────────┐
│                        AWS Cloud                                  │
│                                                                   │
│  ┌───────────┐     ┌──────────────────────────────────────────┐ │
│  │ SNS Topic │────>│ Lambda Durable Function                   │ │
│  └───────────┘     │                                            │ │
│       ▲            │  ┌─────────┐  ┌─────────┐  ┌─────────┐  │ │
│       │            │  │ Step 1  │─>│ Step 2  │─>│ Step 3  │  │ │
│  ┌────┴────┐       │  │(chkpt)  │  │(chkpt)  │  │(chkpt)  │  │ │
│  │Producer │       │  └─────────┘  └─────────┘  └─────────┘  │ │
│  │(EC2/CLI)│       │       │            │            │         │ │
│  └─────────┘       │       ▼            ▼            ▼         │ │
│                    │  ┌────────────────────────────────────┐   │ │
│                    │  │      Checkpoint Store (managed)     │   │ │
│                    │  └────────────────────────────────────┘   │ │
│                    └──────────────────────────────────────────┘ │
│                         │                                        │
│                         ▼                                        │
│                    ┌──────────┐                                   │
│                    │ DynamoDB │                                   │
│                    └──────────┘                                   │
└─────────────────────────────────────────────────────────────────┘
```

### Components

| Component | Role |
|-----------|------|
| **SNS Topic** | Event source that triggers the durable functions |
| **Lambda Durable Functions** | Business logic with automatic checkpointing |
| **Checkpoint Store** | Managed by Lambda; stores step results and execution state |
| **DynamoDB** | Optional application state for this workshop |
| **ECR** | Container registry for the Java function images |
| **Producer (EC2/CLI)** | Sends messages to SNS to trigger workflows |

---

## The Durable Execution Model

### Lifecycle of a Durable Execution

```
1. INVOKE         → Function starts, SDK initializes
2. EXECUTE STEP   → Business logic runs inside ctx.step()
3. CHECKPOINT     → Result saved to checkpoint store
4. WAIT/SUSPEND   → Function exits, no compute charges
5. RESUME         → Backend re-invokes the function
6. REPLAY         → SDK runs from top, skips checkpointed steps
7. CONTINUE       → Execution continues from where it left off
```

### Replay: The Core Mechanism

When a durable function resumes (after a wait, retry delay, or interruption), the SDK uses **replay**:

1. Your code runs from the **beginning** of `handleRequest()`
2. When it hits a `step()` that already has a checkpoint, the SDK returns the **stored result** instantly
3. When it hits the first un-checkpointed operation, normal execution resumes

This means your code must be **deterministic** between steps. Do NOT:
- Use `System.currentTimeMillis()` or `Math.random()` outside of steps
- Mutate external state outside of steps
- Branch on non-deterministic values between steps

### What Goes Inside a Step vs. Outside

| Inside `context.step()` | Outside steps |
|--------------------------|---------------|
| API calls | Control flow (if/else, loops) |
| Database operations | Variable assignments from step results |
| Current time / random values | Logging via `context.getLogger()` |
| Side effects (notifications) | Calling other durable operations |
| Non-deterministic code | Pure computation on step results |

---

## Java SDK Reference

### Maven Dependency

```xml
<dependency>
    <groupId>software.amazon.lambda.durable</groupId>
    <artifactId>aws-durable-execution-sdk-java</artifactId>
    <version>1.0.0</version>
</dependency>
```

### Key Packages

```java
import software.amazon.lambda.durable.DurableContext;
import software.amazon.lambda.durable.DurableHandler;
import software.amazon.lambda.durable.DurableFuture;
import software.amazon.lambda.durable.DurableCallbackFuture;
import software.amazon.lambda.durable.StepContext;
import software.amazon.lambda.durable.TypeToken;

import software.amazon.lambda.durable.config.StepConfig;
import software.amazon.lambda.durable.config.StepSemantics;
import software.amazon.lambda.durable.config.CallbackConfig;
import software.amazon.lambda.durable.config.WaitForCallbackConfig;
import software.amazon.lambda.durable.config.ParallelConfig;
import software.amazon.lambda.durable.config.MapConfig;
import software.amazon.lambda.durable.config.CompletionConfig;
import software.amazon.lambda.durable.config.WaitForConditionConfig;
import software.amazon.lambda.durable.config.RunInChildContextConfig;
import software.amazon.lambda.durable.config.InvokeConfig;

import software.amazon.lambda.durable.retry.RetryStrategies;
import software.amazon.lambda.durable.retry.RetryStrategy;
import software.amazon.lambda.durable.retry.RetryDecision;
import software.amazon.lambda.durable.retry.JitterStrategy;
import software.amazon.lambda.durable.retry.WaitStrategies;
import software.amazon.lambda.durable.retry.WaitForConditionWaitStrategy;

import software.amazon.lambda.durable.model.ParallelResult;
import software.amazon.lambda.durable.model.MapResult;
import software.amazon.lambda.durable.model.WaitForConditionResult;

import software.amazon.lambda.durable.exception.StepFailedException;
import software.amazon.lambda.durable.exception.StepInterruptedException;
import software.amazon.lambda.durable.exception.CallbackFailedException;
import software.amazon.lambda.durable.exception.DurableOperationException;
```

---

## DurableHandler Base Class

Every durable function extends `DurableHandler<I, O>`:

```java
public class MyHandler extends DurableHandler<Map<String, Object>, Map<String, Object>> {
    @Override
    public Map<String, Object> handleRequest(Map<String, Object> event, DurableContext context) {
        // Your durable workflow here
        return result;
    }
}
```

- `I` = Input type (the Lambda event)
- `O` = Output type (the return value)
- `DurableContext` replaces the standard Lambda `Context`

### DurableContext Methods

| Method | Description |
|--------|-------------|
| `step(name, resultType, func)` | Execute and checkpoint a unit of work |
| `stepAsync(name, resultType, func)` | Non-blocking step, returns `DurableFuture<T>` |
| `wait(name, duration)` | Suspend for a duration (no compute) |
| `waitAsync(name, duration)` | Non-blocking wait |
| `waitForCondition(name, type, checkFunc, config)` | Poll until condition met |
| `createCallback(name, resultType)` | Create a callback and suspend |
| `waitForCallback(name, resultType, func)` | Create + submit + wait in one call |
| `parallel(name)` | Execute branches concurrently |
| `map(name, items, resultType, func)` | Process collection concurrently |
| `runInChildContext(name, resultType, func)` | Isolated sub-workflow |
| `runInChildContextAsync(name, resultType, func)` | Non-blocking sub-workflow |
| `invoke(name, functionName, payload, resultType)` | Call another Lambda function |
| `getLogger()` | Replay-aware logger |

---

## Durable Operations

### Step

The fundamental building block. Executes code and checkpoints the result.

```java
// Basic step
String result = context.step("my-step", String.class, stepCtx -> {
    return "computed value";
});

// Step with retry configuration
StepConfig config = StepConfig.builder()
    .retryStrategy(RetryStrategies.exponentialBackoff(
        5,                          // maxAttempts
        Duration.ofSeconds(2),      // initialDelay
        Duration.ofMinutes(1),      // maxDelay
        2.0,                        // backoffRate
        JitterStrategy.FULL))       // jitter
    .build();

Map<String, Object> result = context.step("api-call", Map.class, stepCtx -> {
    return callExternalApi();
}, config);
```

**StepContext** provides:
- `stepCtx.getLogger()` - Durable logger
- `stepCtx.getAttempt()` - Current retry attempt (0-based)
- `stepCtx.isReplaying()` - Whether this is a replay

### Wait

Suspends execution without compute charges.

```java
// Fixed delay
context.wait("delay-30s", Duration.ofSeconds(30));

// Async wait (minimum duration pattern)
DurableFuture<Void> timer = context.waitAsync("min-5s", Duration.ofSeconds(5));
DurableFuture<String> work = context.stepAsync("process", String.class, ctx -> doWork());
timer.get();      // Ensure at least 5s elapsed
String r = work.get();  // Get the work result
```

### Wait for Condition (Polling)

Polls an external system with configurable backoff.

```java
WaitForConditionWaitStrategy<Map<String, Object>> strategy = (state, attempt) -> {
    if (attempt >= 20) throw new RuntimeException("Timeout");
    return Duration.ofSeconds(Math.min(5 * (long)Math.pow(2, attempt - 1), 300));
};

Map<String, Object> finalState = context.waitForCondition(
    "poll-status",
    new TypeToken<>() {},
    (state, stepCtx) -> {
        String status = checkStatus((String) state.get("id"));
        Map<String, Object> updated = Map.of("id", state.get("id"), "status", status);
        if ("DONE".equals(status)) {
            return WaitForConditionResult.stopPolling(updated);
        }
        return WaitForConditionResult.continuePolling(updated);
    },
    WaitForConditionConfig.<Map<String, Object>>builder()
        .initialState(Map.of("id", "job-123", "status", "PENDING"))
        .waitStrategy(strategy)
        .build()
);
```

### Callback (Human Interaction)

Suspend and wait for an external system to respond.

```java
// Approach 1: Manual callback
DurableCallbackFuture<Map<String, String>> callback =
    context.createCallback("wait-approval", (Class<Map<String, String>>)(Class<?>)Map.class,
        CallbackConfig.builder().timeout(Duration.ofHours(72)).build());

// Send callback.callbackId() to the approver
notifyApprover(callback.callbackId());

// Execution suspends here until external callback arrives
Map<String, String> decision = callback.get();

// Approach 2: Composite (create + submit + wait)
String result = context.waitForCallback("approval", String.class,
    (callbackId, stepCtx) -> sendApprovalEmail(callbackId));
```

**External system completes callback via AWS CLI:**
```bash
aws lambda send-durable-execution-callback-success \
  --callback-id <id> --result '{"approved":true}'
```

### Parallel (Fan-Out/Fan-In)

Execute different operations concurrently.

```java
DurableFuture<String> aFuture;
DurableFuture<Integer> bFuture;

try (var parallel = context.parallel("my-parallel")) {
    aFuture = parallel.branch("branch-a", String.class, ctx ->
        ctx.step("work-a", String.class, s -> computeA()));
    bFuture = parallel.branch("branch-b", Integer.class, ctx ->
        ctx.step("work-b", Integer.class, s -> computeB()));
    ParallelResult result = parallel.get();
    // result.succeeded(), result.failed()
}

String a = aFuture.get();
int b = bFuture.get();
```

**Configuration options:**
```java
ParallelConfig config = ParallelConfig.builder()
    .maxConcurrency(5)
    .completionConfig(CompletionConfig.firstSuccessful())  // Race pattern
    .build();
```

### Map (Collection Processing)

Apply the same operation to every item in a collection.

```java
MapResult<String> result = context.map(
    "process-items",
    List.of("a", "b", "c"),
    String.class,
    (item, index, ctx) -> ctx.step("transform-" + index, String.class,
        s -> item.toUpperCase()),
    MapConfig.builder()
        .maxConcurrency(3)
        .completionConfig(CompletionConfig.toleratedFailureCount(1))
        .build()
);

List<String> successes = result.succeeded();
```

### Child Context (Sub-Orchestration)

Isolate groups of operations into reusable sub-workflows.

```java
// Sequential sub-workflow
Map<String, Object> result = context.runInChildContext(
    "payment-flow", Map.class,
    child -> {
        String auth = child.step("authorize", String.class, s -> authorize());
        child.wait("delay", Duration.ofSeconds(2));
        return child.step("capture", Map.class, s -> capture(auth));
    });

// Concurrent sub-workflows
DurableFuture<String> paymentFuture = context.runInChildContextAsync(
    "payment", String.class, child -> processPayment(child));
DurableFuture<String> inventoryFuture = context.runInChildContextAsync(
    "inventory", String.class, child -> reserveInventory(child));

List<Object> results = DurableFuture.allOf(paymentFuture, inventoryFuture);
```

### Invoke (Cross-Function Calls)

Call another Lambda function and suspend until it completes.

```java
OrderResult result = context.invoke(
    "process-order",
    "order-processor-function:live",  // Must include alias/version qualifier
    event,
    OrderResult.class
);
```

---

## Error Handling and Retries

### Exception Hierarchy

```
DurableExecutionException (base)
├── UnrecoverableDurableExecutionException
│   ├── IllegalDurableOperationException
│   └── NonDeterministicExecutionException
├── DurableOperationException
│   ├── StepFailedException          ← retry exhausted
│   ├── StepInterruptedException     ← at-most-once interrupted
│   ├── CallbackFailedException      ← external system reported failure
│   └── CallbackTimeoutException     ← callback timed out
└── SerDesException                   ← serialization failed
```

### Retry Strategies

```java
// Built-in exponential backoff
RetryStrategies.exponentialBackoff(maxAttempts, initialDelay, maxDelay, backoffRate, jitter)

// Fixed delay
RetryStrategies.fixedDelay(maxAttempts, fixedDelay)

// Presets
RetryStrategies.Presets.DEFAULT    // 6 attempts, 5s initial, 60s max, 2x, full jitter
RetryStrategies.Presets.NO_RETRY   // Fail immediately

// Custom strategy
RetryStrategy custom = (error, attempt) -> {
    if (error instanceof BusinessLogicException) return RetryDecision.fail();
    if (attempt >= 5) return RetryDecision.fail();
    return RetryDecision.retry(Duration.ofSeconds(attempt * 3));
};
```

### At-Most-Once Semantics

For non-idempotent operations (payments, notifications):

```java
StepConfig config = StepConfig.builder()
    .semantics(StepSemantics.AT_MOST_ONCE_PER_RETRY)
    .build();

try {
    String txnId = context.step("charge", String.class, s -> chargeCard(), config);
} catch (StepInterruptedException e) {
    // Step started but was interrupted before checkpointing
    // Check external system for actual status
}
```

### Saga Compensation Pattern

```java
Map<String, Object> payment = context.step("charge", Map.class, s -> charge());

try {
    context.step("ship", Map.class, s -> shipOrder());
} catch (StepFailedException e) {
    // Compensation: refund the payment
    context.step("refund", Map.class, s -> refund(payment.get("txnId")));
    return Map.of("status", "COMPENSATED");
}
```

---

## Deployment Model

### Container Image (Required for Java)

Java durable functions deploy as **container images** (not zip files).

**Dockerfile:**
```dockerfile
FROM --platform=linux/amd64 amazoncorretto:21-alpine AS builder
WORKDIR /build
COPY pom.xml .
COPY src ./src
RUN apk add --no-cache maven && mvn clean package -DskipTests

FROM public.ecr.aws/lambda/java:21
COPY --from=builder /build/target/*.jar ${LAMBDA_TASK_ROOT}/lib/
CMD ["com.example.MyHandler::handleRequest"]
```

### DurableConfig

When creating the function via CLI:
```bash
aws lambda create-function \
  --function-name my-function \
  --package-type Image \
  --code ImageUri=<ecr-uri> \
  --role <role-arn> \
  --durable-config '{"ExecutionTimeout": 900, "RetentionPeriodInDays": 7}'
```

| Parameter | Description | Range |
|-----------|-------------|-------|
| `ExecutionTimeout` | Max total execution time (seconds) | 1 - 31536000 (1 year) |
| `RetentionPeriodInDays` | How long to keep execution history | 1 - 365 |

### IAM Role

Use the managed policy:
```
arn:aws:iam::aws:policy/service-role/AWSLambdaBasicDurableExecutionRolePolicy
```

For callback support, also add:
```json
{
  "Effect": "Allow",
  "Action": [
    "lambda:SendDurableExecutionCallbackSuccess",
    "lambda:SendDurableExecutionCallbackFailure",
    "lambda:SendDurableExecutionCallbackHeartbeat"
  ],
  "Resource": "*"
}
```

### Versioning

Always invoke with a published version or alias:
```bash
aws lambda publish-version --function-name my-function
# Invoke with :1 or :my-alias, not $LATEST
```

---

## Best Practices

### 1. Keep Steps Focused

Each step should do ONE thing. Don't put multiple API calls in a single step.

```java
// GOOD: One concern per step
String userId = context.step("create-user", String.class, s -> createUser(email));
String walletId = context.step("create-wallet", String.class, s -> createWallet(userId));

// BAD: Multiple concerns in one step
Map<String, String> result = context.step("setup", Map.class, s -> {
    String userId = createUser(email);
    String walletId = createWallet(userId);  // If this fails, createUser re-runs!
    return Map.of("userId", userId, "walletId", walletId);
});
```

### 2. Pass Data Via Return Values

Never rely on shared mutable state between steps.

```java
// GOOD: Data flows through step return values
String userId = context.step("register", String.class, s -> register(email));
context.wait("delay", Duration.ofMinutes(10));
context.step("welcome", Void.class, s -> { sendWelcome(userId); return null; });

// BAD: Shared variable mutation lost on replay
AtomicReference<String> userId = new AtomicReference<>("");
context.step("register", Void.class, s -> { userId.set(register(email)); return null; });
context.wait("delay", Duration.ofMinutes(10));
// userId is "" after replay!
```

### 3. Deterministic Code Between Steps

Code between steps runs on every replay. Keep it deterministic.

```java
// GOOD: Deterministic branching
String status = context.step("check", String.class, s -> getStatus());
if ("READY".equals(status)) {  // Deterministic: same value on replay
    context.step("process", ...);
}

// BAD: Non-deterministic branching
if (System.currentTimeMillis() % 2 == 0) {  // Different on each replay!
    context.step("process", ...);
}
```

### 4. Use Descriptive Step Names

Names appear in logs, execution history, and debugging tools.

```java
// GOOD
context.step("validate-shipping-address", ...);
context.step("charge-credit-card", ...);

// BAD
context.step("step1", ...);
context.step("s", ...);
```

### 5. Configure Appropriate Timeouts

Set `ExecutionTimeout` based on your longest expected execution path including all waits.

### 6. Use Replay-Aware Logging

```java
// GOOD: Uses the durable logger (logs once, not on every replay)
context.getLogger().info("Order processed");

// Inside steps:
context.step("work", String.class, stepCtx -> {
    stepCtx.getLogger().info("Processing...");  // Only logs on actual execution
    return result;
});
```

---

## Testing

### Local Test Runner

```java
import software.amazon.lambda.durable.testing.LocalDurableTestRunner;
import software.amazon.lambda.durable.model.ExecutionStatus;

@Test
void testChainingHandler() {
    var handler = new OrderProcessingHandler();
    var runner = LocalDurableTestRunner.create(Map.class, handler);

    Map<String, Object> event = Map.of(
        "orderId", "TEST-001",
        "totalAmount", 99.99,
        "customerId", "CUST-001"
    );

    var result = runner.runUntilComplete(event);

    assertEquals(ExecutionStatus.SUCCEEDED, result.getStatus());
    Map<String, Object> output = result.getResult(Map.class);
    assertEquals("COMPLETED", output.get("finalStatus"));
}
```

### SAM CLI Local Invoke

```bash
# Build and run locally
sam build
sam local invoke ChainingFunction --event events/chaining-event.json

# For callbacks, use sam local callback
sam local callback succeed <callback-id> --result '{"decision":"APPROVED"}'
```

---

## Common Pitfalls

| Pitfall | Problem | Solution |
|---------|---------|----------|
| Side effects outside steps | Not checkpointed, re-executes on replay | Wrap in `context.step()` |
| Mutable shared state | Lost on replay after wait/resume | Return values from steps |
| Non-deterministic branching | Different path on replay | Only branch on step results |
| `Thread.sleep()` | Blocks compute, charges you | Use `context.wait()` |
| Very large step results | May exceed checkpoint size limit | Keep results under 256KB |
| Nested steps | Not supported | Use `runInChildContext()` |
| Steps inside parallel branches accessing parent context | Corrupts execution state | Use the child context parameter |
| Missing version qualifier | Non-deterministic replay on $LATEST | Always use published version/alias |
| `new Date()` between steps | Non-deterministic on replay | Put inside a step |

---

## Comparison with Python Workshop

This Java workshop covers all patterns from the Python durable functions workshop, with working implementations:

| Python Workshop Module | Java Workshop Equivalent |
|------------------------|--------------------------|
| Function Chaining | Module 3: `OrderProcessingHandler` |
| Fan-Out/Fan-In | Module 4: `ParallelProcessingHandler` |
| Human Interaction | Module 5: `ApprovalWorkflowHandler` |
| Monitor (Polling) | Module 6: `JobMonitorHandler` |
| Timer/Delay | Module 7: `ScheduledReminderHandler` |
| Error Handling | Module 8: `ResilientPaymentHandler` |
| (Not in Python) | Module 9: `BatchDataProcessorHandler` (Map) |
| (Not in Python) | Module 10: `OrderFulfillmentHandler` (Sub-orchestration) |

The Java workshop adds Map Processing and Sub-Orchestration patterns not present in the Python workshop, providing more comprehensive coverage of the SDK's capabilities.
