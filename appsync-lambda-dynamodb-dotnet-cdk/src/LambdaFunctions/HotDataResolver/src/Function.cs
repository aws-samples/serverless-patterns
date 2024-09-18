using Amazon.Lambda.Core;
using Amazon.DynamoDBv2;
using System.Text.Json;
using HotDataResolver.Models;
using HotDataResolver.Serialization;
using Amazon.DynamoDBv2.Model;

namespace HotDataResolver
{
    public class HotDataResolverFunction : IDisposable
    {
        private readonly AmazonDynamoDBClient _dynamoDbClient;
        private readonly string _tableName;

        public HotDataResolverFunction()
        {
            _tableName = Environment.GetEnvironmentVariable("HOT_DATA_TABLE") ?? throw new Exception("HOT_DATA_TABLE environment variable must be set");
            _dynamoDbClient = new AmazonDynamoDBClient();
        }

        public void Dispose()
        {
            GC.SuppressFinalize(this);
            _dynamoDbClient.Dispose();
        }

        public async Task<string> FunctionHandler(object input, ILambdaContext context)
        {
            if (input == null || string.IsNullOrEmpty(input.ToString()))
                throw new Exception("Input is null or empty.");

            try
            {
                // Deserialize the input object into a dictionary
                context.Logger.LogInformation("Query Input: " + input.ToString());

                // GetId
                var id = GetIdArgumentFromInput(input);
                context.Logger.LogInformation("Id: " + id);

                // Get item from DynamoDB
                var item = await GetItemAsync(id) ?? throw new Exception("Item not found in database.");

                // Response
                return JsonSerializer.Serialize(
                    new Data
                    {
                        Id = item["id"].S,
                        Content = item["content"].S,
                        Timestamp = item["timestamp"].S
                    },
                    LambdaFunctionJsonSerializerContext.Default.Data);
            }
            catch (Exception ex)
            {
                context.Logger.LogError($"Error occurred while processing request. Error:{ex.Message}{Environment.NewLine}{ex.StackTrace}");
                throw;
            }
        }

        private static string GetIdArgumentFromInput(object input)
        {
            // Unbox to JsonElement
            var json = (JsonElement)input;
            if (!json.TryGetProperty("arguments", out var argumentsJson))
                throw new Exception("Arguments not found in input.");

            var args = argumentsJson.Deserialize(LambdaFunctionJsonSerializerContext.Default.DictionaryStringString) ?? [];
            if (!args.TryGetValue("id", out var id) || string.IsNullOrEmpty(id))
                throw new Exception("Id not found in arguments.");

            return id;
        }

        private async Task<Dictionary<string, AttributeValue>> GetItemAsync(string id)
        {
            var getItemRequest = new GetItemRequest
            {
                TableName = _tableName,
                Key = new Dictionary<string, AttributeValue>
                {
                    { "id", new AttributeValue { S = id } }
                }
            };

            var getItemResponse = await _dynamoDbClient.GetItemAsync(getItemRequest);
            var item = getItemResponse.Item;

            return item;
        }
    }
}