using System.Text;
using Amazon.DynamoDBv2;
using Amazon.DynamoDBv2.Model;
using Amazon.S3;
using Amazon.S3.Model;
using Newtonsoft.Json.Linq;

namespace IntegrationTests
{
    public class IntegrationTests : IDisposable
    {
        private const string HotDataTableName = "hot-data-table";
        private const string BucketName = "[REPLACE WITH YOUR BUCKET NAME]";
        private const string _apiUrl = "[REPLACE WITH YOUR API URL]";
        private const string _apiKey = "[REPLACE WITH YOUR API KEY]";
        private readonly HttpClient _httpClient;
        private readonly AmazonDynamoDBClient _dynamoDbClient;
        private readonly AmazonS3Client _s3Client;

        public IntegrationTests()
        {
            if (string.IsNullOrEmpty(_apiUrl) || string.IsNullOrEmpty(_apiKey))
                throw new Exception("_apiUrl and _apiKey environment must be set");


            _httpClient = new HttpClient();
            _httpClient.DefaultRequestHeaders.Add("x-api-key", _apiKey);

            _dynamoDbClient = new AmazonDynamoDBClient();
            _s3Client = new AmazonS3Client();
        }

        public void Dispose()
        {
            GC.SuppressFinalize(this);
            _httpClient.Dispose();
            _dynamoDbClient.Dispose();
            _s3Client.Dispose();
        }

        [Fact]
        public async Task GetHotData_ExistingId_ReturnsData()
        {
            var id = Guid.NewGuid().ToString();
            var content = "Test Content " + Guid.NewGuid().ToString();
            var timestamp = DateTime.UtcNow;

            // Arrange
            var query = @"
                query GetHotData($id: ID!) {
                    getHotData(id: $id) {
                        id
                        content
                        timestamp
                    }
                }";
            var variables = new { id = id };

            // Arrange
            var putItemRequest = new PutItemRequest
            {
                TableName = HotDataTableName,
                Item = new Dictionary<string, AttributeValue>
                {
                    { "id", new AttributeValue { S = id } },
                    { "content", new AttributeValue { S = content } },
                    { "timestamp", new AttributeValue { S = timestamp.ToString("yyyy-MM-ddTHH:mm:ssZ") } }
                }
            };
            await _dynamoDbClient.PutItemAsync(putItemRequest);

            // Act
            var response = await ExecuteGraphQLRequest(query, variables);

            // Assert
            AssertSuccessfulResponse(response, "getHotData", id, content, timestamp);

            // Delete item from DynamoDB
            var deleteItemRequest = new DeleteItemRequest
            {
                TableName = HotDataTableName,
                Key = new Dictionary<string, AttributeValue>
                {
                    { "id", new AttributeValue { S = id } }
                }
            };

            await _dynamoDbClient.DeleteItemAsync(deleteItemRequest);
        }

        [Fact]
        public async Task GetHotData_NonExistingId_ReturnsNull_Error()
        {
            // Arrange
            var query = @"
                query GetHotData($id: ID!) {
                    getHotData(id: $id) {
                        id
                        content
                        timestamp
                    }
                }";
            var variables = new { id = "non-existing-id-" + Guid.NewGuid().ToString() };

            // Act
            var response = await ExecuteGraphQLRequest(query, variables);

            // Assert
            AssertFailedResponse(response);
        }

        [Fact]
        public async Task GetColdData_ExistingId_ReturnsData()
        {
            var id = Guid.NewGuid().ToString();
            var content = "Test Content " + Guid.NewGuid().ToString();
            var timestamp = DateTime.UtcNow;

            var csvData = $"{id},{content},{timestamp:O}";
            await _s3Client.PutObjectAsync(new PutObjectRequest
            {
                BucketName = BucketName,
                Key = $"data/{id}.csv",
                ContentBody = csvData
            });

            // Arrange
            var query = @"
                query GetColdData($id: ID!) {
                    getColdData(id: $id) {
                        id
                        content
                        timestamp
                    }
                }";
            var variables = new { id = id };

            // Act
            var response = await ExecuteGraphQLRequest(query, variables);

            // Assert
            AssertSuccessfulResponse(response, "getColdData", id, content, timestamp);

            // Delete uploaded file from S3
            await _s3Client.DeleteObjectAsync(new DeleteObjectRequest
            {
                BucketName = BucketName,
                Key = $"data/{id}.csv"
            });              
        }

        [Fact]
        public async Task GetColdData_NonExistingId_ReturnsNull_Error()
        {
            // Arrange
            var query = @"
                query GetColdData($id: ID!) {
                    getColdData(id: $id) {
                        id
                        content
                        timestamp
                    }
                }";
            var variables = new { id = "non-existing-id-" + Guid.NewGuid().ToString() };

            // Act
            var response = await ExecuteGraphQLRequest(query, variables);

            // Assert
            AssertFailedResponse(response);
        }

        private async Task<JObject> ExecuteGraphQLRequest(string query, object variables)
        {
            var request = new
            {
                query,
                variables
            };

            var content = new StringContent(Newtonsoft.Json.JsonConvert.SerializeObject(request), Encoding.UTF8, "application/json");
            var response = await _httpClient.PostAsync(_apiUrl, content);
            response.EnsureSuccessStatusCode();

            var responseString = await response.Content.ReadAsStringAsync();
            return JObject.Parse(responseString);
        }

        private static void AssertSuccessfulResponse(JObject response, string query, string id, string content, DateTime timestamp)
        {
            Assert.NotEmpty(response?["data"]?[query]?.ToString() ?? string.Empty);
            Assert.Equal(id, response?["data"]?[query]?["id"]?.ToString());
            Assert.Equal(content, response?["data"]?[query]?["content"]?.ToString());
            Assert.Equal(timestamp.ToString("yyyy/MM/dd HH:mm:ss tt"), DateTime.Parse(response?["data"]?[query]?["timestamp"]?.ToString() ?? string.Empty).ToString("yyyy/MM/dd HH:mm:ss tt"));
            Assert.Null(response?["error"]?.ToString());            
        }

        private static void AssertFailedResponse(JObject response)
        {
            Assert.Empty(response?["data"]?["getColdData"]?.ToString() ?? string.Empty);
            Assert.NotEmpty(response?["errors"]?.ToString() ?? string.Empty);
            Assert.Contains("Item not found in database.", response?["errors"]?[0]?["message"]?.ToString());      
        }
    }
}