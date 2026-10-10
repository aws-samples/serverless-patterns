#!/usr/bin/env python3
"""
Local HTTP + WebSocket reverse proxy for Lambda MicroVMs browser access.

code-server (VS Code) requires WebSocket support. This proxy uses aiohttp
to properly handle both HTTP requests and WebSocket upgrade/relay, injecting
the X-aws-proxy-auth header into all upstream connections.

Usage:
    python3 proxy.py <microvm-endpoint> <auth-token> [--port PORT]

Example:
    python3 proxy.py https://abc123.lambda-microvm-gamma.us-east-2.on.aws TOKEN

Requirements:
    pip3 install aiohttp
"""

import sys
import argparse
import asyncio
import webbrowser
import ssl

try:
    import aiohttp
    from aiohttp import web
except ImportError:
    print("ERROR: 'aiohttp' module not found.")
    print("Install with: pip3 install aiohttp")
    sys.exit(1)

from urllib.parse import urlparse


TARGET_ENDPOINT = ""
AUTH_TOKEN = ""


async def handle_websocket(request: web.Request) -> web.WebSocketResponse:
    """Proxy WebSocket connections to the MicroVM endpoint."""
    # Get the protocols requested by the browser (if any)
    client_protocols = request.headers.get("Sec-WebSocket-Protocol", "").split(", ")
    client_protocols = [p.strip() for p in client_protocols if p.strip()]

    ws_client = web.WebSocketResponse(protocols=client_protocols if client_protocols else None)
    await ws_client.prepare(request)

    # Build upstream URL (wss)
    path = request.path_qs
    upstream_url = TARGET_ENDPOINT.replace("https://", "wss://") + path

    # MicroVM authenticates WebSocket via subprotocol
    # Also include the port targeting subprotocol
    upstream_protocols = [
        "lambda-microvms",
        f"lambda-microvms.authentication.{AUTH_TOKEN}",
        "lambda-microvms.port.8080",
    ]

    # Headers for upstream — include both X-aws-proxy-auth header AND subprotocol
    # (non-browser clients can set headers on WS upgrade, unlike browsers)
    headers = {
        "Host": urlparse(TARGET_ENDPOINT).hostname,
        "Origin": TARGET_ENDPOINT,
        "X-aws-proxy-auth": AUTH_TOKEN,
    }
    for key, value in request.headers.items():
        lower = key.lower()
        if lower in ("user-agent", "accept-language", "cache-control", "pragma"):
            headers[key] = value

    ssl_ctx = ssl.create_default_context()

    print(f"[ws] Connecting to: {upstream_url}")
    print(f"[ws] Subprotocols: {upstream_protocols[0]}, {upstream_protocols[1][:40]}..., {upstream_protocols[2]}")
    print(f"[ws] Also sending X-aws-proxy-auth header")

    async with aiohttp.ClientSession() as session:
        try:
            async with session.ws_connect(
                upstream_url,
                headers=headers,
                protocols=upstream_protocols,
                ssl=ssl_ctx,
                autoclose=False,
                autoping=True,
            ) as ws_upstream:

                async def client_to_upstream():
                    async for msg in ws_client:
                        if msg.type == aiohttp.WSMsgType.TEXT:
                            await ws_upstream.send_str(msg.data)
                        elif msg.type == aiohttp.WSMsgType.BINARY:
                            await ws_upstream.send_bytes(msg.data)
                        elif msg.type == aiohttp.WSMsgType.PING:
                            await ws_upstream.ping(msg.data)
                        elif msg.type == aiohttp.WSMsgType.PONG:
                            await ws_upstream.pong(msg.data)
                        elif msg.type in (aiohttp.WSMsgType.CLOSE, aiohttp.WSMsgType.CLOSING, aiohttp.WSMsgType.CLOSED):
                            await ws_upstream.close()
                            return
                        elif msg.type == aiohttp.WSMsgType.ERROR:
                            return

                async def upstream_to_client():
                    async for msg in ws_upstream:
                        if msg.type == aiohttp.WSMsgType.TEXT:
                            await ws_client.send_str(msg.data)
                        elif msg.type == aiohttp.WSMsgType.BINARY:
                            await ws_client.send_bytes(msg.data)
                        elif msg.type == aiohttp.WSMsgType.PING:
                            await ws_client.ping(msg.data)
                        elif msg.type == aiohttp.WSMsgType.PONG:
                            await ws_client.pong(msg.data)
                        elif msg.type in (aiohttp.WSMsgType.CLOSE, aiohttp.WSMsgType.CLOSING, aiohttp.WSMsgType.CLOSED):
                            await ws_client.close()
                            return
                        elif msg.type == aiohttp.WSMsgType.ERROR:
                            return

                # Run both directions concurrently
                await asyncio.gather(
                    client_to_upstream(),
                    upstream_to_client(),
                    return_exceptions=True,
                )

        except Exception as e:
            print(f"[ws] Error connecting to upstream: {e}")
            if not ws_client.closed:
                await ws_client.close(code=1011, message=str(e).encode()[:123])

    return ws_client


