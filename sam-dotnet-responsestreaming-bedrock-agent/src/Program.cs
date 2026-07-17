using System.Net;
using Amazon.BedrockRuntime;
using Amazon.Lambda.APIGatewayEvents;
using Amazon.Lambda.Core;
using Amazon.Lambda.Core.ResponseStreaming;
using Amazon.Lambda.RuntimeSupport;
using Amazon.Lambda.Serialization.SystemTextJson;
using TripPlannerStreaming;

#pragma warning disable CA2252 // Opt in to preview features (response streaming)

var bedrockClient = new AmazonBedrockRuntimeClient();
var agent = new TripPlannerAgent(bedrockClient);

var handler = async (APIGatewayProxyRequest request, ILambdaContext context) =>
{
    var trip = RequestParser.Parse(request);

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
    var formatter = new ResponseFormatter(writer);

    await formatter.WriteHeaderAsync(trip);

    try
    {
        await agent.RunAsync(
            trip,
            onDayPlan: formatter.WriteDayPlanAsync,
            onSummary: formatter.WriteSummaryAsync);

        await formatter.WriteFooterAsync();
    }
    catch (Exception ex)
    {
        context.Logger.LogError($"Error invoking Bedrock: {ex.Message}");
        await formatter.WriteErrorAsync(ex.Message);
    }
};

await LambdaBootstrapBuilder.Create(handler, new DefaultLambdaJsonSerializer())
    .Build()
    .RunAsync();
