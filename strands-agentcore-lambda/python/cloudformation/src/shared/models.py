"""Data models for Serverless AI Agent Gateway."""

import json
from dataclasses import dataclass, field
from typing import Optional, List, Dict, Any
from datetime import datetime


@dataclass
class UserContext:
    """User identity information extracted from JWT token."""
    user_id: str
    username: str
    client_id: str
    
    def to_dict(self) -> dict:
        """Convert to dictionary representation."""
        return {
            'user_id': self.user_id,
            'username': self.username,
            'client_id': self.client_id
        }
    
    @classmethod
    def from_jwt_claims(cls, claims: dict) -> 'UserContext':
        """Create UserContext from JWT claims.
        
        Args:
            claims: Decoded JWT claims containing sub, username, client_id
            
        Returns:
            UserContext instance
        """
        return cls(
            user_id=claims['sub'],
            username=claims['username'],
            client_id=claims['client_id']
        )
    
    @classmethod
    def from_dict(cls, data: dict) -> 'UserContext':
        """Create UserContext from dictionary.
        
        Args:
            data: Dictionary with user_id, username, client_id
            
        Returns:
            UserContext instance
        """
        return cls(
            user_id=data.get('user_id', 'unknown'),
            username=data.get('username', 'unknown'),
            client_id=data.get('client_id', 'unknown')
        )


@dataclass
class AgentRequest:
    """Request to Agent Lambda with authentication."""
    prompt: str
    jwt_token: str
    session_id: Optional[str] = None
    
    @classmethod
    def from_event(cls, event: dict) -> 'AgentRequest':
        """Parse AgentRequest from Lambda event.
        
        Args:
            event: Lambda event with headers and body
            
        Returns:
            AgentRequest instance
        """
        headers = event.get('headers', {})
        body_str = event.get('body', '{}')
        body = json.loads(body_str) if isinstance(body_str, str) else body_str
        
        auth_header = headers.get('Authorization', '')
        jwt_token = auth_header.replace('Bearer ', '')
        
        return cls(
            prompt=body['prompt'],
            jwt_token=jwt_token,
            session_id=body.get('session_id')
        )


@dataclass
class AgentResponse:
    """Response from Agent Lambda."""
    response: str
    session_id: str
    user_context: UserContext
    
    def to_lambda_response(self) -> dict:
        """Convert to Lambda response format.
        
        Returns:
            Lambda response dictionary
        """
        return {
            'statusCode': 200,
            'body': json.dumps({
                'response': self.response,
                'session_id': self.session_id,
                'user_context': self.user_context.to_dict()
            })
        }


@dataclass
class ToolRequest:
    """Tool execution request with user attribution."""
    tool_name: str
    parameters: dict
    user_context: UserContext
    
    @classmethod
    def from_event(cls, event: dict) -> 'ToolRequest':
        """Parse ToolRequest from Lambda event.
        
        When AgentCore Gateway invokes a Lambda target, it only passes the
        arguments from the MCP request, not the tool name. The tool name
        is configured via the TOOL_NAME environment variable.
        
        Args:
            event: Lambda event from AgentCore Gateway
            
        Returns:
            ToolRequest instance
            
        Raises:
            ValueError: If TOOL_NAME environment variable is not set
        """
        import os
        
        # Get tool name from environment variable
        # This is set in CloudFormation for each Lambda function
        tool_name = os.environ.get('TOOL_NAME', '')
        
        if not tool_name:
            raise ValueError(
                "TOOL_NAME environment variable must be set. "
                "This Lambda function must be configured with the tool it handles."
            )
        
        # Extract parameters - Gateway passes arguments directly as event
        parameters = event if isinstance(event, dict) else {}
        
        # Extract user context
        user_context_dict = parameters.get('user_context', {})
        user_context = UserContext.from_dict(user_context_dict)
        
        return cls(
            tool_name=tool_name,
            parameters=parameters,
            user_context=user_context
        )


@dataclass
class ToolResponse:
    """Tool execution response with user attribution."""
    result: dict
    user_context: UserContext
    
    def to_dict(self) -> dict:
        """Convert to dictionary format.
        
        Returns:
            Response dictionary with user context
        """
        return {
            'result': {
                **self.result,
                'user_context': {
                    'user_id': self.user_context.user_id,
                    'username': self.user_context.username
                }
            }
        }


@dataclass
class ConversationTurn:
    """Single turn in a conversation."""
    prompt: str
    response: str
    timestamp: str
    tool_calls: List[dict] = field(default_factory=list)
    
    def to_dict(self) -> dict:
        """Convert to dictionary format."""
        return {
            'prompt': self.prompt,
            'response': self.response,
            'timestamp': self.timestamp,
            'toolCalls': self.tool_calls
        }


@dataclass
class ConversationContext:
    """Complete conversation context for a session."""
    session_id: str
    user_id: str
    turns: List[ConversationTurn]
    created_at: str
    updated_at: str
    
    def to_memory_format(self) -> dict:
        """Convert to AgentCore Memory format.
        
        Returns:
            Memory format dictionary
        """
        return {
            'sessionId': self.session_id,
            'userId': self.user_id,
            'turns': [turn.to_dict() for turn in self.turns],
            'createdAt': self.created_at,
            'updatedAt': self.updated_at
        }
    
    @classmethod
    def from_memory_format(cls, data: dict) -> 'ConversationContext':
        """Create ConversationContext from memory format.
        
        Args:
            data: Memory format dictionary
            
        Returns:
            ConversationContext instance
        """
        turns = [
            ConversationTurn(
                prompt=turn['prompt'],
                response=turn['response'],
                timestamp=turn['timestamp'],
                tool_calls=turn.get('toolCalls', [])
            )
            for turn in data.get('turns', [])
        ]
        
        return cls(
            session_id=data['sessionId'],
            user_id=data['userId'],
            turns=turns,
            created_at=data['createdAt'],
            updated_at=data['updatedAt']
        )


@dataclass
class InterceptorRequest:
    """Request to Gateway Request Interceptor."""
    jwt_token: str
    tool_name: str
    parameters: dict
    
    @classmethod
    def from_event(cls, event: dict) -> 'InterceptorRequest':
        """Parse InterceptorRequest from Lambda event.
        
        Args:
            event: Lambda event from AgentCore Gateway
            
        Returns:
            InterceptorRequest instance
        """
        headers = event.get('headers', {})
        body = event.get('body', {})
        
        auth_header = headers.get('Authorization', '')
        jwt_token = auth_header.replace('Bearer ', '')
        
        return cls(
            jwt_token=jwt_token,
            tool_name=body.get('toolName', ''),
            parameters=body.get('parameters', {})
        )


@dataclass
class InterceptorResponse:
    """Transformed request from Gateway Request Interceptor."""
    tool_name: str
    parameters: dict
    
    def to_dict(self) -> dict:
        """Convert to Gateway response format.
        
        Returns:
            Gateway response dictionary
        """
        return {
            'body': {
                'toolName': self.tool_name,
                'parameters': self.parameters
            }
        }
