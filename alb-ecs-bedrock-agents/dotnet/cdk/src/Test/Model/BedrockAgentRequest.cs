using Amazon.BedrockAgentRuntime.Model;

namespace TestApp.Model;

public sealed class BedrockAgentRequest
{
    public required string SessionId { get; set; }

    public string? MemoryId { get; set; }

    public string? InvocationId { get; set; }

    public required string Message { get; set; }

    public bool EndSession { get; set; }

    public bool EnableTrace { get; set; }

    public Dictionary<string, string>? SessionAttributes { get; set; }
    
    public Dictionary<string, string>? PromptSessionAttributes { get; set; }

    public List<InvocationResultMember>? ReturnControlInvocationResults { get; set; }
}