using Amazon.Lambda.Core;
using Amazon.Athena;
using Amazon.Athena.Model;
using System.Text.Json;
using ColdDataResolver.Serialization;
using ColdDataResolver.Models;

namespace ColdDataResolver
{
    public class ColdDataResolverFunction : IDisposable
    {
        private readonly AmazonAthenaClient _athenaClient;
        private readonly string _bucketName;
        private readonly string _databaseName;
        private readonly string _tableName;

        public ColdDataResolverFunction()
        {
            _bucketName = Environment.GetEnvironmentVariable("COLD_DATA_BUCKET") ?? throw new ArgumentNullException("COLD_DATA_BUCKET");
            _databaseName = Environment.GetEnvironmentVariable("GLUE_DATABASE") ?? throw new ArgumentNullException("GLUE_DATABASE");
            _tableName = Environment.GetEnvironmentVariable("GLUE_TABLE") ?? throw new ArgumentNullException("GLUE_TABLE");

            _athenaClient = new AmazonAthenaClient();
        }

        public void Dispose()
        {
            GC.SuppressFinalize(this);
            _athenaClient.Dispose();
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

                var queryExecutionId = await StartAthenaQuery(id);
                var queryResults = await GetQueryResults(queryExecutionId);

                if (queryResults.ResultSet.Rows.Count <= 1)
                    throw new Exception("Item not found in database.");

                var dataRow = queryResults.ResultSet.Rows[1];
                return JsonSerializer.Serialize(
                    new Data
                    {
                        Id = dataRow.Data[0].VarCharValue,
                        Content = dataRow.Data[1].VarCharValue,
                        Timestamp = dataRow.Data[2].VarCharValue
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

        private async Task<string> StartAthenaQuery(string id)
        {
            var queryString = $"SELECT * FROM {_databaseName}.{_tableName} WHERE id = '{id}'";
            var startQueryExecutionRequest = new StartQueryExecutionRequest
            {
                QueryString = queryString,
                QueryExecutionContext = new QueryExecutionContext
                {
                    Database = _databaseName
                },
                ResultConfiguration = new ResultConfiguration
                {
                    OutputLocation = $"s3://{_bucketName}/athena-results/"
                }
            };

            var startQueryExecutionResponse = await _athenaClient.StartQueryExecutionAsync(startQueryExecutionRequest);
            return startQueryExecutionResponse.QueryExecutionId;
        }

        private async Task<GetQueryResultsResponse> GetQueryResults(string queryExecutionId)
        {
            var getQueryExecutionRequest = new GetQueryExecutionRequest { QueryExecutionId = queryExecutionId };

            while (true)
            {
                var getQueryExecutionResponse = await _athenaClient.GetQueryExecutionAsync(getQueryExecutionRequest);
                var queryState = getQueryExecutionResponse.QueryExecution.Status.State;

                if (queryState == QueryExecutionState.SUCCEEDED)
                {
                    return await _athenaClient.GetQueryResultsAsync(new GetQueryResultsRequest { QueryExecutionId = queryExecutionId });
                }
                else if (queryState == QueryExecutionState.FAILED || queryState == QueryExecutionState.CANCELLED)
                {
                    throw new Exception($"Query failed or was cancelled. State: {queryState}");
                }

                await Task.Delay(500);
            }
        }
    }
}