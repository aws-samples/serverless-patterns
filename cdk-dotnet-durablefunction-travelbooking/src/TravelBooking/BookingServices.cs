namespace TravelBooking;

/// <summary>
/// Checks flight availability and current fare.
/// In production: calls a GDS (Global Distribution System) or airline API.
/// </summary>
internal static class AvailabilityService
{
    public static Task<AvailabilityResult> CheckFlightAsync(FlightDetails flight, CancellationToken ct)
    {
        // "FULL" origin simulates no availability
        if (flight.Origin.Equals("FULL", StringComparison.OrdinalIgnoreCase))
            return Task.FromResult(new AvailabilityResult(false, 0, "No seats available on requested route."));

        var price = Math.Round(250m + Random.Shared.Next(100, 800), 2);
        return Task.FromResult(new AvailabilityResult(true, price, null));
    }
}

/// <summary>
/// Payment gateway mock. Authorize holds funds, Capture settles, Reverse releases.
/// </summary>
internal static class PaymentService
{
    public static Task<PaymentAuthResult> AuthorizeAsync(
        PaymentInfo payment, decimal amount, CancellationToken ct)
    {
        var authId = $"AUTH-{Guid.NewGuid().ToString("N")[..8].ToUpperInvariant()}";
        return Task.FromResult(new PaymentAuthResult(authId, "Authorized", amount));
    }

    public static Task CaptureAsync(string authorizationId, CancellationToken ct)
        => Task.CompletedTask; // Settle the hold

    public static Task ReverseAsync(string authorizationId, CancellationToken ct)
        => Task.CompletedTask; // Release the hold — funds returned
}

/// <summary>
/// Flight booking service mock.
/// In production: calls airline reservation system.
/// </summary>
internal static class FlightService
{
    public static Task<FlightConfirmation> BookAsync(
        FlightDetails flight, string bookingId, CancellationToken ct)
    {
        // "FAIL" origin simulates airline rejecting reservation after payment
        if (flight.Origin.Equals("FAIL", StringComparison.OrdinalIgnoreCase))
            return Task.FromResult(new FlightConfirmation("", "Failed", "", 0));

        var confirmationId = $"FL-{Guid.NewGuid().ToString("N")[..8].ToUpperInvariant()}";
        var flightNumber = $"AW{Random.Shared.Next(100, 999)}";
        var price = Math.Round(250m + Random.Shared.Next(100, 800), 2);

        return Task.FromResult(new FlightConfirmation(confirmationId, "Confirmed", flightNumber, price));
    }

    public static Task CancelAsync(string confirmationId, CancellationToken ct)
        => Task.CompletedTask;
}

/// <summary>
/// Email/notification service mock.
/// In production: SES or SNS with a deep link for seat selection.
/// </summary>
internal static class NotificationService
{
    public static Task SendConfirmationAsync(
        string email, string bookingId, FlightConfirmation flight, CancellationToken ct)
        => Task.CompletedTask;
}

/// <summary>
/// Exception thrown when a booking service cannot complete a reservation.
/// </summary>
public sealed class BookingException : Exception
{
    public BookingException(string message) : base(message) { }
}
