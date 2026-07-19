"""API Gateway entry point for the MCP Server Lambda.

Parses incoming JSON-RPC 2.0 requests forwarded by AgentCore Gateway,
dispatches `tools/list` and `tools/call` methods to the tool registry in
`src.mcp_server.tools`, and shapes every response as the API Gateway
proxy envelope expected by a Lambda `AWS_PROXY` integration.

Protocol rules (see design.md and project-conventions.md):

- HTTP status is always `200`; JSON-RPC errors are conveyed in the body.
- `Content-Type: application/json` on every response.
- Error codes: `-32700` parse error, `-32601` method not found,
  `-32602` invalid params, `-32603` internal error.
- Every request logs the JSON-RPC `method`; every `tools/call` also
  logs the tool `name`.
"""

import json
from decimal import Decimal
from typing import Any

from src.mcp_server import tools
from src.shared.logging_utils import get_logger

logger = get_logger(__name__)


class _DecimalEncoder(json.JSONEncoder):
    """Convert DynamoDB Decimal values to float for JSON serialization."""
    def default(self, obj):
        if isinstance(obj, Decimal):
            return float(obj)
        return super().default(obj)


def json_rpc_response(
    id_: Any,
    result: Any | None = None,
    error: dict[str, Any] | None = None,
) -> dict[str, Any]:
    """Build the API Gateway proxy envelope for a JSON-RPC 2.0 response.

    Exactly one of `result` or `error` is populated in the body. The HTTP
    envelope is always `200` with `Content-Type: application/json` so the
    JSON-RPC error semantics are preserved end-to-end.

    Args:
        id_: The JSON-RPC request id echoed back to the caller. May be
            `None` when the incoming body could not be parsed.
        result: The JSON-RPC `result` payload for success responses.
        error: The JSON-RPC `error` object (`{"code": int, "message": str, ...}`)
            for failure responses.

    Returns:
        An API Gateway proxy response dict with `statusCode`, `headers`,
        and a JSON-encoded `body`.
    """
    body: dict[str, Any] = {"jsonrpc": "2.0", "id": id_}
    if error is not None:
        body["error"] = error
    else:
        body["result"] = result
    return {
        "statusCode": 200,
        "headers": {"Content-Type": "application/json"},
        "body": json.dumps(body, cls=_DecimalEncoder),
    }


def _parse_error(id_: Any = None) -> dict[str, Any]:
    """Return a `-32700` JSON-RPC parse-error envelope."""
    return json_rpc_response(
        id_,
        error={"code": -32700, "message": "parse error"},
    )


def lambda_handler(event: dict[str, Any], context: Any) -> dict[str, Any]:
    """Handle an API Gateway proxy invocation carrying a JSON-RPC request.

    Parses `event["body"]` as a JSON-RPC 2.0 message, validates the
    envelope (`jsonrpc == "2.0"` and a `method` field), and dispatches
    to the tool registry. Unknown methods and unknown tools both map to
    `-32601`; argument-schema violations map to `-32602`; any other
    exception from a tool handler is logged and mapped to `-32603`.

    Args:
        event: The API Gateway proxy event. The JSON-RPC request is in
            the `body` field as a (possibly empty) string.
        context: The Lambda context (unused).

    Returns:
        An API Gateway proxy response dict. `statusCode` is always `200`;
        JSON-RPC errors are returned in the body.
    """
    raw_body = event.get("body")

    # Parse the JSON-RPC envelope. Anything non-parseable or structurally
    # invalid short-circuits to a -32700 parse error with id=None, since
    # we can't reliably recover the request id from an unparseable body.
    try:
        if not isinstance(raw_body, str):
            raise json.JSONDecodeError("body is not a string", "", 0)
        parsed = json.loads(raw_body)
    except json.JSONDecodeError:
        logger.info("mcp_request method=<unparseable> id=None")
        return _parse_error()

    if not isinstance(parsed, dict):
        logger.info("mcp_request method=<non-object-body> id=None")
        return _parse_error()

    request_id = parsed.get("id")
    method = parsed.get("method")

    if parsed.get("jsonrpc") != "2.0" or not isinstance(method, str):
        logger.info("mcp_request method=%r id=%r (invalid envelope)", method, request_id)
        return _parse_error(request_id)

    logger.info("mcp_request method=%s id=%r", method, request_id)

    # MCP protocol handshake — AgentCore sends initialize before tools/list.
    # Respond with the server's capabilities so the session can proceed.
    if method == "initialize":
        return json_rpc_response(request_id, result={
            "protocolVersion": parsed.get("params", {}).get("protocolVersion", "2025-03-26"),
            "capabilities": {"tools": {}},
            "serverInfo": {"name": "agentcore-mcp-server", "version": "1.0.0"},
        })

    # MCP notification — no response needed, return empty 200
    if method == "notifications/initialized":
        return {"statusCode": 200, "headers": {"Content-Type": "application/json"}, "body": ""}

    if method == "tools/list":
        return json_rpc_response(request_id, result=tools.list_tool_catalog())

    if method == "tools/call":
        params = parsed.get("params") or {}
        tool_name = params.get("name") if isinstance(params, dict) else None
        arguments = params.get("arguments") if isinstance(params, dict) else None
        if not isinstance(arguments, dict):
            arguments = {}

        logger.info("mcp_tools_call name=%r id=%r", tool_name, request_id)

        try:
            result = tools.dispatch(tool_name, arguments)
        except tools.UnknownToolError as exc:
            return json_rpc_response(
                request_id,
                error={"code": -32601, "message": str(exc)},
            )
        except tools.InvalidParamsError as exc:
            return json_rpc_response(
                request_id,
                error={"code": -32602, "message": str(exc)},
            )
        except Exception as exc:  # noqa: BLE001 - surface as internal error
            logger.exception("mcp_tool_handler_error name=%r id=%r", tool_name, request_id)
            return json_rpc_response(
                request_id,
                error={"code": -32603, "message": f"internal error: {exc}"},
            )

        return json_rpc_response(request_id, result=result)

    return json_rpc_response(
        request_id,
        error={"code": -32601, "message": f"method not found: {method}"},
    )
