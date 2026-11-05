using Amazon.DynamoDBv2;
using Amazon.DynamoDBv2.Model;
using Amazon.Lambda.Core;
using Amazon.Lambda.DurableExecution;
using Amazon.Lambda.RuntimeSupport;
using Amazon.Lambda.Serialization.SystemTextJson;

[assembly: LambdaSerializer(typeof(DefaultLambdaJsonSerializer))]

namespace TravelBooking;

/// <summary>
/// Lambda Durable Function implementing a flight booking workflow with
/// payment confirmation callback, and saga compensation.
///
/// Workflow:
///   1. Check flight availability and fare
///   2. Wait for payment confirmation (callback — Lambda suspends)
///      Payment gateway handles OTP with user, then calls us back.
///   3. Authorize payment (hold funds after confirmation)
///   4. Book flight with airline
///   4b. SAGA COMPENSATION: if booking fails → reverse payment (checkpointed)
///   5. Wait for airline to confirm reservation (durable timer)
///   6. Capture payment (settle the hold)
///   7. Send confirmation email
///   8. Persist final result
/// </summary>
internal sealed class FlightBookingHandler
{
    private static readonly IAmazonDynamoDB DynamoDbClient = new AmazonDynamoDBClient();

    private static readonly string TableName =
        Environment.GetEnvironmentVariable("BOOKINGS_TABLE_NAME")
        ?? throw new InvalidOperationException("BOOKINGS_TABLE_NAME environment variable is not set.");

    public static async Task Main()
    {
        var handler = new FlightBookingHandler();
        var serializer = new DefaultLambdaJsonSerializer();
        using var wrapper = HandlerWrapper.GetHandlerWrapper<DurableExecutionInvocationInput, DurableExecutionInvocationOutput>(
            handler.Handler, serializer);
        using var bootstrap = new LambdaBootstrap(wrapper);
        await bootstrap.RunAsync();
    }

    public Task<DurableExecutionInvocationOutput> Handler(
        DurableExecutionInvocationInput input, ILambdaContext context)
        => DurableFunction.WrapAsync<FlightBookingRequest, FlightBookingResult>(Workflow, input, context);

