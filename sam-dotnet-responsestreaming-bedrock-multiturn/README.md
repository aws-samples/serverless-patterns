# AWS Lambda Response Streaming with Multi-Turn Bedrock Agent — AI Trip Planner (.NET)

This sample demonstrates a **multi-turn AI agent** that can ask the user clarifying questions before generating a trip itinerary. Conversation state is persisted in DynamoDB between requests, and the final itinerary is streamed token-by-token through API Gateway response streaming.

## Architecture

```
┌──────────────┐        ┌──────────────────┐       ┌────────────────────┐       ┌─────────────┐
│   Client     │        │   API Gateway    │       │   Lambda Function  │       │   Amazon    │
│              │──POST─▶│   REST API       │──────▶│   (Agent Loop)     │◀─────▶│   Bedrock   │
│              │◀───────│                  │◀──────│                    │       │  (Claude)   │
└──────────────┘        └──────────────────┘       └────────┬───────────┘       └─────────────┘
                                                            │
                                                     ┌──────▼───────┐
                                                     │   DynamoDB   │
                                                     │  (Sessions)  │
                                                     │  TTL: 1 hour │
                                                     └──────────────┘

Flow:
  1. POST /plan { destination, days, interests }
     → Agent asks a question → JSON response with sessionId + question
  2. POST /plan { sessionId, message: "answer" }
     → Agent asks another question OR generates itinerary (streamed)
  3. Itinerary streams day-by-day via API Gateway response streaming
```

## What It Demonstrates

- **Multi-turn agent with session persistence** — The agent can pause, ask the user a question, and resume when the user responds. Conversation state (Bedrock message history) is stored in DynamoDB between requests.
- **Tool use for control flow** — Two tools: `ask_user` (suspends the loop, returns a question) and `add_day_plan` (generates itinerary content). The model decides which to call.
- **DynamoDB TTL** — Sessions automatically expire after 1 hour, requiring no cleanup logic.
- **Conditional response format** — Returns JSON when asking questions; switches to streamed text when generating the itinerary.
- **API Gateway response streaming** — The final itinerary streams progressively using `ResponseTransferMode: STREAM`.

## Project Structure

```
├── template.yaml              # SAM template (API Gateway + Lambda + DynamoDB with TTL)
├── events/
│   ├── new-trip.json          # Start a new trip planning conversation
│   └── continue-trip.json     # Continue with an answer to the agent's question
└── src/
    ├── Program.cs             # Entry point — routes new vs continuation requests
    ├── Models.cs              # Request/response records
    ├── TripPlannerAgent.cs    # Agent loop with ask_user suspension support
    ├── ToolDefinitions.cs     # Tool schemas (add_day_plan + ask_user)
    ├── SessionStore.cs        # DynamoDB session persistence with TTL
    ├── ResponseFormatter.cs   # Streaming output formatting
    └── TripPlannerMultiturn.csproj
```

---

## Prerequisites

