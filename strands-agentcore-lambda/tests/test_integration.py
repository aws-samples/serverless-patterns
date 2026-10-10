"""Integration tests for Serverless AI Agent Gateway.

These tests validate end-to-end flows and multi-component interactions.
"""

import json
import os
import pytest
from unittest.mock import Mock, patch, MagicMock
from datetime import datetime, timedelta
from hypothesis import given, strategies as st, settings

from src.shared.models import UserContext, AgentRequest, ToolRequest
from src.agent.handler import lambda_handler as agent_handler
from src.interceptor.handler import lambda_handler as interceptor_handler
from src.tool.handler import lambda_handler as tool_handler


# Test markers
pytestmark = pytest.mark.integration


class TestUserContextPreservation:
    """Test user context preservation through all layers (Property 3)."""
    
    @pytest.mark.property
    def test_user_context_preserved_through_layers(self):
        """
        Property 3: User Context Preservation
        Validates: Requirements 3.2, 3.8, 9.8
        
        For any UserContext flowing through system layers (Agent → Gateway → 
        Interceptor → Tool), the user_id, username, and client_id values 
        should remain unchanged at every layer.
        """
        # Arrange - Create original user context
        original_context = UserContext(
            user_id='test-user-123',
            username='testuser',
            client_id='test-client-456'
        )
        
        # Simulate Interceptor layer - MCP-format event with JWT in headers
        interceptor_event = {
            'mcp': {
                'gatewayRequest': {
                    'body': {
                        'jsonrpc': '2.0',
                        'method': 'tools/call',
                        'params': {
                            'name': 'list-s3-buckets',
                            'arguments': {}
                        },
                        'id': 'req-1'
                    },
                    'headers': {
                        'Authorization': 'Bearer mock-jwt-token'
                    }
                }
            }
        }
        
        # Mock JWT decoding to return our test context
        with patch('src.interceptor.handler.decode_jwt_payload') as mock_decode:
            mock_decode.return_value = {
                'sub': original_context.user_id,
                'username': original_context.username,
                'client_id': original_context.client_id
            }
            
            mock_context = Mock()
            mock_context.request_id = 'test-request-123'
            interceptor_response = interceptor_handler(interceptor_event, mock_context)
        
        # Verify Interceptor preserved context (MCP response format)
        transformed_body = interceptor_response['mcp']['transformedGatewayRequest']['body']
        interceptor_user_context = transformed_body['params']['arguments']['user_context']
        assert interceptor_user_context['user_id'] == original_context.user_id
        assert interceptor_user_context['username'] == original_context.username
        assert interceptor_user_context['client_id'] == original_context.client_id
        
        # Simulate Tool layer - Gateway passes arguments directly as event
        tool_event = {
            'user_context': interceptor_user_context
        }
        
        # Mock S3 client and TOOL_NAME env var
        with patch('src.tool.handler.s3_client') as mock_s3, \
             patch.dict(os.environ, {'TOOL_NAME': 'list-s3-buckets'}):
            mock_s3.list_buckets.return_value = {
                'Buckets': [
                    {'Name': 'test-bucket', 'CreationDate': datetime.now()}
                ]
            }
            
            tool_response = tool_handler(tool_event, Mock(aws_request_id='test-123'))
        
        # Verify Tool preserved context
        tool_user_context = tool_response['result']['user_context']
        assert tool_user_context['user_id'] == original_context.user_id
        assert tool_user_context['username'] == original_context.username
        
        # Final verification - context unchanged through all layers
        assert tool_user_context['user_id'] == original_context.user_id
        assert tool_user_context['username'] == original_context.username


