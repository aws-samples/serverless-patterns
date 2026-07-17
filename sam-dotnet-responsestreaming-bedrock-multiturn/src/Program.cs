using System.Net;
using System.Text.Json;
using Amazon.BedrockRuntime;
using Amazon.DynamoDBv2;
using Amazon.Lambda.APIGatewayEvents;
using Amazon.Lambda.Core;
using Amazon.Lambda.Core.ResponseStreaming;
using Amazon.Lambda.RuntimeSupport;
using Amazon.Lambda.Serialization.SystemTextJson;
using TripPlannerMultiturn;

#pragma warning disable CA2252 // Opt in to preview features (response streaming)

var bedrockClient = new AmazonBedrockRuntimeClient();
var dynamoDbClient = new AmazonDynamoDBClient();
var tableName = System.Environment.GetEnvironmentVariable("SESSION_TABLE_NAME")
    ?? throw new InvalidOperationException("SESSION_TABLE_NAME not set");

var sessionStore = new SessionStore(dynamoDbClient, tableName);
var agent = new TripPlannerAgent(bedrockClient);

var jsonOptions = new JsonSerializerOptions { PropertyNameCaseInsensitive = true };

var handler = async (APIGatewayProxyRequest request, ILambdaContext context) =>
{
    var body = !string.IsNullOrEmpty(request.Body)
        ? JsonSerializer.Deserialize<TripPlannerRequest>(request.Body, jsonOptions)
        : null;

    if (body is null)
    {
        await WriteJsonResponseAsync(400, new { message = "Request body is required." });
        return;
    }

    if (body.SessionId is not null)
        await HandleContinuationAsync(body, context);
    else
        await HandleNewConversationAsync(body, context);

    return;

    // ─── New conversation ───────────────────────────────────────────────────────

    async Task HandleNewConversationAsync(TripPlannerRequest req, ILambdaContext ctx)
    {
        var trip = new TripParameters(
            req.Destination ?? "Tokyo, Japan",
            Math.Clamp(req.Days ?? 3, 1, 14),
            req.Interests ?? "culture, food, and nature");

        var messages = TripPlannerAgent.CreateInitialMessages(trip);
        await RunAgentAndRespondAsync(null, trip, messages, ctx);
    }

    // ─── Continue an existing conversation ──────────────────────────────────────

    async Task HandleContinuationAsync(TripPlannerRequest req, ILambdaContext ctx)
    {
        var session = await sessionStore.LoadSessionAsync(req.SessionId!);
        if (session is null)
        {
            await WriteJsonResponseAsync(404, new { message = "Session not found or expired." });
            return;
        }

        TripPlannerAgent.AppendUserAnswer(session.Messages, session.PendingToolUseId!, req.Message ?? "");
        await RunAgentAndRespondAsync(req.SessionId, session.TripParams, session.Messages, ctx, expectsItinerary: true);
    }

    // ─── Run the agent once and respond based on outcome ────────────────────────

    async Task RunAgentAndRespondAsync(
        string? existingSessionId, TripParameters trip,
        List<Amazon.BedrockRuntime.Model.Message> messages, ILambdaContext ctx,
        bool expectsItinerary = false)
    {
        Stream? responseStream = null;
        StreamWriter? writer = null;
        ResponseFormatter? formatter = null;
        var streamStarted = false;

        // If we expect the itinerary, start streaming immediately to prevent
        // CloudFront's 30-second idle timeout from killing the connection.
        if (expectsItinerary)
        {
            (responseStream, writer, formatter) = CreateStreamingResponse(trip);
            await formatter.WriteHeaderAsync(trip);
            await writer.WriteLineAsync("⏳ Planning your trip...");
            await writer.FlushAsync();
            streamStarted = true;
        }

        try
        {
            // Keepalive: send a dot every 5 seconds while waiting for Bedrock,
            // to prevent CloudFront's 30-second idle timeout from killing the connection.
            using var keepaliveCts = new CancellationTokenSource();
            Task? keepaliveTask = null;
            var keepalivePrinted = false;

            if (streamStarted)
            {
                keepaliveTask = RunKeepaliveAsync(writer!, keepaliveCts.Token);
            }

            var result = await agent.RunAsync(
                trip, messages,
                onDayPlan: async day =>
                {
                    // Stop keepalive before writing content
                    if (keepaliveTask is not null && !keepaliveCts.IsCancellationRequested)
                    {
                        await keepaliveCts.CancelAsync();
                        await keepaliveTask;
                        keepalivePrinted = true;
                    }

                    if (!streamStarted)
                    {
                        (responseStream, writer, formatter) = CreateStreamingResponse(trip);
                        await formatter.WriteHeaderAsync(trip);
                        streamStarted = true;
                    }
                    else if (keepalivePrinted)
                    {
                        // End the dots line before first day plan
                        await writer!.WriteLineAsync();
                        await writer.WriteLineAsync();
                        keepalivePrinted = false;
                    }

                    await formatter!.WriteDayPlanAsync(day);
                },
                onSummary: async text =>
                {
                    if (formatter is not null)
                        await formatter.WriteSummaryAsync(text);
                });

            // Ensure keepalive is stopped
            if (!keepaliveCts.IsCancellationRequested)
                await keepaliveCts.CancelAsync();
            if (keepaliveTask is not null)
                await keepaliveTask;

            if (result is AgentAskedQuestion asked)
            {
                var sessionId = existingSessionId ?? Guid.NewGuid().ToString("N");
                await sessionStore.SaveSessionAsync(sessionId, asked.Messages, trip, asked.ToolUseId);
                ctx.Logger.LogInformation($"Session {sessionId}: agent asked question");

                if (streamStarted)
                {
                    // Already streaming — write the question as text
                    await writer!.WriteLineAsync();
                    await writer.WriteLineAsync($"❓ {asked.Question}");
                    await writer.WriteLineAsync();
                    await writer.WriteLineAsync($"Reply with: {{\"sessionId\": \"{sessionId}\", \"message\": \"your answer\"}}");
                    await writer.FlushAsync();
                }
                else
                {
                    await WriteJsonResponseAsync(200, new QuestionResponse(sessionId, asked.Question));
                }
            }
            else if (streamStarted)
            {
                if (existingSessionId is not null)
                    await sessionStore.DeleteSessionAsync(existingSessionId);
                await formatter!.WriteFooterAsync();
            }
        }
        catch (Exception ex)
        {
            ctx.Logger.LogError($"Error: {ex.Message}");
            if (formatter is not null)
                await formatter.WriteErrorAsync(ex.Message);
            else
                await WriteJsonResponseAsync(500, new { message = $"Error: {ex.Message}" });
        }
        finally
        {
            if (writer is not null) await writer.DisposeAsync();
            if (responseStream is not null) await responseStream.DisposeAsync();
        }
    }

    // ─── Helpers ────────────────────────────────────────────────────────────────

    (Stream responseStream, StreamWriter writer, ResponseFormatter formatter) CreateStreamingResponse(TripParameters trip)
    {
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
        var rs = LambdaResponseStreamFactory.CreateHttpStream(prelude);
        var w = new StreamWriter(rs) { AutoFlush = false };
        var f = new ResponseFormatter(w);
        return (rs, w, f);
    }

    async Task WriteJsonResponseAsync(int statusCode, object responseBody)
    {
        var prelude = new HttpResponseStreamPrelude
        {
            StatusCode = (HttpStatusCode)statusCode,
            Headers = { { "Content-Type", "application/json" } }
        };

        using var rs = LambdaResponseStreamFactory.CreateHttpStream(prelude);
        using var w = new StreamWriter(rs);
        await w.WriteAsync(JsonSerializer.Serialize(responseBody, jsonOptions));
        await w.FlushAsync();
    }

    async Task RunKeepaliveAsync(StreamWriter w, CancellationToken ct)
    {
        try
        {
            while (!ct.IsCancellationRequested)
            {
                await Task.Delay(TimeSpan.FromSeconds(5), ct);
                await w.WriteAsync(".");
                await w.FlushAsync();
            }
        }
        catch (OperationCanceledException) { }
    }
};

await LambdaBootstrapBuilder.Create(handler, new DefaultLambdaJsonSerializer())
    .Build()
    .RunAsync();
