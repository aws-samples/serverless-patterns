import json
import pytest
from unittest.mock import patch, MagicMock
import sys
import os

# Add the parent directory to the path so we can import the app module
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from app import lambda_handler

class TestLambdaHandler:
    """Test cases for the Lambda handler function."""
    
    def test_lambda_handler_empty_event(self):
        """Test lambda handler with empty event."""
        event = {"records": {}}
        context = MagicMock()
        
        result = lambda_handler(event, context)
        assert result == {"statusCode": 200}
    
    def test_lambda_handler_function_exists(self):
        """Test that lambda_handler function exists and is callable."""
        assert callable(lambda_handler)
        
    def test_lambda_handler_with_empty_records(self):
        """Test lambda handler with empty records structure."""
        event = {"records": {}}
        context = MagicMock()
        
        # Should not raise any exceptions
        result = lambda_handler(event, context)
        assert isinstance(result, dict)
        assert result.get("statusCode") == 200
