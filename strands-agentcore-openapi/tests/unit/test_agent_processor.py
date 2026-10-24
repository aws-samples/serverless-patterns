"""Unit tests for Agent Processor."""

import pytest
from unittest.mock import Mock, MagicMock, patch
import uuid

from src.agent.agent_processor import AgentProcessor
from src.shared.models import UserContext
from src.shared.logging_utils import StructuredLogger


@pytest.fixture
def mock_logger():
    """Create mock structured logger."""
    logger = Mock(spec=StructuredLogger)
    return logger


@pytest.fixture
def mock_strands_agent():
    """Create mock Strands agent."""
    agent = Mock()
    return agent


@pytest.fixture
def mock_gateway_client():
    """Create mock Gateway client."""
    client = Mock()
    return client


@pytest.fixture
def agent_processor(mock_logger):
    """Create AgentProcessor with mocked dependencies."""
    with patch('src.agent.agent_processor.StrandsAgent') as mock_strands_cls, \
         patch('src.agent.agent_processor.GatewayClient') as mock_gateway_cls:
        
        processor = AgentProcessor(
            gateway_id='test-gateway-id',
            model_id='anthropic.claude-3-sonnet-20240229-v1:0',
            region='us-east-1',
            logger=mock_logger
        )
        
        # Replace with mocks
        processor.strands_agent = Mock()
        processor.gateway_client = Mock()
        
        return processor


def test_agent_processor_initialization(mock_logger):
    """Test agent processor initializes correctly."""
    with patch('src.agent.agent_processor.StrandsAgent') as mock_strands_cls, \
         patch('src.agent.agent_processor.GatewayClient') as mock_gateway_cls:
        
        processor = AgentProcessor(
            gateway_id='test-gateway-id',
            model_id='anthropic.claude-3-sonnet-20240229-v1:0',
            region='us-east-1',
            logger=mock_logger
        )
        
        # Verify clients were initialized
        mock_strands_cls.assert_called_once_with(
            model_id='anthropic.claude-3-sonnet-20240229-v1:0',
            region='us-east-1',
            logger=mock_logger
        )
        
        mock_gateway_cls.assert_called_once_with(
            gateway_id='test-gateway-id',
            region='us-east-1',
            logger=mock_logger
        )
        
        mock_logger.info.assert_called_with('Agent processor initialized')


def test_process_request_text_response(agent_processor):
    """Test processing request with text response (no tool use)."""
    # Setup mocks
    agent_processor.gateway_client.list_tools.return_value = [
        {
            'name': 'test-tool',
            'description': 'Test tool',
            'input_schema': {}
        }
    ]
    
    agent_processor.strands_agent.format_messages.return_value = [
        {'role': 'user', 'content': 'What is the weather?'}
    ]
    
    agent_processor.strands_agent.invoke_with_tools.return_value = {
        'content': [
            {'type': 'text', 'text': 'The weather is sunny.'}
        ],
        'stop_reason': 'end_turn'
    }
    
    agent_processor.strands_agent.extract_tool_use.return_value = None
    agent_processor.strands_agent.extract_text_response.return_value = 'The weather is sunny.'
    
    # Execute
    response_text, session_id = agent_processor.process_request(
        prompt='What is the weather?',
        jwt_token='test-jwt-token',
        session_id=None
    )
    
    # Verify
    assert response_text == 'The weather is sunny.'
    assert session_id is not None
    assert len(session_id) > 0
    
    # Verify tool discovery was called
    agent_processor.gateway_client.list_tools.assert_called_once_with('test-jwt-token')
    
    # Verify Claude was invoked
    agent_processor.strands_agent.invoke_with_tools.assert_called_once()
    
    # Verify no tool execution
    agent_processor.gateway_client.invoke_tool.assert_not_called()


def test_process_request_with_tool_use(agent_processor):
    """Test processing request with tool use."""
    # Setup mocks
    agent_processor.gateway_client.list_tools.return_value = [
        {
            'name': 'weather-api___getCurrentWeather',
            'description': 'Get current weather',
            'input_schema': {}
        }
    ]
    
    agent_processor.strands_agent.format_messages.return_value = [
        {'role': 'user', 'content': 'What is the weather in Seattle?'}
    ]
    
    # First Claude response with tool use
    agent_processor.strands_agent.invoke_with_tools.side_effect = [
        {
            'content': [
                {
                    'type': 'tool_use',
                    'id': 'tool-use-123',
                    'name': 'weather-api___getCurrentWeather',
                    'input': {'location': 'Seattle'}
                }
            ],
            'stop_reason': 'tool_use'
        },
        # Second Claude response with final text
        {
            'content': [
                {'type': 'text', 'text': 'The weather in Seattle is 65°F and partly cloudy.'}
            ],
            'stop_reason': 'end_turn'
        }
    ]
    
    agent_processor.strands_agent.extract_tool_use.return_value = {
        'id': 'tool-use-123',
        'name': 'weather-api___getCurrentWeather',
        'input': {'location': 'Seattle'}
    }
    
    agent_processor.gateway_client.invoke_tool.return_value = {
        'location': 'Seattle',
        'temperature': 65,
        'conditions': 'Partly Cloudy'
    }
    
    agent_processor.strands_agent.format_tool_result.return_value = {
        'role': 'user',
        'content': [
            {
                'type': 'tool_result',
                'tool_use_id': 'tool-use-123',
                'content': '{"location": "Seattle", "temperature": 65, "conditions": "Partly Cloudy"}'
            }
        ]
    }
    
    agent_processor.strands_agent.extract_text_response.return_value = 'The weather in Seattle is 65°F and partly cloudy.'
    
    # Execute
    response_text, session_id = agent_processor.process_request(
        prompt='What is the weather in Seattle?',
        jwt_token='test-jwt-token',
        session_id=None
    )
    
    # Verify
    assert response_text == 'The weather in Seattle is 65°F and partly cloudy.'
    assert session_id is not None
    
    # Verify tool was executed
    agent_processor.gateway_client.invoke_tool.assert_called_once_with(
        tool_name='weather-api___getCurrentWeather',
        tool_input={'location': 'Seattle'},
        jwt_token='test-jwt-token'
    )
    
    # Verify Claude was invoked twice (initial + after tool result)
    assert agent_processor.strands_agent.invoke_with_tools.call_count == 2


