using System.Text;
using System.Text.Json;
using Amazon.Lambda;
using Amazon.Lambda.APIGatewayEvents;
using Amazon.Lambda.Core;
using Amazon.Lambda.Model;

namespace ExpenseApproval;

/// <summary>
/// Thin API Gateway handler that starts the expense workflow durable execution.
/// Invokes the durable function asynchronously (InvocationType = Event) so the
/// caller gets an immediate response while the long-running workflow executes.
/// </summary>
public class ExpenseStarterHandler
{
    private static readonly IAmazonLambda LambdaClient = new AmazonLambdaClient();

    private static readonly string WorkflowFunctionName =
        System.Environment.GetEnvironmentVariable("WORKFLOW_FUNCTION_NAME")
        ?? throw new InvalidOperationException("WORKFLOW_FUNCTION_NAME environment variable is not set.");

    public async Task<APIGatewayProxyResponse> Handler(APIGatewayProxyRequest request, ILambdaContext context)
    {
        // Validate the request body has a parseable expense report
        ExpenseReport? expense = null;
        if (!string.IsNullOrEmpty(request.Body))
        {
            expense = JsonSerializer.Deserialize<ExpenseReport>(request.Body, new JsonSerializerOptions
            {
                PropertyNameCaseInsensitive = true
            });
        }

        if (expense is null
            || string.IsNullOrEmpty(expense.ExpenseId)
            || expense.Amount <= 0
            || string.IsNullOrEmpty(expense.SubmittedBy)
            || string.IsNullOrEmpty(expense.Description)
            || string.IsNullOrEmpty(expense.Currency)
            || string.IsNullOrEmpty(expense.ManagerEmail))
        {
            return new APIGatewayProxyResponse
            {
                StatusCode = 400,
                Body = JsonSerializer.Serialize(new { message = "Invalid expense report. Provide ExpenseId, Amount (positive), SubmittedBy, Description, Currency, and ManagerEmail." }),
                Headers = new Dictionary<string, string> { { "Content-Type", "application/json" } }
            };
        }

        // Invoke the durable function asynchronously
        var invokeRequest = new InvokeRequest
        {
            FunctionName = WorkflowFunctionName,
            InvocationType = InvocationType.Event,
            Payload = JsonSerializer.Serialize(request)
        };

        var response = await LambdaClient.InvokeAsync(invokeRequest);

        context.Logger.LogInformation(
            $"Started expense workflow for {expense.ExpenseId}, status code: {response.StatusCode}");

        return new APIGatewayProxyResponse
        {
            StatusCode = 202,
            Body = JsonSerializer.Serialize(new
            {
                message = "Expense submitted for approval",
                expenseId = expense.ExpenseId,
                status = "pending_approval"
            }),
            Headers = new Dictionary<string, string> { { "Content-Type", "application/json" } }
        };
    }
}