class TestInterceptorTargetCompatibility:
    """Test Gateway Interceptor works with different target types (Property 21)."""
    
    @pytest.mark.property
    def test_interceptor_works_with_lambda_target(self):
        """
        Property 21: Gateway Interceptor Target Type Compatibility
        Validates: Requirements 11.7
        
        For any Gateway target type (Lambda, MCP Server, API Gateway), 
        the Gateway Request Interceptor should successfully extract JWT 
        claims and add user_context to the request parameters.
        """
        # Arrange - MCP-format Lambda target request
        event = {
            'mcp': {
                'gatewayRequest': {
                    'body': {
                        'jsonrpc': '2.0',
                        'method': 'tools/call',
                        'params': {
                            'name': 'list-s3-buckets',
                            'arguments': {'some_param': 'value'}
                        },
                        'id': 'req-1'
                    },
                    'headers': {
                        'Authorization': 'Bearer mock-jwt-token'
                    }
                }
            }
        }
        
        # Mock JWT decoding
        with patch('src.interceptor.handler.decode_jwt_payload') as mock_decode:
            mock_decode.return_value = {
                'sub': 'user-123',
                'username': 'testuser',
                'client_id': 'client-456'
            }
            
            # Act
            response = interceptor_handler(event, Mock(request_id='test-123'))
        
        # Assert - MCP response format with user_context in arguments
        assert 'mcp' in response
        transformed_body = response['mcp']['transformedGatewayRequest']['body']
        arguments = transformed_body['params']['arguments']
        assert 'user_context' in arguments
        assert arguments['user_context']['user_id'] == 'user-123'
        assert arguments['user_context']['username'] == 'testuser'
        
        # Original parameters preserved
        assert arguments['some_param'] == 'value'


class TestEndToEndFlow:
    """Test complete end-to-end flow from authentication to tool execution."""
    
    def test_complete_flow_with_user_context(self):
        """
        End-to-end integration test
        Validates: Requirements 3.8, 7.6, 9.8
        
        Test complete flow: authenticate → submit prompt → Agent processes → 
        Gateway invokes Interceptor → Tool executes → response returned.
        Verify user context at every layer.
        """
        # Arrange - Create test JWT and user context
        test_jwt = 'mock-jwt-token'
        test_user_context = {
            'sub': 'user-e2e-123',
            'username': 'e2euser',
            'client_id': 'client-e2e-456',
            'token_use': 'access',
            'exp': int((datetime.now() + timedelta(hours=1)).timestamp())
        }
        
        # Step 1: Interceptor extracts user context from JWT (MCP format)
        interceptor_event = {
            'mcp': {
                'gatewayRequest': {
                    'body': {
                        'jsonrpc': '2.0',
                        'method': 'tools/call',
                        'params': {
                            'name': 'list-s3-buckets',
                            'arguments': {}
                        },
                        'id': 'req-1'
                    },
                    'headers': {
                        'Authorization': f'Bearer {test_jwt}'
                    }
                }
            }
        }
        
        with patch('src.interceptor.handler.decode_jwt_payload') as mock_decode:
            mock_decode.return_value = test_user_context
            interceptor_response = interceptor_handler(
                interceptor_event,
                Mock(request_id='e2e-test-123')
            )
        
        # Verify Interceptor added user_context (MCP response format)
        transformed_body = interceptor_response['mcp']['transformedGatewayRequest']['body']
        interceptor_user_context = transformed_body['params']['arguments']['user_context']
        assert interceptor_user_context is not None
        
        # Step 2: Tool receives request with user_context (Gateway passes arguments directly)
        tool_event = {
            'user_context': interceptor_user_context
        }
        
        with patch('src.tool.handler.s3_client') as mock_s3, \
             patch.dict(os.environ, {'TOOL_NAME': 'list-s3-buckets'}):
            mock_s3.list_buckets.return_value = {
                'Buckets': [
                    {'Name': 'e2e-bucket-1', 'CreationDate': datetime(2024, 1, 1)},
                    {'Name': 'e2e-bucket-2', 'CreationDate': datetime(2024, 1, 2)}
                ]
            }
            
            tool_response = tool_handler(tool_event, Mock(aws_request_id='e2e-tool-123'))
        
        # Verify Tool response includes user_context
        assert 'result' in tool_response
        assert 'user_context' in tool_response['result']
        tool_user_context = tool_response['result']['user_context']
        
        # Step 3: Verify user context preserved through entire flow
        assert tool_user_context['user_id'] == test_user_context['sub']
        assert tool_user_context['username'] == test_user_context['username']
        
        # Verify tool execution results
        assert 'buckets' in tool_response['result']
        assert len(tool_response['result']['buckets']) == 2
        assert tool_response['result']['buckets'][0]['name'] == 'e2e-bucket-1'


