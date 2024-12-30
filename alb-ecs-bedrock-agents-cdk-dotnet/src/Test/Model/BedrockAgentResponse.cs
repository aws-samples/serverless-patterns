using Amazon.BedrockAgentRuntime.Model;

namespace TestApp.Model;

public class BedrockAgentResponse
{
    public required string SessionId { get; set; }

    public required string MemoryId { get; set; }

    public string? Message { get; set; }

    public List<BedrockAgentOutputFile>? Files { get; set; }

    public ReturnControlPayload? ReturnControlPayload { get; set; }

    public BedrockAgentTrace? Trace { get; set; }

    public string? Error { get; set; }

    public bool HasError => !string.IsNullOrEmpty(Error);
}