- [.NET 10 SDK](https://dotnet.microsoft.com/download/dotnet/10.0)
- [AWS SAM CLI](https://docs.aws.amazon.com/serverless-application-model/latest/developerguide/install-sam-cli.html)
- AWS account with credentials configured (`aws configure`)
- **Amazon Bedrock model access** — Enable access to Claude Sonnet in the [Bedrock console](https://console.aws.amazon.com/bedrock/home#/modelaccess)

---

## Build & Deploy

```bash
sam build
sam deploy --guided
```

---

## Testing

### 1. Get the API endpoint

```bash
API_URL=$(aws cloudformation describe-stacks \
    --stack-name sam-dotnet-responsestreaming-bedrock-multiturn \
    --query "Stacks[0].Outputs[?OutputKey=='ApiEndpoint'].OutputValue" \
    --output text)
```

### 2. Start a new trip (agent will ask a question)

```bash
curl --no-buffer -s -X POST "$API_URL" \
    -H "Content-Type: application/json" \
    -d '{
        "destination": "Rome, Italy",
        "days": 4,
        "interests": "history, pasta, and architecture"
    }' | python3 -m json.tool
```

Response (JSON — the agent is asking a question):
```json
{
    "SessionId": "a1b2c3d4e5f6...",
    "Question": "What's your budget level — backpacker, mid-range, or luxury? And do you have any dietary restrictions I should consider for restaurant recommendations?",
    "Status": "awaiting_input"
}
```

### 3. Answer the question (agent may ask another or start planning)

```bash
SESSION_ID="<sessionId from above>"

curl --no-buffer -s -X POST "$API_URL" \
    -H "Content-Type: application/json" \
    -d "{
        \"sessionId\": \"$SESSION_ID\",
        \"message\": \"Mid-range budget. No dietary restrictions, but I love wine.\"
    }"
```

If the agent is satisfied, it streams the itinerary:
```
✈️  Trip Planner — Rome, Italy (4 days)
   Interests: history, pasta, and architecture
════════════════════════════════════════════════════════════════

📅 Day 1: Ancient Rome & Trastevere
   🌅 Morning: Start at the Colosseum...
   ☀️  Afternoon: Walk through the Roman Forum...
   🌙 Evening: Cross to Trastevere for dinner...
   💡 Tips: Book Colosseum tickets online...

📅 Day 2: Vatican & Wine Tasting
   ...
```

### 4. Skip questions (go straight to planning)

```bash
curl --no-buffer -s -X POST "$API_URL" \
    -H "Content-Type: application/json" \
    -d '{
        "destination": "Tokyo, Japan",
        "days": 3,
        "interests": "food, anime, and technology. Skip questions and just plan."
    }'
```

---

## How the Multi-Turn Pattern Works

```
Request 1 (new):
  Client → Lambda → Bedrock (calls ask_user tool)
  Lambda saves messages to DynamoDB, returns { sessionId, question }

Request 2 (continue):
  Client → Lambda (loads session from DynamoDB)
  Lambda appends user answer → Bedrock (calls add_day_plan tools)
  Lambda streams itinerary, deletes session
```

Key implementation details:

1. **`ask_user` tool** — When the model calls this, the agent loop returns `AgentAskedQuestion` with the question text and the tool use ID. The Lambda saves the conversation and returns JSON.

2. **Resuming** — On the next request, the Lambda loads the session, appends the user's answer as a `ToolResult` for the pending `ask_user` call, and resumes the agent loop.

3. **DynamoDB TTL** — Each session is stored with an `ExpiresAt` attribute set to 1 hour from creation. DynamoDB automatically deletes expired items, so abandoned conversations don't accumulate.

4. **Streaming only on final generation** — Questions are returned as buffered JSON (fast, small). The itinerary is streamed (large, progressive). The Lambda decides which response mode to use based on the agent's behavior.

---

## DynamoDB Session Schema

| Attribute | Type | Description |
|-----------|------|-------------|
| `SessionId` | String (PK) | Unique conversation identifier |
| `Messages` | String (JSON) | Serialized Bedrock message history |
| `Destination` | String | Trip destination |
| `Days` | Number | Trip duration |
| `Interests` | String | User interests |
| `PendingToolUseId` | String | ID of the ask_user tool call awaiting a response |
| `ExpiresAt` | Number (TTL) | Unix timestamp — DynamoDB auto-deletes after this time |

---

## Cleanup

```bash
sam delete
```

---

## References

- [Building responsive APIs with API Gateway response streaming](https://aws.amazon.com/blogs/compute/building-responsive-apis-with-amazon-api-gateway-response-streaming/)
- [Bedrock Converse API with tool use](https://docs.aws.amazon.com/bedrock/latest/userguide/tool-use.html)
- [DynamoDB Time to Live (TTL)](https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/TTL.html)
- [Lambda Response Streaming (.NET SDK PR)](https://github.com/aws/aws-lambda-dotnet/pull/2288)
- [AWS SAM Developer Guide](https://docs.aws.amazon.com/serverless-application-model/latest/developerguide/)
