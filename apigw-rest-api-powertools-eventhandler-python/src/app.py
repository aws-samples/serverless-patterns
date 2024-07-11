import os
from typing import Any, Dict, List, Union
from uuid import uuid4

import boto3
from aws_lambda_powertools import Logger, Metrics, Tracer
from aws_lambda_powertools.event_handler import APIGatewayRestResolver
from aws_lambda_powertools.logging import correlation_paths
from aws_lambda_powertools.metrics import MetricUnit
from aws_lambda_powertools.utilities.typing import LambdaContext
from botocore.exceptions import ClientError
from pydantic import BaseModel, Field

app = APIGatewayRestResolver(enable_validation=True) 
# Enable Swagger UI
app.enable_swagger(path="/swagger")

tracer = Tracer()
logger = Logger()
metrics = Metrics()
dynamo_table = None

def init_dynamodb():
    global dynamo_table
    if dynamo_table is None:
        dynamodb_resource = boto3.resource("dynamodb")
        table_name = os.getenv("TODOS_TABLE", "TABLE_NAME")
        dynamo_table = dynamodb_resource.Table(table_name)

class Todo(BaseModel):  
    todo_id: str = Field(alias="id", default_factory=lambda: str(uuid4()))
    task: str
    completed: bool

@app.get("/todos")
@tracer.capture_method
def get_todos() -> Union[List[Todo], Dict[str, Any]]:
    metrics.add_metric(name="Get Todos Invocation", unit=MetricUnit.Count, value=1)
    logger.info("Getting all todos")
    try:
        # table = get_table_resource()
        response = dynamo_table.scan()
        items = response.get('Items', [])
        todos = [Todo.parse_obj(item) for item in items]
        return todos
    except ClientError as e:
        logger.error(f"Failed to fetch todos: {e}")
        return {"error": "Failed to fetch todos"}, 500

@app.get("/todos/<todo_id>")
@tracer.capture_method
def get_todo(todo_id: str) -> Union[Todo, Dict[str, Any]]:
    metrics.add_metric(name="Get Todo Invocation", unit=MetricUnit.Count, value=1)
    logger.info(f"Getting todo with id: {todo_id}")
    try:
        # table = get_table_resource()
        response = dynamo_table.get_item(Key={'id': todo_id})
        item = response.get('Item')
        if item:
            return Todo.parse_obj(item)
        else:
            return {"error": "Todo not found"}, 404
    except ClientError as e:
        logger.error(f"Failed to fetch todo: {e}")
        return {"error": "Failed to fetch todo"}, 500

@app.post("/todos")
@tracer.capture_method
def create_todo(new_todo: Todo) -> Union[Todo, Dict[str, Any]]:
    metrics.add_metric(name="Create Todo Invocation", unit=MetricUnit.Count, value=1)
    logger.info(f"Creating todo: {new_todo.dict()}")
    try:
        # Validate and parse the incoming todo data
        new_todo = Todo.parse_obj(new_todo)
        # Insert the new todo into the DynamoDB table
        dynamo_table.put_item(Item=new_todo.dict(by_alias=True))
        logger.info("Todo created", extra=new_todo.dict())
        return new_todo, 201
    except ValueError as e:
        return {"Invalid data": str(e)}, 400
    except ClientError as e:
        logger.error(f"Failed to create todo: {e}")
        return {"error": "Failed to create todo"}, 500

@app.put("/todos/<todo_id>")
@tracer.capture_method
def update_todo(todo_id: str, todo_toupdate: Todo) -> Union[Todo, Dict[str, Any]]:
    metrics.add_metric(name="Update Todo Invocation", unit=MetricUnit.Count, value=1)
    logger.info(f"Updating todo id: {todo_id}")
    try:
        update_expression = "set task = :task, completed = :completed"
        expression_attribute_values = {
            ":task": todo_toupdate.task,
            ":completed": todo_toupdate.completed
        }
        response = dynamo_table.update_item(
            Key={"id": todo_id},
            UpdateExpression=update_expression,
            ExpressionAttributeValues=expression_attribute_values,
            ConditionExpression="attribute_exists(id)",
            ReturnValues="ALL_NEW"
        )
        updated_todo_data = response["Attributes"]
        updated_todo = Todo(
            id=updated_todo_data["id"],
            task=updated_todo_data["task"],
            completed=updated_todo_data["completed"]
        )
        return updated_todo
    except ClientError as e:
        if e.response["Error"]["Code"] == "ConditionalCheckFailedException":
            return {"error": f"Todo with ID {todo_id} not found"}, 404
        logger.error(f"Failed to update todo: {e}")
        return {"error": "Failed to update todo"}, 500

@app.delete("/todos/<todo_id>")
@tracer.capture_method
def delete_todo(todo_id: str):
    metrics.add_metric(name="Delete Todo Invocation", unit=MetricUnit.Count, value=1)
    logger.info(f"Deleting todo id: {todo_id}")
    try:
        response = dynamo_table.delete_item(
            Key={"id": todo_id},
            ConditionExpression="attribute_exists(id)",
            ReturnValues="ALL_OLD"
        )
        if "Attributes" not in response:
            return {"error": f"Todo with ID {todo_id} not found"}, 404
        return {}, 204
    except ClientError as e:
        if e.response["Error"]["Code"] == "ConditionalCheckFailedException":
            return {"error": f"Todo with ID {todo_id} not found"}, 404
        logger.error(f"Failed to delete todo: {e}")
        return {"error": "Failed to delete todo"}, 500

# Enrich logging with contextual information from Lambda
@logger.inject_lambda_context(correlation_id_path=correlation_paths.API_GATEWAY_REST)
# Adding tracer
# See: https://awslabs.github.io/aws-lambda-powertools-python/latest/core/tracer/
@tracer.capture_lambda_handler
# ensures metrics are flushed upon request completion/failure and capturing ColdStart metric
@metrics.log_metrics(capture_cold_start_metric=True)
def lambda_handler(event: dict, context: LambdaContext) -> dict:
    init_dynamodb()
    return app.resolve(event, context)