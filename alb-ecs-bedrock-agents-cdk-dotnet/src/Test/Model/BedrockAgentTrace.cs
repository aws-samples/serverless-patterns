using Amazon.BedrockAgentRuntime.Model;

namespace TestApp.Model;

public class BedrockAgentTrace
{
    public List<FailureTrace> FailureTraces { get; set; } = [];

    public List<GuardrailTrace> GuardrailTraces { get; set; } = [];

    public List<OrchestrationTrace> OrchestrationTraces { get; set; } = [];

    public List<PostProcessingTrace> PostProcessingTraces { get; set; } = [];

    public List<PreProcessingTrace> PreProcessingTraces { get; set; } = [];
}