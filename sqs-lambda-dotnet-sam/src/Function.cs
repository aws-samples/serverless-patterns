using Amazon.Lambda.Core;
using Amazon.Lambda.SQSEvents;
using System.Text.Json;
using Microsoft.Extensions.Logging;

// Assembly attribute to enable the Lambda function's JSON input to be converted into a .NET class.
[assembly: LambdaSerializer(typeof(Amazon.Lambda.Serialization.SystemTextJson.DefaultLambdaJsonSerializer))]

namespace SqsLambdaProcessor;

public class Function
{
    private readonly Random _random;
    private readonly ILogger<Function> _logger;

    public Function()
    {
        _random = new Random();
        _logger = LoggerFactory.Create(builder =>
        {
            builder.AddLambdaLogger();
            builder.SetMinimumLevel(Microsoft.Extensions.Logging.LogLevel.Information);
        }).CreateLogger<Function>();
    }

    /// <summary>
    /// Process SQS messages
    /// </summary>
    /// <param name="evnt">The SQS event containing messages</param>
    /// <param name="context">Lambda context</param>
    /// <returns>Response containing batch item failures</returns>
    public async Task<SQSBatchResponse> FunctionHandler(SQSEvent evnt, ILambdaContext context)
    {
        _logger.LogInformation($"Received event: {JsonSerializer.Serialize(evnt)}");
        var batchItemFailures = new List<SQSBatchResponse.BatchItemFailure>();

        foreach (var record in evnt.Records)
        {
            try
            {
                var result = await ProcessSqsMessageAsync(record);
                if (!result.Success)
                {
                    batchItemFailures.Add(new SQSBatchResponse.BatchItemFailure
                    {
                        ItemIdentifier = record.MessageId
                    });
                }
            }
            catch (Exception ex)
            {
                _logger.LogError(ex, $"Error processing record {record.MessageId}");
                batchItemFailures.Add(new SQSBatchResponse.BatchItemFailure
                {
                    ItemIdentifier = record.MessageId
                });
            }
        }

        return new SQSBatchResponse { BatchItemFailures = batchItemFailures };
    }

    private async Task<ProcessingResult> ProcessSqsMessageAsync(SQSEvent.SQSMessage record)
    {
        try
        {
            // Randomly fail some messages for demonstration
            if (_random.NextDouble() < 0.2)
            {
                _logger.LogInformation($"Randomly failing message: {record.Body}");
                throw new Exception("Random processing failure");
            }

            _logger.LogInformation($"Processing message: {record.MessageId}");
            
            // Simulate some processing, add your business logic here
            await Task.Delay(100); // equivalent to time.sleep(0.1)

            _logger.LogInformation($"Successfully processed message: {record.Body}");
            return new ProcessingResult { Success = true };
        }
        catch (Exception error)
        {
            _logger.LogError(error, $"Failed to process record {record.MessageId}");
            return new ProcessingResult { Success = false };
        }
    }

    private class ProcessingResult
    {
        public bool Success { get; set; }
    }
} 