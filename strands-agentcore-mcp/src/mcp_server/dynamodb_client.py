"""Thin DynamoDB wrapper for the Product_Table.

Provides the data-access primitives used by the MCP tool implementations
in `src/mcp_server/tools.py`. Exceptions from boto3/botocore are allowed
to propagate; the JSON-RPC handler maps them to a `-32603` internal error.
"""

import os
from decimal import Decimal

import boto3
from boto3.dynamodb.conditions import Key

# Module-level resource/table handles. The Lambda runtime reuses them
# across invocations within the same execution environment.
TABLE = boto3.resource("dynamodb").Table(os.environ["PRODUCT_TABLE"])


def _to_dynamodb(obj):
    """Recursively convert floats to Decimal for DynamoDB compatibility."""
    if isinstance(obj, float):
        return Decimal(str(obj))
    if isinstance(obj, dict):
        return {k: _to_dynamodb(v) for k, v in obj.items()}
    if isinstance(obj, list):
        return [_to_dynamodb(v) for v in obj]
    return obj


def list_products(category: str | None = None) -> list[dict]:
    """Return products from Product_Table, optionally filtered by category.

    Uses `Query` on the partition key when a category is provided, and
    falls back to a full `Scan` otherwise.

    Args:
        category: Optional partition-key value to filter by.

    Returns:
        The `Items` list from the DynamoDB response (may be empty).
    """
    if category is not None:
        response = TABLE.query(
            KeyConditionExpression=Key("category").eq(category),
        )
    else:
        response = TABLE.scan()
    return response.get("Items", [])


def get_product(category: str, productId: str) -> dict:
    """Fetch a single product by composite key.

    Args:
        category: Partition key.
        productId: Sort key.

    Returns:
        `{"found": False}` when the item does not exist, otherwise
        `{"found": True, "item": <item>}`.
    """
    response = TABLE.get_item(Key={"category": category, "productId": productId})
    item = response.get("Item")
    if item is None:
        return {"found": False}
    return {"found": True, "item": item}


def put_product(item: dict) -> dict:
    """Write (or overwrite) a product item in Product_Table.

    Args:
        item: The full item to persist. Must include `category` and
            `productId` at minimum.

    Returns:
        `{"written": True, "item": item}`.
    """
    # Convert floats to Decimal — DynamoDB rejects Python float types
    dynamo_item = _to_dynamodb(item)
    TABLE.put_item(Item=dynamo_item)
    return {"written": True, "item": item}
