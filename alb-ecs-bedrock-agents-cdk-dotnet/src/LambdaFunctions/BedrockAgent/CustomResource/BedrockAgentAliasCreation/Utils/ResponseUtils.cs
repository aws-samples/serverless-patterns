using System.Text;
using System.Text.Json;
using Amazon.Lambda.Core;
using BedrockAgentAliasCreation.Models;
using BedrockAgentAliasCreation.Serialization;

namespace BedrockAgentAliasCreation.Utils
{
    public class ResponseUtils
    {
        public static async Task UploadResponse(string url, CfnResponse cfnResponse)
        {
            string json = JsonSerializer.Serialize(cfnResponse, LambdaFunctionJsonSerializerContext.Default.CfnResponse);
            byte[] byteArray = Encoding.UTF8.GetBytes(json);
            LambdaLogger.Log($"trying to upload json {json}");

            using HttpClient httpClient = new();
            HttpRequestMessage httpRequest = new(HttpMethod.Put, url)
            {
                Content = new ByteArrayContent(byteArray)
            };
            httpRequest.Content.Headers.ContentType = new System.Net.Http.Headers.MediaTypeHeaderValue("application/json");

            HttpResponseMessage response = await httpClient.SendAsync(httpRequest);
            LambdaLogger.Log($"Result of upload is {response.StatusCode}");
        }
    }
}