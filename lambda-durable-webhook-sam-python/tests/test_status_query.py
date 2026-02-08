"""
Unit tests for status query function
"""
import json
import os
import sys
import unittest
from unittest.mock import Mock, patch

# Add src to path
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))

from status_query import lambda_handler


class TestStatusQuery(unittest.TestCase):
    """Test cases for status query function"""
    
    @patch.dict(os.environ, {'EVENTS_TABLE_NAME': 'test-table'})
    @patch('status_query.table')
    def test_query_existing_token(self, mock_table):
        """Test querying status for existing execution token"""
        execution_token = 'test-token-123'
        
        # Mock DynamoDB response
        mock_table.get_item.return_value = {
            'Item': {
                'executionToken': execution_token,
                'status': 'completed',
                'currentStep': 'finalize',
                'createdAt': '2025-02-01T10:00:00.000Z',
                'lastUpdated': '2025-02-01T10:00:05.000Z',
                'webhookPayload': {
                    'type': 'order.created',
                    'source': 'test-system',
                    'orderId': 'ORD-123'
                }
            }
        }
        
        event = {
            'pathParameters': {'executionToken': execution_token}
        }
        
        response = lambda_handler(event, None)
        
        self.assertEqual(response['statusCode'], 200)
        body = json.loads(response['body'])
        self.assertEqual(body['executionToken'], execution_token)
        self.assertEqual(body['status'], 'completed')
        self.assertEqual(body['currentStep'], 'finalize')
        self.assertIn('webhookSummary', body)
    
    @patch.dict(os.environ, {'EVENTS_TABLE_NAME': 'test-table'})
    @patch('status_query.table')
    def test_query_nonexistent_token(self, mock_table):
        """Test querying status for non-existent execution token"""
        execution_token = 'nonexistent-token'
        
        # Mock DynamoDB response with no item
        mock_table.get_item.return_value = {}
        
        event = {
            'pathParameters': {'executionToken': execution_token}
        }
        
        response = lambda_handler(event, None)
        
        self.assertEqual(response['statusCode'], 404)
        body = json.loads(response['body'])
        self.assertIn('error', body)
        self.assertEqual(body['executionToken'], execution_token)
    
    @patch.dict(os.environ, {'EVENTS_TABLE_NAME': 'test-table'})
    def test_query_missing_token(self):
        """Test querying status without execution token"""
        event = {
            'pathParameters': {}
        }
        
        response = lambda_handler(event, None)
        
        self.assertEqual(response['statusCode'], 400)
        body = json.loads(response['body'])
        self.assertIn('error', body)
    
    @patch.dict(os.environ, {'EVENTS_TABLE_NAME': 'test-table'})
    @patch('status_query.table')
    def test_query_with_error(self, mock_table):
        """Test querying status for webhook with error"""
        execution_token = 'error-token-123'
        
        # Mock DynamoDB response with error
        mock_table.get_item.return_value = {
            'Item': {
                'executionToken': execution_token,
                'status': 'failed',
                'currentStep': 'validate',
                'error': 'Invalid webhook signature',
                'createdAt': '2025-02-01T10:00:00.000Z',
                'lastUpdated': '2025-02-01T10:00:01.000Z',
                'webhookPayload': {'type': 'test.event'}
            }
        }
        
        event = {
            'pathParameters': {'executionToken': execution_token}
        }
        
        response = lambda_handler(event, None)
        
        self.assertEqual(response['statusCode'], 200)
        body = json.loads(response['body'])
        self.assertEqual(body['status'], 'failed')
        self.assertIn('error', body)
        self.assertEqual(body['error'], 'Invalid webhook signature')
    
    @patch.dict(os.environ, {'EVENTS_TABLE_NAME': 'test-table'})
    @patch('status_query.table')
    def test_query_cors_headers(self, mock_table):
        """Test that CORS headers are present in response"""
        mock_table.get_item.return_value = {
            'Item': {
                'executionToken': 'test-token',
                'status': 'completed',
                'createdAt': '2025-02-01T10:00:00.000Z',
                'lastUpdated': '2025-02-01T10:00:05.000Z',
                'webhookPayload': {}
            }
        }
        
        event = {
            'pathParameters': {'executionToken': 'test-token'}
        }
        
        response = lambda_handler(event, None)
        
        self.assertIn('headers', response)
        self.assertIn('Access-Control-Allow-Origin', response['headers'])
        self.assertEqual(response['headers']['Access-Control-Allow-Origin'], '*')


if __name__ == '__main__':
    unittest.main()
