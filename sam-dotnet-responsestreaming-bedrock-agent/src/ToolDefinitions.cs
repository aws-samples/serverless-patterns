using Amazon.BedrockRuntime.Model;
using Document = Amazon.Runtime.Documents.Document;

namespace TripPlannerStreaming;

/// <summary>
/// Defines the tools available to the trip planner agent.
/// </summary>
public static class ToolDefinitions
{
    public const string AddDayPlanToolName = "add_day_plan";

    public static Tool AddDayPlanTool { get; } = new()
    {
        ToolSpec = new ToolSpecification
        {
            Name = AddDayPlanToolName,
            Description = "Add a single day's plan to the trip itinerary. Call this once for each day of the trip.",
            InputSchema = new ToolInputSchema
            {
                Json = Document.FromObject(new
                {
                    type = "object",
                    properties = new
                    {
                        day_number = new { type = "integer", description = "The day number (1-indexed)" },
                        title = new { type = "string", description = "A short title for the day (e.g., 'Historic Old Town & River Cruise')" },
                        morning = new { type = "string", description = "Morning activities and recommendations (2-3 sentences)" },
                        afternoon = new { type = "string", description = "Afternoon activities and recommendations (2-3 sentences)" },
                        evening = new { type = "string", description = "Evening activities, dinner recommendations (2-3 sentences)" },
                        tips = new { type = "string", description = "Practical tips for this day (transport, tickets, what to pack)" }
                    },
                    required = new[] { "day_number", "title", "morning", "afternoon", "evening", "tips" }
                })
            }
        }
    };

    /// <summary>
    /// Extracts a DayPlan from the tool use input Document.
    /// </summary>
    public static DayPlan ParseDayPlan(ToolUseBlock toolUse)
    {
        var input = toolUse.Input.AsDictionary();
        return new DayPlan(
            DayNumber: input["day_number"].AsInt(),
            Title: input["title"].AsString(),
            Morning: input["morning"].AsString(),
            Afternoon: input["afternoon"].AsString(),
            Evening: input["evening"].AsString(),
            Tips: input["tips"].AsString()
        );
    }
}
