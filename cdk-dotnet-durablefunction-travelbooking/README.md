# AWS Lambda Durable Function — Flight Booking with Payment Callback & Saga Compensation

This sample demonstrates a realistic flight booking workflow using **AWS Lambda Durable Functions** for .NET. The workflow checks availability, suspends while waiting for the payment gateway to confirm (callback), books with the airline, and handles failures with saga compensation — spanning minutes with zero idle compute cost.

## Architecture

```
                                        ┌─────────────────────────────┐
                                        │     Payment Gateway         │
                                        │     (external system)       │
                                        │                             │
                                        │  1. Receives callback token │
                                        │  2. Sends OTP to user       │
                                        │  3. User verifies OTP       │
                                        │  4. Calls us back ──────────┼──┐
                                        └─────────────────────────────┘  │
                                                                         │
┌──────────┐  POST /bookings   ┌───────────────┐                        │
│  Client  │──────────────────▶│  API Gateway  │                        │
└──────────┘                   └───────┬───────┘                        │
                                       │                                │
                                       ▼                                │
                          ┌────────────────────────┐                    │
                          │  Durable Function      │                    │
                          │                        │                    │
                          │  1. Check availability │                    │
                          │  2. Create callback ───┼── token to gateway │
                          │     ⏸ SUSPEND          │                    │
                          │        ...             │                    │
                          │     ⏸ RESUME ◀─────────┼────────────────────┘
                          │  3. Authorize payment  │   POST /bookings/payment-confirmation
                          │  4. Book flight        │         │
                          │     4b. If fails →     │         ▼
                          │         reverse payment│   ┌───────────────┐
                          │  5. ⏸ Wait (timer)     │   │ Payment       │
                          │  6. Capture payment    │   │ Callback      │
                          │  7. Send email         │   │ Lambda        │
                          │  8. Save result        │   │ (thin proxy)  │
                          └────────────────────────┘   └───────────────┘
```

## What It Demonstrates

- **Starter Lambda pattern** — A thin proxy Lambda receives the HTTP request, validates the payload, invokes the durable function asynchronously (`InvocationType.Event`), and returns 202 immediately. This keeps API Gateway response times under 1 second regardless of workflow duration.
- **Callback (external system interaction)** — Workflow suspends at zero cost, waiting for the payment gateway to call back. Resumes instantly when the confirmation arrives. The callback token is passed in the request body (not URL path) because the token is a binary blob that contains URL-unsafe characters.
- **Success or failure resumption** — A confirmed payment resumes the workflow with a result (`SendDurableExecutionCallbackSuccess`); a declined payment resumes it through the failure path (`SendDurableExecutionCallbackFailure`), which surfaces as an exception the workflow catches and ends cleanly with no funds held.
- **Durable timer** — 2-minute wait for airline confirmation that survives Lambda restarts.
- **Saga compensation** — If the airline rejects the booking after payment is authorized, the payment is reversed. Compensation steps are independently checkpointed.
- **Fail-fast validation** — Checks availability before initiating payment. No charge attempt if flights are full.
- **Payment lifecycle** — Authorize (hold) → Capture on success, or Reverse on failure.

## Project Structure

```
├── cdk.json
├── src/
│   ├── CdkDotnetDurablefunctionTravelbooking.slnx
│   ├── .globalconfig
│   ├── Infra/
│   │   ├── Program.cs
│   │   ├── InfraStack.cs
│   │   ├── GlobalSuppressions.cs
│   │   └── Infra.csproj
│   └── TravelBooking/
│       ├── Function.cs                # Durable workflow (FlightBookingHandler)
│       ├── BookingStarterHandler.cs   # Thin Lambda — validates request, invokes workflow async, returns 202
│       ├── PaymentCallbackHandler.cs  # Thin Lambda — resumes workflow on payment confirmation
│       ├── BookingServices.cs         # Mock services (availability, payment, airline, notifications)
│       ├── Models.cs                  # Input/output record types
│       └── TravelBooking.csproj
└── README.md
```

