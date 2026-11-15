using Amazon.S3;
using Amazon.S3.Model;
using Amazon.StepFunctions;
using Amazon.StepFunctions.Model;
using CallbackPatternSample.Models;
using Microsoft.AspNetCore.Mvc;
using Microsoft.Extensions.Options;
using System.Net;

namespace CallbackPatternSample.API.Controllers;

[Route("[controller]")]
[ApiController]
public class OrderRequestController : ControllerBase
{
    ILogger<OrderRequestController> logger;
    IAmazonS3 s3Client;
    IAmazonStepFunctions stepFunctionsClient;
    IOptions<OrderOptions> options;

    public OrderRequestController(ILogger<OrderRequestController> logger,
        IAmazonS3 s3Client,
        IAmazonStepFunctions stepFunctionsClient,
        IOptions<OrderOptions> options)
    {
        this.logger = logger;
        this.s3Client = s3Client;
        this.stepFunctionsClient = stepFunctionsClient;
        this.options = options;
    }
    
    [HttpPost("[action]/{OrderId}")]
    public async Task<IActionResult> OrderStatus(Guid OrderId)
    {
        await Task.Yield();
        return Ok();
    }

    [HttpPost("[action]")]
    public async Task<IActionResult> ProcessOrder([FromBody] Order order, CancellationToken cancellationToken)
    {
        // start the execution
        var startExecutionRequest = new StartExecutionRequest
        {
            Input = System.Text.Json.JsonSerializer.Serialize(order),
            StateMachineArn = options.Value.OrdersStateMachine,
            Name = order.OrderId.ToString() + Guid.NewGuid().ToString()
        };

        await stepFunctionsClient.StartExecutionAsync(startExecutionRequest, cancellationToken);
        return Ok("Order request received and processing started...");
    }

    [HttpPost("[action]")]
    public async Task<IActionResult> CompleteOrder([FromBody] Order order, CancellationToken cancellationToken)
    {
        string? token = await GetTaskToken(order.OrderId, cancellationToken);
        if (!string.IsNullOrEmpty(token))
        {
            if (order.IsConfirmed)
            {
                var response = await stepFunctionsClient.SendTaskSuccessAsync(new SendTaskSuccessRequest()
                {
                    Output = System.Text.Json.JsonSerializer.Serialize(order),
                    TaskToken = token
                }, cancellationToken);
                if (response.HttpStatusCode == HttpStatusCode.OK)
                    return Ok("Order Confirmed.");
            }
            else
            {
                var response = await stepFunctionsClient.SendTaskFailureAsync(new SendTaskFailureRequest()
                {
                    Cause = "Cancelled from client...",
                    TaskToken = token
                }, cancellationToken);
                if (response.HttpStatusCode == HttpStatusCode.OK)
                    return Ok("Order not confirmed..");
            }
        }

        return Problem("Order not confirmed, contact support.");
    }

    private async Task<string> GetTaskToken(Guid orderId, CancellationToken cancellationToken)
    {
        logger.LogInformation("Getting token for : " + orderId.ToString());
        string? token = null;
        GetObjectRequest request = new GetObjectRequest();
        request.BucketName = options.Value.TokenStoreBucket; //Environment.GetEnvironmentVariable("TokenStoreBucket");
        request.Key = orderId.ToString();
        var response = await s3Client.GetObjectAsync(request, cancellationToken);
        using (StreamReader reader = new StreamReader(response.ResponseStream))
        {
            token = await reader.ReadToEndAsync();
        }
        logger.LogInformation("Token received... ");
        return token;
    }
}