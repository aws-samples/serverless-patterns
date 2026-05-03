"""Strands Agents SDK agent deployed on AWS Lambda with Amazon Bedrock."""

import json
import math
from strands import Agent, tool


@tool
def calculate(expression: str) -> str:
    """Evaluate a mathematical expression safely.

    Args:
        expression: A mathematical expression to evaluate (e.g. '2 + 3 * 4').

    Returns:
        The result of the calculation.
    """
    allowed = set("0123456789+-*/.() ")
    if not all(c in allowed for c in expression):
        return "Error: expression contains invalid characters"
    try:
        result = eval(expression, {"__builtins__": {}}, {"math": math})  # noqa: S307
        return str(result)
    except Exception as e:
        return f"Error: {e}"


SYSTEM_PROMPT = """You are a helpful assistant with access to a calculator tool.
When asked math questions, use the calculate tool to compute the answer.
Always show your work by explaining what calculation you performed."""


def handler(event, _context):
    """Lambda handler that runs a Strands agent."""
    prompt = event.get("prompt", "What is 25 * 47 + 13?")

    agent = Agent(
        system_prompt=SYSTEM_PROMPT,
        tools=[calculate],
    )

    response = agent(prompt)
    return {"statusCode": 200, "body": str(response)}
