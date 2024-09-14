using Amazon.Lambda.Core;
using Amazon.Kinesis;
using Amazon.Kinesis.Model;
using System.Text.Json;
using DataIngestFunction.Models;
using DataIngestFunction.Serialization;
using Microsoft.Extensions.Configuration;

namespace DataIngestFunction
{
    public class DataIngestFunction(IConfigurationRoot? configuration = null)
    {             
        private const string KinesisStreamEnvName = "KINESIS_STREAM_NAME";
        private readonly AmazonKinesisClient _kinesisClient = new();
        private readonly string _streamName = 
            (configuration != null ? configuration[KinesisStreamEnvName] : Environment.GetEnvironmentVariable(KinesisStreamEnvName)) 
                ?? throw new ArgumentException(KinesisStreamEnvName);
                
        public async Task<string> FunctionHandler(DataModel data, ILambdaContext context)
        {
            if (data == null)
            {
                context.Logger.LogWarning($"No data received");
                return string.Empty;
            }

            try
            {
                var jsonData = JsonSerializer.Serialize(data, LambdaFunctionJsonSerializerContext.Default.DataModel);
                context.Logger.LogInformation($"Putting data: {jsonData} on stream:{_streamName}");
                var result = await PutRecordToKinesisStream(jsonData);

                context.Logger.LogInformation($"Data ingested successfully. Sequence number: {result.SequenceNumber}");
                return result.SequenceNumber;
            }
            catch (Exception ex)
            {
                context.Logger.LogError($"Error ingesting data: {ex.Message}");
                return string.Empty;
            }
        }

        private async Task<PutRecordResponse> PutRecordToKinesisStream(string data)
        {
            var recordBytes = System.Text.Encoding.UTF8.GetBytes(data);

            var request = new PutRecordRequest
            {
                StreamName = _streamName,
                PartitionKey = Guid.NewGuid().ToString(),
                Data = new MemoryStream(recordBytes)
            };

            return await _kinesisClient.PutRecordAsync(request);
        }
    }
 }