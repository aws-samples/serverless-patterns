using System.Net.Http.Headers;
using System.Net.Http.Json;
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

        // Response from BedrockAgent
        BedrockAgentResponse? response = null;

        while (!cancellationToken.IsCancellationRequested)
        {
            Console.WriteLine("Please enter your input: ");
            var input = Console.ReadLine();
            if (string.IsNullOrEmpty(input))
                continue;

            if (input.Equals("exit", StringComparison.InvariantCultureIgnoreCase))
            {
                break;
            }

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

                    if (!responseMessage.IsSuccessStatusCode)
                    {
                        _logger.LogError("Error sending request to BedrockAgent: {responsePhrase}", responseMessage.ReasonPhrase);
                        continue;
                    }

                    // Content
                    var content = await responseMessage.Content.ReadFromJsonAsync<BedrockAgentResponse>(cancellationToken);

                    // Error
                    if (content?.HasError ?? false)
                        _logger.LogWarning("Error received from BedrockAgent: {error}", content?.Error);
                    // Message
                    else
                    {
                        Console.WriteLine($"Response: {content?.Message}");
                        _logger.LogTrace("Trace: {trace}", content?.Trace);
                    }

                    break;
                }
                catch (Exception ex)
                {
                    _logger.LogError("Error sending request to BedrockAgent: {error}", ex.Message);

                    Console.WriteLine("Do you want to retry the operation (y/N): ");
                    var retry = Console.ReadLine();

                    if (string.IsNullOrEmpty(retry) || !retry.Equals("y", StringComparison.InvariantCultureIgnoreCase))
                        break;
                }
            }
        }
    }

    /// <summary>
    /// <see cref="IDisposable.Dispose"/>
    /// </summary>
    public void Dispose()
    {
        httpClient.Dispose();
    }
}