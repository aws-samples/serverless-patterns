using System.Text.Json;
using Amazon.DynamoDBv2;
using Amazon.DynamoDBv2.Model;
using Amazon.BedrockRuntime;
using Amazon.BedrockRuntime.Model;
using Amazon.Runtime.Documents;
using Document = Amazon.Runtime.Documents.Document;

namespace TripPlannerMultiturn;

/// <summary>
/// Persists conversation state (Bedrock messages + trip parameters) in DynamoDB.
/// Sessions expire automatically via DynamoDB TTL after 1 hour.
/// </summary>
public class SessionStore
{
    private static readonly TimeSpan SessionTtl = TimeSpan.FromHours(1);

    private readonly IAmazonDynamoDB _dynamoDb;
    private readonly string _tableName;

    public SessionStore(IAmazonDynamoDB dynamoDb, string tableName)
    {
        _dynamoDb = dynamoDb;
        _tableName = tableName;
    }

    public async Task SaveSessionAsync(
        string sessionId,
        List<Message> messages,
        TripParameters tripParams,
        string? pendingToolUseId,
        CancellationToken ct = default)
    {
        var expiresAt = DateTimeOffset.UtcNow.Add(SessionTtl).ToUnixTimeSeconds();
        var serializedMessages = SerializeMessages(messages);

        // DynamoDB items have a 400KB limit. Guard against oversized sessions.
        if (serializedMessages.Length > 350_000)
            throw new InvalidOperationException("Conversation history too large to store. Please start a new session.");

        var item = new Dictionary<string, AttributeValue>
        {
            ["SessionId"] = new() { S = sessionId },
            ["Messages"] = new() { S = serializedMessages },
            ["Destination"] = new() { S = tripParams.Destination },
            ["Days"] = new() { N = tripParams.Days.ToString() },
            ["Interests"] = new() { S = tripParams.Interests },
            ["ExpiresAt"] = new() { N = expiresAt.ToString() }
        };

        if (pendingToolUseId is not null)
            item["PendingToolUseId"] = new() { S = pendingToolUseId };

        await _dynamoDb.PutItemAsync(new PutItemRequest
        {
            TableName = _tableName,
            Item = item
        }, ct);
    }

    public async Task<SessionData?> LoadSessionAsync(string sessionId, CancellationToken ct = default)
    {
        var response = await _dynamoDb.GetItemAsync(new GetItemRequest
        {
            TableName = _tableName,
            Key = new Dictionary<string, AttributeValue>
            {
                ["SessionId"] = new() { S = sessionId }
            }
        }, ct);

        if (!response.IsItemSet)
            return null;

        var item = response.Item;
        var messages = DeserializeMessages(item["Messages"].S);
        var tripParams = new TripParameters(
            item["Destination"].S,
            int.TryParse(item["Days"].N, out var days) ? days : 3,
            item["Interests"].S);
        var pendingToolUseId = item.TryGetValue("PendingToolUseId", out var toolId) ? toolId.S : null;

        return new SessionData(messages, tripParams, pendingToolUseId);
    }

    public async Task DeleteSessionAsync(string sessionId, CancellationToken ct = default)
    {
        await _dynamoDb.DeleteItemAsync(new DeleteItemRequest
        {
            TableName = _tableName,
            Key = new Dictionary<string, AttributeValue>
            {
                ["SessionId"] = new() { S = sessionId }
            }
        }, ct);
    }

    private static string SerializeMessages(List<Message> messages)
    {
        var simplified = messages.Select(m => new SerializedMessage
        {
            Role = m.Role.Value,
            Content = m.Content.Select(c =>
            {
                if (c.Text is not null)
                    return new SerializedContent { Type = "text", Text = c.Text };
                if (c.ToolUse is not null)
                    return new SerializedContent
                    {
                        Type = "tool_use",
                        ToolUseId = c.ToolUse.ToolUseId,
                        ToolName = c.ToolUse.Name,
                        ToolInput = SerializeDocument(c.ToolUse.Input)
                    };
                if (c.ToolResult is not null)
                    return new SerializedContent
                    {
                        Type = "tool_result",
                        ToolUseId = c.ToolResult.ToolUseId,
                        Text = c.ToolResult.Content.FirstOrDefault()?.Text
                    };
                return new SerializedContent { Type = "unknown" };
            }).ToList()
        }).ToList();

        return JsonSerializer.Serialize(simplified);
    }

