using System.Net;
using System.Reflection;
using System.Text.Json;
using Amazon.BedrockAgent;
using Amazon.BedrockAgent.Model;
using Amazon.Lambda.Core;
using Amazon.S3;
using Amazon.S3.Model;
using KnowledgeBaseIngestion.Models;
using KnowledgeBaseIngestion.Serialization;
using KnowledgeBaseIngestion.Utils;

namespace KnowledgeBaseIngestion;

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
            PhysicalResourceId = $"{cfnRequest.ResourceProperties.KnowledgeBaseId}-{cfnRequest.ResourceProperties.DataSourceId}",
        };

        try
        {
            switch (cfnRequest.RequestType.ToLowerInvariant())
            {
                case "create":
                    context.Logger.LogInformation("Received Create request");
                    
                    await UploadDocumentsAsync(cfnRequest.ResourceProperties, context);
                    await StartIngestionAsync(cfnRequest.ResourceProperties, context);

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
            response.Status = "FAILED";
            response.Reason = e.Message;
            await ResponseUtils.UploadResponse(cfnRequest.ResponseURL, response);
        }

        context.Logger.LogInformation("Finished");
    }

    /// <summary>
    /// Uploads the documents to the S3 bucket
    /// </summary>
    /// <param name="resourceProperties">Resource properties</param>
    /// <param name="context">Lambda Context</param>
    private static async Task UploadDocumentsAsync(ResourceProperties resourceProperties, ILambdaContext context)
    {
        // Get Region
        var region = resourceProperties.Region?.ToString() ?? throw new Exception("Region not provided from resource properties");
        context.Logger.LogInformation($"UploadDocuments:Region: {region}");

        // Get Bucket Name
        var bucketName = resourceProperties.BucketName?.ToString() ?? throw new Exception("BucketName not provided from resource properties");
        context.Logger.LogInformation($"UploadDocuments:BucketName: {bucketName}");

        try
        {
            context.Logger.LogInformation("Uploading documents to S3 bucket");
            context.Logger.LogInformation($"Current Directory: {Directory.GetCurrentDirectory()}");
            context.Logger.LogInformation($"Executing Assembly Location: {Assembly.GetExecutingAssembly().Location}");

            // Get the list of files in the PolicyFiles folder
            var files = Directory.GetFiles(Directory.GetCurrentDirectory(), "Policies*.md");

            // Create an instance of the AmazonS3Client
            using var s3Client = new AmazonS3Client();
            foreach (var file in files)
            {
                // Get the file name
                var fileName = Path.GetFileName(file);
                context.Logger.LogInformation($"Uploading file {fileName}");

                // Create a PutObjectRequest to upload the file to the S3 bucket
                var putObjectRequest = new PutObjectRequest
                {
                    BucketName = bucketName,
                    Key = fileName,
                    FilePath = file
                };

                // Upload the file to the S3 bucket
                await s3Client.PutObjectAsync(putObjectRequest);
            }

            context.Logger.LogInformation("Documents uploaded to S3 bucket");
        }
        catch (Exception e)
        {
            context.Logger.LogError($"Error uploading documents: {e.Message}{Environment.NewLine}{e.StackTrace}");
            throw;
        }        
    }


    /// <summary>
    /// Starts the ingestion job in Knowledge Base and waits for it to complete
    /// <param name="resourceProperties">Resource properties</param>
    /// <param name="context">Lambda Context</param>
    private static async Task StartIngestionAsync(ResourceProperties resourceProperties, ILambdaContext context)
    {
        // Get Region
        var region = resourceProperties.Region?.ToString() ?? throw new Exception("Region not provided from resource properties");
        context.Logger.LogInformation($"StartIngestion:Region: {region}");

        // Get KnowledgeBaseId
        var knowledgeBaseId = resourceProperties.KnowledgeBaseId?.ToString() ?? throw new Exception("KnowledgeBaseId not provided from resource properties");
        context.Logger.LogInformation($"StartIngestion:KnowledgeBaseId: {knowledgeBaseId}");

        var dataSourceId = resourceProperties.DataSourceId?.ToString() ?? throw new Exception("DataSourceId not provided from resource properties");
        context.Logger.LogInformation($"StartIngestion:DataSourceId: {dataSourceId}");        

        try
        {
            // Start Bedrock Ingestion Job and then call GetIngestionJob in loop till it comoletes
            context.Logger.LogInformation("Starting Bedrock Ingestion Job");

            using var bedrockAgentClient = new AmazonBedrockAgentClient();
            var clientToken = Guid.NewGuid().ToString();

            // Start Ingestion Job
            var startIngestionJobResponse = await bedrockAgentClient.StartIngestionJobAsync(
                new StartIngestionJobRequest
                {
                    KnowledgeBaseId = knowledgeBaseId,
                    DataSourceId = dataSourceId,
                    ClientToken = clientToken
                });

            // Check for successful status code
            if (startIngestionJobResponse.HttpStatusCode >= HttpStatusCode.BadRequest)
                throw new Exception($"Failed to start ingestion job. Status code: {startIngestionJobResponse.HttpStatusCode}");
            else
                context.Logger.LogInformation($"Ingestion Job started successfully, Id: {startIngestionJobResponse.IngestionJob.IngestionJobId}");
            
            // Job
            var ingestionJob = startIngestionJobResponse.IngestionJob;
            var getJobFailureCount = 0;

            while (true)
            {
                if (ingestionJob.Status == IngestionJobStatus.COMPLETE)
                {
                    context.Logger.LogInformation("Ingestion Job completed successfully");
                    break;
                }
                else if (ingestionJob.Status == IngestionJobStatus.FAILED)
                {
                    var failureReasons = string.Join(", ", ingestionJob.FailureReasons);
                    throw new Exception("Ingestion Job failed: " + failureReasons);
                }
                else
                {
                    context.Logger.LogInformation($"Ingestion Job status: {ingestionJob.Status}");

                    // Wait for 10 seconds before checking the status again
                    await Task.Delay(TimeSpan.FromSeconds(10));                    
                }

                var getIngestionJobResponse = await bedrockAgentClient.GetIngestionJobAsync(
                    new GetIngestionJobRequest
                    {
                        KnowledgeBaseId = knowledgeBaseId,
                        DataSourceId = dataSourceId,
                        IngestionJobId = ingestionJob.IngestionJobId
                    });

                // Check for successful status code
                if (getIngestionJobResponse.HttpStatusCode >= HttpStatusCode.BadRequest)
                {
                    getJobFailureCount++;
                    if (getJobFailureCount > 3)
                        throw new Exception($"Failed to get ingestion job. Status code: {getIngestionJobResponse.HttpStatusCode}");
                }

                ingestionJob = getIngestionJobResponse.IngestionJob;
            }
        }
        catch (Exception e)
        {
            context.Logger.LogError($"Error ingesting documents: {e.Message}{Environment.NewLine}{e.StackTrace}");
            throw;
        }
    }    
}