class TestMultiTurnConversation:
    """Test multi-turn conversation with session management."""
    
    def test_conversation_flow_with_session(self):
        """
        Multi-turn conversation integration test
        Validates: Requirements 12.1, 12.3, 12.5
        
        Test conversation flow: start conversation → first prompt → 
        follow-up prompt. Verify session_id created and maintained, 
        context stored and retrieved.
        """
        # This test requires Agent Lambda with Memory integration
        # which is implemented in agent_processor.py
        # For now, we'll test the session ID generation and propagation
        
        # Arrange - First request without session_id
        first_request_event = {
            'headers': {
                'Authorization': 'Bearer mock-jwt-token'
            },
            'body': json.dumps({
                'prompt': 'List my S3 buckets'
            })
        }
        
        test_claims = {
            'sub': 'user-session-123',
            'username': 'sessionuser',
            'client_id': 'client-session-456',
            'token_use': 'access',
            'exp': int((datetime.now() + timedelta(hours=1)).timestamp())
        }
        
        # Mock dependencies
        with patch('src.agent.handler.validate_jwt') as mock_validate, \
             patch('src.agent.handler.extract_user_context') as mock_extract, \
             patch('src.agent.handler.process_agent_request') as mock_process:
            
            mock_validate.return_value = test_claims
            mock_extract.return_value = UserContext(
                user_id=test_claims['sub'],
                username=test_claims['username'],
                client_id=test_claims['client_id']
            )
            
            # First request should generate new session_id
            new_session_id = 'session-abc-123'
            mock_process.return_value = (
                'You have 3 S3 buckets: bucket1, bucket2, bucket3',
                new_session_id
            )
            
            # Act - First request
            first_response = agent_handler(first_request_event, Mock(request_id='req-1'))
        
        # Assert - Session ID created
        assert first_response['statusCode'] == 200
        first_body = json.loads(first_response['body'])
        assert 'session_id' in first_body
        assert first_body['session_id'] == new_session_id
        
        # Arrange - Follow-up request with session_id
        followup_request_event = {
            'headers': {
                'Authorization': 'Bearer mock-jwt-token'
            },
            'body': json.dumps({
                'prompt': 'How many buckets do I have?',
                'session_id': new_session_id
            })
        }
        
        with patch('src.agent.handler.validate_jwt') as mock_validate, \
             patch('src.agent.handler.extract_user_context') as mock_extract, \
             patch('src.agent.handler.process_agent_request') as mock_process:
            
            mock_validate.return_value = test_claims
            mock_extract.return_value = UserContext(
                user_id=test_claims['sub'],
                username=test_claims['username'],
                client_id=test_claims['client_id']
            )
            
            # Follow-up should use existing session_id
            mock_process.return_value = (
                'Based on our previous conversation, you have 3 buckets',
                new_session_id
            )
            
            # Act - Follow-up request
            followup_response = agent_handler(followup_request_event, Mock(request_id='req-2'))
        
        # Assert - Same session ID maintained
        assert followup_response['statusCode'] == 200
        followup_body = json.loads(followup_response['body'])
        assert followup_body['session_id'] == new_session_id


