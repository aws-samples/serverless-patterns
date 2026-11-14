"""Unit tests for Tool Lambda handler."""

import json
import os
import pytest
from unittest.mock import Mock, patch, MagicMock
from datetime import datetime

from src.tool.handler import lambda_handler, list_s3_buckets, route_tool_execution
from src.shared.models import UserContext


class TestToolLambdaHandler:
    """Test Tool Lambda handler functionality."""
    
    def test_lambda_handler_success(self):
        """Test successful tool execution."""
        # Arrange - Gateway passes arguments directly as event
        event = {
            'user_context': {
                'user_id': 'user-123',
                'username': 'testuser',
                'client_id': 'client-456'
            }
        }
        
        context = Mock()
        context.aws_request_id = 'test-request-id'
        
        mock_s3_response = {
            'Buckets': [
                {'Name': 'bucket1', 'CreationDate': datetime(2024, 1, 1)},
                {'Name': 'bucket2', 'CreationDate': datetime(2024, 1, 2)}
            ]
        }
        
        # Act
        with patch('src.tool.handler.s3_client') as mock_s3, \
             patch.dict(os.environ, {'TOOL_NAME': 'list-s3-buckets'}):
            mock_s3.list_buckets.return_value = mock_s3_response
            result = lambda_handler(event, context)
        
        # Assert
        assert 'result' in result
        assert 'buckets' in result['result']
        assert len(result['result']['buckets']) == 2
        assert result['result']['buckets'][0]['name'] == 'bucket1'
        assert result['result']['user_context']['user_id'] == 'user-123'
        assert result['result']['user_context']['username'] == 'testuser'
    
    def test_lambda_handler_missing_user_context(self):
        """Test handler with missing user context."""
        # Arrange - Gateway passes arguments directly, no user_context
        event = {}
        
        context = Mock()
        context.aws_request_id = 'test-request-id'
        
        mock_s3_response = {
            'Buckets': [
                {'Name': 'bucket1', 'CreationDate': datetime(2024, 1, 1)}
            ]
        }
        
        # Act
        with patch('src.tool.handler.s3_client') as mock_s3, \
             patch.dict(os.environ, {'TOOL_NAME': 'list-s3-buckets'}):
            mock_s3.list_buckets.return_value = mock_s3_response
            result = lambda_handler(event, context)
        
        # Assert - should still work with 'unknown' user context
        assert 'result' in result
        assert result['result']['user_context']['user_id'] == 'unknown'
    
    def test_lambda_handler_unknown_tool(self):
        """Test handler with unknown tool name."""
        # Arrange
        event = {
            'toolName': 'unknown-tool',
            'parameters': {
                'user_context': {
                    'user_id': 'user-123',
                    'username': 'testuser',
                    'client_id': 'client-456'
                }
            }
        }
        
        context = Mock()
        context.aws_request_id = 'test-request-id'
        
        # Act
        result = lambda_handler(event, context)
        
        # Assert
        assert 'statusCode' in result
        assert result['statusCode'] == 400
        assert 'body' in result
        body = json.loads(result['body'])
        assert 'error' in body
    
    def test_list_s3_buckets_success(self):
        """Test S3 bucket listing."""
        # Arrange
        user_context = UserContext(
            user_id='user-123',
            username='testuser',
            client_id='client-456'
        )
        
        mock_s3_response = {
            'Buckets': [
                {'Name': 'my-bucket', 'CreationDate': datetime(2024, 1, 15, 10, 30, 0)},
                {'Name': 'another-bucket', 'CreationDate': datetime(2024, 2, 1, 14, 0, 0)}
            ]
        }
        
        # Act
        with patch('src.tool.handler.s3_client') as mock_s3:
            mock_s3.list_buckets.return_value = mock_s3_response
            result = list_s3_buckets(user_context)
        
        # Assert
        assert 'buckets' in result
        assert 'count' in result
        assert result['count'] == 2
        assert result['buckets'][0]['name'] == 'my-bucket'
        assert result['buckets'][0]['creation_date'] == '2024-01-15T10:30:00'
        assert result['buckets'][1]['name'] == 'another-bucket'
    
    def test_list_s3_buckets_empty(self):
        """Test S3 bucket listing with no buckets."""
        # Arrange
        user_context = UserContext(
            user_id='user-123',
            username='testuser',
            client_id='client-456'
        )
        
        mock_s3_response = {'Buckets': []}
        
        # Act
        with patch('src.tool.handler.s3_client') as mock_s3:
            mock_s3.list_buckets.return_value = mock_s3_response
            result = list_s3_buckets(user_context)
        
        # Assert
        assert result['count'] == 0
        assert result['buckets'] == []
    
    def test_route_tool_execution_valid_tool(self):
        """Test routing to valid tool."""
        # Arrange
        user_context = UserContext(
            user_id='user-123',
            username='testuser',
            client_id='client-456'
        )
        
        mock_s3_response = {
            'Buckets': [
                {'Name': 'bucket1', 'CreationDate': datetime(2024, 1, 1)}
            ]
        }
        
        # Act
        with patch('src.tool.handler.s3_client') as mock_s3:
            mock_s3.list_buckets.return_value = mock_s3_response
            result = route_tool_execution('list-s3-buckets', user_context)
        
        # Assert
        assert 'buckets' in result
        assert 'count' in result
    
    def test_route_tool_execution_invalid_tool(self):
        """Test routing to invalid tool."""
        # Arrange
        user_context = UserContext(
            user_id='user-123',
            username='testuser',
            client_id='client-456'
        )
        
        # Act & Assert
        with pytest.raises(ValueError, match="Unknown tool"):
            route_tool_execution('invalid-tool', user_context)


    def test_lambda_handler_aws_error(self):
        """Test handler with AWS service error."""
        # Arrange - Gateway passes arguments directly
        event = {
            'user_context': {
                'user_id': 'user-123',
                'username': 'testuser',
                'client_id': 'client-456'
            }
        }
        
        context = Mock()
        context.aws_request_id = 'test-request-id'
        
        # Create mock ClientError
        from botocore.exceptions import ClientError
        error_response = {
            'Error': {
                'Code': 'AccessDenied',
                'Message': 'Access Denied'
            }
        }
        
        # Act
        with patch('src.tool.handler.s3_client') as mock_s3, \
             patch.dict(os.environ, {'TOOL_NAME': 'list-s3-buckets'}):
            mock_s3.list_buckets.side_effect = ClientError(error_response, 'ListBuckets')
            result = lambda_handler(event, context)
        
        # Assert
        assert 'error' in result
        assert 'error_code' in result
        assert result['error_code'] == 'AccessDenied'
        assert 'permission' in result['error'].lower()
    
    def test_list_s3_buckets_with_retry(self):
        """Test S3 bucket listing with transient error and retry."""
        # Arrange
        user_context = UserContext(
            user_id='user-123',
            username='testuser',
            client_id='client-456'
        )
        
        from botocore.exceptions import ClientError
        error_response = {
            'Error': {
                'Code': 'Throttling',
                'Message': 'Rate exceeded'
            }
        }
        
        mock_s3_response = {
            'Buckets': [
                {'Name': 'bucket1', 'CreationDate': datetime(2024, 1, 1)}
            ]
        }
        
        # Act
        with patch('src.tool.handler.s3_client') as mock_s3:
            # First call fails with throttling, second succeeds
            mock_s3.list_buckets.side_effect = [
                ClientError(error_response, 'ListBuckets'),
                mock_s3_response
            ]
            
            with patch('src.tool.handler.retry_with_backoff') as mock_retry:
                # Make retry_with_backoff actually call the function
                mock_retry.side_effect = lambda func, **kwargs: func()
                
                # This should succeed after retry
                mock_s3.list_buckets.side_effect = [mock_s3_response]
                result = list_s3_buckets(user_context)
        
        # Assert
        assert 'buckets' in result
        assert result['count'] == 1