    private static List<Message> DeserializeMessages(string json)
    {
        var simplified = JsonSerializer.Deserialize<List<SerializedMessage>>(json) ?? [];
        return simplified.Select(m =>
        {
            var message = new Message { Role = new ConversationRole(m.Role) };
            message.Content = m.Content.Select<SerializedContent, ContentBlock>(c => c.Type switch
            {
                "text" => new ContentBlock { Text = c.Text },
                "tool_use" => new ContentBlock
                {
                    ToolUse = new ToolUseBlock
                    {
                        ToolUseId = c.ToolUseId!,
                        Name = c.ToolName!,
                        Input = DeserializeDocument(c.ToolInput!)
                    }
                },
                "tool_result" => new ContentBlock
                {
                    ToolResult = new ToolResultBlock
                    {
                        ToolUseId = c.ToolUseId!,
                        Content = [new ToolResultContentBlock { Text = c.Text }]
                    }
                },
                _ => new ContentBlock { Text = "[unknown content]" }
            }).ToList();
            return message;
        }).ToList();
    }

    private record SerializedMessage
    {
        public string Role { get; init; } = "";
        public List<SerializedContent> Content { get; init; } = [];
    }

    private record SerializedContent
    {
        public string Type { get; init; } = "";
        public string? Text { get; init; }
        public string? ToolUseId { get; init; }
        public string? ToolName { get; init; }
        public string? ToolInput { get; init; }
    }

    /// <summary>
    /// Serializes a Document to a JSON string by converting it to a dictionary structure.
    /// </summary>
    private static string SerializeDocument(Document doc)
    {
        var obj = DocumentToObject(doc);
        return JsonSerializer.Serialize(obj);
    }

    /// <summary>
    /// Deserializes a JSON string back into a Document.
    /// </summary>
    private static Document DeserializeDocument(string json)
    {
        var element = JsonSerializer.Deserialize<JsonElement>(json);
        return JsonElementToDocument(element);
    }

    private static Document JsonElementToDocument(JsonElement element)
    {
        return element.ValueKind switch
        {
            JsonValueKind.String => new Document(element.GetString()!),
            JsonValueKind.Number when element.TryGetInt32(out var i) => new Document(i),
            JsonValueKind.Number when element.TryGetInt64(out var l) => new Document(l),
            JsonValueKind.Number => new Document(element.GetDouble()),
            JsonValueKind.True => new Document(true),
            JsonValueKind.False => new Document(false),
            JsonValueKind.Null => new Document(),
            JsonValueKind.Array => new Document(element.EnumerateArray().Select(JsonElementToDocument).ToList()),
            JsonValueKind.Object => new Document(element.EnumerateObject()
                .ToDictionary(p => p.Name, p => JsonElementToDocument(p.Value))),
            _ => new Document()
        };
    }

    private static object? DocumentToObject(Document doc)
    {
        if (doc.IsString()) return doc.AsString();
        if (doc.IsInt()) return doc.AsInt();
        if (doc.IsLong()) return doc.AsLong();
        if (doc.IsDouble()) return doc.AsDouble();
        if (doc.IsBool()) return doc.AsBool();
        if (doc.IsNull()) return null;
        if (doc.IsList()) return doc.AsList().Select(DocumentToObject).ToList();
        if (doc.IsDictionary())
            return doc.AsDictionary().ToDictionary(kv => kv.Key, kv => DocumentToObject(kv.Value));
        return null;
    }
}

public record SessionData(List<Message> Messages, TripParameters TripParams, string? PendingToolUseId);
