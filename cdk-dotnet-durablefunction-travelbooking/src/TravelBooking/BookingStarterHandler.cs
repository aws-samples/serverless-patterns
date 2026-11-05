using System.Text.Json;
using Amazon.Lambda;
using Amazon.Lambda.APIGatewayEvents;
using Amazon.Lambda.Core;
using Amazon.Lambda.Model;

namespace TravelBooking;

/// <summary>
/// Thin starter function that receives the API Gateway request,
/// validates the booking payload, invokes the durable booking
/// workflow asynchronously, and returns immediately to the client.
///
/// Route: POST /bookings
/// </summary>
public sealed class BookingStarterHandler
{
    private static readonly IAmazonLambda LambdaClient = new AmazonLambdaClient();

    private static readonly string BookingFunctionArn =
        System.Environment.GetEnvironmentVariable("BOOKING_FUNCTION_ARN")
        ?? throw new InvalidOperationException("BOOKING_FUNCTION_ARN environment variable is not set.");

    public async Task<APIGatewayProxyResponse> Handler(
        APIGatewayProxyRequest request, ILambdaContext context)
    {
        if (string.IsNullOrWhiteSpace(request.Body))
        {
            return Response(400, new { message = "Request body is required." });
        }

        FlightBookingRequest? bookingRequest;
        try
        {
            bookingRequest = JsonSerializer.Deserialize<FlightBookingRequest>(request.Body,
                new JsonSerializerOptions { PropertyNameCaseInsensitive = true });
        }
        catch (JsonException ex)
        {
            return Response(400, new { message = $"Invalid JSON: {ex.Message}" });
        }

        if (bookingRequest is null || string.IsNullOrWhiteSpace(bookingRequest.BookingId))
        {
            return Response(400, new { message = "BookingId is required." });
        }

        context.Logger.LogInformation($"Starting booking workflow for {bookingRequest.BookingId}");

        await LambdaClient.InvokeAsync(new InvokeRequest
        {
            FunctionName = BookingFunctionArn,
            InvocationType = InvocationType.Event,
            Payload = request.Body
        });

        context.Logger.LogInformation($"Durable execution started for booking {bookingRequest.BookingId}");

        return Response(202, new
        {
            message = "Booking workflow started. The workflow is now waiting for payment confirmation.",
            bookingId = bookingRequest.BookingId
        });
    }

    private static APIGatewayProxyResponse Response(int statusCode, object body) =>
        new()
        {
            StatusCode = statusCode,
            Body = JsonSerializer.Serialize(body),
            Headers = new Dictionary<string, string> { ["Content-Type"] = "application/json" }
        };
}
