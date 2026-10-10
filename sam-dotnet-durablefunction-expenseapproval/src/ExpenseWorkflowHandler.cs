using System.Text.Json;
using Amazon.DynamoDBv2;
using Amazon.Lambda.APIGatewayEvents;
using Amazon.Lambda.Core;
using Amazon.Lambda.DurableExecution;

[assembly: LambdaSerializer(typeof(Amazon.Lambda.Serialization.SystemTextJson.DefaultLambdaJsonSerializer))]

namespace ExpenseApproval;

/// <summary>
/// Durable Function workflow for expense approval.
///
/// Flow:
///   1. Receive expense submission via API Gateway.
///   2. Save to DynamoDB with "pending_approval" status.
///   3. Create a callback and store the callback ID (so the approver can find it).
///   4. Wait for the manager to approve/reject (up to 72 hours).
///   5. On approval → process reimbursement. On rejection/timeout → mark rejected.
/// </summary>
public class ExpenseWorkflowHandler
{
    private static readonly IAmazonDynamoDB DynamoDbClient = new AmazonDynamoDBClient();

    private static readonly string TableName =
        Environment.GetEnvironmentVariable("EXPENSE_TABLE_NAME")
        ?? throw new InvalidOperationException("EXPENSE_TABLE_NAME environment variable is not set.");

    private readonly ExpenseRepository _repository = new(DynamoDbClient, TableName);

    public Task<DurableExecutionInvocationOutput> Handler(
        DurableExecutionInvocationInput input, ILambdaContext context)
        => DurableFunction.WrapAsync<APIGatewayProxyRequest, APIGatewayProxyResponse>(Workflow, input, context);

    private async Task<APIGatewayProxyResponse> Workflow(APIGatewayProxyRequest request, IDurableContext ctx)
    {
        // ──────────────────────────────────────────────────────────────────
        // Parse the expense report from the request body
        // ──────────────────────────────────────────────────────────────────
        var expense = JsonSerializer.Deserialize<ExpenseReport>(request.Body, new JsonSerializerOptions
        {
            PropertyNameCaseInsensitive = true
        });

        if (expense is null || expense.Amount <= 0)
        {
            return new APIGatewayProxyResponse
            {
                StatusCode = 400,
                Body = JsonSerializer.Serialize(new { message = "Invalid expense report. Amount must be positive." }),
                Headers = new Dictionary<string, string> { { "Content-Type", "application/json" } }
            };
        }

        // ──────────────────────────────────────────────────────────────────
        // Step 1: Create a callback for the approval decision.
        // The callback ID is stored in DynamoDB so the approver endpoint can find it.
        // ──────────────────────────────────────────────────────────────────
        var callback = await ctx.CreateCallbackAsync<ApprovalDecision>(
            name: "await-manager-approval",
            config: new CallbackConfig
            {
                Timeout = TimeSpan.FromHours(72)
            });

        // ──────────────────────────────────────────────────────────────────
        // Step 2: Save the expense report with the callback ID.
        // ──────────────────────────────────────────────────────────────────
        await ctx.StepAsync(
            async (_, ct) => await _repository.SaveExpenseAsync(expense, callback.CallbackId, ct),
            name: "save-expense",
            config: new StepConfig { RetryStrategy = RetryStrategy.Default });

        // ──────────────────────────────────────────────────────────────────
        // Step 3: Wait for the manager's decision (suspends execution).
        // The Lambda terminates here. Execution resumes when the approver
        // calls SendDurableExecutionCallbackSuccess/Failure.
        // ──────────────────────────────────────────────────────────────────
        ApprovalDecision? decision = null;
        var timedOut = false;

        try
        {
            decision = await callback.GetResultAsync();
        }
        catch (CallbackException ex) when (ex.Message.Contains("timeout", StringComparison.OrdinalIgnoreCase))
        {
            timedOut = true;
        }

        // ──────────────────────────────────────────────────────────────────
        // Step 4: Process the decision
        // ──────────────────────────────────────────────────────────────────
        ExpenseResult result;

        if (timedOut)
        {
            // Approval timed out — auto-reject
            await ctx.StepAsync(
                async (_, ct) => await _repository.UpdateStatusAsync(
                    expense.ExpenseId, "timed_out", null, "Approval timed out after 72 hours", ct),
                name: "handle-timeout",
                config: new StepConfig { RetryStrategy = RetryStrategy.Default });

            var timedOutAt = await ctx.StepAsync(
                (_, _) => Task.FromResult(DateTime.UtcNow),
                name: "get-timeout-timestamp");
            result = new ExpenseResult(
                expense.ExpenseId, "timed_out", null,
                "Approval timed out after 72 hours", null, timedOutAt);
        }
        else if (decision?.Decision == "approved")
        {
            // Process reimbursement
            var reimbursementId = await ctx.StepAsync(
                async (_, ct) =>
                {
                    var id = $"REIMB-{Guid.NewGuid().ToString("N")[..8].ToUpperInvariant()}";
                    await _repository.UpdateStatusAsync(
                        expense.ExpenseId, "approved", decision.DecidedBy, null, ct,
                        reimbursementId: id);
                    return id;
                },
                name: "process-reimbursement",
                config: new StepConfig { RetryStrategy = RetryStrategy.Default });

            var approvedAt = await ctx.StepAsync(
                (_, _) => Task.FromResult(DateTime.UtcNow),
                name: "get-approved-timestamp");
            result = new ExpenseResult(
                expense.ExpenseId, "approved", decision.DecidedBy,
                null, reimbursementId, approvedAt);
        }
        else
        {
            // Rejected
            await ctx.StepAsync(
                async (_, ct) => await _repository.UpdateStatusAsync(
                    expense.ExpenseId, "rejected", decision?.DecidedBy, decision?.Reason, ct),
                name: "handle-rejection",
                config: new StepConfig { RetryStrategy = RetryStrategy.Default });

            var rejectedAt = await ctx.StepAsync(
                (_, _) => Task.FromResult(DateTime.UtcNow),
                name: "get-rejected-timestamp");
            result = new ExpenseResult(
                expense.ExpenseId, "rejected", decision?.DecidedBy,
                decision?.Reason, null, rejectedAt);
        }

        return new APIGatewayProxyResponse
        {
            StatusCode = 200,
            Body = JsonSerializer.Serialize(result),
            Headers = new Dictionary<string, string> { { "Content-Type", "application/json" } }
        };
    }
}
