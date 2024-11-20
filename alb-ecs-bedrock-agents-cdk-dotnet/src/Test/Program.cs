using Microsoft.Extensions.Configuration;
using Microsoft.Extensions.DependencyInjection;
using Microsoft.Extensions.Hosting;
using Microsoft.Extensions.Logging;
using TestApp;

// Create the builder
var builder = Host.CreateDefaultBuilder(args);

// Configuration
builder.ConfigureHostConfiguration(host =>
{
    host.AddEnvironmentVariables();
    host.AddJsonFile("appsettings.json", optional: false, reloadOnChange: true);
});

// Logging
builder.ConfigureLogging((context, logging) =>
{
    logging.AddConfiguration(context.Configuration.GetSection("Logging"));    
    logging.AddConsole();
});

// Services
builder.ConfigureServices(services =>
{
    services.AddHostedService<ChatBotClientWorker>();
    services.AddSingleton<ChatBotClient>();
});

// Host
var host = builder.Build();

// Cancellation Token
using var cts = new CancellationTokenSource();

// Listen for CTRL+C
Console.CancelKeyPress += (sender, eventArgs) =>
{
    eventArgs.Cancel = true;
    cts.Cancel();
};

// Logger
var logger = host.Services.GetRequiredService<ILoggerFactory>().CreateLogger("main");

// Run
try
{
    await host.RunAsync(cts.Token);
}
catch (OperationCanceledException)
{
    logger.LogInformation("Application is shutting down...");
}