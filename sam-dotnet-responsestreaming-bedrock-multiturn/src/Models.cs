namespace TripPlannerMultiturn;

/// <summary>
/// Incoming request body from the client.
/// </summary>
public record TripPlannerRequest
{
    /// <summary>Session ID for continuing a conversation. Null for a new conversation.</summary>
    public string? SessionId { get; init; }

    /// <summary>The user's message (initial request or answer to a question).</summary>
    public string? Message { get; init; }

    /// <summary>Travel destination (used on first request).</summary>
    public string? Destination { get; init; }

    /// <summary>Number of days (used on first request).</summary>
    public int? Days { get; init; }

    /// <summary>Traveler interests (used on first request).</summary>
    public string? Interests { get; init; }
}

/// <summary>
/// A single day's plan extracted from the agent's tool call.
/// </summary>
public record DayPlan(int DayNumber, string Title, string Morning, string Afternoon, string Evening, string Tips);

/// <summary>
/// The result sent back to the client when the agent asks a question.
/// </summary>
public record QuestionResponse(string SessionId, string Question, string Status = "awaiting_input");

/// <summary>
/// Trip parameters stored in the session.
/// </summary>
public record TripParameters(string Destination, int Days, string Interests);
