#!/usr/bin/env python3

import asyncio
import os
import sys

from mcp import ClientSession
from mcp.client.streamable_http import streamablehttp_client

async def main():
    base_url = sys.argv[1].rstrip("/") if len(sys.argv) > 1 else os.environ.get("CF_URL", "").rstrip("/")
    token = sys.argv[2] if len(sys.argv) > 2 else os.environ.get("BEARER_TOKEN", "")
    
    if not base_url or not token:
        print("Usage: python test_mcp.py <cloudfront_url> <bearer_token>")
        print("Or set CF_URL and BEARER_TOKEN environment variables")
        sys.exit(1)
    
    print("=" * 60)
    print("MCP Protocol Validation")
    print("=" * 60)
    print(f"Base URL: {base_url}")
    print(f"Token: {token[:20]}...")
    
    mcp_url = f"{base_url}/mcp/invocations"
    headers = {"Authorization": f"Bearer {token}", "Content-Type": "application/json"}
    
    print(f"\n[TEST] MCP Connection")
    print(f"  [DEBUG] URL: {mcp_url}")
    
    try:
        async with streamablehttp_client(mcp_url, headers, timeout=120, terminate_on_close=False) as (
            read_stream,
            write_stream,
            _,
        ):
            async with ClientSession(read_stream, write_stream) as session:
                await session.initialize()
                print("  [PASS] MCP session initialized")
                
                print("\n[TEST] List Tools")
                tools = await session.list_tools()
                print(f"  [PASS] Found {len(tools.tools)} tools:")
                for tool in tools.tools:
                    print(f"    - {tool.name}")
                
                print("\n[TEST] Call add_numbers tool")
                result = await session.call_tool("add_numbers", {"a": 5, "b": 3})
                print(f"  [PASS] Result: {result.content}")
                
        print("\n" + "=" * 60)
        print("All tests passed!")
        print("=" * 60)
    except Exception as e:
        print(f"\n[FAIL] {e}")
        sys.exit(1)

if __name__ == "__main__":
    asyncio.run(main())
