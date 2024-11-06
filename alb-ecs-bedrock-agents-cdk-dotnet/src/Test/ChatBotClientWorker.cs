using Microsoft.Extensions.Hosting;
using Microsoft.Extensions.Logging;

namespace TestApp;

/// <summary>
/// Worker Class to run <see cref="ChatBotClient"/>
/// </summary>
/// <remarks>
/// Initializes a new instance of <see cref="ChatBotClientWorker"/>
/// </remarks>
/// <param name="chatBotClient">ChatBot client (<see cref="ChatBotClient"/>)</param>
/// <param name="logger">Logger</param>
internal class ChatBotClientWorker(
    ChatBotClient chatBotClient, 
    IHostApplicationLifetime hostApplicationLifetime,
    ILogger<ChatBotClientWorker> logger) 
    : IHostedService
{
    private readonly ChatBotClient _chatBotClient = chatBotClient ?? throw new ArgumentNullException(nameof(chatBotClient));
    private readonly IHostApplicationLifetime _hostApplicationLifetime = hostApplicationLifetime ?? throw new ArgumentNullException(nameof(hostApplicationLifetime));
    private readonly ILogger<ChatBotClientWorker> _logger = logger ?? throw new ArgumentNullException(nameof(logger));
    private CancellationTokenSource? _cancellationTokenSource;

    /// <summary>
    /// Triggered when the application host is ready to start the service, runs <see cref="ChatBotClient"/>
    /// </summary>
    /// <param name="cancellationToken">Indicates that the start process has been aborted.</param>
    /// <returns>A <see cref="Task"/> that represents the asynchronous Start operation.</returns>
    public Task StartAsync(CancellationToken cancellationToken)
    {
        _logger.LogInformation("Worker running at: {time}", DateTimeOffset.Now);
        
        _cancellationTokenSource = CancellationTokenSource.CreateLinkedTokenSource(cancellationToken);
        //return _chatBotClient.RunAsync(_cancellationTokenSource.Token);
        return RunAndMonitorChatBotClientAsync(_cancellationTokenSource.Token);
    }

    /// <summary>
    /// Triggered when the application host is performing a graceful shutdown, stops <see cref="ChatBotClient"/>
    /// </summary>
    /// <param name="cancellationToken">Indicates that the shutdown process should no longer be graceful.</param>
    /// <returns>A <see cref="Task"/> that represents the asynchronous Stop operation.</returns>
    public Task StopAsync(CancellationToken cancellationToken)
    {
        _logger.LogInformation("Worker stopping at: {time}", DateTimeOffset.Now);

        _cancellationTokenSource?.Cancel();
        return Task.CompletedTask;
    }

    /// <summary>
    /// Runs and monitors <see cref="ChatBotClient"/> asynchronously. Exits the application if the client exits.
    /// </summary>
    /// <param name="cancellationToken">Cancellation token</param>
    /// <returns>A <see cref="Task"/> that runs and monitors <see cref="ChatBotClient.RunAsync(CancellationToken)"/></returns>
    private async Task RunAndMonitorChatBotClientAsync(CancellationToken cancellationToken)
    {
        await _chatBotClient.RunAsync(cancellationToken);

        // Task has completed, exit the application
        if (!cancellationToken.IsCancellationRequested)
        {
            _logger.LogInformation("ChatBotClient has exited. Exiting the application...");
            _hostApplicationLifetime.StopApplication();
        }
    }
}