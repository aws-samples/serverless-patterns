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
            PhysicalResourceId = !string.IsNullOrEmpty(cfnRequest.PhysicalResourceId) 
                ? cfnRequest.PhysicalResourceId 
                : $"{cfnRequest.ResourceProperties.AgentId}-{cfnRequest.ResourceProperties.AliasName}",
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
                    await DeleteAllAliasesAsync(cfnRequest.ResourceProperties, context);

                    response.Status = "SUCCESS";
                    response.PhysicalResourceId = cfnRequest.PhysicalResourceId;
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
    private static async Task<(string aliasId, string aliasArn)> CreateBedrockAgentAliasAsync(
        ResourceProperties resourceProperties, ILambdaContext context)
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

    /// <summary>
    /// Deletes all aliases for the given agent
    /// </summary>
    /// <param name="resourceProperties">Resource properties</param>
    /// <param name="context">Lambda context</param>
    private static async Task DeleteAllAliasesAsync(
        ResourceProperties resourceProperties, ILambdaContext context)
    {
        // Get Region
        var region = resourceProperties.Region?.ToString() ?? throw new Exception("Region not provided from resource properties");
        context.Logger.LogInformation($"CreateAlias:Region: {region}");

        // Get AgentId
        var agentId = resourceProperties.AgentId?.ToString() ?? throw new Exception("AgentId not provided from resource properties");
        context.Logger.LogInformation($"CreateAlias:AgentId: {agentId}");

        // Get all agent aliases
        var agentAliases = await GetAllAgentAliasesAsync(agentId, context);

        try
        {
            // Create 
            context.Logger.LogInformation("Deleting All Bedrock Agent Aliases");

            using var bedrockAgentClient = new AmazonBedrockAgentClient();
            
            // Delete all aliases
            agentAliases.ForEach(async agentAliasId =>
            {
                // Delete alias
                var deleteAgentAliasResponse = await bedrockAgentClient.DeleteAgentAliasAsync(
                    new DeleteAgentAliasRequest
                    {
                        AgentAliasId = agentAliasId,
                        AgentId = agentId
                    });

                // Check for successful status code
                if (deleteAgentAliasResponse.HttpStatusCode >= HttpStatusCode.BadRequest)
                    throw new Exception($"Failed to delete agent alias. Status code: {deleteAgentAliasResponse.HttpStatusCode}");
                else
                    context.Logger.LogInformation($"Agent Alias was deleted successfully, Id: {agentAliasId}");
            });
        }
        catch (Exception e)
        {
            context.Logger.LogError($"Error creating agent alias: {e.Message}{Environment.NewLine}{e.StackTrace}");
            throw;
        }
    }

    /// <summary>
    /// Gets all aliases for the given agent
    /// </summary>
    /// <param name="agentId">AgentId</param>
    /// <param name="context">Lambda context</param>
    /// <returns></returns>
    private static async Task<List<string>> GetAllAgentAliasesAsync(string agentId, ILambdaContext context)
    {
        context.Logger.LogInformation("Getting All Bedrock Agent Aliases");

        var agentAliases = new List<string>();
        string? nextToken = null;
        using var bedrockAgentClient = new AmazonBedrockAgentClient();

        try
        {
            while (true)
            {
                // List all aliases
                var listAgentAliasesResponse = await bedrockAgentClient.ListAgentAliasesAsync(
                    new ListAgentAliasesRequest
                    {
                        AgentId = agentId,
                        MaxResults = 10,
                        NextToken = nextToken
                    });

                // Check for successful status code
                if (listAgentAliasesResponse.HttpStatusCode >= HttpStatusCode.BadRequest)
                    throw new Exception($"Failed to create agent alias. Status code: {listAgentAliasesResponse.HttpStatusCode}");

                // Check if there are no aliases
                if (listAgentAliasesResponse.AgentAliasSummaries.Count == 0)
                    break;

                // Add Aliases to list
                agentAliases.AddRange(listAgentAliasesResponse.AgentAliasSummaries.Select(alias => alias.AgentAliasId));

                // Check if there are more aliases
                if (string.IsNullOrEmpty(listAgentAliasesResponse.NextToken))
                    break;

                nextToken = listAgentAliasesResponse.NextToken;
            }

            return agentAliases;
        }
        catch(Exception ex)
        {
            context.Logger.LogError($"Error getting agent aliases: {ex.Message}{Environment.NewLine}{ex.StackTrace}");
            throw;
        }
    }
}