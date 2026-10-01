"""Unit tests for Agent Lambda handler."""

import pytest
import json
from unittest.mock import Mock, patch, MagicMock
import os

from src.agent.handler import lambda_handler
from src.shared.models import UserContext


@pytest.fixture
def mock_env_vars():
    """Set up environment variables for testing."""
    with patch.dict(os.environ, {
        'COGNITO_JWKS_URL': 'https://cognito-idp.us-east-1.amazonaws.com/test-pool/.well-known/jwks.json',
        'GATEWAY_ID': 'test-gateway-id',
        'BEDROCK_MODEL_ID': 'anthropic.claude-3-sonnet-20240229-v1:0',
        'AWS_REGION': 'us-east-1',
        'LOG_LEVEL': 'INFO'
    }):
        yield


@pytest.fixture
def valid_jwt_token():
    """Return a mock valid JWT token."""
    return 'eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCJ9.test.signature'


@pytest.fixture
def valid_jwt_claims():
    """Return mock JWT claims."""
    return {
        'sub': 'user-123',
        'username': 'testuser@example.com',
        'client_id': 'client-456',
        'token_use': 'access'
    }


@pytest.fixture
def valid_event(valid_jwt_token):
    """Create a valid Lambda event."""
    return {
        'headers': {
            'Authorization': f'Bearer {valid_jwt_token}'
        },
        'body': json.dumps({
            'prompt': 'What is the weather in Seattle?',
            'session_id': 'test-session-123'
        })
    }


@pytest.fixture
def mock_context():
    """Create mock Lambda context."""
    context = Mock()
    context.request_id = 'test-request-id'
    return context


def test_lambda_handler_success(mock_env_vars, valid_event, mock_context, valid_jwt_token, valid_jwt_claims):
    """Test successful request processing."""
    with patch('src.agent.handler.validate_jwt') as mock_validate, \
         patch('src.agent.handler.extract_user_context') as mock_extract, \
         patch('src.agent.handler.AgentProcessor') as mock_processor_cls:
        
        # Setup mocks
        mock_validate.return_value = valid_jwt_claims
        mock_extract.return_value = UserContext(
            user_id='user-123',
            username='testuser@example.com',
            client_id='client-456'
        )
        
        mock_processor = Mock()
        mock_processor.process_request.return_value = (
            'The weather in Seattle is 65°F and partly cloudy.',
            'test-session-123'
        )
        mock_processor_cls.return_value = mock_processor
        
        # Execute
        response = lambda_handler(valid_event, mock_context)
        
        # Verify
        assert response['statusCode'] == 200
        
        body = json.loads(response['body'])
        assert body['response'] == 'The weather in Seattle is 65°F and partly cloudy.'
        assert body['session_id'] == 'test-session-123'
        assert body['user_context']['user_id'] == 'user-123'
        assert body['user_context']['username'] == 'testuser@example.com'
        assert body['user_context']['client_id'] == 'client-456'
        
        # Verify JWT was validated (with the JWKS URL from environment)
        mock_validate.assert_called_once()
        call_args = mock_validate.call_args
        assert call_args[0][0] == valid_jwt_token
        # JWKS URL comes from environment variable
        
        # Verify user context was extracted
        mock_extract.assert_called_once_with(valid_jwt_claims)
        
        # Verify processor was called
        mock_processor.process_request.assert_called_once_with(
            prompt='What is the weather in Seattle?',
            jwt_token=valid_jwt_token,
            session_id='test-session-123'
        )


def test_lambda_handler_missing_authorization_header(mock_env_vars, mock_context):
    """Test request with missing Authorization header."""
    event = {
        'headers': {},
        'body': json.dumps({'prompt': 'Test'})
    }
    
    # Execute
    response = lambda_handler(event, mock_context)
    
    # Verify 401 response
    assert response['statusCode'] == 401
    body = json.loads(response['body'])
    assert 'error' in body


def test_lambda_handler_invalid_authorization_format(mock_env_vars, mock_context):
    """Test request with invalid Authorization header format."""
    event = {
        'headers': {
            'Authorization': 'InvalidFormat token123'
        },
        'body': json.dumps({'prompt': 'Test'})
    }
    
    # Execute
    response = lambda_handler(event, mock_context)
    
    # Verify 401 response
    assert response['statusCode'] == 401
    body = json.loads(response['body'])
    assert 'error' in body


def test_lambda_handler_empty_jwt_token(mock_env_vars, mock_context):
    """Test request with empty JWT token."""
    event = {
        'headers': {
            'Authorization': 'Bearer '
        },
        'body': json.dumps({'prompt': 'Test'})
    }
    
    # Execute
    response = lambda_handler(event, mock_context)
    
    # Verify 401 response
    assert response['statusCode'] == 401
    body = json.loads(response['body'])
    assert 'error' in body


