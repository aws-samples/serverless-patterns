using System.Text;
using System.Text.Json;
using Amazon.DynamoDBv2;
using Amazon.Lambda;
using Amazon.Lambda.APIGatewayEvents;
using Amazon.Lambda.Core;
using Amazon.Lambda.Model;

namespace ExpenseApproval;

/// <summary>
/// Handles manager approval/rejection requests.
/// Looks up the callback ID from DynamoDB and sends the decision
/// back to the waiting durable execution via SendDurableExecutionCallbackSuccess.
/// </summary>
public class ApproverHandler
{
    private static readonly IAmazonDynamoDB DynamoDbClient = new AmazonDynamoDBClient();
    private static readonly IAmazonLambda LambdaClient = new AmazonLambdaClient();

    private static readonly string TableName =
        System.Environment.GetEnvironmentVariable("EXPENSE_TABLE_NAME")
        ?? throw new InvalidOperationException("EXPENSE_TABLE_NAME environment variable is not set.");

    private readonly ExpenseRepository _repository = new(DynamoDbClient, TableName);

    public async Task<APIGatewayProxyResponse> Handler(APIGatewayProxyRequest request, ILambdaContext context)
    {
        // Extract expense ID from path parameters
        if (!request.PathParameters.TryGetValue("expenseId", out var expenseId))
        {
            return new APIGatewayProxyResponse
            {
                StatusCode = 400,
                Body = JsonSerializer.Serialize(new { message = "Missing expenseId in path" }),
                Headers = new Dictionary<string, string> { { "Content-Type", "application/json" } }
            };
        }

        // Determine if this is an approval or rejection from the path
        var isApproval = request.Path.EndsWith("/approve", StringComparison.OrdinalIgnoreCase);
        var decisionType = isApproval ? "approved" : "rejected";

        // Parse optional body for decidedBy and reason
        string? decidedBy = null;
        string? reason = null;

        if (!string.IsNullOrEmpty(request.Body))
        {
            var body = JsonSerializer.Deserialize<JsonElement>(request.Body);
            if (body.TryGetProperty("decidedBy", out var db))
                decidedBy = db.GetString();
            if (body.TryGetProperty("reason", out var r))
                reason = r.GetString();
        }

        decidedBy ??= "manager";

        // Look up the callback ID from DynamoDB
        var callbackId = await _repository.GetCallbackIdAsync(expenseId, CancellationToken.None);

        if (callbackId is null)
        {
            return new APIGatewayProxyResponse
            {
                StatusCode = 404,
                Body = JsonSerializer.Serialize(new { message = $"Expense '{expenseId}' not found or already processed" }),
                Headers = new Dictionary<string, string> { { "Content-Type", "application/json" } }
            };
        }

        // Send the decision back to the durable execution via callback
        var decision = new ApprovalDecision(expenseId, decisionType, decidedBy, reason);
        var resultJson = JsonSerializer.Serialize(decision);

        await LambdaClient.SendDurableExecutionCallbackSuccessAsync(
            new SendDurableExecutionCallbackSuccessRequest
            {
                CallbackId = callbackId,
                Result = new MemoryStream(Encoding.UTF8.GetBytes(resultJson))
            });

        // Note: the workflow owns the DynamoDB status transition when it resumes,
        // so we don't write status here to avoid a racy double-write.

        context.Logger.LogInformation($"Expense {expenseId} {decisionType} by {decidedBy}");

        return new APIGatewayProxyResponse
        {
            StatusCode = 200,
            Body = JsonSerializer.Serialize(new
            {
                message = $"Expense {expenseId} has been {decisionType}",
                expenseId,
                decision = decisionType,
                decidedBy
            }),
            Headers = new Dictionary<string, string> { { "Content-Type", "application/json" } }
        };
    }
}
