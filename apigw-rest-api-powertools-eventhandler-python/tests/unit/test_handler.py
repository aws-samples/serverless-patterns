import json
import os
from uuid import uuid4

import boto3
import pytest
from moto import mock_dynamodb

from src.app import lambda_handler

TABLE_NAME = "TODOS"

# Define a static UUID
UUID_1 = str(uuid4())
UUID_2 = str(uuid4())
UUID_3 = str(uuid4())

todos = [
    {"id": UUID_1, "task": "Finish the report", "completed": False},
    {"id": UUID_2, "task": "Schedule a meeting", "completed": False},
    {"id": UUID_3, "task": "Buy groceries", "completed": False}
]

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
            AttributeDefinitions=[{'AttributeName': 'id', 'AttributeType': 'S'}],
            ProvisionedThroughput={'ReadCapacityUnits': 5, 'WriteCapacityUnits': 5}
        )

        # Prepopulate the table with some data
        table = boto3.resource('dynamodb').Table(TABLE_NAME)
        table.put_item(Item=todos[0])
        table.put_item(Item=todos[1])
        table.put_item(Item=todos[2])

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
    assert json.loads(response["body"]) == todos

def test_get_todo(lambda_context, dynamodb_mock):
    minimal_event = {
        "path": f"/todos/{UUID_1}",
        "httpMethod": "GET",
        "requestContext": {"requestId": "227b78aa-779d-47d4-a48e-ce62120393b8"},
    }

    response = lambda_handler(minimal_event, lambda_context)
    assert response["statusCode"] == 200
    assert response["body"] != ""
    assert json.loads(response["body"]) == todos[0]

    minimal_event = {
        "path": "/todos/NOT_PRESENT",
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
    body = json.loads(response["body"])
    assert "id" in body
    assert body["task"] == "Test todo"
    assert body["completed"] == False

def test_update_todo(lambda_context, dynamodb_mock):
    minimal_event = {
        "path": f"/todos/{UUID_2}",
        "httpMethod": "PUT",
        "body": json.dumps({"id": UUID_2, "task": "Updated meeting", "completed": True}),
        "requestContext": {"requestId": "227b78aa-779d-47d4-a48e-ce62120393b8"},
    }

    response = lambda_handler(minimal_event, lambda_context)
    assert response["statusCode"] == 200
    assert response["body"] != ""
    assert json.loads(response["body"]) == {"id": UUID_2, "task": "Updated meeting", "completed": True}

    fakeid= str(uuid4())
    minimal_event = {
        "path": f"/todos/{fakeid}",
        "httpMethod": "PUT",
        "body": json.dumps({"id": fakeid, "task": "Test todo", "completed": False}),
        "requestContext": {"requestId": "227b78aa-779d-47d4-a48e-ce62120393b8"},
    }

    response = lambda_handler(minimal_event, lambda_context)
    assert response["statusCode"] == 404
    assert response["body"] != ""
    assert json.loads(response["body"]) == {"error": f"Todo with ID {fakeid} not found"}

def test_delete_todo(lambda_context, dynamodb_mock):
    minimal_event = {
        "path": f"/todos/{UUID_2}",
        "httpMethod": "DELETE",
        "requestContext": {"requestId": "227b78aa-779d-47d4-a48e-ce62120393b8"},
    }

    response = lambda_handler(minimal_event, lambda_context)
    assert response["statusCode"] == 204
    assert response["body"] == "{}"

    fakeid= str(uuid4())
    minimal_event = {
        "path": f"/todos/{fakeid}",
        "httpMethod": "DELETE",
        "requestContext": {"requestId": "227b78aa-779d-47d4-a48e-ce62120393b8"},
    }

    response = lambda_handler(minimal_event, lambda_context)
    assert response["statusCode"] == 404
    assert response["body"] != ""
    assert json.loads(response["body"]) == {"error": f"Todo with ID {fakeid} not found"}