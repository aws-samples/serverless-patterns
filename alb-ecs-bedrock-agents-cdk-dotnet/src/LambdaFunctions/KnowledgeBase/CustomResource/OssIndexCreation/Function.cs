using System.Text.Json;
using Amazon;
using Amazon.Lambda.Core;
using OpenSearch.Client;
using OpenSearch.Net.Auth.AwsSigV4;
using OssIndexCreation.Models;
using OssIndexCreation.Serialization;
using OssIndexCreation.Utils;

namespace OssIndexCreation;

public class Function
{
    public static async Task FunctionHandler(object request, ILambdaContext context)
    {
        context.Logger.LogInformation($"Received input as {request}");

        var cfnRequest = JsonSerializer.Deserialize(request?.ToString() ?? string.Empty, LambdaFunctionJsonSerializerContext.Default.CfnRequest)
            ?? throw new Exception("Invalid request");

        var response = new CfnResponse
        {
            // build all the common responses from the request
            StackId = cfnRequest.StackId,
            RequestId = cfnRequest.RequestId,
            LogicalResourceId = cfnRequest.LogicalResourceId,
            PhysicalResourceId = cfnRequest.PhysicalResourceId
        };

        try
        {
            switch (cfnRequest.RequestType.ToLowerInvariant())
            {
                case "create":
                    context.Logger.LogInformation("Received Create request");
                    response.PhysicalResourceId = await CreateIndex(cfnRequest.ResourceProperties, context);
                    response.Status = "SUCCESS";
                    break;

                case "delete":
                    context.Logger.LogInformation("Received Delete request");
                    response.Status = "SUCCESS";
                    break;

                case "update":
                    context.Logger.LogInformation("Received Update request");
                    response.Status = "SUCCESS";
                    break;
            }

            context.Logger.LogInformation($"Uploading response to {cfnRequest.ResponseURL} ");
            await ResponseUtils.UploadResponse(cfnRequest.ResponseURL, response);
        }
        catch (Exception e)
        {
            context.Logger.LogError("Error occurred: " + e.Message);
            response.PhysicalResourceId = cfnRequest.PhysicalResourceId ?? cfnRequest.ResourceProperties.AOSSIndexName.ToString();
            response.Status = "FAILED";
            response.Reason = e.Message;
            await ResponseUtils.UploadResponse(cfnRequest.ResponseURL, response);
        }

        context.Logger.LogInformation("Finished");
    }

    private static async Task<string> CreateIndex(ResourceProperties resourceProperties, ILambdaContext context)
    {
        // Get Region
        var region = resourceProperties.Region?.ToString() ?? throw new Exception("Region not provided from resource properties");
        context.Logger.LogInformation($"CreteIndex:Region: {region}");

        // Get AOSS Host Name
        var aossHost = resourceProperties.AOSSHost?.ToString() ?? throw new Exception("AOSSHost not provided from resource properties");
        context.Logger.LogInformation($"CreteIndex:AOSSHost: {aossHost}");

        // Get AOSS Index Name
        var aossIndexName = resourceProperties.AOSSIndexName?.ToString() ?? throw new Exception("AOSSIndexName not provided from resource properties");
        context.Logger.LogInformation($"CreteIndex:AOSSIndexName: {aossIndexName}");

        // Get metadata field name
        var metadataFiledName = resourceProperties.AOSSMetadataFieldName?.ToString() ?? throw new Exception("MetadataFiledName not provided from resource properties");
        context.Logger.LogInformation($"CreteIndex:MetadataFiledName: {metadataFiledName}");

        // Get Text Filed Name
        var textFiledName = resourceProperties.AOSSTextFieldName?.ToString() ?? throw new Exception("TextFiledName not provided from resource properties");
        context.Logger.LogInformation($"CreteIndex:TextFiledName: {textFiledName}");

        // Get Vector Filed Name
        var vectorFiledName = resourceProperties.AOSSVectorFieldName?.ToString() ?? throw new Exception("VectorFiledName not provided from resource properties");
        context.Logger.LogInformation($"CreteIndex:VectorFiledName: {vectorFiledName}");

        try
        {
            // OpenSearch client
            context.Logger.LogInformation($"Creating index {aossIndexName} in {region} region...");

            var endpoint = new Uri($"{aossHost}");
            var connection = new AwsSigV4HttpConnection(RegionEndpoint.GetBySystemName(region), service: AwsSigV4HttpConnection.OpenSearchServerlessService);        
            var config = new ConnectionSettings(endpoint, connection);
            var client = new OpenSearchClient(config);
            
            var response = await client.Indices.CreateAsync(
                aossIndexName,
                cid => 
                cid.Settings(s => s
                    .Setting("index.knn", true)
                    .Setting("index.number_of_shards", 2)
                    .Setting("index.number_of_replicas", 0)
                )
                .Map(m => m
                    .Properties(p => p
                        .Text(t => t.Name(metadataFiledName).Index(false))
                        .Text(t => t.Name(textFiledName))
                        .KnnVector(k => k.Name(vectorFiledName)
                                        .Dimension(1024)
                                        .Method(md => md.Name("hnsw")
                                                        .Engine("faiss")
                                                        .SpaceType("l2")
                                                        .Parameters(p => p))
                        )
                    )
                    .DynamicTemplates(dt => dt
                        .DynamicTemplate("strings", d => d
                            .MatchMappingType("string")
                            .Mapping(m => m
                                .Text(t => t
                                    .Fields(f => f
                                        .Keyword(k => k
                                            .IgnoreAbove(2147483647)
                                            .Name("keyword")
                                        )
                                    )
                                )
                            )
                        )
                    )
                )
            );

            if (!response.IsValid)
                throw new Exception($"Error creating index: {response.ServerError}");

            context.Logger.LogInformation($"Index {aossIndexName} created successfully");

            // Wait, so that the index is available for search
            context.Logger.LogInformation("Waiting for 60 seconds for the index to be available for search...");
            await Task.Delay(TimeSpan.FromSeconds(60));

            return aossIndexName;
        }
        catch (Exception e)
        {
            context.Logger.LogError($"Error creating index: {e.Message}{Environment.NewLine}{e.StackTrace}");
            throw;
        }        
    }
}