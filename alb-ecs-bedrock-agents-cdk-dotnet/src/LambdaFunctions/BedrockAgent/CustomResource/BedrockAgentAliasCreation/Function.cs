using System.Net;
using System.Text.Json;
using Amazon.BedrockAgent;
using Amazon.BedrockAgent.Model;
using Amazon.Lambda.Core;
using BedrockAgentAliasCreation.Models;
using BedrockAgentAliasCreation.Serialization;
using BedrockAgentAliasCreation.Utils;

namespace BedrockAgentAliasCreation;

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
            PhysicalResourceId = $"{cfnRequest.ResourceProperties.AgentId}-{cfnRequest.ResourceProperties.AliasName}",
        };

        try
        {
            switch (cfnRequest.RequestType.ToLowerInvariant())
            {
                case "create":
                    context.Logger.LogInformation("Received Create request");
                    (string aliasId, string aliasArn) = await CreateBedrockAgentAliasAsync(cfnRequest.ResourceProperties, context);

                    response.Status = "SUCCESS";
                    response.PhysicalResourceId = $"{cfnRequest.ResourceProperties.AgentId}-{aliasId}";
                    response.Data = new Dictionary<string, string>
                    {
                        { "AliasId", aliasId },
                        { "AliasArn", aliasArn }
                    };
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
    /// Creates a new Bedrock Agent Alias
    /// </summary>
    /// <param name="resourceProperties">Resource properties</param>
    /// <param name="context">Lambda context</param>
    /// <returns>Created Alias Id</returns>
    private static async Task<(string aliasId, string aliasArn)> CreateBedrockAgentAliasAsync(ResourceProperties resourceProperties, ILambdaContext context)
    {
        // Get Region
        var region = resourceProperties.Region?.ToString() ?? throw new Exception("Region not provided from resource properties");
        context.Logger.LogInformation($"CreateAlias:Region: {region}");

        // Get AliasName
        var aliasName = resourceProperties.AliasName?.ToString() ?? throw new Exception("AliasName not provided from resource properties");
        context.Logger.LogInformation($"CreateAlias:AliasName: {aliasName}");

        // Get AgentId
        var agentId = resourceProperties.AgentId?.ToString() ?? throw new Exception("AgentId not provided from resource properties");
        context.Logger.LogInformation($"CreateAlias:AgentId: {agentId}");        

        // Get Description
        var description = resourceProperties.Description?.ToString() ?? throw new Exception("Description not provided from resource properties");
        context.Logger.LogInformation($"CreateAlias:Description: {description}");

        try
        {
            // Create 
            context.Logger.LogInformation("Creating Bedrock Agent Alias");

            using var bedrockAgentClient = new AmazonBedrockAgentClient();
            var clientToken = Guid.NewGuid().ToString();

            // Create a new alias
            var createAgentAliasResponse = await bedrockAgentClient.CreateAgentAliasAsync(
                new CreateAgentAliasRequest
                {
                    AgentAliasName = aliasName,
                    AgentId = agentId,
                    ClientToken = clientToken,
                    Description = !string.IsNullOrEmpty(description) ? description : "Alias for Bedrock Agent"
                });

            // Check for successful status code
            if (createAgentAliasResponse.HttpStatusCode >= HttpStatusCode.BadRequest)
                throw new Exception($"Failed to create agent alias. Status code: {createAgentAliasResponse.HttpStatusCode}");
            else
                context.Logger.LogInformation($"Agent Alias was created successfully, Id: {createAgentAliasResponse.AgentAlias.AgentAliasId}");

            // Return the created alias id
            return (createAgentAliasResponse.AgentAlias.AgentAliasId,
                createAgentAliasResponse.AgentAlias.AgentAliasArn);
        }
        catch (Exception e)
        {
            context.Logger.LogError($"Error creating agent alias: {e.Message}{Environment.NewLine}{e.StackTrace}");
            throw;
        }
    }    
}