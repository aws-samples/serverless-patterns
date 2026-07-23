using System.Text.Json;
using Amazon.DynamoDBv2;
using Amazon.Lambda.APIGatewayEvents;
using Amazon.Lambda.Core;
using Amazon.SimpleNotificationService;

namespace HeartbeatMonitor;

/// <summary>
/// Receives heartbeat signals from IoT devices via API Gateway.
/// Devices authenticate with an API key (x-api-key header).
///
/// Request: POST /heartbeat with JSON body {"DeviceId": "sensor-001"}
/// Response: 200 OK with confirmation
/// </summary>
internal sealed class HeartbeatReceiverHandler
{
    private static readonly IAmazonDynamoDB DynamoDbClient = new AmazonDynamoDBClient();
    private static readonly IAmazonSimpleNotificationService SnsClient = new AmazonSimpleNotificationServiceClient();

    private static readonly string TableName =
        System.Environment.GetEnvironmentVariable("DEVICE_TABLE_NAME")
        ?? throw new InvalidOperationException("DEVICE_TABLE_NAME environment variable is not set.");

    private static readonly string AlertTopicArn =
        System.Environment.GetEnvironmentVariable("ALERT_TOPIC_ARN") ?? "";

    private readonly DeviceService _deviceService = new(DynamoDbClient, SnsClient, TableName, AlertTopicArn);

    public async Task<APIGatewayProxyResponse> Handler(
        APIGatewayProxyRequest request, ILambdaContext context)
    {
        HeartbeatRequest? heartbeat = null;

        if (!string.IsNullOrEmpty(request.Body))
        {
            heartbeat = JsonSerializer.Deserialize<HeartbeatRequest>(request.Body, new JsonSerializerOptions
            {
                PropertyNameCaseInsensitive = true
            });
        }

        if (heartbeat is null || string.IsNullOrWhiteSpace(heartbeat.DeviceId))
        {
            return new APIGatewayProxyResponse
            {
                StatusCode = 400,
                Body = JsonSerializer.Serialize(new HeartbeatResponse("error", "DeviceId is required", DateTime.UtcNow)),
                Headers = new Dictionary<string, string> { { "Content-Type", "application/json" } }
            };
        }

        await _deviceService.RecordHeartbeatAsync(heartbeat.DeviceId, CancellationToken.None);

        context.Logger.LogInformation($"Heartbeat received from device: {heartbeat.DeviceId}");

        return new APIGatewayProxyResponse
        {
            StatusCode = 200,
            Body = JsonSerializer.Serialize(new HeartbeatResponse("ok", $"Heartbeat recorded for {heartbeat.DeviceId}", DateTime.UtcNow)),
            Headers = new Dictionary<string, string> { { "Content-Type", "application/json" } }
        };
    }
}

internal sealed record HeartbeatRequest(string DeviceId);
internal sealed record HeartbeatResponse(string Status, string Message, DateTime Timestamp);
