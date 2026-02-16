import base64
import json
import logging
import os
import uuid
from decimal import Decimal
from typing import Any, Dict, Optional

import boto3
from botocore.exceptions import ClientError

logger = logging.getLogger()
logger.setLevel(os.getenv("LOG_LEVEL", "INFO"))

table_name = os.environ["CAR_TABLE_NAME"]
dynamodb = boto3.resource("dynamodb")
table = dynamodb.Table(table_name)

def _json_default(value: Any) -> Any:
    if isinstance(value, Decimal):
        if value % 1 == 0:
            return int(value)
        return float(value)
    raise TypeError(f"Object of type {type(value)} is not JSON serializable")

def _response(status_code: int, body: Optional[Dict[str, Any]] = None) -> Dict[str, Any]:
    payload = "" if body is None else json.dumps(body, default=_json_default)
    return {
        "statusCode": status_code,
        "headers": {"Content-Type": "application/json"},
        "body": payload,
    }

def _parse_body(event: Dict[str, Any]) -> Dict[str, Any]:
    raw = event.get("body") or "{}"
    if event.get("isBase64Encoded", False):
        raw = base64.b64decode(raw).decode("utf-8")
    try:
        body = json.loads(raw)
    except json.JSONDecodeError as exc:
        raise ValueError("Invalid JSON body") from exc

    if not isinstance(body, dict):
        raise ValueError("Request body must be a JSON object")

    return body

def _path_parts(path: str) -> list[str]:
    if not path:
        return []
    return [part for part in path.strip("/").split("/") if part]

def _create_car(event: Dict[str, Any]) -> Dict[str, Any]:
    body = _parse_body(event)
    car_id = str(uuid.uuid4())
    car = {
        "id": car_id,
        "make": body.get("make"),
        "model": body.get("model"),
        "year": body.get("year"),
        "color": body.get("color"),
    }
    table.put_item(Item=car)
    return _response(201, car)

def _get_car(car_id: str) -> Dict[str, Any]:
    item = table.get_item(Key={"id": car_id}).get("Item")
    if not item:
        return _response(404, {"message": f"Car with id {car_id} not found"})
    return _response(200, item)

def _update_car(event: Dict[str, Any], car_id: str) -> Dict[str, Any]:
    body = _parse_body(event)

    existing = table.get_item(Key={"id": car_id}).get("Item")
    if not existing:
        return _response(404, {"message": f"Car with id {car_id} not found"})

    updated = {
        "id": car_id,
        "make": body.get("make", existing.get("make")),
        "model": body.get("model", existing.get("model")),
        "year": body.get("year", existing.get("year")),
        "color": body.get("color", existing.get("color")),
    }
    table.put_item(Item=updated)
    return _response(200, updated)


def _delete_car(car_id: str) -> Dict[str, Any]:
    try:
        table.delete_item(
            Key={"id": car_id},
            ConditionExpression="attribute_exists(id)",
        )
    except ClientError as exc:
        if exc.response["Error"]["Code"] == "ConditionalCheckFailedException":
            return _response(404, {"message": f"Car with id {car_id} not found"})
        raise

    return _response(204)

def handler(event: Dict[str, Any], _: Any) -> Dict[str, Any]:
    method = (event.get("httpMethod") or "").upper()
    path = event.get("path") or ""
    parts = _path_parts(path)

    logger.info(json.dumps({"method": method, "path": path}))

    try:
        if method == "POST" and parts == ["cars"]:
            return _create_car(event)

        if len(parts) == 2 and parts[0] == "cars":
            car_id = parts[1]
            if method == "GET":
                return _get_car(car_id)
            if method == "PUT":
                return _update_car(event, car_id)
            if method == "DELETE":
                return _delete_car(car_id)

        return _response(404, {"message": "Route not found"})
    except ValueError as exc:
        return _response(400, {"message": str(exc)})
