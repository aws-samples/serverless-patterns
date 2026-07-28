# AWS Lambda Durable Function — Expense Approval (Human Interaction / Wait for Event)

This sample demonstrates how to build an expense approval workflow using **AWS Lambda durable functions** for .NET with **AWS SAM**. The workflow submits an expense report, pauses execution to wait for a manager's approval via an external callback, then proceeds with reimbursement or rejection.

## Architecture

```
┌────────────┐     ┌─────────────────────────────────────────────────────────────┐
│  POST      │     │        Lambda Durable Function (Expense Workflow)            │
│ /expenses  │────▶│                                                             │
└────────────┘     │  ┌──────────────────────────────────────────────────┐       │
                   │  │ Step: Create callback + save expense to DynamoDB  │       │
                   │  └──────────────────────┬───────────────────────────┘       │
                   │                         ▼                                   │
                   │  ┌──────────────────────────────────────────────────┐       │
                   │  │ WaitForCallback: Suspend up to 72 hours          │       │
                   │  │ (Lambda terminates — no compute charges)          │       │
                   │  └──────────────────────┬───────────────────────────┘       │
                   │                         │                                   │
                   └─────────────────────────┼───────────────────────────────────┘
                                             │
             ┌───────────────────────────────┼───────────────────────────────┐
             │                               │                               │
             ▼                               ▼                               ▼
  ┌───────────────────┐        ┌──────────────────────┐        ┌──────────────────┐
  │ Manager approves  │        │  Manager rejects     │        │  72h timeout     │
  │ POST /approve     │        │  POST /reject        │        │  (auto-reject)   │
  └─────────┬─────────┘        └──────────┬───────────┘        └────────┬─────────┘
            │                              │                             │
            ▼                              ▼                             ▼
  ┌───────────────────┐        ┌──────────────────────┐        ┌──────────────────┐
  │ Process           │        │ Record rejection     │        │ Record timeout   │
  │ reimbursement     │        │ in DynamoDB          │        │ in DynamoDB      │
  └───────────────────┘        └──────────────────────┘        └──────────────────┘
```

## What It Demonstrates

- **Callbacks (Wait for Event)** — The workflow creates a callback ID, stores it in DynamoDB, then suspends. The Lambda terminates with zero compute charges until the manager responds.
- **Human interaction** — A separate API endpoint allows the manager to approve or reject, sending the decision back to the suspended workflow.
- **Durable timers** — If no decision arrives within 72 hours, the callback times out and the expense is auto-rejected.
- **Automatic checkpointing** — Each step is checkpointed. If the Lambda is interrupted during reimbursement processing, it resumes from the last completed step.
- **AWS SAM** — Infrastructure defined in `template.yaml` with API Gateway, DynamoDB, and Lambda.

## Project Structure

```
├── template.yaml                  # SAM template (API Gateway, DynamoDB, Lambda)
├── events/
│   ├── submit-expense.json        # Sample expense submission
│   ├── approve-expense.json       # Sample approval event
│   └── reject-expense.json        # Sample rejection event
└── src/
    ├── ExpenseWorkflowHandler.cs  # Durable workflow (submit → wait → process)
    ├── ApproverHandler.cs         # Manager approval/rejection endpoint
    ├── ExpenseRepository.cs       # DynamoDB persistence
    ├── Models.cs                  # Record types
    └── ExpenseApproval.csproj
```

---

## Prerequisites

