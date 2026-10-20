namespace TravelBooking;

// ─── Input ───────────────────────────────────────────────────────────────────

public sealed record FlightBookingRequest(
    string BookingId,
    string TravelerId,
    string Email,
    FlightDetails Flight,
    PaymentInfo Payment);

public sealed record FlightDetails(
    string Origin,
    string Destination,
    DateTime DepartureDate,
    DateTime ReturnDate,
    string CabinClass);

public sealed record PaymentInfo(
    string CardLast4,
    string CardHolder);

// ─── Service Responses ───────────────────────────────────────────────────────

public sealed record AvailabilityResult(
    bool IsAvailable,
    decimal FarePrice,
    string? UnavailableReason);

public sealed record PaymentAuthResult(
    string AuthorizationId,
    string Status,
    decimal Amount);

public sealed record PaymentConfirmation(
    string Status,
    string TransactionRef);

/// <summary>
/// Inbound request from the payment gateway when confirming a payment.
/// The callback token is passed in the body to avoid URL encoding issues
/// (the token is a binary blob containing characters like / and +).
/// </summary>
public sealed record PaymentCallbackRequest(
    string CallbackId,
    string Status,
    string TransactionRef);

public sealed record FlightConfirmation(
    string ConfirmationId,
    string Status,
    string FlightNumber,
    decimal Price);

// ─── Final Output ────────────────────────────────────────────────────────────

public sealed record FlightBookingResult(
    string BookingId,
    string Status,
    FlightConfirmation? Flight,
    decimal TotalCharged,
    string? FailureReason,
    List<string> Actions);
