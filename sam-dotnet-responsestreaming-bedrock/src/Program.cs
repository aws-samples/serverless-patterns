using System.Net;
using Amazon.BedrockRuntime;
using Amazon.BedrockRuntime.Model;
using Amazon.Lambda.APIGatewayEvents;
using Amazon.Lambda.Core;
using Amazon.Lambda.Core.ResponseStreaming;
using Amazon.Lambda.RuntimeSupport;
using Amazon.Lambda.Serialization.SystemTextJson;

#pragma warning disable CA2252 // Opt in to preview features (response streaming)

var bedrockClient = new AmazonBedrockRuntimeClient();

// The function handler that will be called for each Lambda event.
// Invokes Claude Sonnet via Bedrock ConverseStream and pipes the response
// through API Gateway response streaming to the client.
var handler = async (APIGatewayProxyRequest request, ILambdaContext context) =>
{
    // Parse optional query parameters for story customization
    var genre = "fantasy";
    var setting = "a mysterious ancient library";
    var theme = "the power of curiosity";

    if (request.QueryStringParameters is not null)
    {
        if (request.QueryStringParameters.TryGetValue("genre", out var g) && !string.IsNullOrWhiteSpace(g))
            genre = g;
        if (request.QueryStringParameters.TryGetValue("setting", out var s) && !string.IsNullOrWhiteSpace(s))
            setting = s;
        if (request.QueryStringParameters.TryGetValue("theme", out var t) && !string.IsNullOrWhiteSpace(t))
            theme = t;
    }

    // Build the prompt
    var prompt = $"""
        Write a short story (about 500-800 words) in the {genre} genre.
        Setting: {setting}
        Theme: {theme}
        
        Write in a vivid, engaging style. Start the story immediately without any preamble.
        """;

    // Set up the HTTP response stream
    var prelude = new HttpResponseStreamPrelude
    {
        StatusCode = HttpStatusCode.OK,
        Headers =
        {
            { "Content-Type", "text/plain; charset=utf-8" },
            { "Cache-Control", "no-cache" },
            { "X-Content-Type-Options", "nosniff" }
        }
    };

    using var responseStream = LambdaResponseStreamFactory.CreateHttpStream(prelude);
    using var writer = new StreamWriter(responseStream) { AutoFlush = false };

    // Call Bedrock ConverseStream with Claude Sonnet
    var converseRequest = new ConverseStreamRequest
    {
        ModelId = "us.anthropic.claude-sonnet-5",
        Messages =
        [
            new Message
            {
                Role = ConversationRole.User,
                Content = [new ContentBlock { Text = prompt }]
            }
        ],
        InferenceConfig = new InferenceConfiguration
        {
            MaxTokens = 2048
        }
    };

    try
    {
        var response = await bedrockClient.ConverseStreamAsync(converseRequest);

        // Stream each token as it arrives from Bedrock to the client
        foreach (var item in response.Stream.AsEnumerable())
        {
            if (item is ContentBlockDeltaEvent deltaEvent && deltaEvent.Delta?.Text is not null)
            {
                await writer.WriteAsync(deltaEvent.Delta.Text);
                await writer.FlushAsync();
            }
        }

        // End with a newline
        await writer.WriteLineAsync();
        await writer.FlushAsync();
    }
    catch (Exception ex)
    {
        context.Logger.LogError($"Error invoking Bedrock: {ex.Message}");
        await writer.WriteLineAsync($"\n\n[Error generating story: {ex.Message}]");
        await writer.FlushAsync();
    }
};

// Build and run the Lambda runtime
await LambdaBootstrapBuilder.Create(handler, new DefaultLambdaJsonSerializer())
    .Build()
    .RunAsync();
