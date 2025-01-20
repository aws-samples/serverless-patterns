using System.Text;
using System.Text.Json;
using System.Text.Json.Serialization;
using Amazon.BedrockAgentRuntime;
using Amazon.BedrockAgentRuntime.Model;
using Amazon.Runtime.EventStreams;
using Amazon.Runtime.EventStreams.Internal;
using BedrockAgentsApiProxy.BedrockAgent.Model;

namespace BedrockAgentsApiProxy.BedrockAgent;

/// <summary>
/// Class to process requests to the Bedrock Agent
/// </summary>
/// <typeparam name="BedrockAgentRequestProcessor"></typeparam>
internal sealed class BedrockAgentRequestProcessor(IConfiguration configuration, ILogger<BedrockAgentRequestProcessor> logger) : IDisposable
{
    private readonly AmazonBedrockAgentRuntimeClient _client = new();

    private readonly ILogger<BedrockAgentRequestProcessor> _logger = logger 
        ?? throw new ArgumentNullException(nameof(logger));

    private readonly string _agentId = configuration?.GetValue<string>("AGENT_ID") // Environment.GetEnvironmentVariable("AGENT_ID") 
        ?? throw new ArgumentNullException("AGENT_ID");
        
    private readonly string _agentAliasId = configuration?.GetValue<string>("AGENT_ALIAS_ID") //Environment.GetEnvironmentVariable("AGENT_ALIAS_ID") 
        ?? throw new ArgumentNullException("AGENT_ALIAS_ID");

    private static readonly JsonSerializerOptions _jsonSerializerOptions = 
        new()
        { 
            WriteIndented = true,
            ReferenceHandler = ReferenceHandler.IgnoreCycles
        };

    /// <summary>
    /// Sends a request to the Bedrock Agent
    /// </summary>
    /// <param name="request">Bedrock Agent Request (<see cref="BedrockAgentRequest"/></param>
    /// <param name="cancellationToken">Cancellation token</param>
    /// <returns><see cref="BedrockAgentResponse"/></returns>
    public async Task<BedrockAgentResponse> SendRequestToBedrockAgentAsync(
        BedrockAgentRequest request,
        CancellationToken cancellationToken)
    {
        try
        {
            logger.LogInformation("Sending request to BedrockAgent: {request}",
                JsonSerializer.Serialize(request, _jsonSerializerOptions));

            // Create a request object
            var invokeRequest = new InvokeAgentRequest
            {
                AgentId = _agentId,
                AgentAliasId = _agentAliasId,
                EnableTrace = request.EnableTrace,
                EndSession = request.EndSession,
                InputText = request.Message,
                MemoryId = request.MemoryId,
                SessionId = request.SessionId,
                SessionState = new SessionState
                {
                    Files = [],
                    InvocationId = "",
                    PromptSessionAttributes = request.PromptSessionAttributes,
                    SessionAttributes = request.SessionAttributes,
                    ReturnControlInvocationResults = request.ReturnControlInvocationResults,
                },
            };

            // Send the request to the BedrockAgent using the client
            var response = await _client.InvokeAgentAsync(invokeRequest, cancellationToken);

            // Check if the response is an error
            if (response.HttpStatusCode >= System.Net.HttpStatusCode.BadRequest)
                throw new AmazonBedrockAgentRuntimeException($"Error sending request to BedrockAgent: {response.HttpStatusCode}");
            
            // Process the response from the Bedrock Agent
            var bedrockAgentResponse = await ProcessBedrockInvokeAgentResponseAsync(response, cancellationToken);
            
            // Get rid of Metadata as System.Text.Json has problems serializing it
            bedrockAgentResponse.Trace?.OrchestrationTraces?.ForEach(
                orchestrationTrace => 
                    orchestrationTrace?.Observation?.KnowledgeBaseLookupOutput?.RetrievedReferences?.ForEach(rf => rf.Metadata = null));

            // Log
            logger.LogInformation("Received response from BedrockAgent: {response}", 
                JsonSerializer.Serialize(bedrockAgentResponse, _jsonSerializerOptions));

            return bedrockAgentResponse;
        }
        catch (AmazonBedrockAgentRuntimeException abrEx)
        {
            _logger.LogError(abrEx, "Error sending request to BedrockAgent: {error}.", abrEx.Message);
            return CreateErrorResponse(request.SessionId, request.MemoryId ?? string.Empty, abrEx.Message);
        }
        catch (Exception ex)
        {
            _logger.LogError(ex, "Error sending request to BedrockAgent: {error}.", ex.Message);
            return CreateErrorResponse(request.SessionId, request.MemoryId ?? string.Empty, ex.Message);         
        }
    }

