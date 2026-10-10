from mcp.server.fastmcp import FastMCP

mcp = FastMCP(host="0.0.0.0", stateless_http=True)

@mcp.tool()
def add_numbers(a: int, b: int) -> int:
    return a + b

@mcp.tool()
def multiply_numbers(a: int, b: int) -> int:
    return a * b

@mcp.tool()
def greet_user(name: str) -> str:
    return f"Hello, {name}!"

if __name__ == "__main__":
    mcp.run(transport="streamable-http")
