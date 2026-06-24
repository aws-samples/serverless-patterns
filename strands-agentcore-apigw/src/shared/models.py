"""Data models for Agent Gateway."""

import json
from dataclasses import dataclass
from typing import Optional


@dataclass
class UserContext:
    """User identity information extracted from JWT token."""
    user_id: str
    username: str
    client_id: str

    def to_dict(self) -> dict:
        return {
            'user_id': self.user_id,
            'username': self.username,
            'client_id': self.client_id
        }

    @classmethod
    def from_jwt_claims(cls, claims: dict) -> 'UserContext':
        return cls(
            user_id=claims['sub'],
            username=claims['username'],
            client_id=claims['client_id']
        )

    @classmethod
    def from_dict(cls, data: dict) -> 'UserContext':
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
        return {
            'statusCode': 200,
            'body': json.dumps({
                'response': self.response,
                'session_id': self.session_id,
                'user_context': self.user_context.to_dict()
            })
        }
