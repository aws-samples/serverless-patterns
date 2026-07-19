"""MCP tool registry for the MCP Server Lambda.

Declares the three product-management tools exposed to AgentCore Gateway
via MCP JSON-RPC, along with a dispatcher that validates arguments against
each tool's JSON Schema before invoking the handler.

Tool handlers delegate to `dynamodb_client` for all DynamoDB I/O. Errors
from handlers (e.g. boto3 `ClientError`) propagate out of `dispatch` so
the JSON-RPC handler can map them to `-32603` internal errors.
"""

from dataclasses import dataclass
from typing import Any, Callable

import jsonschema

from src.mcp_server import dynamodb_client


class UnknownToolError(Exception):
    """Raised when a `tools/call` request names a tool not in the registry.

    The JSON-RPC handler maps this to error code `-32601` (method not found).
    """


class InvalidParamsError(Exception):
    """Raised when `tools/call` arguments fail JSON Schema validation.

    The JSON-RPC handler maps this to error code `-32602` (invalid params).
    """


@dataclass(frozen=True)
class Tool:
    """Declarative record for a single MCP tool.

    Attributes:
        name: Tool identifier exposed to the model via `tools/list`.
        description: Human-readable description shown to the model.
        input_schema: JSON Schema describing the shape of `arguments`.
        handler: Callable invoked with the validated arguments dict.
    """

    name: str
    description: str
    input_schema: dict[str, Any]
    handler: Callable[[dict[str, Any]], Any]


LIST_PRODUCTS = Tool(
    name="list_products",
    description="List products, optionally filtered by category.",
    input_schema={
        "type": "object",
        "properties": {"category": {"type": "string"}},
        "additionalProperties": False,
    },
    handler=lambda args: dynamodb_client.list_products(args.get("category")),
)


GET_PRODUCT = Tool(
    name="get_product",
    description="Get a product by category and productId.",
    input_schema={
        "type": "object",
        "properties": {
            "category": {"type": "string"},
            "productId": {"type": "string"},
        },
        "required": ["category", "productId"],
        "additionalProperties": False,
    },
    handler=lambda args: dynamodb_client.get_product(args["category"], args["productId"]),
)


PUT_PRODUCT = Tool(
    name="put_product",
    description="Create or update a product.",
    input_schema={
        "type": "object",
        "properties": {
            "category": {"type": "string"},
            "productId": {"type": "string"},
            "name": {"type": "string"},
            "price": {"type": "number"},
        },
        "required": ["category", "productId", "name", "price"],
        "additionalProperties": False,
    },
    handler=lambda args: dynamodb_client.put_product(args),
)


TOOLS: dict[str, Tool] = {t.name: t for t in (LIST_PRODUCTS, GET_PRODUCT, PUT_PRODUCT)}


def list_tool_catalog() -> dict[str, list[dict[str, Any]]]:
    """Return the `tools/list` response payload.

    Shape matches the MCP spec: a `tools` array where each entry exposes
    `name`, `description`, and `inputSchema`.
    """
    return {
        "tools": [
            {
                "name": t.name,
                "description": t.description,
                "inputSchema": t.input_schema,
            }
            for t in TOOLS.values()
        ]
    }


def dispatch(name: str, arguments: dict[str, Any]) -> dict[str, Any]:
    """Validate arguments and invoke the named tool.

    Args:
        name: Tool name from `params.name` of a `tools/call` request.
        arguments: Tool arguments from `params.arguments`.

    Returns:
        `{"content": <handler return value>}` on success.

    Raises:
        UnknownToolError: `name` is not a registered tool.
        InvalidParamsError: `arguments` fails `inputSchema` validation.
    """
    tool = TOOLS.get(name)
    if tool is None:
        raise UnknownToolError(f"unknown tool: {name}")

    try:
        jsonschema.validate(instance=arguments, schema=tool.input_schema)
    except jsonschema.ValidationError as exc:
        raise InvalidParamsError(f"invalid params: {exc.message}") from exc

    result = tool.handler(arguments)
    # MCP spec requires content to be an array of {type, text} objects
    import json
    from decimal import Decimal

    def _default(obj):
        if isinstance(obj, Decimal):
            return float(obj)
        raise TypeError(f"Object of type {type(obj)} is not JSON serializable")

    return {"content": [{"type": "text", "text": json.dumps(result, default=_default)}]}
