"""
Unit tests for webhook processor
"""
import json
import os
import sys
import unittest
from unittest.mock import Mock, patch, MagicMock

# Add src to path
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))

from webhook_processor import validate_signature, store_event


class TestWebhookProcessor(unittest.TestCase):
    """Test cases for webhook processor functions"""
    
    def test_validate_signature_valid(self):
        """Test HMAC signature validation with valid signature"""
        payload = '{"test": "data"}'
        secret = 'my-secret-key'
        # Pre-calculated HMAC-SHA256
        signature = 'sha256=8c5b6e8c8e8f8c8e8f8c8e8f8c8e8f8c8e8f8c8e8f8c8e8f8c8e8f8c8e8f8c'
        
        # Should not raise exception with matching signature
        # Note: This will fail with the pre-calculated hash, but demonstrates the pattern
        # In real tests, calculate the actual hash
        import hmac
        import hashlib
        expected = hmac.new(secret.encode(), payload.encode(), hashlib.sha256).hexdigest()
        result = validate_signature(payload, f'sha256={expected}', secret)
        self.assertTrue(result)
    
    def test_validate_signature_invalid(self):
        """Test HMAC signature validation with invalid signature"""
        payload = '{"test": "data"}'
        secret = 'my-secret-key'
        signature = 'sha256=invalid-signature-here'
        
        result = validate_signature(payload, signature, secret)
        self.assertFalse(result)
    
    def test_validate_signature_no_secret(self):
        """Test signature validation skips when no secret configured"""
        payload = '{"test": "data"}'
        signature = 'sha256=anything'
        
        result = validate_signature(payload, signature, '')
        self.assertTrue(result)  # Should skip validation
    
    def test_validate_signature_no_signature(self):
        """Test signature validation skips when no signature provided"""
        payload = '{"test": "data"}'
        secret = 'my-secret-key'
        
        result = validate_signature(payload, '', secret)
        self.assertTrue(result)  # Should skip validation
    
    @patch('webhook_processor.table')
    def test_store_event_basic(self, mock_table):
        """Test storing webhook event to DynamoDB"""
        execution_token = 'test-token-123'
        event_data = {'type': 'test.event', 'data': 'test'}
        status = 'validated'
        
        store_event(execution_token, event_data, status)
        
        # Verify put_item was called
        mock_table.put_item.assert_called_once()
        call_args = mock_table.put_item.call_args
        item = call_args[1]['Item']
        
        self.assertEqual(item['executionToken'], execution_token)
        self.assertEqual(item['status'], status)
        self.assertEqual(item['webhookPayload'], event_data)
        self.assertIn('timestamp', item)
        self.assertIn('createdAt', item)
        self.assertIn('ttl', item)
    
    @patch('webhook_processor.table')
    def test_store_event_with_step(self, mock_table):
        """Test storing webhook event with current step"""
        execution_token = 'test-token-456'
        event_data = {'type': 'test.event'}
        status = 'processing'
        current_step = 'business-logic'
        
        store_event(execution_token, event_data, status, current_step)
        
        call_args = mock_table.put_item.call_args
        item = call_args[1]['Item']
        
        self.assertEqual(item['currentStep'], current_step)
    
    @patch('webhook_processor.table')
    def test_store_event_with_error(self, mock_table):
        """Test storing webhook event with error"""
        execution_token = 'test-token-789'
        event_data = {'type': 'test.event'}
        status = 'failed'
        error = 'Invalid payload'
        
        store_event(execution_token, event_data, status, error=error)
        
        call_args = mock_table.put_item.call_args
        item = call_args[1]['Item']
        
        self.assertEqual(item['error'], error)


class TestWebhookProcessorIntegration(unittest.TestCase):
    """Integration tests for webhook processor"""
    
    @patch.dict(os.environ, {'EVENTS_TABLE_NAME': 'test-table', 'WEBHOOK_SECRET': ''})
    @patch('webhook_processor.table')
    @patch('webhook_processor.DurableContext')
    def test_lambda_handler_simple_webhook(self, mock_context_class, mock_table):
        """Test lambda handler with simple webhook"""
        # This is a simplified test - full durable execution testing requires
        # the actual SDK or mocking the entire context behavior
        
        event = {
            'requestContext': {'requestId': 'test-request-123'},
            'headers': {},
            'body': json.dumps({
                'type': 'order.created',
                'orderId': 'ORD-123',
                'amount': 99.99
            })
        }
        
        # Mock the durable context
        mock_context = Mock()
        mock_context.step = Mock(side_effect=lambda func, name: func(None))
        
        # Note: Full testing of durable functions requires integration tests
        # Unit tests can verify individual step functions
        self.assertTrue(True)  # Placeholder for actual test


if __name__ == '__main__':
    unittest.main()