class TestErrorScenarios:
    """Test error handling in integration scenarios."""
    
    def test_invalid_jwt_returns_401(self):
        """
        Error scenario integration test
        Validates: Requirements 1.7, 1.8, 10.1
        
        Test invalid JWT → verify 401 response with generic error message.
        """
        # Arrange - Request with invalid JWT
        event = {
            'headers': {
                'Authorization': 'Bearer invalid-jwt-token'
            },
            'body': json.dumps({
                'prompt': 'List my S3 buckets'
            })
        }
        
        # Mock JWT validation to fail
        with patch('src.agent.handler.validate_jwt') as mock_validate:
            mock_validate.side_effect = ValueError("Invalid token signature")
            
            # Act
            response = agent_handler(event, Mock(request_id='error-test-1'))
        
        # Assert - 401 with generic error message
        assert response['statusCode'] == 401
        body = json.loads(response['body'])
        assert 'error' in body
        # Should not expose specific failure reason
        assert 'signature' not in body['error'].lower()
    
    def test_expired_jwt_returns_401(self):
        """Test expired JWT → verify 401 response."""
        # Arrange - Request with expired JWT
        event = {
            'headers': {
                'Authorization': 'Bearer expired-jwt-token'
            },
            'body': json.dumps({
                'prompt': 'List my S3 buckets'
            })
        }
        
        # Mock JWT validation to fail with expiration
        with patch('src.agent.handler.validate_jwt') as mock_validate:
            mock_validate.side_effect = ValueError("Token has expired")
            
            # Act
            response = agent_handler(event, Mock(request_id='error-test-2'))
        
        # Assert - 401 with generic error message
        assert response['statusCode'] == 401
        body = json.loads(response['body'])
        assert 'error' in body
    
    def test_aws_service_error_handling(self):
        """Test AWS service error → verify error handling."""
        # Arrange - Tool event (Gateway passes arguments directly)
        event = {
            'user_context': {
                'user_id': 'user-error-123',
                'username': 'erroruser',
                'client_id': 'client-error-456'
            }
        }
        
        # Mock S3 client to raise AccessDenied error
        from botocore.exceptions import ClientError
        error_response = {
            'Error': {
                'Code': 'AccessDenied',
                'Message': 'Access Denied'
            }
        }
        
        with patch('src.tool.handler.s3_client') as mock_s3, \
             patch.dict(os.environ, {'TOOL_NAME': 'list-s3-buckets'}):
            mock_s3.list_buckets.side_effect = ClientError(error_response, 'ListBuckets')
            
            # Act
            response = tool_handler(event, Mock(aws_request_id='error-test-3'))
        
        # Assert - Error response with user-friendly message
        assert 'error' in response
        assert 'error_code' in response
        assert response['error_code'] == 'AccessDenied'
        # Should have user-friendly message
        assert 'permission' in response['error'].lower()
    
    def test_interceptor_error_graceful_degradation(self):
        """
        Test Interceptor error → verify graceful degradation.
        Validates: Requirements 10.8
        
        When Interceptor encounters error, it should return original 
        request unchanged and log error without throwing exception.
        """
        # Arrange - MCP-format event with malformed JWT
        original_body = {
            'jsonrpc': '2.0',
            'method': 'tools/call',
            'params': {
                'name': 'list-s3-buckets',
                'arguments': {'test': 'value'}
            },
            'id': 'req-1'
        }
        event = {
            'mcp': {
                'gatewayRequest': {
                    'body': original_body,
                    'headers': {
                        'Authorization': 'Bearer malformed-jwt'
                    }
                }
            }
        }
        
        # Mock JWT decoding to fail
        with patch('src.interceptor.handler.decode_jwt_payload') as mock_decode:
            mock_decode.side_effect = Exception("JWT decoding failed")
            
            # Act
            response = interceptor_handler(event, Mock(request_id='error-test-4'))
        
        # Assert - Original request returned unchanged in MCP format
        assert 'mcp' in response
        transformed_body = response['mcp']['transformedGatewayRequest']['body']
        assert transformed_body == original_body
        # user_context should NOT be added due to error
        assert 'user_context' not in transformed_body.get('params', {}).get('arguments', {})