    private async Task<FlightBookingResult> Workflow(FlightBookingRequest request, IDurableContext ctx)
    {
        var actions = new List<string>();

        // ══════════════════════════════════════════════════════════════════
        // Phase 1: Check availability and current fare
        // Fail fast before taking any payment if no seats exist.
        // ══════════════════════════════════════════════════════════════════
        var availability = await ctx.StepAsync(
            async (_, ct) => await AvailabilityService.CheckFlightAsync(request.Flight, ct),
            name: "check-availability");

        if (!availability.IsAvailable)
        {
            return new FlightBookingResult(
                request.BookingId, "Unavailable", null, 0,
                availability.UnavailableReason, actions);
        }

        actions.Add($"Flight available at ${availability.FarePrice}");

        // ══════════════════════════════════════════════════════════════════
        // Phase 2: Initiate payment — send request to payment gateway
        // The callback ID is sent to the payment gateway along with the
        // charge amount. The gateway handles OTP with the user directly.
        // Once verified, the gateway calls POST /bookings/payment-confirmation
        // to resume this workflow. Lambda suspends (zero cost) until then.
        // ══════════════════════════════════════════════════════════════════
        var otpCallback = await ctx.CreateCallbackAsync<PaymentConfirmation>(
            name: "await-payment-confirmation",
            config: new CallbackConfig { Timeout = TimeSpan.FromMinutes(10) });

        // Store the callback ID so testers can retrieve it.
        // In production this would be sent to the payment gateway instead.
        await ctx.StepAsync(
            async (_, ct) => await SaveCallbackIdAsync(request.BookingId, otpCallback.CallbackId, ct),
            name: "store-payment-callback-id");

        actions.Add($"Payment callback created: {otpCallback.CallbackId}");

        // The callback resumes here. GetResultAsync throws a CallbackException if the
        // payment gateway reported a failure (declined) or if the 10-minute timeout
        // elapsed. Either way, no funds were held, so we fail the booking cleanly.
        PaymentConfirmation? paymentConfirmation;
        try
        {
            paymentConfirmation = await otpCallback.GetResultAsync();
            actions.Add($"Payment confirmed: {paymentConfirmation.TransactionRef}");
        }
        catch (CallbackException ex)
        {
            // Distinguish an explicit decline (failure callback sent by the gateway)
            // from no response at all (the 10-minute callback timeout elapsed).
            var declined = string.Equals(ex.ErrorType, "PaymentDeclined",
                StringComparison.OrdinalIgnoreCase);

            var reason = declined
                ? "Payment was declined by the gateway. No funds were held."
                : "Payment confirmation timed out after 10 minutes. No funds were held.";

            var action = declined ? "Payment declined" : "Payment confirmation timed out";

            var failedResult = new FlightBookingResult(
                request.BookingId, "Failed", null, 0, reason, [..actions, action]);

            // Persist the terminal result so it can be queried like any other outcome.
            await ctx.StepAsync(
                async (_, ct) => await SaveResultAsync(request.BookingId, failedResult, ct),
                name: "save-unconfirmed-result");

            return failedResult;
        }

        // ══════════════════════════════════════════════════════════════════
        // Phase 3: Authorize payment (hold funds after OTP confirmed)
        // Now that the user verified their identity, place the hold.
        // ══════════════════════════════════════════════════════════════════
        var paymentAuth = await ctx.StepAsync(
            async (_, ct) => await PaymentService.AuthorizeAsync(
                request.Payment, availability.FarePrice, ct),
            name: "authorize-payment",
            config: new StepConfig { RetryStrategy = RetryStrategy.Default });

        actions.Add($"Payment authorized: {paymentAuth.AuthorizationId}");

        // ══════════════════════════════════════════════════════════════════
        // Phase 4: Book the flight with the airline
        // ══════════════════════════════════════════════════════════════════
        var flightConfirmation = await ctx.StepAsync(
            async (_, ct) => await FlightService.BookAsync(request.Flight, request.BookingId, ct),
            name: "book-flight",
            config: new StepConfig { RetryStrategy = RetryStrategy.Default });

        // ══════════════════════════════════════════════════════════════════
        // Phase 4b (Saga Compensation): If booking failed, reverse payment.
        // Each compensation is a checkpointed step — if Lambda is
        // interrupted during compensation, it resumes without re-executing.
        // ══════════════════════════════════════════════════════════════════
        if (flightConfirmation.Status == "Failed")
        {
            await ctx.StepAsync(
                async (_, ct) => await PaymentService.ReverseAsync(paymentAuth.AuthorizationId, ct),
                name: "compensate-reverse-payment");

            actions.Add($"Saga compensation: reversed payment {paymentAuth.AuthorizationId}");

            await ctx.StepAsync(
                async (_, ct) => await SaveResultAsync(request.BookingId,
                    new FlightBookingResult(request.BookingId, "Failed", null, 0,
                        "Airline rejected the booking.", actions), ct),
                name: "save-compensated-result");

            return new FlightBookingResult(
                request.BookingId, "Failed", null, 0,
                "Airline rejected the booking.", actions);
        }

        actions.Add($"Flight booked: {flightConfirmation.ConfirmationId}");

        // ══════════════════════════════════════════════════════════════════
        // Phase 5: Wait for airline to process the reservation
        // Airlines confirm asynchronously. Lambda suspends (no cost).
        // ══════════════════════════════════════════════════════════════════
        await ctx.WaitAsync(TimeSpan.FromMinutes(2), name: "await-airline-confirmation");
        actions.Add("Airline confirmation received");

        // ══════════════════════════════════════════════════════════════════
        // Phase 6: Capture payment (settle the hold)
        // ══════════════════════════════════════════════════════════════════
        await ctx.StepAsync(
            async (_, ct) => await PaymentService.CaptureAsync(paymentAuth.AuthorizationId, ct),
            name: "capture-payment",
            config: new StepConfig { RetryStrategy = RetryStrategy.Default });

        actions.Add("Payment captured");

        // ══════════════════════════════════════════════════════════════════
        // Phase 7: Send confirmation email and persist final result
        // ══════════════════════════════════════════════════════════════════
        await ctx.StepAsync(
            async (_, ct) => await NotificationService.SendConfirmationAsync(
                request.Email, request.BookingId, flightConfirmation, ct),
            name: "send-confirmation-email");

        actions.Add("Confirmation email sent");

        // ══════════════════════════════════════════════════════════════════
        // Phase 8: Persist final result
        // ══════════════════════════════════════════════════════════════════
        var result = new FlightBookingResult(
            request.BookingId, "Confirmed", flightConfirmation,
            availability.FarePrice, null, actions);

        await ctx.StepAsync(
            async (_, ct) => await SaveResultAsync(request.BookingId, result, ct),
            name: "save-result");

        return result;
    }

    // ─── DynamoDB Helpers ────────────────────────────────────────────────────

    private async Task SaveCallbackIdAsync(
        string bookingId, string callbackId, CancellationToken ct)
    {
        await DynamoDbClient.PutItemAsync(new PutItemRequest
        {
            TableName = TableName,
            Item = new Dictionary<string, AttributeValue>
            {
                ["BookingId"] = new() { S = bookingId },
                ["SK"] = new() { S = "CALLBACK#otp" },
                ["CallbackId"] = new() { S = callbackId },
                ["CreatedAt"] = new() { S = DateTime.UtcNow.ToString("O") }
            }
        }, ct);
    }

    private async Task SaveResultAsync(
        string bookingId, FlightBookingResult result, CancellationToken ct)
    {
        var item = new Dictionary<string, AttributeValue>
        {
            ["BookingId"] = new() { S = bookingId },
            ["SK"] = new() { S = "RESULT" },
            ["Status"] = new() { S = result.Status },
            ["TotalCharged"] = new() { N = result.TotalCharged.ToString("F2") },
            ["CompletedAt"] = new() { S = DateTime.UtcNow.ToString("O") }
        };

        if (result.Flight is not null)
        {
            item["FlightConfirmation"] = new() { S = result.Flight.ConfirmationId };
            item["FlightNumber"] = new() { S = result.Flight.FlightNumber };
        }

        if (result.FailureReason is not null)
            item["FailureReason"] = new() { S = result.FailureReason };

        if (result.Actions.Count > 0)
            item["Actions"] = new() { SS = result.Actions };

        await DynamoDbClient.PutItemAsync(new PutItemRequest
        {
            TableName = TableName,
            Item = item
        }, ct);
    }
}