    /// <summary>
    /// Process the response from the Bedrock Agent
    /// </summary>
    /// <param name="response">Response from Bedrock Agent(<see cref="InvokeAgentResponse"/></param>
    /// <param name="cancellationToken">Cancellation token</param>
    /// <returns><see cref="BedrockAgentResponse"/></returns>
    private static async Task<BedrockAgentResponse> ProcessBedrockInvokeAgentResponseAsync(
        InvokeAgentResponse response, 
        CancellationToken cancellationToken)
    {
        ArgumentNullException.ThrowIfNull(response, nameof(response));

        try
        {
            // Agent response
            var bedrockAgentResponse = new BedrockAgentResponse
            {
                SessionId = response.SessionId,
                MemoryId = response.MemoryId
            };

            // Chunk Received Event
            response.Completion.ChunkReceived += ChunkReceived;
            void ChunkReceived(object? sender, EventStreamEventReceivedArgs<PayloadPart> e)
            {
                var bytes = e.EventStreamEvent.Bytes.ToArray();
                bedrockAgentResponse.Message += Encoding.UTF8.GetString(bytes);
            }

            // Exception Received
            response.Completion.ExceptionReceived += ExceptionReceived;
            void ExceptionReceived(object? sender, EventStreamExceptionReceivedArgs<BedrockAgentRuntimeEventStreamException> e)
            {
                bedrockAgentResponse.Error = e.EventStreamException.Message;
            };

            // Files received
            response.Completion.FilesReceived += FilesReceived;
            void FilesReceived(object? sender, EventStreamEventReceivedArgs<FilePart> e)
            {
                bedrockAgentResponse.Files ??= [];

                bedrockAgentResponse.Files.AddRange(
                    e.EventStreamEvent.Files.Select(
                        file => new BedrockAgentOutputFile
                        {
                            Data = Encoding.UTF8.GetString(file.Bytes.ToArray()),
                            Name = file.Name,
                            Type = file.Type
                        }));
            };

            // Initial Response Received
            response.Completion.InitialResponseReceived += InitialResponseReceived;
            void InitialResponseReceived(object? sender, EventStreamEventReceivedArgs<InitialResponseEvent> e)
            {
                var bytes = e.EventStreamEvent.Payload.ToArray();
                bedrockAgentResponse.Message += Encoding.UTF8.GetString(bytes);
            };

            // Control Received
            response.Completion.ReturnControlReceived += ReturnControlReceived;
            void ReturnControlReceived(object? sender, EventStreamEventReceivedArgs<ReturnControlPayload> e)
            {
                bedrockAgentResponse.ReturnControlPayload = new ReturnControlPayload
                {
                    InvocationId = e.EventStreamEvent.InvocationId,
                    InvocationInputs = e.EventStreamEvent.InvocationInputs,
                };
            };

            // Trace Received
            response.Completion.TraceReceived += TraceReceived;
            void TraceReceived(object? sender, EventStreamEventReceivedArgs<TracePart> e)
            {
                bedrockAgentResponse.Trace ??= new BedrockAgentTrace();

                if (e.EventStreamEvent.Trace.FailureTrace != null)
                    bedrockAgentResponse.Trace.FailureTraces.Add(e.EventStreamEvent.Trace.FailureTrace);
                if (e.EventStreamEvent.Trace.GuardrailTrace != null)
                    bedrockAgentResponse.Trace.GuardrailTraces.Add(e.EventStreamEvent.Trace.GuardrailTrace);
                if (e.EventStreamEvent.Trace.OrchestrationTrace != null)
                    bedrockAgentResponse.Trace.OrchestrationTraces.Add(e.EventStreamEvent.Trace.OrchestrationTrace);
                if (e.EventStreamEvent.Trace.PostProcessingTrace != null)
                    bedrockAgentResponse.Trace.PostProcessingTraces.Add(e.EventStreamEvent.Trace.PostProcessingTrace);
                if (e.EventStreamEvent.Trace.PreProcessingTrace != null)
                    bedrockAgentResponse.Trace.PreProcessingTraces.Add(e.EventStreamEvent.Trace.PreProcessingTrace);
            };

            // Start processing the response
            await response.Completion.StartProcessingAsync();

            // Wait for the response to finish processing
            while (!cancellationToken.IsCancellationRequested)
            {
                // Hack - ResponseStream should expose IsProcessing
                try
                {
                    if (!response.Completion.Any())
                        break;
                }
                catch (Exception)
                {
                    try
                    {
                        await Task.Delay(100, cancellationToken);
                    }
                    catch (TaskCanceledException)
                    {
                        // Operation got cancelled
                        bedrockAgentResponse = CreateErrorResponse(response.SessionId, response.MemoryId, "Operation cancelled.");
                        break;
                    }
                }
            }

            // Unsubscribe from all events to prevent memory-leak
            response.Completion.ChunkReceived -= ChunkReceived;
            response.Completion.ExceptionReceived -= ExceptionReceived;
            response.Completion.FilesReceived -= FilesReceived;
            response.Completion.InitialResponseReceived -= InitialResponseReceived;
            response.Completion.ReturnControlReceived -= ReturnControlReceived;
            response.Completion.TraceReceived -= TraceReceived;            

            return bedrockAgentResponse;
        }
        catch (Exception ex)
        {
            return CreateErrorResponse(response.SessionId, response.MemoryId, ex.Message);
        }
        finally
        {
            response.Completion.Dispose();
        }
    }

    /// <summary>
    /// Creates an error response
    /// </summary>
    /// <param name="sessionId">SessionId</param>
    /// <param name="memoryId">MemoryId</param>
    /// <param name="error">Exception Error</param>
    /// <returns><see cref="BedrockAgentResponse"/></returns>
    private static BedrockAgentResponse CreateErrorResponse(string sessionId, string memoryId, string error)
    {
        return new BedrockAgentResponse
        {
            SessionId = sessionId,
            MemoryId = memoryId,
            Error = error
        };
    }

    /// <summary>
    /// <see cref="IDisposable.Dispose()"/>
    /// </summary>
    public void Dispose()
    {
        GC.SuppressFinalize(this);
        _client.Dispose();
    }
}