def test_process_request_with_existing_session_id(agent_processor):
    """Test processing request with existing session ID."""
    # Setup mocks
    agent_processor.gateway_client.list_tools.return_value = []
    agent_processor.strands_agent.format_messages.return_value = [
        {'role': 'user', 'content': 'Hello'}
    ]
    agent_processor.strands_agent.invoke_with_tools.return_value = {
        'content': [{'type': 'text', 'text': 'Hi there!'}],
        'stop_reason': 'end_turn'
    }
    agent_processor.strands_agent.extract_tool_use.return_value = None
    agent_processor.strands_agent.extract_text_response.return_value = 'Hi there!'
    
    existing_session_id = 'existing-session-123'
    
    # Execute
    response_text, session_id = agent_processor.process_request(
        prompt='Hello',
        jwt_token='test-jwt-token',
        session_id=existing_session_id
    )
    
    # Verify session ID is preserved
    assert session_id == existing_session_id


def test_process_request_tool_discovery_failure(agent_processor):
    """Test processing request when tool discovery fails."""
    # Setup mocks - tool discovery fails
    agent_processor.gateway_client.list_tools.side_effect = Exception('Gateway unavailable')
    
    agent_processor.strands_agent.format_messages.return_value = [
        {'role': 'user', 'content': 'Hello'}
    ]
    agent_processor.strands_agent.invoke_with_tools.return_value = {
        'content': [{'type': 'text', 'text': 'Hi there!'}],
        'stop_reason': 'end_turn'
    }
    agent_processor.strands_agent.extract_tool_use.return_value = None
    agent_processor.strands_agent.extract_text_response.return_value = 'Hi there!'
    
    # Execute - should continue without tools
    response_text, session_id = agent_processor.process_request(
        prompt='Hello',
        jwt_token='test-jwt-token',
        session_id=None
    )
    
    # Verify response is still generated
    assert response_text == 'Hi there!'
    
    # Verify Claude was invoked with empty tools list
    call_args = agent_processor.strands_agent.invoke_with_tools.call_args
    assert call_args[1]['tools'] == []


def test_process_request_bedrock_failure(agent_processor):
    """Test processing request when Bedrock invocation fails."""
    # Setup mocks
    agent_processor.gateway_client.list_tools.return_value = []
    agent_processor.strands_agent.format_messages.return_value = [
        {'role': 'user', 'content': 'Hello'}
    ]
    agent_processor.strands_agent.invoke_with_tools.side_effect = Exception('Bedrock error')
    
    # Execute - should raise exception
    with pytest.raises(Exception) as exc_info:
        agent_processor.process_request(
            prompt='Hello',
            jwt_token='test-jwt-token',
            session_id=None
        )
    
    assert 'AI service temporarily unavailable' in str(exc_info.value)


def test_process_request_tool_execution_failure(agent_processor):
    """Test processing request when tool execution fails."""
    # Setup mocks
    agent_processor.gateway_client.list_tools.return_value = [
        {
            'name': 'test-tool',
            'description': 'Test tool',
            'input_schema': {}
        }
    ]
    
    agent_processor.strands_agent.format_messages.return_value = [
        {'role': 'user', 'content': 'Test'}
    ]
    
    agent_processor.strands_agent.invoke_with_tools.return_value = {
        'content': [
            {
                'type': 'tool_use',
                'id': 'tool-use-123',
                'name': 'test-tool',
                'input': {}
            }
        ],
        'stop_reason': 'tool_use'
    }
    
    agent_processor.strands_agent.extract_tool_use.return_value = {
        'id': 'tool-use-123',
        'name': 'test-tool',
        'input': {}
    }
    
    # Tool execution fails
    agent_processor.gateway_client.invoke_tool.side_effect = Exception('Tool error')
    
    # Execute
    response_text, session_id = agent_processor.process_request(
        prompt='Test',
        jwt_token='test-jwt-token',
        session_id=None
    )
    
    # Verify error message is returned
    assert 'encountered an error' in response_text.lower()
    assert 'test tool' in response_text.lower()


def test_generate_session_id(agent_processor):
    """Test session ID generation."""
    session_id = agent_processor._generate_session_id()
    
    # Verify it's a valid UUID
    assert session_id is not None
    assert len(session_id) > 0
    
    # Verify it can be parsed as UUID
    uuid.UUID(session_id)
    
    # Verify multiple calls generate different IDs
    session_id2 = agent_processor._generate_session_id()
    assert session_id != session_id2