---

## Prerequisites

- [.NET 10 SDK](https://dotnet.microsoft.com/download/dotnet/10.0)
- [AWS CDK CLI](https://docs.aws.amazon.com/cdk/v2/guide/getting-started.html) (`npm install -g aws-cdk`)
- AWS account with credentials configured (`aws configure`)
- CDK bootstrapped in your target account/region (`cdk bootstrap`)

---

## Build & Deploy

```bash
dotnet build src/CdkDotnetDurablefunctionTravelbooking.slnx -c Release
cdk deploy
```

This creates:

| Resource | Description |
|----------|-------------|
| DynamoDB Table | Stores callback tokens (for testing) and booking results |
| Booking Lambda | Durable workflow (512 MB, 15-min execution timeout) |
| Booking Starter Lambda | Thin proxy — validates request, invokes workflow async, returns 202 |
| Payment Callback Lambda | Thin proxy — resumes the durable function on payment confirmation |
| API Gateway (REST) | Two routes: `POST /bookings` and `POST /bookings/payment-confirmation` |

---

## Testing

### Capture stack outputs

```bash
STACK_NAME="CdkDotnetDurablefunctionTravelbookingStack"

API_URL=$(aws cloudformation describe-stacks --stack-name $STACK_NAME \
    --query "Stacks[0].Outputs[?OutputKey=='ApiUrl'].OutputValue" --output text)

TABLE_NAME=$(aws cloudformation describe-stacks --stack-name $STACK_NAME \
    --query "Stacks[0].Outputs[?OutputKey=='BookingsTableName'].OutputValue" --output text)
```

### Step 1: Start a booking

```bash
curl -X POST "${API_URL}bookings" \
  -H "Content-Type: application/json" \
  -d '{
    "BookingId": "BK-001",
    "TravelerId": "traveler-123",
    "Email": "traveler@example.com",
    "Flight": {
      "Origin": "SEA",
      "Destination": "JFK",
      "DepartureDate": "2026-08-15T00:00:00Z",
      "ReturnDate": "2026-08-22T00:00:00Z",
      "CabinClass": "Economy"
    },
    "Payment": {
      "CardLast4": "4242",
      "CardHolder": "Jane Doe"
    }
  }'
```

The workflow starts and suspends at the payment callback. The Lambda is not running.

### Step 2: Get the callback ID

```bash
CALLBACK_ID=$(aws dynamodb get-item \
    --table-name $TABLE_NAME \
    --key '{"BookingId":{"S":"BK-001"},"SK":{"S":"CALLBACK#otp"}}' \
    --query "Item.CallbackId.S" --output text)

echo $CALLBACK_ID
```

### Step 3: Simulate payment gateway confirming

```bash
curl -X POST "${API_URL}bookings/payment-confirmation" \
  -H "Content-Type: application/json" \
  -d "{
    \"CallbackId\": \"${CALLBACK_ID}\",
    \"Status\": \"Confirmed\",
    \"TransactionRef\": \"TXN-abc123\"
  }"
```

This resumes the durable function. It continues through authorization → booking → airline wait → capture → email → save.

### Step 4: Check the result

Wait approximately 2–3 minutes for the durable timer (airline confirmation wait) and remaining steps to complete, then query:

```bash
aws dynamodb get-item \
    --table-name $TABLE_NAME \
    --key '{"BookingId":{"S":"BK-001"},"SK":{"S":"RESULT"}}' | jq .
```

### Test: No availability (fails fast)

Use `"FULL"` as origin — the workflow completes immediately with an "Unavailable" result. No payment is initiated and no callback is created:

```bash
curl -X POST "${API_URL}bookings" \
  -H "Content-Type: application/json" \
  -d '{
    "BookingId": "BK-002",
    "TravelerId": "t-456",
    "Email": "t@example.com",
    "Flight": {"Origin":"FULL","Destination":"LAX","DepartureDate":"2026-09-01T00:00:00Z","ReturnDate":"2026-09-05T00:00:00Z","CabinClass":"Economy"},
    "Payment": {"CardLast4":"1234","CardHolder":"John Doe"}
  }'
```

The response is still 202 (the starter always invokes async), but the durable function finishes in under a second. You can verify no callback was stored:

```bash
aws dynamodb get-item \
    --table-name $TABLE_NAME \
    --key '{"BookingId":{"S":"BK-002"},"SK":{"S":"CALLBACK#otp"}}' | jq .
```

### Test: Booking failure (saga compensation)

Use `"FAIL"` as origin — passes availability check but the airline rejects the booking after payment authorization, triggering saga compensation:

```bash
curl -X POST "${API_URL}bookings" \
  -H "Content-Type: application/json" \
  -d '{
    "BookingId": "BK-003",
    "TravelerId": "t-789",
    "Email": "t@example.com",
    "Flight": {"Origin":"FAIL","Destination":"LAX","DepartureDate":"2026-09-01T00:00:00Z","ReturnDate":"2026-09-05T00:00:00Z","CabinClass":"Business"},
    "Payment": {"CardLast4":"5678","CardHolder":"Bob Smith"}
  }'
```

This workflow also suspends at the payment callback. Retrieve the callback ID and confirm payment (same as Step 2 and 3 above, using `BK-003`). After the callback resumes the workflow, the airline rejects the booking and the payment is automatically reversed.

Check the compensated result:

```bash
aws dynamodb get-item \
    --table-name $TABLE_NAME \
    --key '{"BookingId":{"S":"BK-003"},"SK":{"S":"RESULT"}}' | jq .
```

You should see `"Status": "Failed"`, `"FailureReason": "Airline rejected the booking."`, and the actions list showing the payment reversal.

### Test: Declined payment (failure callback)

Start a booking as in Step 1 (use `BK-004`), retrieve the callback ID as in Step 2, then send a **declined** confirmation. Any `Status` other than `Confirmed` resumes the workflow through the failure path:

```bash
curl -X POST "${API_URL}bookings/payment-confirmation" \
  -H "Content-Type: application/json" \
  -d "{
    \"CallbackId\": \"${CALLBACK_ID}\",
    \"Status\": \"Declined\",
    \"TransactionRef\": \"TXN-declined\"
  }"
```

The callback Lambda calls `SendDurableExecutionCallbackFailure`, which surfaces inside the workflow as a `CallbackException`. The workflow ends cleanly with `"Status": "Failed"` and no payment authorization is ever attempted (no funds held).

### Test: No response (callback timeout)

Start a booking as in Step 1 (use `BK-005`) but **do not** send a payment confirmation. The callback has a 10-minute timeout (`CallbackConfig.Timeout`). When it elapses, Lambda resumes the workflow through the failure path and the booking ends as `Failed`:

```bash
aws dynamodb get-item \
    --table-name $TABLE_NAME \
    --key '{"BookingId":{"S":"BK-005"},"SK":{"S":"RESULT"}}' | jq .
```

After ~10 minutes you should see `"Status": "Failed"` with `"FailureReason": "Payment confirmation timed out after 10 minutes. No funds were held."`. This is the same catch block as the declined case, distinguished by the callback error type.

---

## Cleanup

```bash
cdk destroy
```

---

## References

- [Amazon.Lambda.DurableExecution SDK](https://github.com/aws/aws-lambda-dotnet/tree/master/Libraries/src/Amazon.Lambda.DurableExecution)
- [Durable Functions — Callbacks](https://docs.aws.amazon.com/durable-execution/sdk-reference/)
- [AWS CDK .NET Reference](https://docs.aws.amazon.com/cdk/api/v2/dotnet/)
