namespace TripPlannerStreaming;

/// <summary>
/// Parsed trip planning request parameters.
/// </summary>
public record TripRequest(string Destination, int Days, string Interests)
{
    public const string DefaultDestination = "Tokyo, Japan";
    public const int DefaultDays = 3;
    public const string DefaultInterests = "culture, food, and nature";
    public const int MaxDays = 14;
}

/// <summary>
/// A single day's plan extracted from the agent's tool call.
/// </summary>
public record DayPlan(int DayNumber, string Title, string Morning, string Afternoon, string Evening, string Tips);
