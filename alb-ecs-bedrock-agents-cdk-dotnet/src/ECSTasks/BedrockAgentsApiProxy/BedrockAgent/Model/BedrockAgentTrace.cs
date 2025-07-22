using Amazon.BedrockAgentRuntime.Model;

namespace BedrockAgentsApiProxy.BedrockAgent.Model;

public class BedrockAgentTrace
{
    public List<FailureTrace> FailureTraces { get; } = [];

    public List<GuardrailTrace> GuardrailTraces { get; } = [];

    public List<OrchestrationTrace> OrchestrationTraces { get; } = [];

    public List<PostProcessingTrace> PostProcessingTraces { get; } = [];

    public List<PreProcessingTrace> PreProcessingTraces { get; } = [];
}