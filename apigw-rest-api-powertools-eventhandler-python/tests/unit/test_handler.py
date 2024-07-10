import json
import pytest
from src.app import lambda_handler
from moto import mock_dynamodb
import boto3

TABLE_NAME = "TABLE_NAME"

@pytest.fixture
def lambda_context():
    class LambdaContext:
        function_name: str = "test"
        memory_limit_in_mb: int = 128
        invoked_function_arn: str = "arn:aws:lambda:eu-west-1:123456789012:function:test"
        aws_request_id: str = "da658bd3-2d6f-4e7b-8ec2-937234644fdc"

    return LambdaContext()

@pytest.fixture(scope='session')
def dynamodb_mock():
    with mock_dynamodb():
        # Create DynamoDB resource and table
        client = boto3.client("dynamodb")
        client.create_table(
            TableName=TABLE_NAME,
            KeySchema=[{'AttributeName': 'id', 'KeyType': 'HASH'}],
            AttributeDefinitions=[{'AttributeName': 'id', 'AttributeType': 'N'}],
            ProvisionedThroughput={'ReadCapacityUnits': 5, 'WriteCapacityUnits': 5}
        )

        # Prepopulate the table with some data
        table = boto3.resource('dynamodb').Table(TABLE_NAME)
        table.put_item(Item={'id': 1, 'task': 'Finish the report', 'completed': False})
        table.put_item(Item={'id': 2, 'task': 'Schedule a meeting', 'completed': False})
        table.put_item(Item={'id': 3, 'task': 'Buy groceries', 'completed': False})

        yield
        

def test_get_todos(lambda_context, dynamodb_mock):
   
    minimal_event = {
        "path": "/todos",
        "httpMethod": "GET",
        "requestContext": {"requestId": "227b78aa-779d-47d4-a48e-ce62120393b8"},  # correlation ID
    }
    
    response = lambda_handler(minimal_event, lambda_context)
    
    assert response["statusCode"] == 200
    assert response["body"] != ""
    assert json.loads(response["body"]) == [
        {"id": 1, "task": "Finish the report", "completed": False},
        {"id": 2, "task": "Schedule a meeting", "completed": False},
        {"id": 3, "task": "Buy groceries", "completed": False},
    ]

def test_get_todo(lambda_context, dynamodb_mock):
    minimal_event = {
        "path": "/todos/1",
        "httpMethod": "GET",
        "requestContext": {"requestId": "227b78aa-779d-47d4-a48e-ce62120393b8"},
    }

    response = lambda_handler(minimal_event, lambda_context)
    assert response["statusCode"] == 200
    assert response["body"] != ""
    assert json.loads(response["body"]) == {"id": 1, "task": "Finish the report", "completed": False}

    minimal_event = {
        "path": "/todos/4",
        "httpMethod": "GET",
        "requestContext": {"requestId": "227b78aa-779d-47d4-a48e-ce62120393b8"},
    }
    response = lambda_handler(minimal_event, lambda_context)
   
    assert response["statusCode"] == 404
    assert response["body"] != ""
    assert json.loads(response["body"]) == {"error": "Todo not found"}
    
def test_create_todo(lambda_context, dynamodb_mock):
    minimal_event = {
        "path": "/todos",
        "httpMethod": "POST",
        "body": json.dumps({"task": "Test todo", "completed": False}),
        "requestContext": {"requestId": "227b78aa-779d-47d4-a48e-ce62120393b8"},
    }

    response = lambda_handler(minimal_event, lambda_context)
    assert response["statusCode"] == 201
    assert response["body"] != ""
    assert json.loads(response["body"]) == {"id": 4, "task": "Test todo", "completed": False}

def test_update_todo(lambda_context, dynamodb_mock):
    minimal_event = {
        "path": "/todos/2",
        "httpMethod": "PUT",
        "body": json.dumps({"id": 2, "task": "Updated meeting", "completed": True}),
        "requestContext": {"requestId": "227b78aa-779d-47d4-a48e-ce62120393b8"},
    }

    response = lambda_handler(minimal_event, lambda_context)
    assert response["statusCode"] == 200
    assert response["body"] != ""
    assert json.loads(response["body"]) == {"id": 2, "task": "Updated meeting", "completed": True}

    minimal_event = {
        "path": "/todos/5",
        "httpMethod": "PUT",
        "body": json.dumps({"id": 4, "task": "Test todo", "completed": False}),
        "requestContext": {"requestId": "227b78aa-779d-47d4-a48e-ce62120393b8"},
    }

    response = lambda_handler(minimal_event, lambda_context)
    assert response["statusCode"] == 404
    assert response["body"] != ""
    assert json.loads(response["body"]) == {"error": "Todo not found"}

def test_delete_todo(lambda_context, dynamodb_mock):
    minimal_event = {
        "path": "/todos/2",
        "httpMethod": "DELETE",
        "requestContext": {"requestId": "227b78aa-779d-47d4-a48e-ce62120393b8"},
    }

    response = lambda_handler(minimal_event, lambda_context)
    assert response["statusCode"] == 204
    assert response["body"] == "{}"

    minimal_event = {
        "path": "/todos/5",
        "httpMethod": "DELETE",
        "requestContext": {"requestId": "227b78aa-779d-47d4-a48e-ce62120393b8"},
    }

    response = lambda_handler(minimal_event, lambda_context)
    assert response["statusCode"] == 404
    assert response["body"] != ""
    assert json.loads(response["body"]) == {"error": "Todo not found"}