async def handle_http(request: web.Request) -> web.Response:
    """Proxy regular HTTP requests to the MicroVM endpoint."""
    path = request.path_qs
    upstream_url = TARGET_ENDPOINT + path

    # Build headers with auth
    headers = {"X-aws-proxy-auth": AUTH_TOKEN}
    for key, value in request.headers.items():
        lower = key.lower()
        if lower not in ("host", "connection", "accept-encoding", "transfer-encoding"):
            headers[key] = value

    body = await request.read()

    ssl_ctx = ssl.create_default_context()

    async with aiohttp.ClientSession() as session:
        try:
            async with session.request(
                method=request.method,
                url=upstream_url,
                headers=headers,
                data=body if body else None,
                ssl=ssl_ctx,
                allow_redirects=False,
                timeout=aiohttp.ClientTimeout(total=120),
            ) as resp:
                # Read response
                resp_body = await resp.read()

                # Build response headers
                resp_headers = {}
                for key, value in resp.headers.items():
                    lower = key.lower()
                    if lower not in ("transfer-encoding", "connection", "content-encoding",
                                     "content-length"):
                        resp_headers[key] = value

                return web.Response(
                    status=resp.status,
                    body=resp_body,
                    headers=resp_headers,
                )
        except Exception as e:
            return web.Response(
                status=502,
                text=f"Proxy error: {e}",
                content_type="text/plain",
            )


async def route_handler(request: web.Request):
    """Route to WebSocket or HTTP handler based on upgrade header."""
    if (request.headers.get("Upgrade", "").lower() == "websocket" and
            "upgrade" in request.headers.get("Connection", "").lower()):
        return await handle_websocket(request)
    return await handle_http(request)


async def test_connection(endpoint: str, token: str) -> bool:
    """Test HTTP connectivity before starting the proxy."""
    print("Testing connection to MicroVM endpoint...")
    ssl_ctx = ssl.create_default_context()
    async with aiohttp.ClientSession() as session:
        try:
            async with session.get(
                f"{endpoint}/",
                headers={"X-aws-proxy-auth": token},
                ssl=ssl_ctx,
                timeout=aiohttp.ClientTimeout(total=10),
            ) as resp:
                body = await resp.text()
                print(f"  Status: {resp.status}")
                if resp.status == 200:
                    print("  ✓ Connection successful!")
                    return True
                elif resp.status == 403:
                    print(f"  ✗ Authentication failed: {body[:200]}")
                    return False
                else:
                    print(f"  Response ({resp.status}): {body[:200]}")
                    return True
        except Exception as e:
            print(f"  ✗ Connection error: {e}")
            return False


def main():
    global TARGET_ENDPOINT, AUTH_TOKEN

    parser = argparse.ArgumentParser(
        description="Local HTTP+WebSocket proxy for Lambda MicroVM code-server"
    )
    parser.add_argument("url", help="MicroVM endpoint URL (https://...)")
    parser.add_argument("token", help="Auth token (X-aws-proxy-auth value)")
    parser.add_argument(
        "--port", type=int, default=8080, help="Local proxy port (default: 8080)"
    )
    parser.add_argument(
        "--no-browser", action="store_true", help="Don't open browser automatically"
    )
    parser.add_argument(
        "--skip-test", action="store_true", help="Skip connection test"
    )
    args = parser.parse_args()

    TARGET_ENDPOINT = args.url.rstrip("/")
    AUTH_TOKEN = args.token

    # Test connection
    if not args.skip_test:
        loop = asyncio.new_event_loop()
        if not loop.run_until_complete(test_connection(TARGET_ENDPOINT, AUTH_TOKEN)):
            print("\nConnection test failed. Possible causes:")
            print("  1. Token expired (max 60 min TTL)")
            print("  2. MicroVM is suspended or terminated")
            print(f"\nTo regenerate a token:")
            print(f"  aws lambda-microvms create-microvm-auth-token \\")
            print(f"    --microvm-identifier <mvm-id> --expiration-in-minutes 60 \\")
            print(f"    --allowed-ports allPorts={{}} \\")
            print(f"    --query 'authToken.\"X-aws-proxy-auth\"' --output text")
            sys.exit(1)
        loop.close()

    # Build aiohttp app with catch-all route
    app = web.Application()
    app.router.add_route("*", "/{path_info:.*}", route_handler)

    local_url = f"http://127.0.0.1:{args.port}/"
    print(f"\n{'═' * 60}")
    print(f"  Lambda MicroVM Code Server Proxy (HTTP + WebSocket)")
    print(f"{'═' * 60}")
    print(f"  Browser:  {local_url}")
    print(f"  Target:   {TARGET_ENDPOINT}")
    print(f"  Token:    {AUTH_TOKEN[:12]}...")
    print(f"{'═' * 60}")
    print(f"\n  Press Ctrl+C to stop.\n")

    if not args.no_browser:
        import threading
        threading.Timer(1.0, lambda: webbrowser.open(local_url)).start()

    web.run_app(app, host="127.0.0.1", port=args.port, print=None)


if __name__ == "__main__":
    main()
