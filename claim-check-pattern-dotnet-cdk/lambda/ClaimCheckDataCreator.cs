using System.Text.Json;
using Amazon.Lambda.Core;
using Amazon.SQS;
using ClaimCheckPattern.Models;

namespace ClaimCheckPattern;

public class ClaimCheckDataCreator
{
    private static readonly AmazonSQSClient SqsClient = new();

    public async Task FunctionHandler(object _, ILambdaContext context)
    {
        context.Logger.LogInformation($"{nameof(ClaimCheckDataCreator)} called.");

        // Create message
        var fullMessage = new FullMessage
        {
            Id = Guid.NewGuid(),
            CreatedAt = DateTime.UtcNow,
            CreatedBy = "John Doe",
            Data = new Dictionary<string, string>
            {
                {"demoKey1", "demoValue1"},
                {"demoKey2", "demoValue2"},
                {"demoKey3", "demoValue3"}
            }
        };

        // Put message on queue
        context.Logger.LogInformation($"Putting full message with id: '{fullMessage.Id}' on queue...");
        var queueUrl = Environment.GetEnvironmentVariable("QUEUE_URL");
        var messageBody = JsonSerializer.Serialize(fullMessage);
        await SqsClient.SendMessageAsync(queueUrl, messageBody);
        context.Logger.LogInformation("Full message was put on queue successfully.");
    }
}
