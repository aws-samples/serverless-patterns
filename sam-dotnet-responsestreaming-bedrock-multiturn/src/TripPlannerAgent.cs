using Amazon.BedrockRuntime;
using Amazon.BedrockRuntime.Model;

namespace TripPlannerMultiturn;

/// <summary>
/// Result of a single agent turn. Either the agent asks a question (and suspends),
/// or it completes the full itinerary.
/// </summary>
public abstract record AgentResult;
public record AgentAskedQuestion(string Question, string ToolUseId, List<Message> Messages) : AgentResult;
public record AgentCompleted : AgentResult;

/// <summary>
/// Orchestrates the multi-turn Bedrock conversation. Supports suspending when
/// the agent calls ask_user and resuming when the user responds.
/// </summary>
public class TripPlannerAgent
{
    private const string ModelId = "us.anthropic.claude-sonnet-5";
    private const int MaxTokens = 4096;
    private const int MaxTurns = 20;

    private readonly IAmazonBedrockRuntime _bedrockClient;

    public TripPlannerAgent(IAmazonBedrockRuntime bedrockClient)
    {
        _bedrockClient = bedrockClient;
    }

    /// <summary>
    /// Runs the agent loop from the given messages. Returns when the agent either
    /// asks a question (AgentAskedQuestion) or finishes the itinerary (AgentCompleted).
    /// </summary>
    public async Task<AgentResult> RunAsync(
        TripParameters trip,
        List<Message> messages,
        Func<DayPlan, Task> onDayPlan,
        Func<string, Task> onSummary)
    {
        var systemPrompt = BuildSystemPrompt(trip);

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
                // Check if the agent wants to ask the user a question
                var askUserTool = toolUseBlocks.FirstOrDefault(t => t.Name == ToolDefinitions.AskUserToolName);
                if (askUserTool is not null)
                {
                    var question = ToolDefinitions.ParseQuestion(askUserTool);
                    return new AgentAskedQuestion(question, askUserTool.ToolUseId, messages);
                }

                // Process day plan tool calls (and return errors for unknown tools)
                var toolResults = await ProcessToolCallsAsync(toolUseBlocks, onDayPlan);
                messages.Add(new Message
                {
                    Role = ConversationRole.User,
                    Content = toolResults
                });
            }
            else
            {
                // No tool calls — emit final summary
                await EmitSummaryAsync(assistantContent, onSummary);
                return new AgentCompleted();
            }
        }

        return new AgentCompleted();
    }

    /// <summary>
    /// Creates the initial messages list for a new conversation.
    /// </summary>
    public static List<Message> CreateInitialMessages(TripParameters trip)
    {
        return
        [
            new Message
            {
                Role = ConversationRole.User,
                Content = [new ContentBlock { Text = BuildUserMessage(trip) }]
            }
        ];
    }

    /// <summary>
    /// Appends the user's answer to a pending ask_user tool call.
    /// </summary>
    public static void AppendUserAnswer(List<Message> messages, string toolUseId, string answer)
    {
        messages.Add(new Message
        {
            Role = ConversationRole.User,
            Content =
            [
                new ContentBlock
                {
                    ToolResult = new ToolResultBlock
                    {
                        ToolUseId = toolUseId,
                        Content = [new ToolResultContentBlock { Text = answer }]
                    }
                }
            ]
        });
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
                Tools = ToolDefinitions.AllTools
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
            else
            {
                // Unknown tool — return an error result so the model can recover
                toolResults.Add(new ContentBlock
                {
                    ToolResult = new ToolResultBlock
                    {
                        ToolUseId = toolUse.ToolUseId,
                        Status = ToolResultStatus.Error,
                        Content = [new ToolResultContentBlock
                        {
                            Text = $"Unknown tool '{toolUse.Name}'. Available tools: add_day_plan, ask_user."
                        }]
                    }
                });
            }
        }

        return toolResults;
    }

    private static async Task EmitSummaryAsync(List<ContentBlock> content, Func<string, Task> onSummary)
    {
        var textBlocks = content.Where(c => c.Text is not null).Select(c => c.Text!).ToList();
        foreach (var text in textBlocks)
        {
            await onSummary(text);
        }
    }

    private static string BuildSystemPrompt(TripParameters trip) => $"""
        You are an expert travel planner. Create a detailed {trip.Days}-day itinerary for {trip.Destination}.
        The traveler is interested in: {trip.Interests}.
        
        IMPORTANT RULES:
        1. Before planning, you SHOULD ask 1-2 clarifying questions using the ask_user tool to
           understand the traveler better (e.g., budget, pace preference, dietary needs, mobility).
           Ask only ONE question at a time.
        2. Once you have enough information, use the add_day_plan tool exactly {trip.Days} times.
        3. Plan the days in order. Make each day distinct with specific place names.
        4. After all days, provide a brief closing summary.
        
        If the user says to skip questions or just plan, proceed directly with add_day_plan.
        """;

    private static string BuildUserMessage(TripParameters trip) =>
        $"Plan my {trip.Days}-day trip to {trip.Destination}. I'm interested in {trip.Interests}.";
}
