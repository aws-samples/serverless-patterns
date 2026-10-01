"""Shared data models for the agent application.

Target-type agnostic data classes used across agent and shared modules.
"""

from dataclasses import dataclass
from typing import Optional


@dataclass
class UserContext:
    """Represents an authenticated user's context."""
    username: str
    token: str


@dataclass
class AgentRequest:
    """Represents a request to the agent."""
    prompt: str
    user_context: UserContext


@dataclass
class AgentResponse:
    """Represents a response from the agent."""
    success: bool
    response: str
    error: Optional[str] = None
