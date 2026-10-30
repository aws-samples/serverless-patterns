# Project Steering: CDK .NET Durable Function — Image Processing

## Overview

This project implements a serverless image-processing pipeline using **AWS Lambda Durable Functions** for .NET, deployed with **AWS CDK** (C#). Lambda Durable Functions allow you to build resilient, long-running workflows that automatically checkpoint progress, resume after failures, and can run for up to one year — with charges only for active compute time.

## Technology Stack

- **Runtime:** .NET 10 (Lambda `dotnet10` managed runtime)
- **SDK:** `Amazon.Lambda.DurableExecution` (preview, 0.x)
- **Infrastructure:** AWS CDK v2 (C#)
- **Packaging:** Zip deployment (required for durable functions)
- **Serialization:** `Amazon.Lambda.Serialization.SystemTextJson`

## Project Structure

```
src/
├── infra/                  # CDK infrastructure (C#)
│   ├── Program.cs          # CDK app entry point
│   ├── InfraStack.cs       # Stack definition
│   └── infra.csproj        # CDK project file
└── CdkDotnetDurablefunctionImageprocessing.sln
```

Lambda function projects should be added under `src/` as sibling directories to `infra/`.

## Building Lambda Durable Functions in .NET

### NuGet Package

```bash
dotnet add package Amazon.Lambda.DurableExecution
```

### Core Concepts

Lambda Durable Functions use **deterministic replay** to resume workflows from checkpoints. Your handler delegates to `DurableFunction.WrapAsync`, which provides an `IDurableContext` — the interface to all durable operations:

- `ctx.StepAsync` — Run code and checkpoint the result. On replay, cached results are returned without re-executing.
- `ctx.WaitAsync` — Suspend execution for a duration without compute charges (1s to ~1 year).
- `ctx.WaitForConditionAsync` — Poll a check function until a condition is met, suspending between polls.
- `ctx.CreateCallbackAsync` / `ctx.WaitForCallbackAsync` — Wait for external events (approvals, webhooks).
- `ctx.RunInChildContextAsync` — Run an isolated child context with its own checkpoint log.
- `ctx.ParallelAsync` — Fan out independent branches concurrently with configurable completion policies.

### Programming Models

#### Executable Model (recommended for AOT/custom runtimes)

```csharp
using Amazon.Lambda.Core;
using Amazon.Lambda.DurableExecution;
using Amazon.Lambda.RuntimeSupport;
using Amazon.Lambda.Serialization.SystemTextJson;

public class ImageProcessor
{
    public static async Task Main()
    {
        var handler = new ImageProcessor();
        var serializer = new DefaultLambdaJsonSerializer();
        using var wrapper = HandlerWrapper.GetHandlerWrapper<DurableExecutionInvocationInput, DurableExecutionInvocationOutput>(
            handler.Handler, serializer);
        using var bootstrap = new LambdaBootstrap(wrapper);
        await bootstrap.RunAsync();
    }

    public Task<DurableExecutionInvocationOutput> Handler(
        DurableExecutionInvocationInput input, ILambdaContext context)
        => DurableFunction.WrapAsync<ImageInput, ImageResult>(Workflow, input, context);

    private async Task<ImageResult> Workflow(ImageInput input, IDurableContext ctx)
    {
        // workflow body
    }
}
```

#### Class-Library Model (managed `dotnet10` runtime)

```csharp
using Amazon.Lambda.Core;
using Amazon.Lambda.DurableExecution;
using Amazon.Lambda.Serialization.SystemTextJson;

[assembly: LambdaSerializer(typeof(DefaultLambdaJsonSerializer))]

namespace ImageProcessor;

public class Function
{
    public Task<DurableExecutionInvocationOutput> Handler(
        DurableExecutionInvocationInput input, ILambdaContext context)
        => DurableFunction.WrapAsync<ImageInput, ImageResult>(Workflow, input, context);

    private async Task<ImageResult> Workflow(ImageInput input, IDurableContext ctx)
    {
        // workflow body
    }
}
```

Handler string: `Assembly::Namespace.Type::Method`

#### Lambda Annotations Model

```csharp
using Amazon.Lambda.Annotations;
using Amazon.Lambda.DurableExecution;

public class ImageProcessor
{
    [LambdaFunction]
    [DurableExecution(executionTimeout: 300, RetentionPeriodInDays = 7)]
    public async Task<ImageResult> Workflow(ImageInput input, IDurableContext ctx)
    {
        // workflow body — handler wrapper is source-generated
    }
}
```

### Steps — Checkpointed Work Units

```csharp
var thumbnail = await ctx.StepAsync(
    async (_, ct) => await resizeService.CreateThumbnailAsync(imageUrl, ct),
    name: "create-thumbnail");
```

Every step must have a unique, stable `name` within the workflow. The `CancellationToken` parameter links the caller's token with the SDK's workflow-shutdown signal — always pass it to async APIs.

#### Retry Strategies

```csharp
var result = await ctx.StepAsync(
    async (stepCtx, ct) => await unreliableService.CallAsync(ct),
    name: "call-service",
    config: new StepConfig
    {
        RetryStrategy = RetryStrategy.Exponential(
            maxAttempts: 5,
            initialDelay: TimeSpan.FromSeconds(2),
            maxDelay: TimeSpan.FromSeconds(30),
            backoffRate: 2.0,
            jitter: JitterStrategy.Full)
    });
```

Built-in strategies: `RetryStrategy.Default` (6 attempts, 2× backoff), `RetryStrategy.Transient` (3 attempts), `RetryStrategy.None`, `RetryStrategy.Exponential(...)`, `RetryStrategy.FromDelegate(...)`.

#### Step Semantics

- `StepSemantics.AtLeastOncePerRetry` (default) — Body may re-execute if interrupted. Use for idempotent operations.
- `StepSemantics.AtMostOncePerRetry` — Body executes at most once per attempt. Use for non-idempotent operations (payments, emails). Combine with `RetryStrategy.None` for true at-most-once.

### Wait — Suspend Without Compute Charges

```csharp
await ctx.WaitAsync(TimeSpan.FromHours(24), name: "wait-for-approval-window");
```

Duration: 1 second to ~1 year. The Lambda terminates and is re-invoked when the timer fires.

### Wait For Condition — Poll Until Ready

```csharp
var status = await ctx.WaitForConditionAsync(
    check: async (state, checkCtx, ct) =>
    {
        return await processingService.GetStatusAsync(jobId, ct);
    },
    config: new WaitForConditionConfig<ProcessingStatus>
    {
        InitialState = ProcessingStatus.Pending,
        WaitStrategy = WaitStrategy.Exponential<ProcessingStatus>(
            isDone: s => s == ProcessingStatus.Complete || s == ProcessingStatus.Failed,
            maxAttempts: 60,
            initialDelay: TimeSpan.FromSeconds(5),
            maxDelay: TimeSpan.FromSeconds(300))
    },
    name: "poll-processing-status");
```

Built-in wait strategies: `WaitStrategy.Exponential<T>`, `WaitStrategy.Linear<T>`, `WaitStrategy.Fixed<T>`, `WaitStrategy.FromDelegate<T>`.

Throws `WaitForConditionException` when max attempts are exhausted without the condition being met.

### Callbacks — Wait for External Events

```csharp
var approval = await ctx.WaitForCallbackAsync<ApprovalResult>(
    submitter: async (callbackId, cbCtx, ct) =>
    {
        // Hand callbackId to an external system (e.g., invoke another Lambda, send to SQS)
        await notificationService.RequestApprovalAsync(callbackId, ct);
    },
    name: "human-approval",
    config: new WaitForCallbackConfig
    {
        Timeout = TimeSpan.FromHours(48),
        HeartbeatTimeout = TimeSpan.FromHours(1)
    });
```

The external system completes the callback via the Lambda API:
- `SendDurableExecutionCallbackSuccessAsync` — resume with a result
- `SendDurableExecutionCallbackFailureAsync` — resume with failure
- `SendDurableExecutionCallbackHeartbeatAsync` — extend the heartbeat deadline

### Child Contexts — Isolated Sub-Workflows

```csharp
var phaseResult = await ctx.RunInChildContextAsync<ProcessedImage>(
    async (childCtx, ct) =>
    {
        var validated = await childCtx.StepAsync(
            async (_, c) => await validator.ValidateAsync(image, c), name: "validate");
        var processed = await childCtx.StepAsync(
            async (_, c) => await processor.ProcessAsync(validated, c), name: "process");
        return processed;
    },
    name: "image-pipeline",
    config: new ChildContextConfig { SubType = "ImageProcessing" });
```

The child context has its own operation-ID space. Its return value is checkpointed as a single operation in the parent.

### Parallel — Fan-Out Concurrent Work

```csharp
var batch = await ctx.ParallelAsync(
    new[]
    {
        new DurableBranch<ImageResult>("thumbnail", async (branchCtx, ct) =>
            await branchCtx.StepAsync((_, t) => resizer.ResizeAsync(image, Size.Thumb, t), name: "resize")),
        new DurableBranch<ImageResult>("medium", async (branchCtx, ct) =>
            await branchCtx.StepAsync((_, t) => resizer.ResizeAsync(image, Size.Medium, t), name: "resize")),
        new DurableBranch<ImageResult>("large", async (branchCtx, ct) =>
            await branchCtx.StepAsync((_, t) => resizer.ResizeAsync(image, Size.Large, t), name: "resize")),
    },
    name: "resize-all",
    config: new ParallelConfig
    {
        MaxConcurrency = 3,
        CompletionConfig = CompletionConfig.AllSuccessful()
    });

var results = batch.GetResults(); // IReadOnlyList<ImageResult>
if (batch.HasFailure)
{
    batch.ThrowIfError();
}
```

Completion policies: `CompletionConfig.AllSuccessful()` (default, fail-fast), `CompletionConfig.AllCompleted()` (run all, inspect failures), `CompletionConfig.FirstSuccessful()` (race).

## Determinism Rules

Durable functions replay from checkpoints. The workflow body MUST be deterministic:

- **DO** put all side effects inside `StepAsync` (HTTP calls, DB writes, SDK calls).
- **DO** use `WaitAsync` instead of `Task.Delay` for delays.
- **DO** give every step/operation a stable, unique `name`.
- **DO** pass `CancellationToken` to all async operations inside step bodies.
- **DON'T** use `DateTime.Now`, `Guid.NewGuid()`, `Random`, or other non-deterministic values outside steps.
- **DON'T** branch workflow logic on `CancellationToken.IsCancellationRequested`.
- **DON'T** catch `OperationCanceledException` and continue — rethrow or don't catch.

## Cancellation

Every user `Func` receives a `CancellationToken` that is a linked source combining:
1. The caller's cancel intent.
2. The SDK's workflow-shutdown signal (fires when the workflow is being torn down).

Pass it to all cancellation-aware APIs. If the token fires and the body throws `OperationCanceledException`, no FAIL checkpoint is written — the exception propagates up. Unrelated `OperationCanceledException` (token never fired) is treated as a normal failure subject to retry.

## CDK Deployment

Infrastructure is defined in `src/infra/InfraStack.cs`. When adding the Lambda function:

```csharp
using Amazon.CDK;
using Amazon.CDK.AWS.Lambda;
using Constructs;

public class InfraStack : Stack
{
    internal InfraStack(Construct scope, string id, IStackProps props = null) : base(scope, id, props)
    {
        var imageProcessor = new Function(this, "ImageProcessorFunction", new FunctionProps
        {
            Runtime = Runtime.DOTNET_10,            // managed runtime
            Handler = "ImageProcessor::ImageProcessor.Function::Handler",
            Code = Code.FromAsset("src/ImageProcessor/bin/Release/net10.0/publish"),
            MemorySize = 512,
            Timeout = Duration.Seconds(900),
            // DurableConfig is applied via the DurableExecution feature at deploy time
        });
    }
}
```

## Build & Deploy Commands

```bash
# Build the solution
dotnet build src

# Synthesize CloudFormation
cdk synth

# Deploy
cdk deploy

# Compare changes
cdk diff
```

## Key Constraints

- `Amazon.Lambda.DurableExecution` is **preview (0.x)** — APIs may change before 1.0.
- Packaging must be **Zip** (container image is not supported for durable functions).
- Workflows can run for up to **1 year**.
- `WaitAsync` duration: minimum 1 second, maximum ~1 year (31,622,400 seconds).
- Step results must be serializable by the configured `ILambdaSerializer`.
- For AOT/trimmed deployments, use `SourceGeneratorLambdaJsonSerializer<TContext>`.

## References

- [Amazon.Lambda.DurableExecution SDK](https://github.com/aws/aws-lambda-dotnet/tree/master/Libraries/src/Amazon.Lambda.DurableExecution)
- [Steps documentation](https://github.com/aws/aws-lambda-dotnet/blob/master/Libraries/src/Amazon.Lambda.DurableExecution/docs/core/steps.md)
- [Wait documentation](https://github.com/aws/aws-lambda-dotnet/blob/master/Libraries/src/Amazon.Lambda.DurableExecution/docs/core/wait.md)
- [Wait For Condition documentation](https://github.com/aws/aws-lambda-dotnet/blob/master/Libraries/src/Amazon.Lambda.DurableExecution/docs/core/wait-for-condition.md)
- [Callbacks documentation](https://github.com/aws/aws-lambda-dotnet/blob/master/Libraries/src/Amazon.Lambda.DurableExecution/docs/core/callbacks.md)
- [Child Contexts documentation](https://github.com/aws/aws-lambda-dotnet/blob/master/Libraries/src/Amazon.Lambda.DurableExecution/docs/core/child-contexts.md)
- [Parallel documentation](https://github.com/aws/aws-lambda-dotnet/blob/master/Libraries/src/Amazon.Lambda.DurableExecution/docs/core/parallel.md)
- [Cancellation documentation](https://github.com/aws/aws-lambda-dotnet/blob/master/Libraries/src/Amazon.Lambda.DurableExecution/docs/core/cancellation.md)
