using System.Globalization;
using Amazon.DynamoDBv2;
using Amazon.DynamoDBv2.Model;

namespace ExpenseApproval;

/// <summary>
/// Persists expense reports and their status to DynamoDB.
/// </summary>
public sealed class ExpenseRepository(IAmazonDynamoDB dynamoDb, string tableName)
{
    private readonly IAmazonDynamoDB _dynamoDb = dynamoDb;
    private readonly string _tableName = tableName;

    public async Task SaveExpenseAsync(ExpenseReport expense, string callbackId, CancellationToken ct)
    {
        ArgumentNullException.ThrowIfNull(expense);
        ArgumentException.ThrowIfNullOrEmpty(expense.ExpenseId, nameof(expense.ExpenseId));
        ArgumentException.ThrowIfNullOrEmpty(expense.SubmittedBy, nameof(expense.SubmittedBy));
        ArgumentException.ThrowIfNullOrEmpty(expense.Description, nameof(expense.Description));
        ArgumentException.ThrowIfNullOrEmpty(expense.Currency, nameof(expense.Currency));
        ArgumentException.ThrowIfNullOrEmpty(expense.ManagerEmail, nameof(expense.ManagerEmail));

        var item = new Dictionary<string, AttributeValue>
        {
            ["ExpenseId"] = new() { S = expense.ExpenseId },
            ["SubmittedBy"] = new() { S = expense.SubmittedBy },
            ["Description"] = new() { S = expense.Description },
            ["Amount"] = new() { N = expense.Amount.ToString(CultureInfo.InvariantCulture) },
            ["Currency"] = new() { S = expense.Currency },
            ["ManagerEmail"] = new() { S = expense.ManagerEmail },
            ["CallbackId"] = new() { S = callbackId },
            ["Status"] = new() { S = "pending_approval" },
            ["SubmittedAt"] = new() { S = DateTime.UtcNow.ToString("O", CultureInfo.InvariantCulture) }
        };

        await _dynamoDb.PutItemAsync(new PutItemRequest
        {
            TableName = _tableName,
            Item = item
        }, ct);
    }

    public async Task<string?> GetCallbackIdAsync(string expenseId, CancellationToken ct)
    {
        var response = await _dynamoDb.GetItemAsync(new GetItemRequest
        {
            TableName = _tableName,
            Key = new Dictionary<string, AttributeValue>
            {
                ["ExpenseId"] = new() { S = expenseId }
            },
            ProjectionExpression = "CallbackId"
        }, ct);

        return response.Item is not null
            && response.Item.TryGetValue("CallbackId", out var attr) ? attr.S : null;
    }

    public async Task UpdateStatusAsync(string expenseId, string status, string? decidedBy, string? reason, CancellationToken ct, string? reimbursementId = null)
    {
        var expressionValues = new Dictionary<string, AttributeValue>
        {
            [":status"] = new() { S = status },
            [":decidedAt"] = new() { S = DateTime.UtcNow.ToString("O", CultureInfo.InvariantCulture) }
        };

        var updateExpression = "SET #st = :status, DecidedAt = :decidedAt";

        if (decidedBy is not null)
        {
            expressionValues[":decidedBy"] = new() { S = decidedBy };
            updateExpression += ", DecidedBy = :decidedBy";
        }

        if (reason is not null)
        {
            expressionValues[":reason"] = new() { S = reason };
            updateExpression += ", Reason = :reason";
        }

        if (reimbursementId is not null)
        {
            expressionValues[":reimbursementId"] = new() { S = reimbursementId };
            updateExpression += ", ReimbursementId = :reimbursementId";
        }

        await _dynamoDb.UpdateItemAsync(new UpdateItemRequest
        {
            TableName = _tableName,
            Key = new Dictionary<string, AttributeValue>
            {
                ["ExpenseId"] = new() { S = expenseId }
            },
            UpdateExpression = updateExpression,
            ExpressionAttributeNames = new Dictionary<string, string>
            {
                ["#st"] = "Status"
            },
            ExpressionAttributeValues = expressionValues
        }, ct);
    }
}