- [.NET 10 SDK](https://dotnet.microsoft.com/download/dotnet/10.0)
- [AWS SAM CLI](https://docs.aws.amazon.com/serverless-application-model/latest/developerguide/install-sam-cli.html)
- AWS account with credentials configured (`aws configure`)

---

## Build & Deploy

### Build

```bash
sam build
```

### Deploy

```bash
sam deploy --guided
```

Follow the prompts to configure stack name, region, and confirm IAM role creation. On subsequent deploys:

```bash
sam deploy
```

---

## Testing

### 1. Submit an expense report

```bash
API_URL=$(aws cloudformation describe-stacks \
    --stack-name sam-dotnet-durablefunction-expenseapproval \
    --query "Stacks[0].Outputs[?OutputKey=='ApiEndpoint'].OutputValue" \
    --output text)

curl -X POST "$API_URL/expenses" \
    -H "Content-Type: application/json" \
    -d '{
        "ExpenseId": "EXP-001",
        "SubmittedBy": "jane.doe@example.com",
        "Description": "Client dinner - Q3 planning",
        "Amount": 142.50,
        "Currency": "USD",
        "ManagerEmail": "john.manager@example.com"
    }'
```

The workflow starts, saves the expense, and suspends waiting for approval. The API returns HTTP 202 with a confirmation body:

```json
{
    "ExpenseId": "EXP-001",
    "SubmittedBy": "jane.doe@example.com",
    "Description": "Client dinner - Q3 planning",
    "Amount": 142.50,
    "Currency": "USD",
    "ManagerEmail": "john.manager@example.com"
}
```

### 2. Check the pending expense in DynamoDB

```bash
TABLE_NAME=$(aws cloudformation describe-stacks \
    --stack-name sam-dotnet-durablefunction-expenseapproval \
    --query "Stacks[0].Outputs[?OutputKey=='ExpenseTableName'].OutputValue" \
    --output text)

aws dynamodb get-item \
    --table-name $TABLE_NAME \
    --key '{"ExpenseId":{"S":"EXP-001"}}'
```

You'll see `Status: "pending_approval"` and a `CallbackId`. After approval, the item will also contain `Status: "approved"` and a `ReimbursementId`.

### 3. Approve the expense (manager action)

```bash
curl -X POST "$API_URL/expenses/EXP-001/approve" \
    -H "Content-Type: application/json" \
    -d '{"decidedBy": "john.manager@example.com"}'
```

This resumes the suspended workflow, which processes the reimbursement and updates DynamoDB.

### 4. Or reject it

```bash
curl -X POST "$API_URL/expenses/EXP-001/reject" \
    -H "Content-Type: application/json" \
    -d '{
        "decidedBy": "john.manager@example.com",
        "reason": "Amount exceeds per-diem limit"
    }'
```

### 5. Check execution status

```bash
FUNCTION_ARN=$(aws cloudformation describe-stacks \
    --stack-name sam-dotnet-durablefunction-expenseapproval \
    --query "Stacks[0].Outputs[?OutputKey=='ExpenseWorkflowFunctionArn'].OutputValue" \
    --output text)

aws lambda list-durable-executions-by-function \
    --function-name $FUNCTION_ARN
```

---

## How the Callback Pattern Works

```csharp
// 1. Create a callback — allocates a unique ID
var callback = await ctx.CreateCallbackAsync<ApprovalDecision>(
    name: "await-manager-approval",
    config: new CallbackConfig { Timeout = TimeSpan.FromHours(72) });

// 2. Store the callback ID so the external system can find it
await ctx.StepAsync(
    async (_, ct) => await _repository.SaveExpenseAsync(expense, callback.CallbackId, ct),
    name: "save-expense");

// 3. Suspend execution — Lambda terminates, no compute charges
var decision = await callback.GetResultAsync();
// Execution resumes here when the manager calls SendDurableExecutionCallbackSuccess
```

The approver endpoint resolves the callback:

```csharp
await LambdaClient.SendDurableExecutionCallbackSuccessAsync(
    new SendDurableExecutionCallbackSuccessRequest
    {
        CallbackId = callbackId,
        Result = new MemoryStream(Encoding.UTF8.GetBytes(resultJson))
    });
```

If 72 hours pass without a response, the callback times out and the workflow catches the timeout to auto-reject.

---

## Cleanup

```bash
sam delete
```

---

## References

- [AWS Lambda Durable Execution SDK for .NET](https://github.com/aws/aws-lambda-dotnet/tree/master/Libraries/src/Amazon.Lambda.DurableExecution)
- [Callbacks documentation](https://github.com/aws/aws-lambda-dotnet/blob/master/Libraries/src/Amazon.Lambda.DurableExecution/docs/core/callbacks.md)
- [AWS SAM Developer Guide](https://docs.aws.amazon.com/serverless-application-model/latest/developerguide/)
