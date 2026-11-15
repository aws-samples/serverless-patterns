"""Unit tests for shared data models."""

import pytest
from unittest.mock import patch
from src.shared.models import (
    UserContext,
    AgentRequest,
    AgentResponse,
    ToolRequest,
    ToolResponse,
    ConversationTurn,
    ConversationContext,
    InterceptorRequest,
    InterceptorResponse
)


class TestUserContext:
    """Tests for UserContext model."""
    
    def test_user_context_creation(self):
        """Test UserContext can be created with required fields."""
        user_context = UserContext(
            user_id='user-123',
            username='john.doe',
            client_id='app-456'
        )
        
        assert user_context.user_id == 'user-123'
        assert user_context.username == 'john.doe'
        assert user_context.client_id == 'app-456'
    
    def test_user_context_to_dict(self):
        """Test UserContext converts to dictionary correctly."""
        user_context = UserContext(
            user_id='user-123',
            username='john.doe',
            client_id='app-456'
        )
        
        result = user_context.to_dict()
        
        assert result == {
            'user_id': 'user-123',
            'username': 'john.doe',
            'client_id': 'app-456'
        }
    
    def test_user_context_from_jwt_claims(self):
        """Test UserContext can be created from JWT claims."""
        claims = {
            'sub': 'user-123',
            'username': 'john.doe',
            'client_id': 'app-456'
        }
        
        user_context = UserContext.from_jwt_claims(claims)
        
        assert user_context.user_id == 'user-123'
        assert user_context.username == 'john.doe'
        assert user_context.client_id == 'app-456'
    
    def test_user_context_from_dict(self):
        """Test UserContext can be created from dictionary."""
        data = {
            'user_id': 'user-123',
            'username': 'john.doe',
            'client_id': 'app-456'
        }
        
        user_context = UserContext.from_dict(data)
        
        assert user_context.user_id == 'user-123'
        assert user_context.username == 'john.doe'
        assert user_context.client_id == 'app-456'
    
    def test_user_context_from_dict_with_missing_fields(self):
        """Test UserContext handles missing fields with defaults."""
        data = {}
        
        user_context = UserContext.from_dict(data)
        
        assert user_context.user_id == 'unknown'
        assert user_context.username == 'unknown'
        assert user_context.client_id == 'unknown'


class TestAgentRequest:
    """Tests for AgentRequest model."""
    
    def test_agent_request_from_event(self):
        """Test AgentRequest can be parsed from Lambda event."""
        event = {
            'headers': {
                'Authorization': 'Bearer test-token-123'
            },
            'body': '{"prompt": "List my S3 buckets", "session_id": "session-456"}'
        }
        
        request = AgentRequest.from_event(event)
        
        assert request.prompt == 'List my S3 buckets'
        assert request.jwt_token == 'test-token-123'
        assert request.session_id == 'session-456'
    
    def test_agent_request_from_event_without_session(self):
        """Test AgentRequest handles missing session_id."""
        event = {
            'headers': {
                'Authorization': 'Bearer test-token-123'
            },
            'body': '{"prompt": "List my S3 buckets"}'
        }
        
        request = AgentRequest.from_event(event)
        
        assert request.prompt == 'List my S3 buckets'
        assert request.jwt_token == 'test-token-123'
        assert request.session_id is None


class TestAgentResponse:
    """Tests for AgentResponse model."""
    
    def test_agent_response_to_lambda_response(self):
        """Test AgentResponse converts to Lambda response format."""
        user_context = UserContext(
            user_id='user-123',
            username='john.doe',
            client_id='app-456'
        )
        
        response = AgentResponse(
            response='You have 3 S3 buckets',
            session_id='session-456',
            user_context=user_context
        )
        
        result = response.to_lambda_response()
        
        assert result['statusCode'] == 200
        assert 'body' in result
        
        import json
        body = json.loads(result['body'])
        assert body['response'] == 'You have 3 S3 buckets'
        assert body['session_id'] == 'session-456'
        assert body['user_context']['user_id'] == 'user-123'


