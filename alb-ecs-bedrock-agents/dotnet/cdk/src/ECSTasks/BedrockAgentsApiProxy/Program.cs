using Serilog;
using BedrockAgentsApiProxy.BedrockAgent.Model;
using BedrockAgentsApiProxy.BedrockAgent;
using System.Diagnostics;
using System.Reflection;
using System.Text.Json.Serialization;
using Microsoft.AspNetCore.Mvc;

// Unset following and set proper AGENT_ID and AGENT_ALIAS_ID to test this proxy from
// local machine against actual agent
// This will be set automatically as a part of deployment on ECS Task
//
// Environment.SetEnvironmentVariable("AGENT_ID", "");
// Environment.SetEnvironmentVariable("AGENT_ALIAS_ID", "");

// Create the web application
var app = CreateWebApplication(args);

// Configure the endpoints
ConfigurEndpoints(app);

// Run the app
var port = app.Environment.IsDevelopment() ? 5176 : 8080;
await app.RunAsync($"http://0.0.0.0:{port}");

/// <summary>
/// Create the web application
/// </summary>
/// <param name="args">Command-line arguments</param>
/// <returns><see cref="WebApplication"/></returns>
static WebApplication CreateWebApplication(string[] args)
{
    // Create the builder and configure the app
    var builder = WebApplication.CreateBuilder(args);

    // Configuration
    builder.Configuration.AddEnvironmentVariables();
    builder.Configuration.AddJsonFile("appsettings.json", optional: false, reloadOnChange: true);

    // Add services to the container.
    builder.Services.AddEndpointsApiExplorer();
    builder.Services.AddSwaggerGen();
    builder.Services.AddSingleton<BedrockAgentRequestProcessor>();
    builder.Services.ConfigureHttpJsonOptions(
        options =>
        {
            options.SerializerOptions.ReferenceHandler = ReferenceHandler.IgnoreCycles;
        });
    builder.Services.Configure<JsonOptions>(
        option =>
        {
            option.JsonSerializerOptions.ReferenceHandler = ReferenceHandler.IgnoreCycles;
        });

    // configure logging
    builder.Logging.AddConfiguration(builder.Configuration.GetSection("Logging"));

    // Enable for detailed HTTP request/response logging
    // builder.Services.AddHttpLogging(logging => { });

    // Configure Serilog
    // Log to console, AWS Logs configuration in TaskDefinition will pipe the logs to CloudWatch
    var loggerConfiguration = new LoggerConfiguration()
        .Enrich.FromLogContext()
        .WriteTo.Console();

    // Serilog Default logger
    Log.Logger = loggerConfiguration.CreateLogger();

    // Add Serilog to the builder
    builder.Logging.AddSerilog(Log.Logger, dispose: true);

    // Build the app
    var app = builder.Build();

    // Enable for detailed HTTP request/response logging
    // app.UseHttpLogging();

    // Configure the HTTP request pipeline.
    if (app.Environment.IsDevelopment())
    {
        app.UseSwagger();
        app.UseSwaggerUI();
    }

    // Uncomment if using HTTPS
    // app.UseHttpsRedirection();    

    return app;
}

/// <summary>
/// Configure the endpoints
/// </summary>
/// <param name="app"><see cref="WebApplication"/></param>
static void ConfigurEndpoints(WebApplication app)
{
    // Add the endpoints to the app to handle requests
    app.MapPost("/message", async (BedrockAgentRequest request, CancellationToken cancellationToken) =>
    {
        try
        {
            var processor = app.Services.GetService<BedrockAgentRequestProcessor>();
            if (processor == null)
            {
                app.Logger.LogError("BedrockAgentRequestProcessor not found in the service container.");
                throw new InvalidOperationException("BedrockAgentRequestProcessor not found in the service container.");
            }

            var response = await processor.SendRequestToBedrockAgentAsync(request, cancellationToken);
            return Results.Ok(response);
        }
        catch (OperationCanceledException oex)
        {
            app.Logger.LogWarning(oex, "The request was canceled.");
            return Results.StatusCode(StatusCodes.Status499ClientClosedRequest);
        }
        catch (Exception ex)
        {
            app.Logger.LogError(ex, "An error occurred while processing the request.");
            return Results.StatusCode(StatusCodes.Status500InternalServerError);
        }
    })
    .WithName("PostMessage")
    .WithOpenApi();

    // Add Health Endpoint
    app.MapGet("/health", () => 
    {
        var healthStatus = new
        {
            Status = "Healthy",
            UpTime = (DateTime.UtcNow - Process.GetCurrentProcess().StartTime.ToUniversalTime()).ToString("c"),
            Version = FileVersionInfo.GetVersionInfo(Assembly.GetExecutingAssembly().Location).FileVersion
        };

        return Results.Ok(healthStatus);
    })
    .WithName("Health")
    .WithOpenApi();    
}