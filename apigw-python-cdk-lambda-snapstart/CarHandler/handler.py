import json
import os
import uuid
from decimal import Decimal
from typing import Any

import boto3
from botocore.exceptions import ClientError

from aws_lambda_powertools import Logger
from aws_lambda_powertools.event_handler import (
    APIGatewayRestResolver,
    Response,
    content_types,
)
from aws_lambda_powertools.event_handler.exceptions import BadRequestError, NotFoundError
from aws_lambda_powertools.logging import correlation_paths
from aws_lambda_powertools.utilities.typing import LambdaContext

logger = Logger(level=os.getenv("LOG_LEVEL", "INFO"))
app = APIGatewayRestResolver()

table_name = os.environ["CAR_TABLE_NAME"]
dynamodb = boto3.resource("dynamodb")
table = dynamodb.Table(table_name)

def _json_default(value: Any) -> Any:
    if isinstance(value, Decimal):
        if value % 1 == 0:
            return int(value)
        return float(value)
    raise TypeError(f"Object of type {type(value)} is not JSON serializable")


def _json_body() -> dict:
    """Parse request body as JSON object; empty or missing body returns {}."""
    raw = app.current_event.json_body
    if raw is None:
        return {}
    if not isinstance(raw, dict):
        raise BadRequestError("Request body must be a JSON object")
    return raw


@app.post("/cars")
def create_car() -> Response:
    body = _json_body()
    car_id = str(uuid.uuid4())
    car = {
        "id": car_id,
        "make": body.get("make"),
        "model": body.get("model"),
        "year": body.get("year"),
        "color": body.get("color"),
    }
    table.put_item(Item=car)
    return Response(
        status_code=201,
        content_type=content_types.APPLICATION_JSON,
        body=json.dumps(car, default=_json_default),
    )


@app.get("/cars/<car_id>")
def get_car(car_id: str) -> Response:
    item = table.get_item(Key={"id": car_id}).get("Item")
    if not item:
        raise NotFoundError(f"Car with id {car_id} not found")
    return Response(
        status_code=200,
        content_type=content_types.APPLICATION_JSON,
        body=json.dumps(item, default=_json_default),
    )


@app.put("/cars/<car_id>")
def update_car(car_id: str) -> Response:
    body = _json_body()
    existing = table.get_item(Key={"id": car_id}).get("Item")
    if not existing:
        raise NotFoundError(f"Car with id {car_id} not found")
    updated = {
        "id": car_id,
        "make": body.get("make", existing.get("make")),
        "model": body.get("model", existing.get("model")),
        "year": body.get("year", existing.get("year")),
        "color": body.get("color", existing.get("color")),
    }
    table.put_item(Item=updated)
    return Response(
        status_code=200,
        content_type=content_types.APPLICATION_JSON,
        body=json.dumps(updated, default=_json_default),
    )


@app.delete("/cars/<car_id>")
def delete_car(car_id: str) -> Response:
    try:
        table.delete_item(
            Key={"id": car_id},
            ConditionExpression="attribute_exists(id)",
        )
    except ClientError as exc:
        if exc.response["Error"]["Code"] == "ConditionalCheckFailedException":
            raise NotFoundError(f"Car with id {car_id} not found") from exc
        raise
    return Response(status_code=204, body="")


@app.exception_handler(NotFoundError)
def handle_not_found(exc: NotFoundError) -> Response:
    return Response(
        status_code=404,
        content_type=content_types.APPLICATION_JSON,
        body=json.dumps({"message": str(exc)}),
    )


@app.exception_handler(BadRequestError)
def handle_bad_request(exc: BadRequestError) -> Response:
    return Response(
        status_code=400,
        content_type=content_types.APPLICATION_JSON,
        body=json.dumps({"message": str(exc)}),
    )


@app.not_found
def handle_route_not_found(_exc: Exception) -> Response:
    return Response(
        status_code=404,
        content_type=content_types.APPLICATION_JSON,
        body=json.dumps({"message": "Route not found"}),
    )


@logger.inject_lambda_context(correlation_id_path=correlation_paths.API_GATEWAY_REST)
def handler(event: dict, context: LambdaContext) -> dict:
    return app.resolve(event, context)
