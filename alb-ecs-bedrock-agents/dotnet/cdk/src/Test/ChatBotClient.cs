using System.Net.Http.Headers;
using System.Net.Http.Json;
using System.Text.Json;
using System.Text.Json.Serialization;
using Microsoft.Extensions.Configuration;
using Microsoft.Extensions.Logging;
using TestApp.Model;

namespace TestApp;

/// <summary>
/// ChatBot Client
/// </summary>
internal sealed class ChatBotClient : IDisposable
{
    private readonly IConfiguration _configuration;
    private readonly ILogger<ChatBotClient> _logger;
    private readonly HttpClient httpClient;
    private readonly bool _enableTrace;
    private readonly string _albMessageEndpointUrl;
    private static readonly JsonSerializerOptions _jsonSerializerOptions = 
        new()
        { 
            WriteIndented = true,
            ReferenceHandler = ReferenceHandler.IgnoreCycles,
            PropertyNameCaseInsensitive = true
        };
        
    /// <summary>
    /// Initializes a new instance of <see cref="ChatBotClient"/>
    /// </summary>
    /// <param name="configuration">Configuration</param>
    /// <param name="logger">Logger</param>
    public ChatBotClient(IConfiguration configuration, ILogger<ChatBotClient> logger)
    {
        _configuration = configuration ?? throw new ArgumentNullException(nameof(configuration));
        _logger = logger ?? throw new ArgumentNullException(nameof(logger));

        httpClient = new();
        
        // ALB Name
        var albDnsName = _configuration["ALB_DNS_NAME"] ?? string.Empty;
        if (string.IsNullOrEmpty(albDnsName))
            throw new Exception("ALB_DNS_NAME is required. Please set it in appsettings.json file.");

        // Port
        var portStr = _configuration["PORT"];
        if (portStr == null || !int.TryParse(portStr, out var port))
            port = 80;

        // ALB URL;
        _albMessageEndpointUrl = $"http://{albDnsName}:{port}/message";

        // Enable Trace
        var enableTraceStr = _configuration["enableTrace"];
        if (enableTraceStr == null || !bool.TryParse(enableTraceStr, out _enableTrace))
            throw new Exception("A valid value (True/False) must be defined for 'enableTrace' in appsettings.json file.");
    }

    /// <summary>
    /// Runs ChatBotClient asynchronously
    /// </summary>
    /// <param name="cancellationToken">Cancellation token</param>
    public async Task RunAsync(CancellationToken cancellationToken)
    {
        // Ids
        var sessionId = Guid.NewGuid().ToString();

        // Iteration
        var iteration = 0;

        // Response from BedrockAgent
        BedrockAgentResponse? response = null;

        while (!cancellationToken.IsCancellationRequested)
        {   
            iteration++;
            string? input = null;
            Console.WriteLine("Please enter your input: ");
            try
            {
                input = await ReadLineAsync(cancellationToken);
            }
            catch(OperationCanceledException)
            {
                break; //break from main loop
            }

            // No input
            if (string.IsNullOrEmpty(input))
                continue;

            // Exit
            if (input.Equals("exit", StringComparison.InvariantCultureIgnoreCase))
                break; //break from main loop

            // Try in loop for retry
            while (!cancellationToken.IsCancellationRequested)
            {
                try
                {
                    httpClient.DefaultRequestHeaders.Accept.Add(new MediaTypeWithQualityHeaderValue("application/json"));
                    httpClient.DefaultRequestHeaders.Add("User-Agent", "BedrockAgentClient");

                    var responseMessage = await httpClient.PostAsJsonAsync(
                        _albMessageEndpointUrl,
                        new BedrockAgentRequest
                        {
                            Message = input,
                            SessionId = response?.SessionId ?? sessionId,
                            MemoryId = response?.MemoryId,
                            EndSession = false,
                            EnableTrace = _enableTrace,
                            SessionAttributes = [],
                            PromptSessionAttributes = [],
                            InvocationId = response?.ReturnControlPayload?.InvocationId,
                            ReturnControlInvocationResults = null, // can be updated based on previous response
                        },
                        cancellationToken: cancellationToken);

                    // Success
                    responseMessage.EnsureSuccessStatusCode();

                    // Response
                    response = await responseMessage.Content.ReadFromJsonAsync<BedrockAgentResponse>(_jsonSerializerOptions, cancellationToken);

                    // Error
                    if (response?.HasError ?? false)
                        _logger.LogWarning("Error received from BedrockAgent: {error}", response?.Error);
                    // Message
                    else
                    {
                        Console.WriteLine($"Response: {response?.Message}");

                        // Write Trace
                        if (_enableTrace)
                            await WriteTraceAsync(iteration, sessionId, input, response?.Message, response?.Trace);
                    }

                    break; //break from retry loop
                }
                catch (Exception ex)
                {
                    _logger.LogError("Error sending request to BedrockAgent: {error}", ex.Message);

                    ConsoleKey responseKey;
                    do
                    {
                        Console.WriteLine("Do you want to retry the operation (y/N): ");
                        responseKey = Console.ReadKey(false).Key;
                        if (responseKey != ConsoleKey.Enter)
                            Console.WriteLine();
                    } while (responseKey != ConsoleKey.Y && responseKey != ConsoleKey.N);

                    if (responseKey == ConsoleKey.N)
                        break; //break from retry loop
                }
            }
        }
    }

    /// <summary>
    /// Reads a line from console asynchronously
    /// </summary>
    /// <param name="cancellationToken">Cancellation token</param>
    /// <returns>String from console</returns>
    private static async Task<string?> ReadLineAsync(CancellationToken cancellationToken = default)
    {
        var readTask = Task.Run(Console.ReadLine);
        await Task.WhenAny(readTask, Task.Delay(-1, cancellationToken));

        cancellationToken.ThrowIfCancellationRequested();

        string? result = readTask.Result;
        return result;
    }

    /// <summary>
    /// Writes trace to file asynchronously
    /// </summary>
    /// <param name="iteration">Iteration count</param>
    /// <param name="sessionId">Session Id</param>
    /// <param name="input">user input</param>
    /// <param name="output">Agent output</param>
    /// <param name="trace">Trace</param>
    /// <returns>A <see cref="Task"/></returns>
    private static async Task WriteTraceAsync(
        int iteration, 
        string sessionId, 
        string input,
        string? output,
        BedrockAgentTrace? trace)
    {
        if (trace == null)
            return;

        var fileName = $"trace_{sessionId}_{iteration}.json";
        await File.WriteAllTextAsync(
            fileName, 
            JsonSerializer.Serialize(
                new
                {
                    Input = input,
                    Output = output,
                    Trace = trace
                },
                _jsonSerializerOptions));
    }

    /// <summary>
    /// <see cref="IDisposable.Dispose"/>
    /// </summary>
    public void Dispose()
    {
        httpClient.Dispose();
    }
}