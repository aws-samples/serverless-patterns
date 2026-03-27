"""
Strands Agent for AgentCore Runtime.
Accepts a role-based prompt, invokes the LLM, and returns the result.
Used by Step Functions via synchronous InvokeAgentRuntime calls.
"""
import json
import logging

from strands import Agent
from strands.models import BedrockModel
from bedrock_agentcore.runtime import BedrockAgentCoreApp

logger = logging.getLogger(__name__)
app = BedrockAgentCoreApp()

SYSTEM_PROMPTS = {
    "market_data": (
        "You are a market data research analyst. "
        "Provide quantitative market data, trends, market size, growth rates, "
        "and key financial metrics relevant to the topic."
    ),
    "competitive_analysis": (
        "You are a competitive intelligence analyst. "
        "Identify key competitors, their strengths and weaknesses, market positioning, "
        "and strategic differentiators relevant to the topic."
    ),
    "news": (
        "You are a news research analyst. "
        "Summarize the most recent and relevant news, announcements, regulatory changes, "
        "and industry developments related to the topic."
    ),
    "synthesis": (
        "You are a senior research director. "
        "You receive research findings from three analysts covering market data, "
        "competitive analysis, and recent news. Synthesize these into a single cohesive "
        "executive report with key findings, implications, and recommendations."
    ),
}


@app.entrypoint
def entrypoint(payload):
    """
    Main entrypoint invoked by AgentCore Runtime.

    Expects payload:
      - prompt: the research question or combined findings
      - role: one of market_data, competitive_analysis, news, synthesis
      - model (optional): { modelId: "..." }
    """
    prompt = payload.get("prompt", "")
    role = payload.get("role", "synthesis")
    model_config = payload.get("model", {})
    model_id = model_config.get(
        "modelId", "us.anthropic.claude-sonnet-4-5-20250929-v1:0"
    )

    system_prompt = SYSTEM_PROMPTS.get(role, SYSTEM_PROMPTS["synthesis"])

    model = BedrockModel(model_id=model_id, max_tokens=4096, temperature=0.7)
    agent = Agent(model=model, system_prompt=system_prompt)

    result = agent(prompt)
    return {"role": role, "answer": str(result)}


if __name__ == "__main__":
    app.run()
