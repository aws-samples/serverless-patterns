# AWS Lambda Response Streaming with Amazon Bedrock — Story Generator (.NET)

This sample demonstrates **Lambda Response Streaming through Amazon API Gateway** combined with **Amazon Bedrock** (Claude Sonnet) for .NET. A Lambda function invokes Claude Sonnet via the Bedrock `ConverseStream` API and streams the generated story token-by-token back to the client through API Gateway response streaming.

## Architecture

```
┌──────────────┐       ┌──────────────────┐       ┌────────────────────┐       ┌─────────────┐
│   Client     │       │   API Gateway    │       │   Lambda Function  │       │   Amazon    │
│  (curl)      │──GET─▶│   REST API       │──────▶│   (Response        │──────▶│   Bedrock   │
│              │◀─stream│  ResponseTransfer │◀stream│    Streaming)      │◀stream│  (Claude)   │
│              │       │  Mode: STREAM    │       │                    │       │             │
└──────────────┘       └──────────────────┘       └────────────────────┘       └─────────────┘
```

## What It Demonstrates

- **End-to-end streaming** — Bedrock streams tokens → Lambda pipes them through → API Gateway streams to client. The user sees the story appear word-by-word.
- **API Gateway response streaming** — Uses `ResponseTransferMode: STREAM` with the `/response-streaming-invocations` Lambda endpoint.
- **Bedrock ConverseStream API** — Uses the AWS SDK's `ConverseStreamAsync` to get streaming responses from Claude Sonnet.
- **Customizable story generation** — Users can specify genre, setting, and theme via query parameters.
- **Minimal latency** — First tokens appear within seconds, no waiting for the full generation to complete.

## Project Structure

```
├── template.yaml              # SAM template (API Gateway REST API + Lambda + Bedrock IAM)
├── events/
│   └── generate-story.json    # Sample API Gateway proxy event
└── src/
    ├── Program.cs             # Streaming handler (Bedrock → Lambda → API Gateway → Client)
    └── StoryStreaming.csproj
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
    --stack-name sam-dotnet-responsestreaming-bedrock \
    --query "Stacks[0].Outputs[?OutputKey=='ApiEndpoint'].OutputValue" \
    --output text)
```

### 2. Generate a story with defaults

```bash
curl --no-buffer "$API_URL"
```

You'll see the story appear word-by-word in real-time as Claude generates it.

### 3. Customize the story

```bash
# Science fiction story
curl --no-buffer "$API_URL?genre=science+fiction&setting=a+space+station+orbiting+Jupiter&theme=finding+home"

# Mystery story
curl --no-buffer "$API_URL?genre=mystery&setting=a+foggy+Victorian+London+street&theme=trust+and+betrayal"

# Horror story
curl --no-buffer "$API_URL?genre=horror&setting=an+abandoned+hospital&theme=facing+your+fears"
```

### Parameters

| Parameter | Default | Description |
|-----------|---------|-------------|
| `genre`   | fantasy | The genre of the story (e.g., science fiction, mystery, horror, romance) |
| `setting` | a mysterious ancient library | Where the story takes place |
| `theme`   | the power of curiosity | The central theme or message |

---

## How It Works

### API Gateway → Lambda (Response Streaming)

The API Gateway integration uses `/response-streaming-invocations` to invoke Lambda with streaming:

```yaml
Integration:
  Type: AWS_PROXY
  IntegrationHttpMethod: POST
  ResponseTransferMode: STREAM
  Uri: !Sub arn:aws:apigateway:${AWS::Region}:lambda:path/2021-11-15/functions/${StoryFunction.Arn}/response-streaming-invocations
```

### Lambda → Bedrock (ConverseStream)

The Lambda function calls Bedrock's streaming API and pipes each token to the response stream:

```csharp
// Set up Lambda response streaming
using var responseStream = LambdaResponseStreamFactory.CreateHttpStream(prelude);
using var writer = new StreamWriter(responseStream);

// Call Bedrock with streaming
var response = await bedrockClient.ConverseStreamAsync(converseRequest);

// Pipe each token from Bedrock → API Gateway → Client
foreach (var item in response.Stream.AsEnumerable())
{
    if (item is ContentBlockDeltaEvent deltaEvent && deltaEvent.Delta?.Text is not null)
    {
        await writer.WriteAsync(deltaEvent.Delta.Text);
        await writer.FlushAsync();  // Sends immediately to the client
    }
}
```

Key points:
- `ConverseStreamAsync` returns an event stream that yields `ContentBlockDeltaEvent` items as Claude generates tokens.
- Each `FlushAsync()` pushes the token(s) through API Gateway to the client immediately.
- The model used is `us.anthropic.claude-sonnet-5` (cross-region inference profile for higher availability).
- `Temperature: 0.8` and `TopP: 0.9` produce creative, varied stories.

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
- [Serverless strategies for streaming LLM responses](https://aws.amazon.com/blogs/compute/serverless-strategies-for-streaming-llm-responses/)
- [Lambda Response Streaming (.NET SDK PR)](https://github.com/aws/aws-lambda-dotnet/pull/2288)
- [Amazon Bedrock ConverseStream API](https://docs.aws.amazon.com/bedrock/latest/APIReference/API_runtime_ConverseStream.html)
- [Claude Sonnet on Bedrock](https://docs.aws.amazon.com/bedrock/latest/userguide/model-card-anthropic-claude-sonnet-5.html)
- [AWS SAM Developer Guide](https://docs.aws.amazon.com/serverless-application-model/latest/developerguide/)
