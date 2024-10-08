using Amazon.Lambda.Core;
using Amazon.Lambda.KinesisEvents;
using System.Text.Json;
using DataProcessFunction.Models;
using DataProcessFunction.Serialization;
using Amazon.DynamoDBv2;
using Microsoft.Extensions.Configuration;
using Amazon.DynamoDBv2.Model;

namespace DataProcessFunction
{
    public class DataProcessFunction(IConfigurationRoot? configuration = null)
    {
        private const string ProcessedTableEnvName = "PROCESSED_TABLE_NAME";
        private const string ErrorTableEnvName = "ERROR_TABLE_NAME";

        private readonly IAmazonDynamoDB _dynamoDbClient = new AmazonDynamoDBClient();
        private readonly string _processedTableName =
            (configuration != null ? configuration[ProcessedTableEnvName] : Environment.GetEnvironmentVariable(ProcessedTableEnvName))
                    ?? throw new ArgumentException(ProcessedTableEnvName);
        private readonly string _errorTableName =
            (configuration != null ? configuration[ErrorTableEnvName] : Environment.GetEnvironmentVariable(ErrorTableEnvName))
                    ?? throw new ArgumentException(ErrorTableEnvName);

        public async Task<StreamsEventResponse> FunctionHandler(KinesisEvent kinesisEvent, ILambdaContext context)
        {
            if (kinesisEvent.Records.Count == 0)
            {
                context.Logger.LogInformation("Empty Kinesis Event received");
                return new StreamsEventResponse();
            }

            foreach (var record in kinesisEvent.Records)
            {
                try
                {
                    string recordData = GetRecordContents(record.Kinesis);
                    context.Logger.LogInformation($"Processing record: {recordData}");

                    var data = JsonSerializer.Deserialize(recordData, LambdaFunctionJsonSerializerContext.Default.DataModel);
                    if (data == null)
                    {
                        context.Logger.LogWarning("Failed to deserialize record data");
                        continue;
                    }

                    // Process the data (e.g., aggregate, transform)
                    var processedData = ProcessData(data);

                    // Here you would typically send the processed data to a storage solution
                    // that PowerBI can connect to, such as SQL Database, Cosmos DB, or blob storage.
                    await StoreProcessedDataAsync(processedData, context);
                }
                catch (Exception ex)
                {
                    context.Logger.LogError($"Error processing Kinesis event: {ex.Message}");

                    // Log Error in DynamoDB
                    await LogError(record.Kinesis.SequenceNumber, ex, context);

                    // Let Kinesis know that the record failed to process
                    return new StreamsEventResponse
                    {
                        BatchItemFailures =
                        [
                            new StreamsEventResponse.BatchItemFailure { ItemIdentifier = record.Kinesis.SequenceNumber }
                        ]
                    };
                }
            }

            context.Logger.LogInformation($"Successfully processed {kinesisEvent.Records.Count} records.");
            return new StreamsEventResponse();            
        }

        private static string GetRecordContents(KinesisEvent.Record streamRecord)
        {
            using var reader = new StreamReader(streamRecord.Data);
            return reader.ReadToEnd();
        }

        private static ProcessedDataModel ProcessData(DataModel data)
        {
            // Implement your data processing logic here
            return new ProcessedDataModel
            {
                Id = data.Id,
                Timestamp = data.Timestamp,
                Value = data.Value,
                Category = data.Category,
                ProcessedValue = data.Value * 2,
                ProcessedTimestamp = DateTime.UtcNow.ToString("o")
            };
        }

        private async Task StoreProcessedDataAsync(ProcessedDataModel data, ILambdaContext context)
        {
            ArgumentNullException.ThrowIfNull(data, nameof(data));

            try
            {
                var serializedData = JsonSerializer.Serialize(data, LambdaFunctionJsonSerializerContext.Default.ProcessedDataModel);

                // Implement logic to store processed data
                // This could be inserting into a database, writing to blob storage, etc.
                context.Logger.LogInformation($"Storing processed data: {serializedData}");

                var request = new PutItemRequest
                {
                    TableName = _processedTableName,
                    Item = new Dictionary<string, AttributeValue>
                    {
                        ["Id"] = new AttributeValue { S = data.Id },
                        ["Timestamp"] = new AttributeValue { S = data.Timestamp.ToString("o") },
                        ["Value"] = new AttributeValue { N = data.Value.ToString() },
                        ["Category"] = new AttributeValue { S = data.Category },
                        ["ProcessedValue"] = new AttributeValue { N = data.ProcessedValue.ToString() },
                        ["ProcessedTimestamp"] = new AttributeValue { S = data.ProcessedTimestamp }
                    }
                };

                await _dynamoDbClient.PutItemAsync(request);
            }
            catch (Exception ex)
            {
                context.Logger.LogError($"Error storing processed data: {ex.Message} for RecordId: {data.Id}");
                throw;
            }
        }

        private async Task LogError(string sequenceNumber, Exception ex, ILambdaContext context)
        {
            try
            {
                var request = new PutItemRequest
                {
                    TableName = _errorTableName,
                    Item = new Dictionary<string, AttributeValue>
                    {
                        ["ErrorId"] = new AttributeValue { S = Guid.NewGuid().ToString() },
                        ["Timestamp"] = new AttributeValue { N = DateTime.UtcNow.Ticks.ToString() },
                        ["SequenceNumber"] = new AttributeValue { S = sequenceNumber },
                        ["ErrorMessage"] = new AttributeValue { S = ex.Message },
                        ["StackTrace"] = new AttributeValue { S = ex.StackTrace }
                    }
                };
        
                await _dynamoDbClient.PutItemAsync(request);
            }
            catch (Exception logEx)
            {
                context.Logger.LogError($"Error logging error: {logEx.Message}");
            }
        }
    }
}