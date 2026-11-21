using System.Text;
using System.Text.Json;
using Amazon.Lambda;
using Amazon.Lambda.APIGatewayEvents;
using Amazon.Lambda.Core;
using Amazon.Lambda.Model;

namespace TravelBooking;

/// <summary>
/// Payment confirmation callback handler.
/// The payment gateway calls this endpoint after the user completes
/// OTP verification on the gateway's side. This resumes the suspended
/// durable function so booking can proceed.
///
/// Route: POST /bookings/payment-confirmation
/// Body:  { "CallbackId": "...", "Status": "Confirmed", "TransactionRef": "TXN-abc123" }
///
/// The callback token is passed in the request body (not as a URL path parameter)
/// because the token is a binary blob that contains characters like '/' and '+'
/// which break API Gateway path routing.
/// </summary>
public sealed class PaymentCallbackHandler
{
    private static readonly IAmazonLambda LambdaClient = new AmazonLambdaClient();

    private static readonly JsonSerializerOptions JsonOptions = new()
    {
        PropertyNameCaseInsensitive = true
    };

    public async Task<APIGatewayProxyResponse> Handler(
        APIGatewayProxyRequest request, ILambdaContext context)
    {
        if (string.IsNullOrWhiteSpace(request.Body))
        {
            return Response(400, new { message = "Request body is required." });
        }

        PaymentCallbackRequest? callbackRequest;
        try
        {
            callbackRequest = JsonSerializer.Deserialize<PaymentCallbackRequest>(request.Body, JsonOptions);
        }
        catch (JsonException ex)
        {
            return Response(400, new { message = $"Invalid JSON: {ex.Message}" });
        }

        if (callbackRequest is null || string.IsNullOrWhiteSpace(callbackRequest.CallbackId))
        {
            return Response(400, new { message = "CallbackId is required in the request body." });
        }

        var isConfirmed = string.Equals(callbackRequest.Status, "Confirmed",
            StringComparison.OrdinalIgnoreCase);

        if (isConfirmed)
        {
            // Resume the workflow with a successful result. The durable function
            // deserializes this payload as a PaymentConfirmation and continues.
            var confirmationPayload = JsonSerializer.Serialize(new PaymentConfirmation(
                callbackRequest.Status,
                callbackRequest.TransactionRef));

            await LambdaClient.SendDurableExecutionCallbackSuccessAsync(
                new SendDurableExecutionCallbackSuccessRequest
                {
                    CallbackId = callbackRequest.CallbackId,
                    Result = new MemoryStream(Encoding.UTF8.GetBytes(confirmationPayload))
                });

            context.Logger.LogInformation(
                $"Payment confirmed via callback (TransactionRef: {callbackRequest.TransactionRef})");

            return Response(200, new
            {
                message = "Payment confirmed. Booking will proceed.",
                transactionRef = callbackRequest.TransactionRef
            });
        }

        // Payment was declined by the gateway. Resume the workflow through its
        // failure path — inside the workflow this surfaces as a CallbackException,
        // which the booking handler catches and treats as "no funds held".
        await LambdaClient.SendDurableExecutionCallbackFailureAsync(
            new SendDurableExecutionCallbackFailureRequest
            {
                CallbackId = callbackRequest.CallbackId,
                Error = new ErrorObject
                {
                    ErrorType = "PaymentDeclined",
                    ErrorMessage = $"Payment gateway reported status '{callbackRequest.Status}'."
                }
            });

        context.Logger.LogInformation(
            $"Payment declined via callback (status: {callbackRequest.Status})");

        return Response(200, new
        {
            message = "Payment declined. Booking will be cancelled.",
            status = callbackRequest.Status
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
