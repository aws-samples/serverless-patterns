using System.Text.Json;
using Amazon.DynamoDBv2;
using Amazon.Lambda;
using Amazon.Lambda.Core;
using Amazon.Lambda.DurableExecution;
using Amazon.Lambda.Model;
using Amazon.Lambda.RuntimeSupport;
using Amazon.Lambda.Serialization.SystemTextJson;
using Amazon.SimpleNotificationService;

[assembly: LambdaSerializer(typeof(DefaultLambdaJsonSerializer))]

namespace HeartbeatMonitor;

/// <summary>
/// Eternal durable orchestration that monitors a device's heartbeat.
///
/// Pattern: Runs in a loop, waiting for the heartbeat timeout each cycle.
/// If no heartbeat is received within the timeout, marks the device offline and alerts.
/// After MaxCyclesBeforeRestart cycles, performs "continue-as-new" by invoking itself
/// with fresh state to prevent unbounded checkpoint history growth.
///
/// Flow per cycle:
///   1. Wait for heartbeat timeout duration.
///   2. Check DynamoDB for a recent heartbeat.
///   3. If heartbeat received → mark online, reset missed count.
///   4. If no heartbeat → increment missed count, mark offline, send SNS alert.
///   5. If cycle limit reached → self-invoke (continue-as-new) and return.
/// </summary>
internal sealed class HeartbeatMonitorHandler
{
    private static readonly IAmazonDynamoDB DynamoDbClient = new AmazonDynamoDBClient();
    private static readonly IAmazonSimpleNotificationService SnsClient = new AmazonSimpleNotificationServiceClient();
    private static readonly IAmazonLambda LambdaClient = new AmazonLambdaClient();

    private static readonly string TableName =
        System.Environment.GetEnvironmentVariable("DEVICE_TABLE_NAME")
        ?? throw new InvalidOperationException("DEVICE_TABLE_NAME environment variable is not set.");

    private static readonly string AlertTopicArn =
        System.Environment.GetEnvironmentVariable("ALERT_TOPIC_ARN")
        ?? throw new InvalidOperationException("ALERT_TOPIC_ARN environment variable is not set.");

    private readonly DeviceService _deviceService = new(DynamoDbClient, SnsClient, TableName, AlertTopicArn);

    public static async Task Main()
    {
        var handler = new HeartbeatMonitorHandler();
        var serializer = new DefaultLambdaJsonSerializer();
        using var wrapper = HandlerWrapper.GetHandlerWrapper<DurableExecutionInvocationInput, DurableExecutionInvocationOutput>(
            handler.Handler, serializer);
        using var bootstrap = new LambdaBootstrap(wrapper);
        await bootstrap.RunAsync();
    }

    public Task<DurableExecutionInvocationOutput> Handler(
        DurableExecutionInvocationInput input, ILambdaContext context)
        => DurableFunction.WrapAsync<MonitorInput, MonitorResult>(Workflow, input, context);

    private async Task<MonitorResult> Workflow(MonitorInput input, IDurableContext ctx)
    {
        var timeout = TimeSpan.FromSeconds(input.HeartbeatTimeoutSeconds);
        var cycleCount = 0;
        var missedHeartbeats = 0;

        // ──────────────────────────────────────────────────────────────────
        // Initialize: Mark device as being monitored and record start time.
        // lastHeartbeatAt MUST be inside a step to be deterministic on replay.
        // ──────────────────────────────────────────────────────────────────
        var lastHeartbeatAt = await ctx.StepAsync(
            async (_, ct) =>
            {
                await _deviceService.UpdateDeviceStatusAsync(input.DeviceId, "monitoring_started", 0, ct);
                return DateTime.UtcNow;
            },
            name: "init-monitoring",
            config: new StepConfig { RetryStrategy = RetryStrategy.Default });

        // ──────────────────────────────────────────────────────────────────
        // Eternal loop: monitor heartbeats until cycle limit is reached
        // ──────────────────────────────────────────────────────────────────
        while (cycleCount < input.MaxCyclesBeforeRestart)
        {
            cycleCount++;

            // Wait for the heartbeat timeout period (Lambda suspends — no charges)
            await ctx.WaitAsync(timeout, name: $"wait-cycle-{cycleCount}");

            // Check if a heartbeat was received during the wait
            var heartbeatTime = await ctx.StepAsync(
                async (_, ct) => await _deviceService.GetLastHeartbeatAsync(input.DeviceId, ct),
                name: $"check-heartbeat-{cycleCount}",
                config: new StepConfig { RetryStrategy = RetryStrategy.Transient });

            if (heartbeatTime.HasValue && heartbeatTime.Value > lastHeartbeatAt)
            {
                // Heartbeat received — device is alive
                lastHeartbeatAt = heartbeatTime.Value;
                missedHeartbeats = 0;

                await ctx.StepAsync(
                    async (_, ct) => await _deviceService.UpdateDeviceStatusAsync(
                        input.DeviceId, "online", 0, ct),
                    name: $"mark-online-{cycleCount}",
                    config: new StepConfig { RetryStrategy = RetryStrategy.Transient });
            }
            else
            {
                // No heartbeat — device may be offline
                missedHeartbeats++;

                await ctx.StepAsync(
                    async (_, ct) =>
                    {
                        await _deviceService.UpdateDeviceStatusAsync(
                            input.DeviceId, "offline", missedHeartbeats, ct);
                        await _deviceService.SendOfflineAlertAsync(
                            input.DeviceId, missedHeartbeats, ct);
                    },
                    name: $"alert-offline-{cycleCount}",
                    config: new StepConfig { RetryStrategy = RetryStrategy.Default });
            }
        }

        // ──────────────────────────────────────────────────────────────────
        // Continue-as-new: self-invoke with fresh state to reset history.
        // This prevents unbounded checkpoint log growth.
        // ──────────────────────────────────────────────────────────────────
        await ctx.StepAsync(
            async (_, ct) =>
            {
                var payload = JsonSerializer.Serialize(input);
                var functionName = System.Environment.GetEnvironmentVariable("AWS_LAMBDA_FUNCTION_NAME")!;

                await LambdaClient.InvokeAsync(new InvokeRequest
                {
                    FunctionName = $"{functionName}:$LATEST",
                    InvocationType = InvocationType.Event,
                    Payload = payload
                }, ct);
            },
            name: "continue-as-new",
            config: new StepConfig { RetryStrategy = RetryStrategy.Default });

        return new MonitorResult(
            DeviceId: input.DeviceId,
            Reason: "cycle_limit_reached",
            CompletedCycles: cycleCount,
            RestartedAt: DateTime.UtcNow);
    }
}