class TestToolRequest:
    """Tests for ToolRequest model."""
    
    def test_tool_request_from_event(self):
        """Test ToolRequest can be parsed from Lambda event."""
        import os
        # Gateway passes arguments directly as event; tool name comes from env var
        event = {
            'user_context': {
                'user_id': 'user-123',
                'username': 'john.doe',
                'client_id': 'app-456'
            }
        }
        
        with patch.dict(os.environ, {'TOOL_NAME': 'list-s3-buckets'}):
            request = ToolRequest.from_event(event)
        
        assert request.tool_name == 'list-s3-buckets'
        assert request.user_context.user_id == 'user-123'
        assert request.user_context.username == 'john.doe'
    
    def test_tool_request_from_event_with_missing_user_context(self):
        """Test ToolRequest handles missing user_context."""
        import os
        event = {}
        
        with patch.dict(os.environ, {'TOOL_NAME': 'list-s3-buckets'}):
            request = ToolRequest.from_event(event)
        
        assert request.tool_name == 'list-s3-buckets'
        assert request.user_context.user_id == 'unknown'
        assert request.user_context.username == 'unknown'


class TestToolResponse:
    """Tests for ToolResponse model."""
    
    def test_tool_response_to_dict(self):
        """Test ToolResponse converts to dictionary with user context."""
        user_context = UserContext(
            user_id='user-123',
            username='john.doe',
            client_id='app-456'
        )
        
        response = ToolResponse(
            result={'buckets': ['bucket1', 'bucket2']},
            user_context=user_context
        )
        
        result = response.to_dict()
        
        assert 'result' in result
        assert result['result']['buckets'] == ['bucket1', 'bucket2']
        assert result['result']['user_context']['user_id'] == 'user-123'
        assert result['result']['user_context']['username'] == 'john.doe'


class TestConversationModels:
    """Tests for conversation-related models."""
    
    def test_conversation_turn_to_dict(self):
        """Test ConversationTurn converts to dictionary."""
        turn = ConversationTurn(
            prompt='List my buckets',
            response='You have 3 buckets',
            timestamp='2024-01-15T10:30:00Z',
            tool_calls=[{'tool': 'list-s3-buckets'}]
        )
        
        result = turn.to_dict()
        
        assert result['prompt'] == 'List my buckets'
        assert result['response'] == 'You have 3 buckets'
        assert result['timestamp'] == '2024-01-15T10:30:00Z'
        assert len(result['toolCalls']) == 1
    
    def test_conversation_context_to_memory_format(self):
        """Test ConversationContext converts to memory format."""
        turn = ConversationTurn(
            prompt='List my buckets',
            response='You have 3 buckets',
            timestamp='2024-01-15T10:30:00Z'
        )
        
        context = ConversationContext(
            session_id='session-123',
            user_id='user-456',
            turns=[turn],
            created_at='2024-01-15T10:30:00Z',
            updated_at='2024-01-15T10:30:00Z'
        )
        
        result = context.to_memory_format()
        
        assert result['sessionId'] == 'session-123'
        assert result['userId'] == 'user-456'
        assert len(result['turns']) == 1
        assert result['turns'][0]['prompt'] == 'List my buckets'


class TestInterceptorModels:
    """Tests for interceptor-related models."""
    
    def test_interceptor_request_from_event(self):
        """Test InterceptorRequest can be parsed from Lambda event."""
        event = {
            'headers': {
                'Authorization': 'Bearer test-token-123'
            },
            'body': {
                'toolName': 'list-s3-buckets',
                'parameters': {}
            }
        }
        
        request = InterceptorRequest.from_event(event)
        
        assert request.jwt_token == 'test-token-123'
        assert request.tool_name == 'list-s3-buckets'
        assert request.parameters == {}
    
    def test_interceptor_response_to_dict(self):
        """Test InterceptorResponse converts to Gateway format."""
        response = InterceptorResponse(
            tool_name='list-s3-buckets',
            parameters={
                'user_context': {
                    'user_id': 'user-123',
                    'username': 'john.doe',
                    'client_id': 'app-456'
                }
            }
        )
        
        result = response.to_dict()
        
        assert 'body' in result
        assert result['body']['toolName'] == 'list-s3-buckets'
        assert 'user_context' in result['body']['parameters']
