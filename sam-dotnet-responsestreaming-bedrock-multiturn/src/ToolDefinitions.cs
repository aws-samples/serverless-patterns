using Amazon.BedrockRuntime.Model;
using Document = Amazon.Runtime.Documents.Document;

namespace TripPlannerMultiturn;

/// <summary>
/// Defines the tools available to the trip planner agent.
/// </summary>
public static class ToolDefinitions
{
    public const string AddDayPlanToolName = "add_day_plan";
    public const string AskUserToolName = "ask_user";

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
                        title = new { type = "string", description = "A short title for the day" },
                        morning = new { type = "string", description = "Morning activities (2-3 sentences)" },
                        afternoon = new { type = "string", description = "Afternoon activities (2-3 sentences)" },
                        evening = new { type = "string", description = "Evening activities and dinner (2-3 sentences)" },
                        tips = new { type = "string", description = "Practical tips for this day" }
                    },
                    required = new[] { "day_number", "title", "morning", "afternoon", "evening", "tips" }
                })
            }
        }
    };

    public static Tool AskUserTool { get; } = new()
    {
        ToolSpec = new ToolSpecification
        {
            Name = AskUserToolName,
            Description = """
                Ask the user a clarifying question before proceeding with planning.
                Use this when you need more information to create a better itinerary,
                such as budget level, mobility constraints, dietary restrictions,
                preferred pace, or specific must-see places.
                You may ask at most 2 questions total before proceeding with planning.
                """,
            InputSchema = new ToolInputSchema
            {
                Json = Document.FromObject(new
                {
                    type = "object",
                    properties = new
                    {
                        question = new { type = "string", description = "The question to ask the user" }
                    },
                    required = new[] { "question" }
                })
            }
        }
    };

    public static readonly List<Tool> AllTools = [AddDayPlanTool, AskUserTool];

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

    public static string ParseQuestion(ToolUseBlock toolUse)
    {
        var input = toolUse.Input.AsDictionary();
        return input["question"].AsString();
    }
}