def test_lambda_handler_jwt_validation_failure(mock_env_vars, valid_event, mock_context):
    """Test request with invalid JWT token."""
    with patch('src.agent.handler.validate_jwt') as mock_validate:
        # Setup mock to raise validation error
        mock_validate.side_effect = ValueError('Token has expired')
        
        # Execute
        response = lambda_handler(valid_event, mock_context)
        
        # Verify 401 response
        assert response['statusCode'] == 401
        body = json.loads(response['body'])
        assert 'error' in body


def test_lambda_handler_missing_prompt(mock_env_vars, valid_jwt_token, mock_context, valid_jwt_claims):
    """Test request with missing prompt."""
    event = {
        'headers': {
            'Authorization': f'Bearer {valid_jwt_token}'
        },
        'body': json.dumps({
            'session_id': 'test-session-123'
        })
    }
    
    with patch('src.agent.handler.validate_jwt') as mock_validate, \
         patch('src.agent.handler.extract_user_context') as mock_extract:
        
        mock_validate.return_value = valid_jwt_claims
        mock_extract.return_value = UserContext(
            user_id='user-123',
            username='testuser@example.com',
            client_id='client-456'
        )
        
        # Execute
        response = lambda_handler(event, mock_context)
        
        # Verify 400 response
        assert response['statusCode'] == 400
        body = json.loads(response['body'])
        assert 'error' in body
        assert 'prompt' in body['error'].lower()


def test_lambda_handler_invalid_json_body(mock_env_vars, valid_jwt_token, mock_context, valid_jwt_claims):
    """Test request with invalid JSON body."""
    event = {
        'headers': {
            'Authorization': f'Bearer {valid_jwt_token}'
        },
        'body': 'invalid json {'
    }
    
    with patch('src.agent.handler.validate_jwt') as mock_validate, \
         patch('src.agent.handler.extract_user_context') as mock_extract:
        
        mock_validate.return_value = valid_jwt_claims
        mock_extract.return_value = UserContext(
            user_id='user-123',
            username='testuser@example.com',
            client_id='client-456'
        )
        
        # Execute
        response = lambda_handler(event, mock_context)
        
        # Verify 400 response
        assert response['statusCode'] == 400
        body = json.loads(response['body'])
        assert 'error' in body


def test_lambda_handler_agent_processing_failure(mock_env_vars, valid_event, mock_context, valid_jwt_token, valid_jwt_claims):
    """Test request when agent processing fails."""
    with patch('src.agent.handler.validate_jwt') as mock_validate, \
         patch('src.agent.handler.extract_user_context') as mock_extract, \
         patch('src.agent.handler.AgentProcessor') as mock_processor_cls:
        
        # Setup mocks
        mock_validate.return_value = valid_jwt_claims
        mock_extract.return_value = UserContext(
            user_id='user-123',
            username='testuser@example.com',
            client_id='client-456'
        )
        
        mock_processor = Mock()
        mock_processor.process_request.side_effect = Exception('Processing failed')
        mock_processor_cls.return_value = mock_processor
        
        # Execute
        response = lambda_handler(valid_event, mock_context)
        
        # Verify 500 response
        assert response['statusCode'] == 500
        body = json.loads(response['body'])
        assert 'error' in body


def test_lambda_handler_without_session_id(mock_env_vars, valid_jwt_token, mock_context, valid_jwt_claims):
    """Test request without session_id (new conversation)."""
    event = {
        'headers': {
            'Authorization': f'Bearer {valid_jwt_token}'
        },
        'body': json.dumps({
            'prompt': 'Hello'
        })
    }
    
    with patch('src.agent.handler.validate_jwt') as mock_validate, \
         patch('src.agent.handler.extract_user_context') as mock_extract, \
         patch('src.agent.handler.AgentProcessor') as mock_processor_cls:
        
        # Setup mocks
        mock_validate.return_value = valid_jwt_claims
        mock_extract.return_value = UserContext(
            user_id='user-123',
            username='testuser@example.com',
            client_id='client-456'
        )
        
        mock_processor = Mock()
        mock_processor.process_request.return_value = (
            'Hi there!',
            'new-session-456'
        )
        mock_processor_cls.return_value = mock_processor
        
        # Execute
        response = lambda_handler(event, mock_context)
        
        # Verify
        assert response['statusCode'] == 200
        body = json.loads(response['body'])
        assert body['session_id'] == 'new-session-456'
        
        # Verify processor was called with None session_id
        mock_processor.process_request.assert_called_once_with(
            prompt='Hello',
            jwt_token=valid_jwt_token,
            session_id=None
        )


def test_lambda_handler_user_context_extraction_failure(mock_env_vars, valid_event, mock_context, valid_jwt_claims):
    """Test request when user context extraction fails."""
    with patch('src.agent.handler.validate_jwt') as mock_validate, \
         patch('src.agent.handler.extract_user_context') as mock_extract:
        
        # Setup mocks
        mock_validate.return_value = valid_jwt_claims
        mock_extract.side_effect = ValueError('Missing required claims')
        
        # Execute
        response = lambda_handler(valid_event, mock_context)
        
        # Verify 400 response
        assert response['statusCode'] == 400
        body = json.loads(response['body'])
        assert 'error' in body
