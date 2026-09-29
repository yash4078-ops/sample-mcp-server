
from mcp.server.fastmcp import FastMCP

mcp = FastMCP("sample-mcp-server")


@mcp.tool()
def echo(text: str) -> str:
    """Echo back the provided text. Harmless diagnostic tool."""
    return text


@mcp.tool()
def add(a: int, b: int) -> int:
    """Add two integers. Harmless diagnostic tool."""
    return a + b


if __name__ == "__main__":
    mcp.run()