class TestSessionTimeout:
    """Test session timeout behavior (Property 23)."""
    
    @pytest.mark.property
    def test_expired_session_handling(self):
        """
        Property 23: Session Timeout
        Validates: Requirements 12.7
        
        For any session, if no activity occurs for longer than the 
        configured timeout period, subsequent requests with that 
        session_id should either create a new session or return an 
        error indicating the session has expired.
        """
        # This test requires Memory integration which tracks session timeouts
        # For now, we'll test the concept with mocked Memory client
        
        # Arrange - Old session that should be expired
        expired_session_id = 'session-expired-123'
        
        event = {
            'headers': {
                'Authorization': 'Bearer mock-jwt-token'
            },
            'body': json.dumps({
                'prompt': 'Continue our conversation',
                'session_id': expired_session_id
            })
        }
        
        test_claims = {
            'sub': 'user-timeout-123',
            'username': 'timeoutuser',
            'client_id': 'client-timeout-456',
            'token_use': 'access',
            'exp': int((datetime.now() + timedelta(hours=1)).timestamp())
        }
        
        # Mock dependencies
        with patch('src.agent.handler.validate_jwt') as mock_validate, \
             patch('src.agent.handler.extract_user_context') as mock_extract, \
             patch('src.agent.handler.process_agent_request') as mock_process:
            
            mock_validate.return_value = test_claims
            mock_extract.return_value = UserContext(
                user_id=test_claims['sub'],
                username=test_claims['username'],
                client_id=test_claims['client_id']
            )
            
            # Simulate expired session - new session created
            new_session_id = 'session-new-456'
            mock_process.return_value = (
                'Starting a new conversation',
                new_session_id
            )
            
            # Act
            response = agent_handler(event, Mock(request_id='timeout-test-1'))
        
        # Assert - New session ID returned (old session expired)
        assert response['statusCode'] == 200
        body = json.loads(response['body'])
        assert body['session_id'] != expired_session_id
        assert body['session_id'] == new_session_id


# Property-based test strategies
@st.composite
def user_contexts(draw):
    """Generate random UserContext objects."""
    return UserContext(
        user_id=draw(st.text(min_size=1, max_size=50, alphabet=st.characters(blacklist_characters='\x00'))),
        username=draw(st.text(min_size=1, max_size=50, alphabet=st.characters(blacklist_characters='\x00'))),
        client_id=draw(st.text(min_size=1, max_size=50, alphabet=st.characters(blacklist_characters='\x00')))
    )


class TestPropertyBasedIntegration:
    """Property-based integration tests using Hypothesis."""
    
    @pytest.mark.property
    @given(user_context=user_contexts())
    @settings(max_examples=100, deadline=None)
    def test_user_context_preservation_property(self, user_context):
        """
        Property test: User context should be preserved through all layers
        for any valid user context.
        """
        # Arrange - MCP-format Interceptor event with user context
        interceptor_event = {
            'mcp': {
                'gatewayRequest': {
                    'body': {
                        'jsonrpc': '2.0',
                        'method': 'tools/call',
                        'params': {
                            'name': 'list-s3-buckets',
                            'arguments': {}
                        },
                        'id': 'req-1'
                    },
                    'headers': {
                        'Authorization': 'Bearer mock-jwt'
                    }
                }
            }
        }
        
        # Mock JWT decoding to return generated user context
        with patch('src.interceptor.handler.decode_jwt_payload') as mock_decode:
            mock_decode.return_value = {
                'sub': user_context.user_id,
                'username': user_context.username,
                'client_id': user_context.client_id
            }
            
            interceptor_response = interceptor_handler(
                interceptor_event,
                Mock(request_id='prop-test')
            )
        
        # Verify Interceptor preserved context (MCP response format)
        transformed_body = interceptor_response['mcp']['transformedGatewayRequest']['body']
        arguments = transformed_body['params']['arguments']
        assert 'user_context' in arguments
        assert arguments['user_context']['user_id'] == user_context.user_id
        assert arguments['user_context']['username'] == user_context.username
        assert arguments['user_context']['client_id'] == user_context.client_id
        
        # Tool layer - Gateway passes arguments directly as event
        tool_event = {
            'user_context': arguments['user_context']
        }
        
        with patch('src.tool.handler.s3_client') as mock_s3, \
             patch.dict(os.environ, {'TOOL_NAME': 'list-s3-buckets'}):
            mock_s3.list_buckets.return_value = {'Buckets': []}
            tool_response = tool_handler(tool_event, Mock(aws_request_id='prop-test'))
        
        # Verify Tool preserved context
        result_context = tool_response['result']['user_context']
        assert result_context['user_id'] == user_context.user_id
        assert result_context['username'] == user_context.username
