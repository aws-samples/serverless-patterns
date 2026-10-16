# AWS Lambda Response Streaming with Bedrock Agent — AI Trip Planner (.NET)

This sample demonstrates an **AI agent** built with Amazon Bedrock (Claude Sonnet) **tool use** combined with **Lambda Response Streaming through API Gateway**. The agent uses a tool-calling loop to build a day-by-day trip itinerary, streaming each day's plan to the client as it's generated.

## Architecture

```
┌──────────────┐       ┌──────────────────┐       ┌────────────────────┐       ┌─────────────┐
│   Client     │       │   API Gateway    │       │   Lambda Function  │       │   Amazon    │
│  (curl)      │──GET─▶│   REST API       │──────▶│   (Agent Loop)     │◀─────▶│   Bedrock   │
│              │◀─stream│  ResponseTransfer │◀stream│                    │       │  (Claude)   │
│              │       │  Mode: STREAM    │       │  Day 1... Day 2... │       │             │
└──────────────┘       └──────────────────┘       └────────────────────┘       └─────────────┘
                                                          │
                                                    Tool Use Loop:
                                                    1. Model calls add_day_plan tool
                                                    2. Lambda formats & streams day to client
                                                    3. Lambda returns tool result to model
                                                    4. Repeat until all days planned
```

## What It Demonstrates

- **Agentic tool use** — The model calls an `add_day_plan` tool for each day, driving a structured multi-turn loop. The Lambda orchestrates the conversation and decides when the agent is done.
- **Streaming structured output** — Each day's itinerary is streamed to the client as soon as the model generates it, giving progressive feedback during a multi-step agent workflow.
- **API Gateway response streaming** — Uses `ResponseTransferMode: STREAM` so the client sees each day appear incrementally over the connection.
- **No external dependencies** — The agent relies only on Claude Sonnet's knowledge. No databases, APIs, or third-party services needed.
- **Practical AI pattern** — Represents a real-world agentic pattern where a model drives a structured workflow through tool calling.

## Project Structure

```
├── template.yaml              # SAM template (API Gateway + Lambda + Bedrock IAM)
├── events/
│   └── plan-trip.json         # Sample API Gateway proxy event
└── src/
    ├── Program.cs             # Agent loop: Bedrock tool use → stream formatted output
    └── TripPlannerStreaming.csproj
```

---

## Prerequisites

- [.NET 10 SDK](https://dotnet.microsoft.com/download/dotnet/10.0)
- [AWS SAM CLI](https://docs.aws.amazon.com/serverless-application-model/latest/developerguide/install-sam-cli.html)
- AWS account with credentials configured (`aws configure`)
- **Amazon Bedrock model access** — Enable access to Claude Sonnet in the [Bedrock console](https://console.aws.amazon.com/bedrock/home#/modelaccess)

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

### 1. Get the API endpoint

```bash
API_URL=$(aws cloudformation describe-stacks \
    --stack-name sam-dotnet-responsestreaming-bedrock-agent \
    --query "Stacks[0].Outputs[?OutputKey=='ApiEndpoint'].OutputValue" \
    --output text)
```

### 2. Plan a trip with defaults (Tokyo, 3 days)

```bash
curl --no-buffer "$API_URL"
```

You'll see each day's plan stream in progressively:

```
✈️  Trip Planner — Tokyo, Japan (3 days)
   Interests: culture, food, and nature
════════════════════════════════════════════════════════════════

📅 Day 1: Traditional Tokyo — Temples & Tsukiji
   🌅 Morning: Start at Senso-ji temple in Asakusa...
   ☀️  Afternoon: Explore the Tsukiji Outer Market...
   🌙 Evening: Head to Shinjuku for yakitori...
   💡 Tips: Get a Suica card at the airport...

📅 Day 2: Modern Tokyo — Shibuya & Harajuku
   ...

📅 Day 3: Nature & Serenity — Day Trip to Nikko
   ...

════════════════════════════════════════════════════════════════

Overall trip tips: ...

✅ Happy travels!
```

### 3. Custom trips

```bash
# Barcelona for 5 days, food & architecture
curl --no-buffer "$API_URL?destination=Barcelona,+Spain&days=5&interests=architecture,+tapas,+and+beach"

# Iceland adventure
curl --no-buffer "$API_URL?destination=Iceland&days=7&interests=northern+lights,+glaciers,+and+hot+springs"

# Quick weekend in Paris
curl --no-buffer "$API_URL?destination=Paris,+France&days=2&interests=art,+pastries,+and+wine"
```

### Parameters

| Parameter     | Default              | Range  | Description                            |
|---------------|----------------------|--------|----------------------------------------|
| `destination` | Tokyo, Japan         | —      | Where to travel                        |
| `days`        | 3                    | 1–14   | Number of days for the trip            |
| `interests`   | culture, food, and nature | — | Traveler's interests (comma-separated) |

---

## How the Agent Loop Works

```
┌─────────────────────────────────────────────────────────────┐
│                    Agent Loop (Lambda)                        │
│                                                              │
│  1. Send user request + tool definition to Bedrock           │
│  2. Model responds with add_day_plan tool call               │
│  3. Lambda formats the day plan and streams it to client     │
│  4. Lambda returns tool result ("Day N added") to model      │
│  5. Model calls tool again for next day (or ends turn)       │
│  6. Repeat until model provides final summary (no tool call) │
│                                                              │
└─────────────────────────────────────────────────────────────┘
```

```csharp
while (continueLoop)
{
    var response = await bedrockClient.ConverseAsync(converseRequest);

    // If model used the add_day_plan tool, format and stream it
    foreach (var toolUse in toolUseBlocks)
    {
        // Extract structured day plan from tool input
        var title = input.GetProperty("title").GetString();
        // ... format and write to response stream ...
        await writer.FlushAsync();  // Stream to client immediately

        // Return result so model continues to next day
        toolResults.Add(new ContentBlock { ToolResult = ... });
    }

    // If no tool use, model is done — stream the summary
    if (response.StopReason == StopReason.EndTurn)
        continueLoop = false;
}
```

Key points:
- **Tool use drives structure** — Instead of free-form text, the model outputs structured day plans via the `add_day_plan` tool, ensuring consistent formatting.
- **Progressive streaming** — Each day appears as soon as the model generates it. The client doesn't wait for the entire itinerary.
- **Multi-turn conversation** — The agent loop sends tool results back to the model, maintaining conversation context across turns.
- **Graceful termination** — When the model stops calling tools and provides text directly, the loop ends and streams the summary.

---

## Cleanup

```bash
sam delete
```

---

## Useful Commands

| Command | Description |
|---------|-------------|
| `sam build` | Build the Lambda function |
| `sam deploy --guided` | Deploy with interactive prompts |
| `sam deploy` | Deploy with saved config |
| `sam logs --tail` | Tail CloudWatch logs |
| `sam delete` | Tear down the stack |
| `dotnet build src/` | Build locally without SAM |

---

## References

- [Building responsive APIs with API Gateway response streaming](https://aws.amazon.com/blogs/compute/building-responsive-apis-with-amazon-api-gateway-response-streaming/)
- [Bedrock Converse API with tool use](https://docs.aws.amazon.com/bedrock/latest/userguide/tool-use.html)
- [Lambda Response Streaming (.NET SDK PR)](https://github.com/aws/aws-lambda-dotnet/pull/2288)
- [Claude Sonnet on Bedrock](https://docs.aws.amazon.com/bedrock/latest/userguide/model-card-anthropic-claude-sonnet-5.html)
- [AWS SAM Developer Guide](https://docs.aws.amazon.com/serverless-application-model/latest/developerguide/)
