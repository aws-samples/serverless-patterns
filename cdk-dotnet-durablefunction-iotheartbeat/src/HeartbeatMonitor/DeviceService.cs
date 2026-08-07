using System.Globalization;
using Amazon.DynamoDBv2;
using Amazon.DynamoDBv2.Model;
using Amazon.SimpleNotificationService;
using Amazon.SimpleNotificationService.Model;

namespace HeartbeatMonitor;

/// <summary>
/// Handles device status persistence and alerting.
/// </summary>
internal sealed class DeviceService(IAmazonDynamoDB dynamoDb, IAmazonSimpleNotificationService sns, string tableName, string alertTopicArn)
{
    private readonly IAmazonDynamoDB _dynamoDb = dynamoDb;
    private readonly IAmazonSimpleNotificationService _sns = sns;
    private readonly string _tableName = tableName;
    private readonly string _alertTopicArn = alertTopicArn;

    /// <summary>
    /// Checks if a heartbeat has been received since the given time.
    /// </summary>
    public async Task<DateTime?> GetLastHeartbeatAsync(string deviceId, CancellationToken ct)
    {
        var response = await _dynamoDb.GetItemAsync(new GetItemRequest
        {
            TableName = _tableName,
            Key = new Dictionary<string, AttributeValue>
            {
                ["DeviceId"] = new() { S = deviceId }
            },
            ProjectionExpression = "LastHeartbeatAt"
        }, ct);

        if (response.Item.TryGetValue("LastHeartbeatAt", out var attr))
        {
            return DateTime.Parse(attr.S, CultureInfo.InvariantCulture, DateTimeStyles.RoundtripKind);
        }

        return null;
    }

    /// <summary>
    /// Updates the device status in DynamoDB.
    /// </summary>
    public async Task UpdateDeviceStatusAsync(string deviceId, string status, int missedHeartbeats, CancellationToken ct)
    {
        await _dynamoDb.UpdateItemAsync(new UpdateItemRequest
        {
            TableName = _tableName,
            Key = new Dictionary<string, AttributeValue>
            {
                ["DeviceId"] = new() { S = deviceId }
            },
            UpdateExpression = "SET #st = :status, MissedHeartbeats = :missed, UpdatedAt = :now",
            ExpressionAttributeNames = new Dictionary<string, string>
            {
                ["#st"] = "Status"
            },
            ExpressionAttributeValues = new Dictionary<string, AttributeValue>
            {
                [":status"] = new() { S = status },
                [":missed"] = new() { N = missedHeartbeats.ToString(CultureInfo.InvariantCulture) },
                [":now"] = new() { S = DateTime.UtcNow.ToString("O", CultureInfo.InvariantCulture) }
            }
        }, ct);
    }

    /// <summary>
    /// Sends an alert that a device has gone offline.
    /// </summary>
    public async Task SendOfflineAlertAsync(string deviceId, int missedHeartbeats, CancellationToken ct)
    {
        var message = $"⚠️ Device '{deviceId}' is OFFLINE.\n" +
                      $"Missed heartbeats: {missedHeartbeats}\n" +
                      $"Time: {DateTime.UtcNow:O}";

        await _sns.PublishAsync(new PublishRequest
        {
            TopicArn = _alertTopicArn,
            Subject = $"Device Offline: {deviceId}",
            Message = message
        }, ct);
    }

    /// <summary>
    /// Records a heartbeat from a device (called by the receiver function).
    /// </summary>
    public async Task RecordHeartbeatAsync(string deviceId, CancellationToken ct)
    {
        await _dynamoDb.UpdateItemAsync(new UpdateItemRequest
        {
            TableName = _tableName,
            Key = new Dictionary<string, AttributeValue>
            {
                ["DeviceId"] = new() { S = deviceId }
            },
            UpdateExpression = "SET #st = :status, LastHeartbeatAt = :now, MissedHeartbeats = :zero",
            ExpressionAttributeNames = new Dictionary<string, string>
            {
                ["#st"] = "Status"
            },
            ExpressionAttributeValues = new Dictionary<string, AttributeValue>
            {
                [":status"] = new() { S = "online" },
                [":now"] = new() { S = DateTime.UtcNow.ToString("O", CultureInfo.InvariantCulture) },
                [":zero"] = new() { N = "0" }
            }
        }, ct);
    }
}
