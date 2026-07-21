using Amazon.BedrockRuntime;
using Amazon.BedrockRuntime.Model;

namespace TripPlannerStreaming;

/// <summary>
/// Orchestrates the multi-turn conversation with Bedrock to produce a trip itinerary.
/// Calls the provided callback each time a day plan is generated, enabling streaming.
/// </summary>
public class TripPlannerAgent
{
    private const string ModelId = "us.anthropic.claude-sonnet-5";
    private const int MaxTokens = 4096;
    private const int MaxTurns = 20; // Safety limit to prevent infinite loops

    private readonly IAmazonBedrockRuntime _bedrockClient;

    public TripPlannerAgent(IAmazonBedrockRuntime bedrockClient)
    {
        _bedrockClient = bedrockClient;
    }

    /// <summary>
    /// Runs the agent loop. Invokes onDayPlan for each day generated and onSummary for the final text.
    /// </summary>
    public async Task RunAsync(TripRequest trip, Func<DayPlan, Task> onDayPlan, Func<string, Task> onSummary)
    {
        var systemPrompt = BuildSystemPrompt(trip);
        var messages = new List<Message>
        {
            new()
            {
                Role = ConversationRole.User,
                Content = [new ContentBlock { Text = BuildUserMessage(trip) }]
            }
        };

        for (var turn = 0; turn < MaxTurns; turn++)
        {
            var response = await CallModelAsync(systemPrompt, messages);
            var assistantContent = response.Output.Message.Content;

            messages.Add(new Message
            {
                Role = ConversationRole.Assistant,
                Content = assistantContent
            });

            var toolUseBlocks = assistantContent
                .Where(c => c.ToolUse is not null)
                .Select(c => c.ToolUse)
                .ToList();

            if (toolUseBlocks.Count > 0)
            {
                var toolResults = await ProcessToolCallsAsync(toolUseBlocks, onDayPlan);
                messages.Add(new Message
                {
                    Role = ConversationRole.User,
                    Content = toolResults
                });
            }
            else
            {
                // No tool calls — emit any final text as the summary
                await EmitSummaryAsync(assistantContent, onSummary);
                break;
            }

            if (response.StopReason == StopReason.End_turn)
            {
                await EmitSummaryAsync(assistantContent, onSummary);
                break;
            }
        }
    }

    private async Task<ConverseResponse> CallModelAsync(string systemPrompt, List<Message> messages)
    {
        var request = new ConverseRequest
        {
            ModelId = ModelId,
            System = [new SystemContentBlock { Text = systemPrompt }],
            Messages = messages,
            ToolConfig = new ToolConfiguration
            {
                Tools = [ToolDefinitions.AddDayPlanTool]
            },
            InferenceConfig = new InferenceConfiguration
            {
                MaxTokens = MaxTokens
            }
        };

        return await _bedrockClient.ConverseAsync(request);
    }

    private static async Task<List<ContentBlock>> ProcessToolCallsAsync(
        List<ToolUseBlock> toolUseBlocks, Func<DayPlan, Task> onDayPlan)
    {
        var toolResults = new List<ContentBlock>();

        foreach (var toolUse in toolUseBlocks)
        {
            if (toolUse.Name == ToolDefinitions.AddDayPlanToolName)
            {
                var dayPlan = ToolDefinitions.ParseDayPlan(toolUse);
                await onDayPlan(dayPlan);

                toolResults.Add(new ContentBlock
                {
                    ToolResult = new ToolResultBlock
                    {
                        ToolUseId = toolUse.ToolUseId,
                        Content = [new ToolResultContentBlock
                        {
                            Text = $"Day {dayPlan.DayNumber} added to itinerary successfully."
                        }]
                    }
                });
            }
        }

        return toolResults;
    }

    private static async Task EmitSummaryAsync(List<ContentBlock> content, Func<string, Task> onSummary)
    {
        var textBlocks = content
            .Where(c => c.Text is not null)
            .Select(c => c.Text)
            .ToList();

        foreach (var text in textBlocks)
        {
            await onSummary(text!);
        }
    }

    private static string BuildSystemPrompt(TripRequest trip) => $"""
        You are an expert travel planner. Create a detailed {trip.Days}-day itinerary for {trip.Destination}.
        The traveler is interested in: {trip.Interests}.
        
        You MUST use the add_day_plan tool exactly {trip.Days} times, once for each day.
        Plan the days in order from day 1 to day {trip.Days}.
        Make each day distinct and well-paced. Include specific place names and local recommendations.
        After adding all days, provide a brief closing summary with overall trip tips.
        """;

    private static string BuildUserMessage(TripRequest trip) =>
        $"Plan my {trip.Days}-day trip to {trip.Destination}. I'm interested in {trip.Interests}.";
}
